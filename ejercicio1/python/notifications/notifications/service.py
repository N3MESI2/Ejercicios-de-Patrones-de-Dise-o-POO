from __future__ import annotations
from typing import List
from .contracts import Evento, BusEventos, EstrategiaNotificacion, FabricaNotificacion, Destinatario, Canal, PreferenciasUsuario

class ServicioNotificaciones:
    def __init__(self, bus: BusEventos, estrategias: List[EstrategiaNotificacion], fabrica: FabricaNotificacion):
        self.bus = bus
        self.estrategias = estrategias
        self.fabrica = fabrica
        self.bus.suscribir(self.on_evento)

    def on_evento(self, evento: Evento) -> None:
        destinatarios = [
            Destinatario(id="u1", direccion="u1@example.com", canal=Canal.EMAIL),
            Destinatario(id="u1", direccion="+5493700000000", canal=Canal.SMS),
        ]
        prefs = PreferenciasUsuario(locale="es-AR", canales=[Canal.EMAIL, Canal.SMS])
        for r in destinatarios:
            estr = next((s for s in self.estrategias if s.puede_manejar(evento.nombre, r.canal)), None)
            if not estr:
                continue
            msg = estr.renderizar(evento, prefs)
            remitente = self.fabrica.para_canal(r.canal, None)
            remitente.enviar(r, msg)
