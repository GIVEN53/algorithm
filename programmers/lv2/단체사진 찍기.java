package programmers.lv2;

class Solution {
    private String[] members = new String[] { "A", "C", "F", "J", "M", "N", "R", "T" };
    private boolean[] visited = new boolean[8];
    private int answer;

    public int solution(int n, String[] data) {
        answer = 0;
        createPermutation("", data);
        return answer;
    }

    private void createPermutation(String result, String[] data) {
        if (result.length() == 8) {
            for (String condition : data) {
                if (!validate(result, condition)) {
                    return;
                }
            }
            answer++;
            return;
        }

        for (int i = 0; i < 8; i++) {
            if (visited[i]) {
                continue;
            }
            visited[i] = true;
            createPermutation(result + members[i], data);
            visited[i] = false;
        }
    }

    private boolean validate(String lines, String condition) {
        char operator = condition.charAt(3);
        char friend1 = condition.charAt(0);
        char friend2 = condition.charAt(2);
        int interval = Character.getNumericValue(condition.charAt(4));

        int differenceIndex = Math.abs(lines.indexOf(friend1) - lines.indexOf(friend2)) - 1;

        switch (operator) {
            case '=' -> {
                if (differenceIndex == interval) {
                    return true;
                }
            }
            case '>' -> {
                if (differenceIndex > interval) {
                    return true;
                }
            }
            case '<' -> {
                if (differenceIndex < interval) {
                    return true;
                }
            }
        }
        return false;
    }
}
