package supplement.standardAPI;

import java.util.Arrays;
import java.util.List;
import java.util.function.Function;
import java.util.function.ToIntFunction;

public class FunctionExample1 {
    private static List<Student2> list = Arrays.asList(
            new Student2("홍길동", 90, 96),
            new Student2("신용권", 95, 93)
    );

    public static void printString(Function<Student2, String> function) {
        for (Student2 student : list) {
            System.out.print(function.apply(student) + " ");
        }
        System.out.println();
    }

    public static void printInt(ToIntFunction<Student2> function) {
        for (Student2 student : list) {
            System.out.print(function.applyAsInt(student) + " ");
        }
        System.out.println();
    }

    public static void main(String[] args) {
        System.out.println("[학생 이름]");
        printString(t -> t.getName());
        System.out.println("[영어 점수]");
        printInt(t -> t.getEnglishScore());
        System.out.println("[수학 점수]");
        printInt(t -> t.getMathScore());
    }
}
