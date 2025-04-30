package ch15.exam.sungJuk.command;

import ch15.exam.sungJuk.SungJukDTO;

import java.util.ArrayList;
import java.util.Scanner;

public class SungJukUpdate implements SungJuk{
    @Override
    public void execute(ArrayList<SungJukDTO> list) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("번호 입력 : ");
        int no = scanner.nextInt();

        SungJukDTO selectedSungJuk = null;

        for (SungJukDTO sj: list) {
            if (sj.getNo() == no) {
                selectedSungJuk = sj;
                break;
            }
        }

        if (selectedSungJuk == null) {
            System.out.println("잘못된 번호 입니다.");
            return;
        }

        System.out.println(selectedSungJuk);

        System.out.print("수정할 이름 입력 : ");
        scanner.nextLine();
        String name = scanner.nextLine();

        System.out.print("수정할 국어 입력 : ");
        int kor = scanner.nextInt();
        System.out.print("수정할 영어 입력 : ");
        int eng = scanner.nextInt();
        System.out.print("수정할 수학 입력 : ");
        int math = scanner.nextInt();

        selectedSungJuk.setName(name);
        selectedSungJuk.setKor(kor);
        selectedSungJuk.setEng(eng);
        selectedSungJuk.setMath(math);

        selectedSungJuk.calc();

        System.out.println("수정하였습니다.");
    }
}
