package ch12.exam;

import java.text.ParseException;
import java.text.SimpleDateFormat;
import java.util.Date;
import java.util.Scanner;

public class Birthday {
    public static void main(String[] args) throws ParseException {
        Scanner scanner = new Scanner(System.in);

        System.out.print("생일 날짜 입력 (yyyyMMddHH): ");
        String input = scanner.nextLine();

        SimpleDateFormat sdf = new SimpleDateFormat("yyyyMMddHH");
        Date birthday = sdf.parse(input);

        System.out.println("내 생일: " + birthday);

        SimpleDateFormat sdf2 = new SimpleDateFormat("yyyy년 MM월 dd일 HH시 mm분 ss초");
        System.out.println("내 생일: " + sdf2.format(birthday));
    }
}
