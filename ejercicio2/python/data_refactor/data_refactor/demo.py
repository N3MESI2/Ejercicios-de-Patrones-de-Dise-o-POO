from __future__ import annotations
from .sqlite_repo import UnitOfWork, SqliteOrderRepository
from .domain import Order

def main():
    uow = UnitOfWork()
    with uow.transaction() as conn:
        repo = SqliteOrderRepository(conn)
        oid = repo.save(Order(id=None, customer_id=1, amount=1500.0))
        print("Creado:", repo.get(oid))
        print("Por cliente:", repo.find_by_customer(1))
        repo.save(Order(id=oid, customer_id=1, amount=1999.0))
        print("Actualizado:", repo.get(oid))
        repo.delete(oid)
        print("Eliminado → obtener:", repo.get(oid))

if __name__ == "__main__":
    main()
