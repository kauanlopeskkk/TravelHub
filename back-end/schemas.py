from __future__ import annotations

from datetime import date, datetime
from typing import List, Literal, Optional

from pydantic import BaseModel, ConfigDict, Field


class Destino(BaseModel):
    id: int
    cidade: str
    pais: str
    avaliacao: int = Field(ge=0, le=5)

    model_config = ConfigDict(from_attributes=True)


# Alias só pra você continuar usando `DestinoOut` no main.
DestinoOut = Destino


class PrevisaoVOo(BaseModel):
    aeroporto_origem: str = Field(default="REC", min_length=3, max_length=4)
    pais: str
    cidade: str
    data: Optional[date] = None
    tipo: Literal["partida", "chegada"] = "partida"

    model_config = ConfigDict(from_attributes=True)


class VooPrevisto(BaseModel):
    numero_voo: Optional[str] = None
    companhia: Optional[str] = None
    tipo: Literal["partida", "chegada"]
    horario_estimado: datetime
    atraso_minutos: Optional[int] = Field(default=None, ge=0)
    confianca: float = Field(ge=0, le=1)  # 0..1 (ex: 0.72 = 72%)
    status: Optional[str] = None

    model_config = ConfigDict(from_attributes=True)


class PrevisaoVooResponse(BaseModel):
    aeroporto_origem: str
    pais: str
    cidade: str
    data: date
    tipo: Literal["partida", "chegada"]
    gerado_em: datetime
    voos: List[VooPrevisto]

    model_config = ConfigDict(from_attributes=True)
