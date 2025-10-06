package payments.contracts;
public record ProviderResult(boolean ok, String provider, String status, String error) {
    @Override public String toString(){
        if (ok) return "Proveedor=%s · Estado=%s".formatted(provider, status);
        return "Proveedor=%s · ERROR=%s".formatted(provider, error == null ? "desconocido" : error);
    }
}
