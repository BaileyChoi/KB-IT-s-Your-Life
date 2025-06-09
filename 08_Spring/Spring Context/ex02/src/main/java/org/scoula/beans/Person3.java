package org.scoula.beans;

import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.stereotype.Component;

@Component
public class Person3 {
    private String name = "Bingbong3";

    private final Parrot3 parrot;

    @Autowired
    public Person3(Parrot3 parrot) {
        this.parrot = parrot;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public Parrot3 getParrot() {
        return parrot;
    }
}
