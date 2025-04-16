package ch06.sec13.exam03.package2;

import ch06.sec13.exam03.package1.*;

public class C {
    public C() {
        //객체 생성
        A a = new A();

        //필드값 변경
        a.field1 = 1; // (o)
        //a.field2 = 1; // (x) → 패키지가 다르면 default 접근 불가(컴파일 에러)
        //a.field3 = 1; // (x) → private 접근 불가(컴파일 에러)

        //메소드 호출
        a.method1(); // (o)
        //a.method2(); // (x) → 패키지가 다르면 default 접근 불가(컴파일 에러)
        //a.method3(); // (x) → private 접근 불가(컴파일 에러)
    }
}
