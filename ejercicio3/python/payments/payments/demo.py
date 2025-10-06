from __future__ import annotations
from .contracts import PaymentIntent, Money
from .factory_cb import GatewayFactory

def main():
    factory = GatewayFactory()
    gw = factory.for_provider("mercadopago")
    intent = PaymentIntent(id="pi_1", order_id="A1", amount=Money(1000,"ARS"), idempotency_key="A1-1000-ARS")
    print("Autorización:", gw.authorize(intent))
    print("Captura:", gw.capture(intent.id))
    print("Reembolso:", gw.refund("pay_1", Money(500,"ARS")))

if __name__ == "__main__":
    main()
