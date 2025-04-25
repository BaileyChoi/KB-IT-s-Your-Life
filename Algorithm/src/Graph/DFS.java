package Graph;

import ch08.sec10.exam01.D;

import java.util.*;

public class DFS {
    // visited를 set으로 구현
    public void dfs1(List<List<Integer>> graph, Set<Integer> visited, int curVertex ) {
        visited.add(curVertex);
        for (int nextVertex: graph.get(curVertex)) {
            if (!visited.contains(nextVertex)) {
                dfs1(graph, visited, nextVertex);
            }
        }
    }

    public void solve1(List<List<Integer>> graph) {
        Set<Integer> visited = new HashSet<>();
        dfs1(graph, visited, 0);
    }


    // visited를 array로 구현
    public void dfs2(List<List<Integer>> graph, boolean[] visited, int curVertex) {
        visited[curVertex] = true;
        for (int nextVertex:graph.get(curVertex)) {
            if (!visited[nextVertex]) {
                dfs2(graph, visited, nextVertex);
            }
        }
    }

    public void solve2(List<List<Integer>> graph) {
        final int N = graph.size();
        boolean[] visited = new boolean[N];
        dfs2(graph, visited, 0);
    }

    public static void main(String[] args) {
        DFS dfs = new DFS();

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

        // DFS 실행
        System.out.println("DFS (Set 사용):");
        dfs.solve1(graph);  // Set을 사용한 DFS

        System.out.println("\nDFS (배열 사용):");
        dfs.solve2(graph);  // 배열을 사용한 DFS
    }
}
