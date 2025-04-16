package ch06.exam;

public class DatabaseExample {
    public static void main(String[] args) {
        Database database1 = Database.getInstance();

        System.out.println("데이터베이스:" + database1.connect());
        database1.close();
    }



}
