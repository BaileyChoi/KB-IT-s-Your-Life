package supplement.standardAPI;

import java.util.Arrays;
import java.util.List;
import java.util.function.Predicate;

public class PredicateExample {
    private static List<Student1> list = Arrays.asList(
            new Student1("홍길동", "남자", 90),
            new Student1("김순희", "여자", 90),
            new Student1("감자바", "남자", 95),
            new Student1("박한나", "여자", 92)
    );

    public static double avg(Predicate<Student1> predicate) {
        int count = 0, sum = 0;
        for (Student1 Student1 : list) {
            if (predicate.test(Student1)) {
                count++;
                sum += Student1.getScore();
            }
        }
        return (double) sum / count;
    }

    public static void main(String[] args) {
        double maleAvg = avg(t -> t.getSex().equals("남자"));
        System.out.println("남자 평균 점수: " + maleAvg);


        double femaleAvg = avg(t -> t.getSex().equals("여자"));
        System.out.println("여자 평균 점수: " + femaleAvg);
    }
}
