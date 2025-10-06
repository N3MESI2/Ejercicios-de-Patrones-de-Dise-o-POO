package data.repo;
import java.util.*;
import data.domain.Order;
public interface OrderRepository {
    Optional<Order> get(int id);
    List<Order> findByCustomer(int customerId, int limit, int offset);
    int save(Order order);
    void delete(int id);
}
