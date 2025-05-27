package Proxy;

public class Main {
    public static void main(String[] args) {
        Printable p = new PrintProxy("Bailey");
        System.out.println("이름은 현재 " + p.getPrintName() + "입니다.");
        p.setPrinterName("Bingbong");
        p.print("Hello, world!");
    }
}
