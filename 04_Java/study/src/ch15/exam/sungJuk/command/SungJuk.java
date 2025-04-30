package ch15.exam.sungJuk.command;

import ch15.exam.sungJuk.SungJukDTO;

import java.util.ArrayList;

public interface SungJuk {
    public void execute(ArrayList<SungJukDTO> list);
}
