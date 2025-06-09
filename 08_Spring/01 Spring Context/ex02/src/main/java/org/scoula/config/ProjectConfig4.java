package org.scoula.config;

import org.scoula.beans.Parrot;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.ComponentScan;
import org.springframework.context.annotation.Configuration;

@Configuration
@ComponentScan(basePackages = "org.scoula.beans")
public class ProjectConfig4 {

    @Bean("riki")
    public Parrot parrot1() {
        Parrot p = new Parrot();
        p.setName("Riki");
        return p;
    }

    @Bean("miki")
    public Parrot parrot2() {
        Parrot p = new Parrot();
        p.setName("Miki");
        return p;
    }
}
