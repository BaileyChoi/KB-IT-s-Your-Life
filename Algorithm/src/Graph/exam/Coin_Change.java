package Graph.exam;

import java.util.*;

public class Coin_Change {
    public static int coinChange(int[] coins, int amount) {
        if (amount == 0) return 0;

        boolean[] visited = new boolean[amount + 1];
        Queue<int[]> queue = new LinkedList<>();

        queue.offer(new int[]{amount, 0});


        return -1;
    }

    public static void main(String[] args) {
        int[] coins = {1, 2, 5};
        int amount = 11;

        System.out.println(coinChange(coins, amount));
    }
}
