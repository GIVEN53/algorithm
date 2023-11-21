package programmers.lv3;

import java.util.*;

class Solution {
    private static int MAX = Integer.MAX_VALUE;

    public int[] solution(int n, int[][] paths, int[] gates, int[] summits) {
        Map<Integer, Integer>[] mountain = generateMountain(n, paths);
        boolean[] isSummit = findSummit(n, summits);

        int[] intensity = new int[n + 1];
        Arrays.fill(intensity, MAX);

        PriorityQueue<Node> pq = new PriorityQueue<>();
        for (int gate : gates) {
            intensity[gate] = 0;
            for (int key : mountain[gate].keySet()) {
                pq.offer(new Node(key, mountain[gate].get(key)));
            }
        }

        while (!pq.isEmpty()) {
            Node now = pq.poll();
            if (now.time >= intensity[now.vertex]) {
                continue;
            }
            intensity[now.vertex] = now.time;
            if (isSummit[now.vertex]) {
                continue;
            }
            for (int next_vertex : mountain[now.vertex].keySet()) {
                int next_time = mountain[now.vertex].get(next_vertex);
                pq.offer(new Node(next_vertex, Math.max(now.time, next_time)));
            }
        }

        Arrays.sort(summits);
        int[] answer = { 0, MAX };
        for (int summit : summits) {
            int time = intensity[summit];
            if (time < answer[1]) {
                answer[0] = summit;
                answer[1] = time;
            }
        }
        return answer;
    }

    private Map<Integer, Integer>[] generateMountain(int n, int[][] paths) {
        Map<Integer, Integer>[] mountain = new Map[n + 1];
        for (int i = 1; i < mountain.length; i++) {
            mountain[i] = new HashMap<>();
        }
        for (int[] path : paths) {
            int start = path[0];
            int end = path[1];
            int w = path[2];
            mountain[start].put(end, w);
            mountain[end].put(start, w);
        }

        return mountain;
    }

    private boolean[] findSummit(int n, int[] summits) {
        boolean[] isSummit = new boolean[n + 1];

        for (int s : summits) {
            isSummit[s] = true;
        }

        return isSummit;
    }
}

class Node implements Comparable<Node> {
    int vertex;
    int time;

    Node(int vertex, int time) {
        this.vertex = vertex;
        this.time = time;
    }

    @Override
    public int compareTo(Node node) {
        return this.time - node.time;
    }
}
