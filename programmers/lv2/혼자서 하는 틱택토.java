package programmers.lv2;

class Solution {
    public int solution(String[] board) {
        int[] o = new int[8];
        int[] x = new int[8];
        int oCnt = 0;
        int xCnt = 0;
        for (int i = 0; i < board.length; i++) {
            String[] b = board[i].split("");
            for (int j = 0; j < b.length; j++) {
                if (b[j].equals("O")) {
                    o[i]++;
                    o[3 + j]++;
                    findDiagonal(i, j, o);
                } else if (b[j].equals("X")) {
                    x[i]++;
                    x[3 + j]++;
                    findDiagonal(i, j, x);
                }
            }
            oCnt += o[i];
            xCnt += x[i];
        }

        boolean oWin = isWin(o);
        boolean xWin = isWin(x);
        if (oWin && xWin) {
            return 0;
        } else if (oWin && oCnt != xCnt + 1) {
            return 0;
        } else if (xWin && oCnt != xCnt) {
            return 0;
        } else if (oCnt > 1 + xCnt || oCnt < xCnt) {
            return 0;
        }
        return 1;
    }

    private void findDiagonal(int i, int j, int[] arr) {
        if (i == 1 && j == 1) {
            arr[6]++;
            arr[7]++;
        } else if (i == j) {
            arr[6]++;
        } else if (Math.abs(i - j) == 2) {
            arr[7]++;
        }
    }

    private boolean isWin(int[] arr) {
        for (int i = 0; i < arr.length; i++) {
            if (arr[i] == 3) {
                return true;
            }
        }
        return false;
    }
}
