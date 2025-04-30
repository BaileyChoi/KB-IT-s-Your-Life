package ch15.exam.sungJuk.command;

import ch15.exam.sungJuk.SungJukDTO;

import java.util.ArrayList;
import java.util.Scanner;

public class SungJukDelete implements SungJuk{
    @Override
    public void execute(ArrayList<SungJukDTO> list) {
        Scanner scanner = new Scanner(System.in);

        System.out.print("삭제할 이름 입력 : ");
        String name = scanner.nextLine();

        int deletedCount = 0;

        for (int i =0; i < list.size(); i++) {
            SungJukDTO sj = list.get(i);
            if (sj.getName().equals(name)) {
                list.remove(i);
                deletedCount++;
                i--;
            }
        }

        if (deletedCount == 0) {
            System.out.println("회원의 정보가 없습니다.");
        } else {
            System.out.println(deletedCount + "건의 항목을 삭제하였습니다.");
        }
    }
}
