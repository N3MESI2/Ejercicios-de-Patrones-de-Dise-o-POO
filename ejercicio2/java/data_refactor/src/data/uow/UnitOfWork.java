package data.uow;
import data.repo.OrderRepository;
public interface UnitOfWork {
    <T> T runInTx(Work<T> work);
    OrderRepository orders();
    interface Work<T> { T apply(); }
}
