from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="TravelHub API", version="0.1.0")

# Exemplo temporário de dados (vai para o banco quando você tiver database).
# Formato: id, cidade, pais, Avaliacao
destinos = [
    {
        "id": 1232323,
        "cidade": "Paris",
        "pais": "França",
        "Avaliacao": 5,
    }
]

app.add_middleware(
    CORSMiddleware,
    # Se seu frontend rodar em outra URL/host, ajuste aqui.
    allow_origins=["http://localhost:5173", "http://127.0.0.1:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/health")
def health_check():
    return {
        "status": "ok",
        "message": "Bem-vindo ao TravelHub API."
    }


@app.get("/destinos")
def listar_destinos():
    return destinos


# Quando você criar rotas reais em back-end/routes/__init__.py (um `router`),
# a gente inclui aqui:
#
# from routes import router as api_router
# app.include_router(api_router, prefix="/api")
