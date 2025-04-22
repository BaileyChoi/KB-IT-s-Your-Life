package Adapter.exam02;

public class PrintBanner extends Print {
    private Banner banner;  // 위임 객체

    public PrintBanner(String string) {
        this.banner = new Banner(string);
    }

    public PrintBanner(Banner banner) {
        this.banner = banner;
    }

    @Override
    public void printWeak() {
        banner.showWithParen(); // 기능 위임
    }

    @Override
    public void printStrong() {
        banner.showWithAster(); // 기능 위임
    }
}
