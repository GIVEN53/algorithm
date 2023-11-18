package programmers.lv2;

import java.util.*;

class Solution {
    public int solution(int[] queue1, int[] queue2) {
        long queue1Sum = Arrays.stream(queue1).sum();
        long queue2Sum = Arrays.stream(queue2).sum();
        if ((queue1Sum + queue2Sum) % 2 != 0) {
            return -1;
        }

        Queue<Integer> q1 = generateQueue(queue1);
        Queue<Integer> q2 = generateQueue(queue2);

        int cnt = 0;
        while (cnt < 600000) {
            if (queue1Sum > queue2Sum) {
                int num = q1.poll();
                queue1Sum -= num;
                q2.add(num);
                queue2Sum += num;
                cnt += 1;
            } else if (queue1Sum < queue2Sum) {
                int num = q2.poll();
                queue2Sum -= num;
                q1.add(num);
                queue1Sum += num;
                cnt += 1;
            } else {
                return cnt;
            }
        }
        return -1;
    }

    private Queue<Integer> generateQueue(int[] arr) {
        Queue<Integer> q = new LinkedList<>();
        for (int i : arr) {
            q.add(i);
        }
        return q;
    }
}