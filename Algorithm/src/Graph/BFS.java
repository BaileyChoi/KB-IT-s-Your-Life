package Graph;

import java.util.*;

public class BFS {
    // visited를 set으로 구현
    public void bfs1(List<List<Integer>> graph, int startVertex) {
        // 시작점 예약
        Queue<Integer> queue = new LinkedList<>();
        Set<Integer> visited = new HashSet<>();
        queue.add(startVertex);
        visited.add(startVertex);
        // queue가 비어있을 때까지 반복
        while(!queue.isEmpty()) {
            // 현재 노드 방문
            int curVertex = queue.remove();
            // 다음 노드 예약
            for (int nextVertex: graph.get(curVertex)) {
                if (!visited.contains(nextVertex)) {
                    queue.add(nextVertex);
                    visited.add(nextVertex);
                }
            }
        }
    }

    public void solve1(List<List<Integer>> graph) {
        bfs1(graph, 0);
    }


    // visited를 array로 구현
    public void bfs2(List<List<Integer>> graph, int startVertex) {
        // 시작점 예약
        Queue<Integer> queue = new LinkedList<>();
        final int N = graph.size();
        boolean[] visited = new boolean[N];
        queue.add(startVertex);
        visited[startVertex] = true;
        // queue가 비어있을 때까지 반복
        while(!queue.isEmpty()) {
            // 현재 노드 방문
            int curVertex = queue.remove();
            // 다음 노드 예약
            for (int nextVertex: graph.get(curVertex)) {
                if (!visited[nextVertex]) {
                    queue.add(nextVertex);
                    visited[nextVertex] = true;
                }
            }
        }
    }

    public void solve2(List<List<Integer>> graph) {
        bfs2(graph, 0);
    }

    public static void main(String[] args) {
        BFS bfs = new BFS();

        // 그래프 초기화 (인접 리스트 형태)
        List<List<Integer>> graph = new ArrayList<>();
        graph.add(List.of(1, 3, 6));
        graph.add(List.of(0, 3));
        graph.add(List.of(3));
        graph.add(List.of(0, 1, 2, 7));
        graph.add(List.of(5));
        graph.add(List.of(4, 6, 7));
        graph.add(List.of(0, 5));
        graph.add(List.of(3, 5));

        // BFS 실행
        System.out.println("BFS (Set 사용):");
        bfs.solve1(graph);  // Set을 사용한 BFS

        System.out.println("\nBFS (배열 사용):");
        bfs.solve2(graph);  // 배열을 사용한 BFS
    }
}
