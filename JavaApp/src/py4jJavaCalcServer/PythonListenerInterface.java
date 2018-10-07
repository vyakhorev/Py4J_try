package py4jJavaCalcServer;

public interface PythonListenerInterface {
    /**
    * An instance implementing this interface shall be received
    * from Python code.
    * So that we can notify Python app about events going on
    * inside Java application.
    * */

    Object notify(Object source);

}
