package org.scoula.main;

import org.scoula.beans.Person4;
import org.scoula.config.ProjectConfig4;
import org.springframework.context.annotation.AnnotationConfigApplicationContext;

public class Main4 {
    public static void main(String[] args) {
        var context = new AnnotationConfigApplicationContext(ProjectConfig4.class);

        Person4 p = context.getBean(Person4.class);

        System.out.println("Person's name: " + p.getName());
//        System.out.println("Person's parrot: " + p.getParrot());
    }
}
