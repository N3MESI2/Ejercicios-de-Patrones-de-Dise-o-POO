package notifications.strategies;
import notifications.contracts.*;
public class WelcomeEmailStrategy implements NotificationStrategy {
    @Override public boolean canHandle(String eventName, Channel channel){
        return "UserRegistered".equals(eventName) && channel == Channel.EMAIL;
    }
    @Override public RenderedMessage render(Event event, UserPrefs prefs){
        var name = String.valueOf(event.payload().getOrDefault("name","usuario"));
        return new RenderedMessage("¡Bienvenido/a, "+name+"!", "Hola "+name+", gracias por registrarte.");
    }
}
