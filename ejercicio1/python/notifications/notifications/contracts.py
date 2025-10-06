from __future__ import annotations
from typing import Protocol, Callable, Any, Dict, Optional, List
from dataclasses import dataclass
from enum import Enum

class Canal(str, Enum):
    EMAIL = "email"
    SMS = "sms"
    PUSH = "push"

@dataclass
class Evento:
    id: str
    nombre: str
    payload: Dict[str, Any]
    ocurrido_en: float
    meta: Dict[str,str]

@dataclass
class Destinatario:
    id: str
    direccion: str
    canal: Canal

@dataclass
class PreferenciasUsuario:
    locale: str = "es-AR"
    canales: List[Canal] = None

@dataclass
class MensajeRenderizado:
    asunto: str
    cuerpo: str

@dataclass
class ResultadoEntrega:
    ok: bool
    proveedor: str
    error: Optional[str] = None

class EstrategiaNotificacion(Protocol):
    def puede_manejar(self, nombre_evento: str, canal: Canal) -> bool: ...
    def renderizar(self, evento: Evento, prefs: PreferenciasUsuario) -> MensajeRenderizado: ...

class RemitenteNotificacion(Protocol):
    def enviar(self, a: Destinatario, msg: MensajeRenderizado) -> ResultadoEntrega: ...

class FabricaNotificacion(Protocol):
    def para_canal(self, canal: Canal, proveedor: Optional[str] = None) -> RemitenteNotificacion: ...

Suscriptor = Callable[[Evento], None]

class BusEventos:
    def __init__(self) -> None:
        self._subs: list[Suscriptor] = []

    def publicar(self, evento: Evento) -> None:
        for fn in list(self._subs):
            fn(evento)

    def suscribir(self, fn: Suscriptor):
        self._subs.append(fn)
        def desuscribir():
            self._subs.remove(fn)
        return desuscribir
