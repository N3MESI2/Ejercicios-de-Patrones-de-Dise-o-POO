package notifications.contracts;
import java.util.Map;
public record Event(String id, String name, Map<String, Object> payload, long occurredAt, Map<String,String> meta) {}
