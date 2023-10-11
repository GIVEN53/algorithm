package programmers.lv2;

import java.util.Arrays;

class Solution {
    public int solution(int[][] targets) {
        Arrays.sort(targets, (o1, o2) -> o1[1] - o2[1]);
        
        int x = 0;
        int answer = 0;
        for (int[] target : targets) {
            if (x <= target[0]) {
                x = target[1];
                answer++;
            }
        }
        return answer;
    }
}