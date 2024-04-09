package programmers.lv4;

import java.util.*;

class Solution {
    public int solution(int[][] land, int height) {
        int n = land.length;
        int[] directions = { 1, 0, -1, 0 };

        PriorityQueue<Node> pq = new PriorityQueue<>((o1, o2) -> o1.cost - o2.cost);
        boolean[][] visited = new boolean[n][n];
        pq.offer(new Node(0, 0, 0));
        int totalCost = 0;
        while (!pq.isEmpty()) {
            Node now = pq.poll();
            if (visited[now.r][now.c]) {
                continue;
            }
            totalCost += now.cost;
            visited[now.r][now.c] = true;

            for (int i = 0; i < 4; i++) {
                int nr = now.r + directions[i];
                int nc = now.c + directions[3 - i];

                if (nr < 0 || n <= nr || nc < 0 || n <= nc) {
                    continue;
                }
                int heightDiff = Math.abs(land[now.r][now.c] - land[nr][nc]);
                if (heightDiff <= height) {
                    pq.offer(new Node(0, nr, nc));
                } else {
                    pq.offer(new Node(heightDiff, nr, nc));
                }
            }
        }
        return totalCost;
    }

    class Node {
        final int cost;
        final int r;
        final int c;

        public Node(int cost, int r, int c) {
            this.cost = cost;
            this.r = r;
            this.c = c;
        }
    }
}