package payments.adapters;
import payments.contracts.*;
public class LocalBankAdapter implements PaymentGateway {
    @Override public ProviderResult authorize(PaymentIntent intent){ return new ProviderResult(true, "banco_local", "autorizado", null); }
    @Override public ProviderResult capture(String intentId, Money amount){ return new ProviderResult(true, "banco_local", "capturado", null); }
    @Override public ProviderResult refund(String paymentId, Money amount){ return new ProviderResult(true, "banco_local", "reembolsado", null); }
    @Override public String webhookHandler(java.util.Map<String,String> headers, Object body){ return "ok"; }
}
