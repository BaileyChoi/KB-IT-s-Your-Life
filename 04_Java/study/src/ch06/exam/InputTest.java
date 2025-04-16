package ch06.exam;

public class InputTest {
    public static void main(String[] args) {
        Input myInput = new Input();

        String read1 = myInput.read("이름");
        System.out.println("입력값: " + read1);

        String read2 = myInput.read("이름", "홍길동");
        System.out.println("입력값: " + read2);

        int readInt = myInput.readInt("나이");
        System.out.println("입력값: " + readInt);

        boolean confirm1 = myInput.confirm("종료할까요?", true);
        System.out.println("입력값: " + String.valueOf(confirm1));

        boolean confirm2 = myInput.confirm("종료할까요?");
        System.out.println("입력값: " + String.valueOf(confirm2));
    }
}
