package notifications.contracts;
public record DeliveryResult(boolean ok, String provider, String error) {}
