from typing import List

from fastapi import Depends, FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy.orm import Session

from database import SessionLocal, get_db, init_db
from models import Destino as DestinoDB
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

    # Seed simples pra /destinos já mostrar algo sem você inserir manualmente.
    db = SessionLocal()
    try:
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
    finally:
        db.close()


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.get("/destinos", response_model=List[DestinoOut])
def listar_destinos(db: Session = Depends(get_db)):
    return db.query(DestinoDB).all()
