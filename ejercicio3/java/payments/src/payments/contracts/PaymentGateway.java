package payments.contracts;
public interface PaymentGateway {
    ProviderResult authorize(PaymentIntent intent);
    ProviderResult capture(String intentId, Money amount);
    ProviderResult refund(String paymentId, Money amount);
    String webhookHandler(java.util.Map<String,String> headers, Object body);
}
