from __future__ import annotations
from typing import Optional
from .contracts import FabricaNotificacion, Canal, RemitenteNotificacion
from .senders import RemitenteEmail, RemitenteSMS, RemitentePush

class FabricaPorDefecto(FabricaNotificacion):
    def para_canal(self, canal: Canal, proveedor: Optional[str] = None) -> RemitenteNotificacion:
        if canal == Canal.EMAIL:
            return RemitenteEmail(proveedor or "sendgrid")
        if canal == Canal.SMS:
            return RemitenteSMS(proveedor or "twilio")
        if canal == Canal.PUSH:
            return RemitentePush(proveedor or "fcm")
        raise ValueError(f"Canal desconocido {canal}")
