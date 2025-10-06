package notifications.strategies;
import notifications.contracts.*;
public class PaymentFailedSmsStrategy implements NotificationStrategy {
    @Override public boolean canHandle(String eventName, Channel channel){
        return "PaymentFailed".equals(eventName) && channel == Channel.SMS;
    }
    @Override public RenderedMessage render(Event event, UserPrefs prefs){
        var orderId = String.valueOf(event.payload().get("orderId"));
        return new RenderedMessage("Pago fallido", "Tu pago para la orden "+orderId+" fue rechazado.");
    }
}
