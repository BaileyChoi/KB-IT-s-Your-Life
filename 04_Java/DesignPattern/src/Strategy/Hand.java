package Strategy;

import lombok.AllArgsConstructor;

import java.util.function.Predicate;

@AllArgsConstructor
public enum Hand {
    ROCK("바위", 0),
    SCISSORS("가위", 1),
    PAPER("보", 2);

    private String name;        // 손의 이름
    private int handvalue;     // 손의 값

    private static Hand[] hands = {
            ROCK, PAPER, SCISSORS
    };

    public static Hand getHand(int handvalue) {
        return hands[handvalue];
    }

    // 무승부는 0, this가 이기면 1, h가 이기면 -1
    private int fight(Hand h) {
        if (this == h) {
            return 0;
        } else if ((this.handvalue + 1) % 3 == h.handvalue) {
            return 1;
        } else {
            return -1;
        }
    }

    // this가 h보다 강할 때 true
    //Predicate<Hand> isStrongerThan = h -> fight(h) == 1;
    public boolean isStrongerThan(Hand h) {
        return fight(h) == 1;
    }

    // this가 h보다 약할 때 true
    public boolean isWeakerThan(Hand h) {
        return fight(h) == -1;
    }

    // 가위 바위 보의 문자열 표현
    @Override
    public String toString() {
        return name;
    }
}
