package Facade.pagemaker;

import lombok.NoArgsConstructor;

import java.io.FileReader;
import java.io.IOException;
import java.util.Properties;

@NoArgsConstructor
public class Database {
    //데이터베이스 이름에서 Properties를 얻는다
    public static Properties getProperties(String dbname) throws IOException {
        String filename = "04_Java/DesignPattern/src/Facade/" + dbname + ".txt";
        Properties prop = new Properties();
        prop.load(new FileReader(filename));
        return prop;
    }

}
