package py4jJavaCalcServer;

import py4j.GatewayServer;

import java.util.Map;
import java.util.HashMap;

// just to call the example
import java.util.concurrent.Executors;
import java.util.concurrent.ScheduledExecutorService;
import java.util.concurrent.TimeUnit;

public class PythonServiceApp {

    /**
     * All public methods of this class shall be available in the Python application.
     * The Python app is public, so stay safe!
    * */

    // ScriptName -> PythonCallback
    private Map<String, PythonScriptCallback> python_callbacks = new HashMap<String, PythonScriptCallback>();

    private Boolean isCalcServerAlive;

    // Called from Python application on startup
    public void setPythonCalcServerStatusAlive(){
        System.out.println("Python server is alive");
        this.isCalcServerAlive = true;
    }

    // Called from Python application on shutdown
    public void setPythonCalcServerStatusDead(){
        System.out.println("Python server is dead");
        this.isCalcServerAlive = false;
    }

    // Called multiple times from python on startup (by no means this thing is safe)
    public void registerCallback(PythonScriptCallback py_callback){
        String callback_name = (String)py_callback.get_script_name();
        this.python_callbacks.put(callback_name, py_callback);
        System.out.println(String.format("a callback listener for %s is registered", callback_name));
    }

    // Called from Java application when the user wants to call python script (from script editor)
    private double callPythonScript(String script_name){
        if (this.python_callbacks.containsKey(script_name)) {
            PythonScriptCallback callback = this.python_callbacks.get(script_name);

            HashMap<String, Double> calc_context = new HashMap<String, Double>();
            calc_context.put("Attr1", 10.0);
            calc_context.put("Attr2", 20.0);
            return (double)callback.calculate(calc_context);
        }
        System.out.println(String.format("we've got an exceptional situation with %s script here", script_name));
        throw new java.lang.RuntimeException(String.format("python script %s is not registered", script_name));
    }

    @Override
    public String toString() {
        return "<PythonServiceApp> instance";
    }

    /* main loop */
    public static void main(String[] args) {
        PythonServiceApp pyapp = new PythonServiceApp();
        GatewayServer gatewayServer = new GatewayServer(pyapp);
        gatewayServer.start(true);
        System.out.println("Gateway Server Started");

        // Usage example

        // You have 5 seconds to start python app
        int delay_for_python_startup = 5;
        int call_interval = 1;  // seconds
        // Start calling python scripts every call_interval seconds

        final ScheduledExecutorService executorService = Executors.newSingleThreadScheduledExecutor();
        executorService.scheduleAtFixedRate(() -> pyapp.someoneCallsScript(),
                                            delay_for_python_startup,
                                            call_interval,
                                            TimeUnit.SECONDS);

        final ScheduledExecutorService executorService2 = Executors.newSingleThreadScheduledExecutor();
        executorService2.scheduleAtFixedRate(() -> pyapp.someoneCallsOtherScript(),
                                             delay_for_python_startup,
                                             call_interval,
                                             TimeUnit.SECONDS);
    }

    // imitate user calling a script
    private void someoneCallsScript() {
        System.out.println("going to calc...");
        double calc_result = this.callPythonScript("HeavyCall");
        System.out.println(String.format("calc result is %f", calc_result));
    }

    // imitate user calling another script
    private void someoneCallsOtherScript() {
        System.out.println("going to calc...");
        double calc_result = this.callPythonScript("SomeLogisticRegression");
        System.out.println(String.format("calc result is %f", calc_result));
    }



}