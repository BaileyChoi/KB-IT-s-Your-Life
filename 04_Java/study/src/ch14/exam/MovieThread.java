package ch14.exam;

public class MovieThread extends Thread {
    @Override
    public void run() {
        for (int i = 0; i < 3; i++) {
            try {
                System.out.println("동영상 재생!");
                Thread.sleep(1000);
            } catch (Exception e) {
            }
        }
    }
}
