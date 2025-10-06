package notifications.contracts;
public interface NotificationStrategy {
    boolean canHandle(String eventName, Channel channel);
    RenderedMessage render(Event event, UserPrefs prefs);
}
