package ch14.exam;

public class ThreadExample {
    public static void main(String[] args) {
        MovieThread movieThread = new MovieThread();
        MusicRunnable musicRunnable = new MusicRunnable();

        Thread musicThread = new Thread(musicRunnable);

        movieThread.start();
        musicThread.start();
    }
}
