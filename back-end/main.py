from typing import List
from datetime import date, datetime, timedelta

from fastapi import Depends, FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

from database import SessionLocal, get_db, init_db
from models import Destino as DestinoDB
from models import PrevisaoVoo as PrevisaoVooDB
from models import VooPrevisto as VooPrevistoDB
from schemas import DestinoOut

app = FastAPI(title="TravelHub API", version="0.1.0")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173", "http://127.0.0.1:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.on_event("startup")
def startup() -> None:
    init_db()

    db = SessionLocal()
    try:
        # Seed simples pra /destinos já mostrar algo sem você inserir manualmente.
        if db.query(DestinoDB).count() == 0:
            db.add_all(
                [
                    DestinoDB(cidade="Paris", pais="França", avaliacao=5),
                    DestinoDB(cidade="Lisboa", pais="Portugal", avaliacao=4),
                    DestinoDB(cidade="Tóquio", pais="Japão", avaliacao=5),
                    DestinoDB(cidade="Recife", pais="Brasil", avaliacao=5),
                ]
            )
            db.commit()

        # Seed simples pra /api/voos já retornar dados pro frontend.
        # (Se você for alimentar o banco depois, pode remover ou ajustar.)
        if db.query(PrevisaoVooDB).count() == 0:
            previsao = PrevisaoVooDB(
                aeroporto_origem="REC",
                pais="Brasil",
                cidade="Recife",
                data=date.today(),
                tipo="partida",
            )
            db.add(previsao)
            db.flush()  # garante previsao.id

            base = datetime.utcnow()
            db.add_all(
                [
                    VooPrevistoDB(
                        previsao_id=previsao.id,
                        numero_voo="GR 1203",
                        companhia="Gulfair",
                        tipo="partida",
                        horario_estimado=base + timedelta(minutes=85),
                        atraso_minutos=0,
                        confianca=0.72,
                        status="Embarque",
                    ),
                    VooPrevistoDB(
                        previsao_id=previsao.id,
                        numero_voo="TA 4410",
                        companhia="Tropic Air",
                        tipo="partida",
                        horario_estimado=base + timedelta(minutes=140),
                        atraso_minutos=18,
                        confianca=0.64,
                        status="Atrasado",
                    ),
                    VooPrevistoDB(
                        previsao_id=previsao.id,
                        numero_voo="SA 0882",
                        companhia="Sapphire",
                        tipo="partida",
                        horario_estimado=base + timedelta(minutes=200),
                        atraso_minutos=0,
                        confianca=0.58,
                        status="Em Sala",
                    ),
                    VooPrevistoDB(
                        previsao_id=previsao.id,
                        numero_voo="OR 0077",
                        companhia="Orion",
                        tipo="partida",
                        horario_estimado=base + timedelta(minutes=520),
                        atraso_minutos=None,
                        confianca=0.21,
                        status="Cancelado",
                    ),
                ]
            )
            db.commit()
    finally:
        db.close()


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.get("/destinos", response_model=List[DestinoOut])
def listar_destinos(db: Session = Depends(get_db)):
    return db.query(DestinoDB).all()


@app.get("/api/voos")
def listar_voos(db: Session = Depends(get_db)):
    # Pega a previsão mais recente para montar os voos.
    previsao = db.query(PrevisaoVooDB).order_by(PrevisaoVooDB.id.desc()).first()
    if not previsao:
        return []

    voos_db = (
        db.query(VooPrevistoDB)
        .filter(VooPrevistoDB.previsao_id == previsao.id)
        .order_by(VooPrevistoDB.horario_estimado.asc())
        .all()
    )

    # Formato esperado pelo frontend (TabelaFlight.jsx)
    return [
        {
            "id": v.id,
            "flightNumber": v.numero_voo,
            "airline": v.companhia,
            "origin": previsao.aeroporto_origem,
            "destination": previsao.cidade,
            "status": v.status,
        }
        for v in voos_db
    ]
