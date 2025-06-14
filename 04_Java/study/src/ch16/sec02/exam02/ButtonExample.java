package ch16.sec02.exam02;

public class ButtonExample {
    public static void main(String[] args) {
        Button btnOk = new Button();

        //Ok 버튼 객체에 람다식(ClickListener 익명 구현 객체) 주입
        btnOk.setClickListener(() -> {
            System.out.println("Ok 버튼 클릭");
        });

        btnOk.click();  //Ok 버튼 클릭하기

        Button btnCancel = new Button();

        //Cancel 버튼 객체에 람다식(ClickListener 익명 구현 객체) 주입
        btnCancel.setClickListener(() -> {
            System.out.println("Cancel 버튼 클릭");
        });

        btnCancel.click(); //Cancel 버튼 클릭하기
    }
}
