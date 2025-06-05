package Graph.exam;

import java.util.*;

public class Coin_Change {
    public static int coinChange(int[] coins, int amount) {
        if (amount == 0) return 0;

        boolean[] visited = new boolean[amount + 1];
        Queue<int[]> queue = new LinkedList<>();

        // 초기 상태 추가
        queue.offer(new int[]{amount, 0});
        visited[amount] = true;

        while (!queue.isEmpty()) {
            int[] current = queue.poll();
            int remaining = current[0];
            int numCoins = current[1];

            // 금액을 정확히 맞춸을 경우
            if (remaining == 0) {
                return numCoins;
            }

            // 가능한 동전으로 다음 상태 탐색
            for (int coin: coins) {
                int next = remaining - coin;
                if (next >= 0 && !visited[next]) {
                    queue.offer(new int[]{next, numCoins + 1});
                    visited[next] = true;
                }
            }
        }

        return -1;
    }

    public static void main(String[] args) {
        int[] coins = {1, 2, 5};
        int amount = 11;

        System.out.println(coinChange(coins, amount));
    }
}
