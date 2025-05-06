package ch15.exam.sungJuk.command;

import ch15.exam.sungJuk.SungJukDTO;

import java.util.*;

public class SungJukSort implements SungJuk, Comparator<SungJukDTO> {
    @Override
    public int compare(SungJukDTO o1, SungJukDTO o2) {
        // 총점 내림차순 정렬
        if (o1.getTot() < o2.getTot()) return 1;
        else if (o1.getTot() > o2.getTot()) return -1;
        else {
            return o1.getName().compareTo(o2.getName());
        }
    }

    @Override
    public void execute(ArrayList<SungJukDTO> list) {
        Scanner scanner = new Scanner(System.in);

        System.out.println("********************");
        System.out.println("1. 총점으로 내림차순");
        System.out.println("2. 이름으로 오름차순");
        System.out.println("3. 이전 메뉴");
        System.out.println("********************");

        System.out.print("번호 : ");
        int no = scanner.nextInt();

        switch (no) {
            case 1:
                Collections.sort(list, this);
                System.out.println("총점으로 내림차순 정렬");
                break;
            case 2:
                Collections.sort(list, new Comparator<SungJukDTO>() {
                    @Override
                    public int compare(SungJukDTO o1, SungJukDTO o2) {
                        return o1.getName().compareTo(o2.getName());
                    }
                });
                System.out.println("이름으로 오름차순 정렬");
                break;
            case 3:
                return;
            default:
                System.out.println("잘못된 선택입니다.");
        }

        for (SungJukDTO sj: list) {
            System.out.println(sj);
        }
    }
}
