from __future__ import annotations
from .contracts import PaymentGateway, PaymentIntent, ProviderResult, Money

class StripeAdapter(PaymentGateway):
    def authorize(self, intent: PaymentIntent) -> ProviderResult:
        return ProviderResult(ok=True, provider="stripe", status="autorizado")
    def capture(self, intent_id: str, amount: Money | None = None) -> ProviderResult:
        return ProviderResult(ok=True, provider="stripe", status="capturado")
    def refund(self, payment_id: str, amount: Money | None = None) -> ProviderResult:
        return ProviderResult(ok=True, provider="stripe", status="reembolsado")
    def webhook_handler(self, headers, body) -> str:
        return "ok"

class MercadoPagoAdapter(PaymentGateway):
    def authorize(self, intent: PaymentIntent) -> ProviderResult:
        return ProviderResult(ok=True, provider="mercadopago", status="autorizado")
    def capture(self, intent_id: str, amount: Money | None = None) -> ProviderResult:
        return ProviderResult(ok=True, provider="mercadopago", status="capturado")
    def refund(self, payment_id: str, amount: Money | None = None) -> ProviderResult:
        return ProviderResult(ok=True, provider="mercadopago", status="reembolsado")
    def webhook_handler(self, headers, body) -> str:
        return "ok"

class LocalBankAdapter(PaymentGateway):
    def authorize(self, intent: PaymentIntent) -> ProviderResult:
        return ProviderResult(ok=True, provider="banco_local", status="autorizado")
    def capture(self, intent_id: str, amount: Money | None = None) -> ProviderResult:
        return ProviderResult(ok=True, provider="banco_local", status="capturado")
    def refund(self, payment_id: str, amount: Money | None = None) -> ProviderResult:
        return ProviderResult(ok=True, provider="banco_local", status="reembolsado")
    def webhook_handler(self, headers, body) -> str:
        return "ok"
