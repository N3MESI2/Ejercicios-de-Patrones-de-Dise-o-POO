import notifications.contracts.*;
import notifications.infra.*;
import notifications.strategies.*;
import notifications.app.*;
import java.util.Map;
import java.util.List;
public class Main {
    public static void main(String[] args){
        var service = new NotificationService(
            List.of(new WelcomeEmailStrategy(), new PaymentFailedSmsStrategy()),
            new DefaultFactory()
        );
        service.onEvent(new Event("e1","UserRegistered", Map.of("name","Tomás"), System.currentTimeMillis(), Map.of()));
        service.onEvent(new Event("e2","PaymentFailed", Map.of("orderId","A123"), System.currentTimeMillis(), Map.of()));
    }
}
