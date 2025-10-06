package data.repo;
import java.util.*;
import data.domain.Order;
public class InMemoryOrderRepository implements OrderRepository {
    private final Map<Integer, Order> db = new HashMap<>();
    private int seq = 1;
    @Override public Optional<Order> get(int id){ return Optional.ofNullable(db.get(id)); }
    @Override public List<Order> findByCustomer(int customerId, int limit, int offset){
        return db.values().stream().filter(o -> o.customerId == customerId).skip(offset).limit(limit).toList();
    }
    @Override public int save(Order order){
        if (order.id == null){ order.id = seq++; }
        db.put(order.id, order);
        return order.id;
    }
    @Override public void delete(int id){ db.remove(id); }
}
