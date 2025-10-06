package payments.adapters;
import payments.contracts.*;
public class MercadoPagoAdapter implements PaymentGateway {
    @Override public ProviderResult authorize(PaymentIntent intent){ return new ProviderResult(true, "mercadopago", "autorizado", null); }
    @Override public ProviderResult capture(String intentId, Money amount){ return new ProviderResult(true, "mercadopago", "capturado", null); }
    @Override public ProviderResult refund(String paymentId, Money amount){ return new ProviderResult(true, "mercadopago", "reembolsado", null); }
    @Override public String webhookHandler(java.util.Map<String,String> headers, Object body){ return "ok"; }
}
