package payments.factory;
import payments.contracts.*;
public class CircuitBreaker implements PaymentGateway {
    private final PaymentGateway inner;
    private int failures = 0;
    private final int threshold;
    public CircuitBreaker(PaymentGateway inner){ this(inner, 3); }
    public CircuitBreaker(PaymentGateway inner, int threshold){ this.inner = inner; this.threshold = threshold; }
    private void check(){ if (failures >= threshold) throw new RuntimeException("circuito abierto"); }
    private ProviderResult run(java.util.function.Supplier<ProviderResult> s){
        check();
        try { return s.get(); } catch(Exception e){ failures++; throw e; }
    }
    @Override public ProviderResult authorize(PaymentIntent intent){ return run(() -> inner.authorize(intent)); }
    @Override public ProviderResult capture(String intentId, Money amount){ return run(() -> inner.capture(intentId, amount)); }
    @Override public ProviderResult refund(String paymentId, Money amount){ return run(() -> inner.refund(paymentId, amount)); }
    @Override public String webhookHandler(java.util.Map<String,String> headers, Object body){ return inner.webhookHandler(headers, body); }
}
