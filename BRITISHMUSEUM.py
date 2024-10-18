import java.util.*;

public class MuseumSearch {
    public static void main(String[] args) {
        // Graph with weighted edges
        Map<String, Map<String, Integer>> map = new HashMap<>();

        map.put("Start", Map.of("NodeA", 3, "NodeB", 5));
        map.put("NodeA", Map.of("Start", 3, "NodeB", 4, "NodeD", 3));
        map.put("NodeB", Map.of("Start", 5, "NodeA", 4, "NodeC", 4));
        map.put("NodeC", Map.of("NodeB", 4, "NodeE", 6));
        map.put("NodeE", Map.of("NodeC", 6));
        map.put("NodeD", Map.of("NodeA", 3, "Goal", 5));
        map.put("Goal", Map.of("NodeD", 5));

        searchMuseum(map, "Start", "Goal", 2);  // Search for 2 paths to the goal
    }

    // British Museum Search (BMS) algorithm
    public static void searchMuseum(Map<String, Map<String, Integer>> map, String source, String target, int maxRoutes) {
        Queue<List<String>> pathsQueue = new LinkedList<>();
        List<String> startPath = new ArrayList<>();
        startPath.add(source);
        pathsQueue.add(startPath);
        int pathsFound = 0;

        while (!pathsQueue.isEmpty() && pathsFound < maxRoutes) {
            List<String> currentPath = pathsQueue.poll();
            String currentNode = currentPath.get(currentPath.size() - 1);

            if (currentNode.equals(target)) {
                System.out.println("Found path to goal: " + currentPath);
                pathsFound++;
            }

            Map<String, Integer> adjacentNodes = map.getOrDefault(currentNode, new HashMap<>());
            for (String neighbor : adjacentNodes.keySet()) {
                if (!currentPath.contains(neighbor)) {
                    List<String> newPath = new ArrayList<>(currentPath);
                    newPath.add(neighbor);
                    pathsQueue.add(newPath);
                }
            }
        }
    }
}
