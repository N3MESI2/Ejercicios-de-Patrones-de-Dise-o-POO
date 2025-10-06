from __future__ import annotations
from typing import Protocol, Dict, Any, Optional
from dataclasses import dataclass

@dataclass
class Money:
    amount: int
    currency: str

@dataclass
class PaymentIntent:
    id: str
    order_id: str
    amount: Money
    idempotency_key: str

@dataclass
class ProviderResult:
    ok: bool
    provider: str
    status: str
    error: Optional[str] = None

    def __str__(self) -> str:
        return f"Proveedor={self.provider} · Estado={self.status}" if self.ok else f"Proveedor={self.provider} · ERROR={self.error or 'desconocido'}"

class PaymentGateway(Protocol):
    def authorize(self, intent: PaymentIntent) -> ProviderResult: ...
    def capture(self, intent_id: str, amount: Optional[Money] = None) -> ProviderResult: ...
    def refund(self, payment_id: str, amount: Optional[Money] = None) -> ProviderResult: ...
    def webhook_handler(self, headers: Dict[str,str], body: Any) -> str: ...
