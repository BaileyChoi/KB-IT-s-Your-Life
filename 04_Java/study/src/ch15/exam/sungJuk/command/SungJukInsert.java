package ch15.exam.sungJuk.command;

import ch15.exam.sungJuk.SungJukDTO;

import java.util.ArrayList;
import java.util.Scanner;

public class SungJukInsert implements SungJuk {
    @Override
    public void execute(ArrayList<SungJukDTO> list) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("번호 입력 : ");
        int no = scanner.nextInt();

        scanner.nextLine();

        System.out.print("이름 입력 : ");
        String name = scanner.nextLine();

        System.out.print("국어 입력 : ");
        int ko = scanner.nextInt();

        System.out.print("영어 입력 : ");
        int eng = scanner.nextInt();

        System.out.print("수학 입력 : ");
        int math = scanner.nextInt();

        SungJukDTO sungJuk = new SungJukDTO(no, name, ko, eng, math);
        sungJuk.calc();

        list.add(sungJuk);

        System.out.println("입력되었습니다");
    }
}
