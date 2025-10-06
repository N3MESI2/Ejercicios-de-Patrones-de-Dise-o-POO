package notifications.infra;
import notifications.contracts.*;
public class PushSender implements NotificationSender {
    private final String provider;
    public PushSender(String provider){ this.provider = provider == null ? "fcm" : provider; }
    @Override public DeliveryResult send(Recipient to, RenderedMessage msg){
        System.out.println("[PUSH::"+provider+"] para="+to.address()+" cuerpo="+msg.body());
        return new DeliveryResult(true, provider, null);
    }
}
