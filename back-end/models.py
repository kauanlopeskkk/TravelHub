from __future__ import annotations

from datetime import datetime

from sqlalchemy import Column, Date, DateTime, Float, ForeignKey, Integer, String
from sqlalchemy.orm import relationship

from database import Base


class Destino(Base):
    __tablename__ = "destinos"

    id = Column(Integer, primary_key=True, index=True)
    cidade = Column(String, nullable=False)
    pais = Column(String, nullable=False)
    avaliacao = Column(Integer, nullable=False, default=0)


class PrevisaoVoo(Base):
    __tablename__ = "previsoes_voo"

    id = Column(Integer, primary_key=True, index=True)

    aeroporto_origem = Column(String, nullable=False)
    pais = Column(String, nullable=False)
    cidade = Column(String, nullable=False)
    data = Column(Date, nullable=False)
    tipo = Column(String, nullable=False)
    gerado_em = Column(DateTime, nullable=False, default=datetime.utcnow)

    voos = relationship(
        "VooPrevisto",
        back_populates="previsao",
        cascade="all, delete-orphan",
    )


class VooPrevisto(Base):
    __tablename__ = "voos_previstos"

    id = Column(Integer, primary_key=True, index=True)
    previsao_id = Column(Integer, ForeignKey("previsoes_voo.id"), nullable=False)

    numero_voo = Column(String, nullable=True)
    companhia = Column(String, nullable=True)
    tipo = Column(String, nullable=False)

    horario_estimado = Column(DateTime, nullable=False)
    atraso_minutos = Column(Integer, nullable=True)
    confianca = Column(Float, nullable=False, default=0.0)
    status = Column(String, nullable=True)

    previsao = relationship("PrevisaoVoo", back_populates="voos")
