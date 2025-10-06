package notifications.infra;
import notifications.contracts.*;
public class DefaultFactory implements NotificationFactory {
    @Override public NotificationSender forChannel(Channel channel, String provider){
        return switch (channel) {
            case EMAIL -> new EmailSender(provider);
            case SMS -> new SmsSender(provider);
            case PUSH -> new PushSender(provider);
        };
    }
}
