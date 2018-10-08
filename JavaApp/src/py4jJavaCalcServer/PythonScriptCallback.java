package py4jJavaCalcServer;

public interface PythonScriptCallback {

    Object get_script_name();  // (String)

    Object calculate(Object obj);  // (float)

}
