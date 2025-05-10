package ch18.sec02.exam02;

import java.io.FileOutputStream;
import java.io.IOException;
import java.io.OutputStream;

public class WriteExample {
    public static void main(String[] args) {
        try (OutputStream os = new FileOutputStream("C:/KB_Bingbong/04_Java/study/src/ch18/sec02/exam02/test2.db")) {
            byte[] array = {10, 20, 30, 40, 50};

            os.write(array, 1, 3);
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
