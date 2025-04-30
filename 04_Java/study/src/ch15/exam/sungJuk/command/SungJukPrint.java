package ch15.exam.sungJuk.command;

import ch15.exam.sungJuk.SungJukDTO;

import java.util.ArrayList;

public class SungJukPrint implements SungJuk {
    @Override
    public void execute(ArrayList<SungJukDTO> list) {
        if (!list.isEmpty()) {
            for (SungJukDTO sungJuk : list) {
                System.out.println(sungJuk);
            }
        } else {
            System.out.println("입력된 성적이 없습니다.");
        }
    }
}
