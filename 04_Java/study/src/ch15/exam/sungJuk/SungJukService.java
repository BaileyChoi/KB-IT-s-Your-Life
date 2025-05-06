package ch15.exam.sungJuk;

import ch15.exam.sungJuk.command.*;

import java.util.*;

public class SungJukService {
    private ArrayList<SungJukDTO> list = new ArrayList<SungJukDTO>();

    public void menu() {

        Scanner scanner = new Scanner(System.in);
        boolean run = true;

        while (run) {
            System.out.println("===============");
            System.out.println("1. 입력");
            System.out.println("2. 출력");
            System.out.println("3. 수정");
            System.out.println("4. 삭제");
            System.out.println("5. 정렬");
            System.out.println("6. 끝");
            System.out.println("===============");
            System.out.print("선택> ");

            int strNum = scanner.nextInt();

            switch (strNum) {
                case 1:
                    new SungJukInsert().execute(list);
                    break;
                case 2:
                    new SungJukPrint().execute(list);
                    break;
                case 3:
                    new SungJukUpdate().execute(list);
                    break;
                case 4:
                    new SungJukDelete().execute(list);
                    break;
                case 5:
                    new SungJukSort().execute(list);
                    break;
                case 6:
                    run = false;
                    break;
                default:
                    System.out.println("1 ~ 6번 중에 선택하세요.");
                    break;
            }

        }
    }
}
