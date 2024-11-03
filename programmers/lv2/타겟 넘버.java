package programmers.lv2;

class Solution {
    public int solution(int[] numbers, int target) {
        return dfs(0, 0, numbers, target);
    }
    
    private int dfs(int d, int sum, int[] numbers, int target) {
        if (d == numbers.length) {
            if (sum == target) {
                return 1;
            }
            return 0;
        }
        
        int res = 0;
        int now = numbers[d];
        for (int i = 0; i < 2; i++) {
            now *= -1;
            res += dfs(d + 1, sum + now, numbers, target);
        }
        return res;
    }
}
