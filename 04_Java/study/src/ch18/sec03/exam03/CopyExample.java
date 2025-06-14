package ch18.sec03.exam03;

import java.io.FileInputStream;
import java.io.FileOutputStream;
import java.io.InputStream;
import java.io.OutputStream;

public class CopyExample {
    public static void main(String[] args) {
        String originalFileName = "C:/KB_Bingbong/04_Java/study/src/ch18/sec03/exam03/originalFile1.jpg";
        String targetFileName = "C:/KB_Bingbong/04_Java/study/src/ch18/sec03/exam03/originalFile2.jpg";

        try (
                InputStream is = new FileInputStream(originalFileName);
                OutputStream os = new FileOutputStream(targetFileName);
        ) {

            byte[] data = new byte[1024];  // 배열 버퍼 생성
            while (true) {
                int num = is.read(data);    // 최대 1024바이트 읽기
                if (num == -1) break;       // 파일을 다 읽으면 while 문 종료
                os.write(data, 0, num); // 읽은 데이터 파일에 쓰기
            }

            os.flush(); // 내부 버퍼 잔류 바이트를 출력하고 버퍼를 비움
            System.out.println("복사가 잘 되었습니다.");
        } catch (Exception e) {
            e.printStackTrace();
        }
    }
}

