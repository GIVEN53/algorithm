package programmers.lv2;

import java.util.*;

class Solution {
    private int[] ryan = new int[11];
    private int[] apeach;
    private List<int[]> candidates = new ArrayList<>();
    private int maxDiff;

    public int[] solution(int n, int[] info) {
        this.apeach = info;
        dfs(n, 0, -getApeachScore());

        if (maxDiff == 0) {
            return new int[] {-1};
        }
        return selectRyan();
    }

    private int getApeachScore() {
        int score = 0;
        for (int i = 0; i < 11; i++) {
            if (apeach[i] > 0) {
                score += 10 - i;
            }
        }
        return score;
    }

    private void dfs(int arrow, int i, int scoreDiff) {
        if (arrow == 0) {
            registerCandidate(scoreDiff);
            return;
        }
        if (i == 11) {
            return;
        }

        for (int cnt = apeach[i] + 1; cnt > -1; cnt--) {
            ryan[i] = cnt;
            dfs(arrow - cnt, i + 1, calculateScoreDiff(i, scoreDiff));
            ryan[i] = 0;
        }
    }

    private int calculateScoreDiff(int i, int prevScoreDiff) {
        if (ryan[i] <= apeach[i]) {
            return prevScoreDiff;
        }
        if (apeach[i] == 0) {
            return prevScoreDiff + (10 - i);
        }
        return prevScoreDiff + (10 - i) * 2;
    }

    private void registerCandidate(int scoreDiff) {
        if (scoreDiff < maxDiff) {
            return;
        }

        if (scoreDiff > maxDiff) {
            maxDiff = scoreDiff;
            candidates.clear();
        }
        candidates.add(ryan.clone());
    }

    private int[] selectRyan() {
        for (int i = 10; i > -1; i--) {
            if (candidates.size() == 1) {
                break;
            }

            int maxArrow = 0;
            List<int[]> tmp = new ArrayList<>();
            for (int[] candidate : candidates) {
                if (candidate[i] > maxArrow) {
                    maxArrow = candidate[i];
                    tmp.clear();
                    tmp.add(candidate);
                } else if (candidate[i] == maxArrow) {
                    tmp.add(candidate);
                }
            }
            candidates = tmp;
        }
        return candidates.get(0);
    }
}
