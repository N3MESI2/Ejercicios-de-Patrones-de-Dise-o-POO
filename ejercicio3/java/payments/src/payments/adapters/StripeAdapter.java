package payments.adapters;
import payments.contracts.*;
public class StripeAdapter implements PaymentGateway {
    @Override public ProviderResult authorize(PaymentIntent intent){ return new ProviderResult(true, "stripe", "autorizado", null); }
    @Override public ProviderResult capture(String intentId, Money amount){ return new ProviderResult(true, "stripe", "capturado", null); }
    @Override public ProviderResult refund(String paymentId, Money amount){ return new ProviderResult(true, "stripe", "reembolsado", null); }
    @Override public String webhookHandler(java.util.Map<String,String> headers, Object body){ return "ok"; }
}
