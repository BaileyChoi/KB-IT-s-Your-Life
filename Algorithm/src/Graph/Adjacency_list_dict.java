package Graph;

import java.util.*;

public class Adjacency_list_dict {
    public static void main(String[] args) {
        int n = 8;  // 노드 개수
        int[][] edges = {
                {0, 1}, {0, 3}, {0, 6}, {1, 3}, {2, 3}, {3, 7}, {4, 5}, {5, 6}, {5, 7}
        };

        // 인접 리스트 초기화
        Map<Integer, List<Integer>> graph = new HashMap<>();
        for (int i = 0; i < n; i++) {
            graph.put(i, new ArrayList<>()); // 각 노드에 대해 빈 리스트 추가
        }

        // 양방향 간선 추가
        for (int[] edge : edges) {
            int a = edge[0];
            int b = edge[1];

            graph.get(a).add(b); // a -> b 연결
            graph.get(b).add(a); // b -> a 연결 (양방향)
        }

        // 인접 리스트 출력
        int curVertex = 3; // 현재 노드
        for (int nextVertex : graph.get(curVertex)) {
            System.out.println("노드 " + curVertex + " → 다음 노드 " + nextVertex);
        }
    }
}
