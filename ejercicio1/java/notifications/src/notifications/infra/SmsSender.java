package notifications.infra;
import notifications.contracts.*;
public class SmsSender implements NotificationSender {
    private final String provider;
    public SmsSender(String provider){ this.provider = provider == null ? "twilio" : provider; }
    @Override public DeliveryResult send(Recipient to, RenderedMessage msg){
        System.out.println("[SMS::"+provider+"] para="+to.address()+" cuerpo="+msg.body());
        return new DeliveryResult(true, provider, null);
    }
}
