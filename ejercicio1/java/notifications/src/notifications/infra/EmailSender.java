package notifications.infra;
import notifications.contracts.*;
public class EmailSender implements NotificationSender {
    private final String provider;
    public EmailSender(String provider){ this.provider = provider == null ? "sendgrid" : provider; }
    @Override public DeliveryResult send(Recipient to, RenderedMessage msg){
        System.out.println("[EMAIL::"+provider+"] para="+to.address()+" asunto="+msg.subject()+" cuerpo="+msg.body());
        return new DeliveryResult(true, provider, null);
    }
}
