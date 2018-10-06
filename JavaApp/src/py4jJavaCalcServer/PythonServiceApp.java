package py4jJavaCalcServer;

import py4j.GatewayServer;

import java.util.ArrayList;
import java.util.List;

public class PythonServiceApp {

    private List<PythonListenerInterface> listeners = new ArrayList<PythonListenerInterface>();

    public void registerListener(PythonListenerInterface listener) {
        System.out.println("a listener is registered");
        listeners.add(listener);
    }

    public void notifyAllListeners() {
        System.out.println("notification call");
        for (PythonListenerInterface listener: listeners) {
            Object returnValue = listener.notify(this);
            System.out.println(returnValue);
        }
    }

    @Override
    public String toString() {
        return "<PythonServiceApp> instance";
    }

    public static void main(String[] args) {
        PythonServiceApp application = new PythonServiceApp();
        GatewayServer gatewayServer = new GatewayServer(application);
        gatewayServer.start(true);
        System.out.println("Gateway Server Started");
    }

}