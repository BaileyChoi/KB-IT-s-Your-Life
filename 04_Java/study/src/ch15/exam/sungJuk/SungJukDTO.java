package ch15.exam.sungJuk;

import lombok.Data;

@Data
public class SungJukDTO {
    private int no;
    private String name;
    private int kor;
    private int eng;
    private int math;
    private int tot;
    private double avg;

    public SungJukDTO(int no, String name, int kor, int eng, int math) {
        this.no = no;
        this.name = name;
        this.kor = kor;
        this.eng = eng;
        this.math = math;
    }

    @Override
    public String toString() {
        return no + "\t" + name + "\t" + kor + "\t" + eng + "\t" + math + "\t" + tot + "\t" + String.format("%.2f",avg);
    }

    public void calc() {
        tot = this.kor + this.eng + this.math;
        avg = (double) this.tot / 3;
    }
}
