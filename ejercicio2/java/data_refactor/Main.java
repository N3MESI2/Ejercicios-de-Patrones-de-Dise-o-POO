import data.uow.*;
import data.domain.Order;
public class Main {
    public static void main(String[] args){
        UnitOfWork uow = new SimpleUnitOfWork();
        uow.runInTx(() -> {
            var id = uow.orders().save(new Order(null, 1, 1500.0));
            System.out.println("Creado: " + uow.orders().get(id));
            System.out.println("Por cliente: " + uow.orders().findByCustomer(1, 100, 0));
            uow.orders().save(new Order(id, 1, 1999.0));
            System.out.println("Actualizado: " + uow.orders().get(id));
            uow.orders().delete(id);
            System.out.println("Eliminado → obtener: " + uow.orders().get(id));
            return null;
        });
    }
}
