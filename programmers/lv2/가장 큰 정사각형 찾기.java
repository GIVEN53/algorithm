package programmers.lv2;

class Solution {
    public int solution(int[][] board) {
        int row = board.length + 1;
        int col = board[0].length + 1;
        
        int maxSide = 0;
        int[][] dp = new int[row][col];
        for (int r = 1; r < row; r++) {
            for (int c = 1; c < col; c++) {
                if (board[r - 1][c - 1] == 1) {
                    dp[r][c] = Math.min(dp[r][c - 1], Math.min(dp[r - 1][c], dp[r - 1][c - 1])) + 1;
                    maxSide = Math.max(maxSide, dp[r][c]);
                }
            }
        }

        return maxSide * maxSide;
    }
}