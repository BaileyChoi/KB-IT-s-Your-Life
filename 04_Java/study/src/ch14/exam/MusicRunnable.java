package ch14.exam;

public class MusicRunnable implements Runnable {
    @Override
    public void run() {
        for (int i = 0; i < 6; i++) {
            try {
                System.out.println("음악 재생~");
                Thread.sleep(500);
            } catch (Exception e) {
            }
        }
    }
}
