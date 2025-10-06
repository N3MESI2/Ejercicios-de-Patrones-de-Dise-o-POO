package payments.contracts;
public record PaymentIntent(String id, String orderId, Money amount, String idempotencyKey) {}
