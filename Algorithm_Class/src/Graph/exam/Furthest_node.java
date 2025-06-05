package Graph.exam;

import java.util.*;

public class Furthest_node {
    public static int solution(int n, int[][] edge) {
        // 인접 리스트로 변환
        List<List<Integer>> graph = new ArrayList<>();
        for (int i = 0; i < n + 1; i++) {
            graph.add(new ArrayList<>());
        }
        // 양방향 간선 추가
        for (int[] e : edge) {
            graph.get(e[0]).add(e[1]);
            graph.get(e[1]).add(e[0]);
        }

        return bfs(graph, n);
    }

    public static int bfs(List<List<Integer>> graph, int size) {
        Queue<Integer> queue = new LinkedList<>();
        boolean[] visited = new boolean[size + 1];
        int[] distance = new int[size + 1];

        queue.add(1);
        visited[1] = true;
        distance[1] = 0;

        while (!queue.isEmpty()) {
            int curVertex = queue.remove();
            for (int nextVertex : graph.get(curVertex)) {
                if (!visited[nextVertex]) {
                    queue.add(nextVertex);
                    visited[nextVertex] = true;
                    distance[nextVertex] = distance[curVertex] + 1;
                }
            }
        }

        // 가장 먼 거리 구하기
        int maxDistance = 0;
        for (int i = 1; i <= size; i++) {
            maxDistance = Math.max(maxDistance, distance[i]);
        }

        // 가장 먼 거리를 가진 노드의 개수 구하기
        int count = 0;
        for (int i = 1; i<= size; i++) {
            if (maxDistance == distance[i]) {
                count++;
            }
        }

        return count;

    }

    public static void main(String[] args) {
        int n = 6;
        int[][] edge = {
                {3, 6},
                {4, 3},
                {3, 2},
                {1, 3},
                {1, 2},
                {2, 4},
                {5, 2}
        };

        System.out.println(solution(n, edge));
    }
}
