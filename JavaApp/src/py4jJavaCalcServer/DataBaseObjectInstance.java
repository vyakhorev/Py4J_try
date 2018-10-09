package py4jJavaCalcServer;

import java.util.HashMap;

public class DataBaseObjectInstance {
    /** Represents an object in the database
     * */

    public HashMap<Object, Object> getDataFromDatabase() {
        HashMap<Object, Object> immutable_database_data = new HashMap<Object, Object>();
        /* Some data required to calculate  */
        immutable_database_data.put("Height", 170.0);
        immutable_database_data.put("AverageIncome", 100000.0);
        immutable_database_data.put("Gender", "M");
        return immutable_database_data;
    }


}
