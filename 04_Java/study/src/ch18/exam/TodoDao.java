package ch18.exam;

import java.io.*;
import java.util.HashMap;

public class TodoDao  {
    HashMap<Integer, Todo> data;
    int maxId;

    private static TodoDao instance = new TodoDao();

    private TodoDao() {
    }

    public void load() {
        File file = new File("./todo.dat");
        if (file.exists()) {
            try(ObjectInputStream oi = new ObjectInputStream(new FileInputStream(file))) {
                maxId = oi.readInt();
                data = (HashMap<Integer, Todo>) oi.readObject();
            } catch (Exception e) {
                System.out.println("파일 읽기 에러 : " + e.getMessage());
            }
        } else {
            data = new HashMap<>();
            data.put(1, new Todo(1, "ES6 학습", "ES6 심화 과정 실습하기", false));
            data.put(2, new Todo(2, "React 학습", "React 기초 공부하기", false));
            data.put(3, new Todo(3, "ContextAPI 학습", "컨텍스트 훅 공부하기", false));
            data.put(4, new Todo(4, "야구 경기 관람", "NC대 두산 야구 관람하기", true));
            data.put(5, new Todo(5, "Java 공부", "Java 컬렉션 공부하기", false));
            maxId = 6;
        }
    }

    public void save() {
        File file = new File("./todo.dat");

        try(ObjectOutputStream oo = new ObjectOutputStream(new FileOutputStream(file))) {
            oo.writeInt(maxId);
            oo.writeObject(data);
            oo.flush();
        } catch (Exception e) {
            System.err.println("파일 쓰기 에러 : " + e.getMessage());
        }
    }
}
