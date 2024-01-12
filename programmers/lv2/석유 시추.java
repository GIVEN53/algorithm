package programmers.lv2;

import java.util.*;

class Solution {
    private int n;
    private int m;
    private Map<Integer, Integer> oilAmount = new HashMap<>();
    private int[] directions = new int[] { 1, 0, -1, 0 };

    public int solution(int[][] land) {
        this.n = land.length;
        this.m = land[0].length;

        int num = 2;
        for (int i = 0; i < n; i++) {
            for (int j = 0; j < m; j++) {
                if (land[i][j] == 1) {
                    bfs(i, j, land, num);
                    num++;
                }
            }
        }

        int[] result = new int[m];
        for (int j = 0; j < m; j++) {
            Set<Integer> oilGroup = new HashSet<>();
            for (int i = 0; i < n; i++) {
                if (land[i][j] > 1) {
                    oilGroup.add(land[i][j]);
                }
            }

            for (int groupNumber : oilGroup) {
                result[j] += oilAmount.get(groupNumber);
            }
        }

        Arrays.sort(result);
        return result[result.length - 1];
    }

    private void bfs(int i, int j, int[][] land, int groupNumber) {
        Queue<Node> q = new LinkedList<>();
        q.offer(new Node(i, j));
        land[i][j] = groupNumber;
        int amount = 1;
        while (!q.isEmpty()) {
            Node now = q.poll();

            for (int d = 0; d < 4; d++) {
                int ni = now.i + directions[d];
                int nj = now.j + directions[3 - d];

                if (!isOutOfRange(ni, nj) && land[ni][nj] == 1) {
                    land[ni][nj] = groupNumber;
                    q.offer(new Node(ni, nj));
                    amount++;
                }
            }
        }
        oilAmount.put(groupNumber, amount);
    }

    private boolean isOutOfRange(int i, int j) {
        return i < 0 || i >= n || j < 0 || j >= m;
    }

    class Node {
        int i;
        int j;

        Node(int i, int j) {
            this.i = i;
            this.j = j;
        }
    }
}
