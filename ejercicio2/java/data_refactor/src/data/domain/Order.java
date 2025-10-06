package data.domain;
public class Order {
    public Integer id;
    public int customerId;
    public double amount;
    public Order(Integer id, int customerId, double amount){
        this.id = id; this.customerId = customerId; this.amount = amount;
    }
    @Override public String toString(){ return "Pedido{id=%s, clienteId=%s, monto=%.2f}".formatted(id, customerId, amount); }
}
