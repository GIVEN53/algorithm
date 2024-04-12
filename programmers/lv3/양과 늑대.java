package programmers.lv3;

import java.util.*;

class Solution {
    private int n;
    private int[] info;
    private int[] left = new int[17];
    private int[] right = new int[17];
    private boolean[] visited = new boolean[1 << 17];

    public int solution(int[] info, int[][] edges) {
        this.n = info.length;
        this.info = info;

        Arrays.fill(left, -1);
        Arrays.fill(right, -1);
        for (int[] edge : edges) {
            int parent = edge[0];
            int child = edge[1];
            if (left[parent] == -1) {
                left[parent] = child;
            } else {
                right[parent] = child;
            }
        }

        return bfs(0);
    }

    private int bfs(int start) {
        Queue<Integer> q = new LinkedList<>();
        q.offer(1 << start);
        int ans = 0;
        while (!q.isEmpty()) {
            int now = q.poll();
            if (visited[now]) {
                continue;
            }
            visited[now] = true;

            int sheep = 0;
            int wolf = 0;
            for (int i = 0; i < n; i++) {
                if ((1 << i & now) == 0) { // 현재 지나온 정점이 아닌 것
                    continue;
                }

                if (info[i] == 0) {
                    sheep++;
                } else {
                    wolf++;
                }
            }
            if (sheep <= wolf) {
                continue;
            }
            ans = Math.max(ans, sheep);

            for (int i = 0; i < n; i++) {
                if ((1 << i & now) == 0) {
                    continue;
                }
                if (left[i] != -1) {
                    q.offer(1 << left[i] | now);
                }
                if (right[i] != -1) {
                    q.offer(1 << right[i] | now);
                }
            }
        }
        return ans;
    }
}
