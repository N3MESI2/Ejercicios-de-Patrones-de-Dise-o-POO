from __future__ import annotations
from time import time
from .contracts import BusEventos, Evento
from .strategies import BienvenidaEmail, PagoFallidoSMS
from .factory import FabricaPorDefecto
from .service import ServicioNotificaciones

def main():
    bus = BusEventos()
    servicio = ServicioNotificaciones(bus, [BienvenidaEmail(), PagoFallidoSMS()], FabricaPorDefecto())

    bus.publicar(Evento(id="e1", nombre="UsuarioRegistrado", payload={"nombre":"Tomás"}, ocurrido_en=time(), meta={}))
    bus.publicar(Evento(id="e2", nombre="PagoFallido", payload={"ordenId":"A123"}, ocurrido_en=time(), meta={}))

if __name__ == "__main__":
    main()
