package org.scoula.beans;

import org.springframework.stereotype.Component;

@Component
public class Parrot3 {
    private String name = "Koko3";

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    @Override
    public String toString() {
        return "Parrot3 : " + name;
    }
}
