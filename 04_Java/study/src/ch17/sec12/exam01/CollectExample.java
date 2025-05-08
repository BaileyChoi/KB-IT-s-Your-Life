package ch17.sec12.exam01;

import java.util.ArrayList;
import java.util.List;
import java.util.Map;
import java.util.stream.Collectors;

public class CollectExample {
    public static void main(String[] args) {
        List<Student> totalList = new ArrayList<>();
        totalList.add(new Student("홍길동", "남", 92));
        totalList.add(new Student("김수영", "여", 87));
        totalList.add(new Student("감자바", "남", 95));
        totalList.add(new Student("오해영", "여", 93));

        //Stream 없이 남학생 출력
        for (Student student : totalList) {
            if (student.getSex().equals("남")) {
                System.out.println(student.getName());
            }
        }
        System.out.println();

        // 스트림을 사용하는 경우
        //남학생만 묶어 List 생성
        List<Student> maleList = totalList.stream()
                .filter(s -> s.getSex().equals("남"))
                .toList();

        maleList.forEach(s -> System.out.println(s.getName()));
        System.out.println();

        maleList.stream()
                .map(Student::getName)
                .forEach(System.out::println);

//        List<Student> maleList = totalList.stream()
//                .filter(s -> s.getSex().equals("남"))
//                .collect(Collectors.toList());

        System.out.println();

        //성적으로 내림차순 정렬, 하위 2명을 추출
        List<Student> topList = totalList.stream()
                .sorted((s1, s2) -> Integer.compare(s2.getScore(), s1.getScore()))
                .limit(2)
                .toList();

        topList.forEach(s -> System.out.println(s.getName() + ": " + s.getScore()));
        System.out.println();

        //학생 이름을 키, 학생의 점수를 값으로 갖는 Map 생성
        Map<String, Integer> map = totalList.stream()
                .collect(
                        Collectors.toMap(
                                Student::getName,   //Student 객체에서 키가 될 부분 리턴
                                Student::getScore   //Student 객체에서 값이 될 부분 리턴
                        )
                );
        System.out.println(map);
        System.out.println();


    }
}
