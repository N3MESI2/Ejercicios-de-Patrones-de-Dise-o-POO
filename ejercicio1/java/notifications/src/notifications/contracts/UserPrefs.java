package notifications.contracts;
import java.util.List;
public record UserPrefs(String locale, List<Channel> channels) {}
