package ch16.sec05.exam03;

public class Person {
    public Member getMember1(Creatable1 creatable) {
        String id = "summer";
        Member member = creatable.create(id);
        return member;
    }

    public Member getMember2(Creatable2 creatable) {
        String id = "summer";
        String name = "한여름";
        Member member = creatable.create(id, name);
        return member;
    }
}
