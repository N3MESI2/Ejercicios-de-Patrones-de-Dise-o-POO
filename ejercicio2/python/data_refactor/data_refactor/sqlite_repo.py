from __future__ import annotations
import sqlite3
from typing import List, Optional
from contextlib import contextmanager
from .domain import Order
from .repositories import OrderRepository

class UnitOfWork:
    def __init__(self, db_path: str = ":memory:"):
        self.conn = sqlite3.connect(db_path)
        self.conn.execute("CREATE TABLE IF NOT EXISTS orders(id INTEGER PRIMARY KEY, customer_id INTEGER, amount REAL)")
        self.conn.commit()

    @contextmanager
    def transaction(self):
        try:
            yield self.conn
            self.conn.commit()
        except Exception:
            self.conn.rollback()
            raise

class SqliteOrderRepository(OrderRepository):
    def __init__(self, conn: sqlite3.Connection):
        self.conn = conn

    def get(self, id: int) -> Optional[Order]:
        cur = self.conn.execute("SELECT id, customer_id, amount FROM orders WHERE id=?", (id,))
        row = cur.fetchone()
        return Order(*row) if row else None

    def find_by_customer(self, customer_id: int, limit: int = 100, offset: int = 0) -> List[Order]:
        cur = self.conn.execute("SELECT id, customer_id, amount FROM orders WHERE customer_id=? LIMIT ? OFFSET ?", (customer_id, limit, offset))
        return [Order(*r) for r in cur.fetchall()]

    def save(self, order: Order) -> int:
        if order.id is None:
            cur = self.conn.execute("INSERT INTO orders(customer_id, amount) VALUES (?,?)", (order.customer_id, order.amount))
            return cur.lastrowid
        else:
            self.conn.execute("UPDATE orders SET customer_id=?, amount=? WHERE id=?", (order.customer_id, order.amount, order.id))
            return order.id

    def delete(self, id: int) -> None:
        self.conn.execute("DELETE FROM orders WHERE id=?", (id,))
