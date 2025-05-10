package ch18.sec11;

import java.io.File;
import java.io.IOException;
import java.nio.charset.Charset;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.text.SimpleDateFormat;
import java.util.Date;

public class FileExample {
    public static void main(String[] args) throws Exception {
        //File 객체 생성
        File dir = new File("04_Java/study/src/ch18/sec11/images");
        File file1 = new File("04_Java/study/src/ch18/sec11/file1.txt");
        File file2 = new File("04_Java/study/src/ch18/sec11/file2.txt");
        File file3 = new File("04_Java/study/src/ch18/sec11/file3.txt");

        //존재하지 않으면 디렉토리 또는 파일 생성
        if (!dir.exists()) {
            dir.mkdir();
        }
        if (!file1.exists()) {
            file1.createNewFile();
        }
        if (!file2.exists()) {
            file2.createNewFile();
        }
        if (!file3.exists()) {
            file3.createNewFile();
        }

        //Temp 폴더의 내용을 출력
        File temp = new File("04_Java/study/src/ch18/sec11");
        File[] contents = temp.listFiles();

        SimpleDateFormat sdf = new SimpleDateFormat("yyyy-MM-dd a HH:mm");
        for (File file : contents) {
            System.out.printf("%-25s", sdf.format(new Date(file.lastModified())));
            if (file.isDirectory()) {
                System.out.printf("%-10s%-20s", "<DIR>", file.getName());
            } else {
                System.out.printf("%-10s%-20s", file.length(), file.getName());
            }
            System.out.println();
        }
        System.out.println();

        try {
            String data = "" +
                    "id: summer\n" +
                    "email: summer@mycompany.com\n" +
                    "tel: 010-1234-1234";

            //Path 객체 생성
            Path path = Paths.get("04_Java/study/src/ch18/sec11/user.txt");

            //파일 생성 및 데이터 저장
            Files.writeString(Paths.get("04_Java/study/src/ch18/sec11/user.txt"), data, Charset.forName("UTF-8"));

            //파일 정보 얻기
            System.out.println("파일 유형: " + Files.probeContentType(path));
            System.out.println("파일 크기: " + Files.size(path) + " bytes");

            //파일 읽기
            String content = Files.readString(path, Charset.forName("UTF-8"));
            System.out.println(content);
        } catch (IOException e) {
            e.printStackTrace();
        }
    }
}
