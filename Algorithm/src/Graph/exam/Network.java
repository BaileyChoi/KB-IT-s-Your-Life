package Graph.exam;

public class Network {
    public static int solution(int n, int[][] computers) {
        int answer = 0;

        boolean[] visited = new boolean[n];

        for (int i = 0; i < n; i++) {
            if (!visited[i]) {
                dfs(computers, visited, i);
                answer++;
            }
        }

        return answer;
    }

    public static void dfs(int[][] graph, boolean[] visited, int curVertex) {
        visited[curVertex] = true;
        for (int nextVertex = 0; nextVertex < graph[curVertex].length; nextVertex++) {
            if (graph[curVertex][nextVertex] == 1 && !visited[nextVertex]) {
                dfs(graph, visited, nextVertex);
            }
        }
    }

    public static void main(String[] args) {
        int n = 3;
        int[][] computers = {
                {1, 1, 0},
                {1, 1, 0},
                {0, 0, 1}
        };

        System.out.println(solution(n, computers));
    }
}
