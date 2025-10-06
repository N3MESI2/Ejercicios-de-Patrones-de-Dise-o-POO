package notifications.contracts;
public interface NotificationFactory {
    NotificationSender forChannel(Channel channel, String provider);
}
