package notifications.contracts;
public interface NotificationSender {
    DeliveryResult send(Recipient to, RenderedMessage msg);
}
