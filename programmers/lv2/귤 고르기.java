package programmers.lv2;

import java.util.*;

class Solution {
    public int solution(int k, int[] tangerine) {
        Map<Integer, Integer> tangerines = new HashMap<>();
        for (int t : tangerine) {
            tangerines.put(t, tangerines.getOrDefault(t, 0) + 1);
        }

        List<Integer> cnt = new ArrayList<>(tangerines.values());
        cnt.sort(Comparator.reverseOrder());
        int answer = 0;
        for (int c : cnt) {
            k -= c;
            answer++;
            if (k <= 0) {
                break;
            }
        }

        return answer;
    }
}