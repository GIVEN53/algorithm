package programmers.lv2;

import java.util.*;

class Solution {
    private List<Integer> date = new ArrayList<>();
    private int[] direction = { 1, 0, -1, 0 };
    private int n;
    private int m;
    private boolean[][] visited;

    public int[] solution(String[] maps) {
        this.n = maps.length;
        this.m = maps[0].length();
        this.visited = new boolean[n][m];

        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                char now = maps[i].charAt(j);
                if (now != 'X' && !visited[i][j]) {
                    bfs(now - '0', i, j, maps);
                }
            }
        }

        if (date.size() == 0) {
            return new int[] { -1 };
        }
        return date.stream()
                .mapToInt(i -> i)
                .sorted()
                .toArray();
    }

    private void bfs(int sum, int r, int c, String[] maps) {
        Queue<int[]> q = new LinkedList<>();
        q.offer(new int[] { r, c });
        visited[r][c] = true;

        while (!q.isEmpty()) {
            int[] now = q.poll();

            for (int i = 0; i < 4; i++) {
                int nr = now[0] + direction[i];
                int nc = now[1] + direction[3 - i];

                if (isOutOfRange(nr, nc) || visited[nr][nc]) {
                    continue;
                }

                char next = maps[nr].charAt(nc);
                if (next == 'X') {
                    continue;
                }
                visited[nr][nc] = true;
                sum += next - '0';
                q.offer(new int[] { nr, nc });
            }
        }

        date.add(sum);
    }

    private boolean isOutOfRange(int r, int c) {
        return r < 0 || r >= n || c < 0 || c >= m;
    }
}
