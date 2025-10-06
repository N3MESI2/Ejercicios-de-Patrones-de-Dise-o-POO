package notifications.app;
import notifications.contracts.*;
import java.util.List;
public class NotificationService {
    private final java.util.List<NotificationStrategy> strategies;
    private final NotificationFactory factory;
    public NotificationService(java.util.List<NotificationStrategy> strategies, NotificationFactory factory){
        this.strategies = strategies;
        this.factory = factory;
    }
    public void onEvent(Event event){
        var recs = java.util.List.of(
            new Recipient("u1","u1@example.com", Channel.EMAIL),
            new Recipient("u1","+5493700000000", Channel.SMS)
        );
        var prefs = new UserPrefs("es-AR", java.util.List.of(Channel.EMAIL, Channel.SMS));
        for (var r : recs){
            var strat = strategies.stream().filter(s -> s.canHandle(event.name(), r.channel())).findFirst().orElse(null);
            if (strat == null) continue;
            var msg = strat.render(event, prefs);
            var sender = factory.forChannel(r.channel(), null);
            sender.send(r, msg);
        }
    }
}
