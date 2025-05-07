package supplement.standardAPI;

import java.util.Arrays;
import java.util.List;
import java.util.function.ToIntFunction;

public class FunctionExample2 {
    private static List<Student2> list = Arrays.asList(
            new Student2("홍길동", 90, 96),
            new Student2("신용권", 95, 93)
    );

    public static double avg(ToIntFunction<Student2> function) {
        int sum = 0;
        for (Student2 student : list) {
            sum += function.applyAsInt(student);
        }
        double avg = (double) sum / list.size();
        return avg;
    }

    public static void main(String[] args) {
        double englishAvg = avg(s -> s.getEnglishScore());
        System.out.println("영어 평균 점수: " + englishAvg);

        double mathAvg = avg(s -> s.getMathScore());
        System.out.println("수학 평균 점수: " + mathAvg);
    }
}
