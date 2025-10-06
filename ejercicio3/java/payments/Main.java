import payments.factory.*;
import payments.contracts.*;
public class Main {
    public static void main(String[] args){
        var factory = new GatewayFactory();
        var gw = factory.forProvider("mercadopago");
        var intent = new PaymentIntent("pi_1","A1", new Money(1000,"ARS"), "A1-1000-ARS");
        System.out.println("Autorización: " + gw.authorize(intent));
        System.out.println("Captura: " + gw.capture(intent.id(), intent.amount()));
        System.out.println("Reembolso: " + gw.refund("pay_1", new Money(500,"ARS")));
    }
}
