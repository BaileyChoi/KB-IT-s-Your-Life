package org.scoula.main;

import org.scoula.beans.Person3;
import org.scoula.config.ProjectConfig2;
import org.scoula.config.ProjectConfig4;
import org.springframework.context.annotation.AnnotationConfigApplicationContext;

public class Main3 {
    public static void main(String[] args) {
        var context = new AnnotationConfigApplicationContext(ProjectConfig4.class);

        Person3 p = context.getBean(Person3.class);

        System.out.println("Person's name: " + p.getName());
        System.out.println("Person's parrot: " + p.getParrot());
    }
}
