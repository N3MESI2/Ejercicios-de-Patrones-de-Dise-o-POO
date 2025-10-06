from __future__ import annotations
from typing import Optional
from time import monotonic
from .contracts import PaymentGateway
from .adapters import StripeAdapter, MercadoPagoAdapter, LocalBankAdapter

class GatewayFactory:
    def for_provider(self, name: str) -> PaymentGateway:
        name = name.lower()
        if name == "stripe":
            return CircuitBreaker(StripeAdapter())
        if name in ("mp","mercadopago"):
            return CircuitBreaker(MercadoPagoAdapter())
        if name in ("local","banco_local"):
            return CircuitBreaker(LocalBankAdapter())
        raise ValueError(f"Proveedor desconocido {name}")

class CircuitBreaker(PaymentGateway):
    def __init__(self, inner: PaymentGateway, threshold: int = 3, cooldown: float = 5.0):
        self.inner = inner
        self.failures = 0
        self.threshold = threshold
        self.cooldown = cooldown
        self.next_try = 0.0

    def _check(self):
        if self.failures >= self.threshold and monotonic() < self.next_try:
            raise RuntimeError("circuito abierto")
        if self.failures >= self.threshold and monotonic() >= self.next_try:
            self.failures = 0  # medio-abierto

    def _wrap(self, fn, *args, **kwargs):
        self._check()
        try:
            res = fn(*args, **kwargs)
            return res
        except Exception as e:
            self.failures += 1
            from time import monotonic as _m
            self.next_try = _m() + self.cooldown
            raise

    def authorize(self, *a, **k): return self._wrap(self.inner.authorize, *a, **k)
    def capture(self, *a, **k):   return self._wrap(self.inner.capture, *a, **k)
    def refund(self, *a, **k):    return self._wrap(self.inner.refund, *a, **k)
    def webhook_handler(self, *a, **k): return self.inner.webhook_handler(*a, **k)
