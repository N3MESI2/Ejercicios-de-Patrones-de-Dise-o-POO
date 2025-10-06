from dataclasses import dataclass

@dataclass
class Order:
    id: int | None
    customer_id: int
    amount: float

    def __str__(self) -> str:
        return f"Pedido(id={self.id}, clienteId={self.customer_id}, monto={self.amount:.2f})"
