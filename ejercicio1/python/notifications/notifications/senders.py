from __future__ import annotations
from .contracts import RemitenteNotificacion, Destinatario, MensajeRenderizado, ResultadoEntrega

class RemitenteEmail(RemitenteNotificacion):
    def __init__(self, proveedor: str = "sendgrid") -> None:
        self.proveedor = proveedor
    def enviar(self, a: Destinatario, msg: MensajeRenderizado) -> ResultadoEntrega:
        print(f"[EMAIL::{self.proveedor}] para={a.direccion} asunto={msg.asunto} cuerpo={msg.cuerpo}")
        return ResultadoEntrega(ok=True, proveedor=self.proveedor)

class RemitenteSMS(RemitenteNotificacion):
    def __init__(self, proveedor: str = "twilio") -> None:
        self.proveedor = proveedor
    def enviar(self, a: Destinatario, msg: MensajeRenderizado) -> ResultadoEntrega:
        print(f"[SMS::{self.proveedor}] para={a.direccion} cuerpo={msg.cuerpo}")
        return ResultadoEntrega(ok=True, proveedor=self.proveedor)

class RemitentePush(RemitenteNotificacion):
    def __init__(self, proveedor: str = "fcm") -> None:
        self.proveedor = proveedor
    def enviar(self, a: Destinatario, msg: MensajeRenderizado) -> ResultadoEntrega:
        print(f"[PUSH::{self.proveedor}] para={a.direccion} cuerpo={msg.cuerpo}")
        return ResultadoEntrega(ok=True, proveedor=self.proveedor)
