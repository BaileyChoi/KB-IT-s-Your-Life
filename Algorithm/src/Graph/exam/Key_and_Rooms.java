package Graph.exam;

import java.util.*;

public class Key_and_Rooms {
    public static boolean canVisitAllRooms(List<List<Integer>> rooms) {
        return bfs(rooms, 0);
    }

    public static boolean bfs(List<List<Integer>> rooms, int startVertex) {
        Queue<Integer> queue = new LinkedList<>();
        Set<Integer> visited = new HashSet<>();
        queue.add(startVertex);
        visited.add(startVertex);
        while (!queue.isEmpty()) {
            int curVertex = queue.remove();
            for (int nextVertex : rooms.get(curVertex)) {
                if (!visited.contains(nextVertex)) {
                    queue.add(nextVertex);
                    visited.add(nextVertex);
                }
            }
        }

        // 모든 방의 키가 있는지 확인
        return visited.size() == rooms.size();
    }

    public static void main(String[] args) {
        List<List<Integer>> rooms = new ArrayList<>() {{
            add(List.of(1, 3));
            add(List.of(3, 0, 1));
            add(List.of(2));
            add(List.of(0));
        }};

        System.out.println(canVisitAllRooms(rooms));
    }
}
