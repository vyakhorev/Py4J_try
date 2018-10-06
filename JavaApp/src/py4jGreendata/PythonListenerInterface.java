package py4jGreendata;

public interface PythonListenerInterface {
    /*
    * An instance implementing this interface shall be received
    * from Python code.
    * We can't define concrete classes for this purpose, only
    * interfaces.
    * */

    Object notify(Object source);

}
