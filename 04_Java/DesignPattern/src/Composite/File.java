package Composite;

import lombok.AllArgsConstructor;
import lombok.Data;

@AllArgsConstructor
public class File extends Entry {
    private String name;
    private int size;

    @Override
    public String getName() {
        return name;
    }
    @Override
    public int getSize() {
        return size;
    }

    @Override
    public void printList(String prefix) {
        System.out.println(prefix + "/" + this);
    }
}
