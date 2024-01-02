package programmers.lv1;

import java.util.*;

class Solution {
    private static final char[][] MBTI = new char[][] { { 'R', 'T' }, { 'C', 'F' }, { 'J', 'M' }, { 'A', 'N' } };
    private Map<Character, Integer> scores = new HashMap<>();

    public String solution(String[] survey, int[] choices) {
        for (int i = 0; i < survey.length; i++) {
            int score = Math.abs(choices[i] - 4);

            if (choices[i] < 4) {
                increaseScore(survey[i].charAt(0), score);
            } else if (4 < choices[i]) {
                increaseScore(survey[i].charAt(1), score);
            }
        }

        String answer = "";
        for (char[] m : MBTI) {
            if (scores.getOrDefault(m[0], 0) >= scores.getOrDefault(m[1], 0)) {
                answer += m[0];
            } else {
                answer += m[1];
            }
        }

        return answer;
    }

    private void increaseScore(char mbti, int score) {
        scores.put(mbti, scores.getOrDefault(mbti, 0) + score);
    }
}
