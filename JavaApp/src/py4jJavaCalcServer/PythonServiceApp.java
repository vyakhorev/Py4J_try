package py4jJavaCalcServer;

import py4j.GatewayServer;

import java.util.ArrayList;
import java.util.List;
import java.util.Map;

public class PythonServiceApp {

    /**
     * All public methods of this class shall be available in the Python application
    * */

//    /* Object data interface */
//    public DBObjectReference getInstance(String DBKey) {
//        return
//    }

    public void updateObjectData(Map<Long, String> data_map) {
        for (Map.Entry<Long, String> entry : data_map.entrySet()) {
            System.out.println(entry.getKey() + "/" + entry.getValue());
        }
    }

    /* Events */

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