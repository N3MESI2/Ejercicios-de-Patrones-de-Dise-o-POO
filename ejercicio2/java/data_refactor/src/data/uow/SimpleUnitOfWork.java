package data.uow;
import data.repo.*;
public class SimpleUnitOfWork implements UnitOfWork {
    private final OrderRepository orders = new InMemoryOrderRepository();
    @Override public <T> T runInTx(Work<T> work){
        return work.apply();
    }
    @Override public OrderRepository orders(){ return orders; }
}
