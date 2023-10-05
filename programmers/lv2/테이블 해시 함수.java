package programmers.lv2;

import java.util.Arrays;
import java.util.stream.IntStream;

class Solution {
    public int solution(int[][] data, int col, int row_begin, int row_end) {
        int[][] sortedData = sort(data, col - 1);
        return IntStream.range(row_begin - 1, row_end)
            .map(i -> modAndSum(i + 1, sortedData[i]))
            .reduce(0, (a, b) -> a ^ b);
    }
    
    private int[][] sort(int[][] data, int col) {
        Arrays.sort(data, (o1, o2) -> {
            if (o1[col] == o2[col]) {
                return o2[0] - o1[0];
            }
                return o1[col] - o2[col];
            });
        return data;
    }
    
    private int modAndSum(int modNum, final int[] data) {
        return Arrays.stream(data)
            .map(d -> d % modNum)
            .sum();
    }
}
