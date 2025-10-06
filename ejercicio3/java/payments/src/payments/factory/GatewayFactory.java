package payments.factory;
import payments.contracts.*;
import payments.adapters.*;
public class GatewayFactory {
    public PaymentGateway forProvider(String name){
        name = name.toLowerCase();
        PaymentGateway gw = switch (name) {
            case "stripe" -> new StripeAdapter();
            case "mp", "mercadopago" -> new MercadoPagoAdapter();
            case "local", "banco_local" -> new LocalBankAdapter();
            default -> throw new IllegalArgumentException("Proveedor desconocido "+name);
        };
        return new CircuitBreaker(gw);
    }
}
