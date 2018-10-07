package py4jJavaCalcServer;

public interface DBObjectReference {
    /**
     * Represents object instance.
     * */

     Object setGUID(Object database_ID);  // don't call it in Python

     Object getGUID(Object database_ID);


}
