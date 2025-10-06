from __future__ import annotations
from .contracts import EstrategiaNotificacion, Canal, Evento, PreferenciasUsuario, MensajeRenderizado

class BienvenidaEmail(EstrategiaNotificacion):
    def puede_manejar(self, nombre_evento: str, canal: Canal) -> bool:
        return nombre_evento == "UsuarioRegistrado" and canal == Canal.EMAIL

    def renderizar(self, evento: Evento, prefs: PreferenciasUsuario) -> MensajeRenderizado:
        from datetime import datetime  # ← Import adentro del método o al inicio del archivo
        nombre = evento.payload.get("nombre", "usuario")
        fecha_legible = datetime.fromtimestamp(evento.ocurrido_en).strftime("%d/%m/%Y %H:%M:%S")

        return MensajeRenderizado(
            asunto=f"¡Bienvenido/a, {nombre}!",
            cuerpo=f"Hola {nombre}, gracias por registrarte el {fecha_legible}."
        )



class PagoFallidoSMS(EstrategiaNotificacion):
    def puede_manejar(self, nombre_evento: str, canal: Canal) -> bool:
        return nombre_evento == "PagoFallido" and canal == Canal.SMS

    def renderizar(self, evento: Evento, prefs: PreferenciasUsuario) -> MensajeRenderizado:
        orden = evento.payload.get("ordenId")
        return MensajeRenderizado(
            asunto="Pago fallido",
            cuerpo=f"Tu pago para la orden {orden} fue rechazado. Intenta nuevamente."
        )
