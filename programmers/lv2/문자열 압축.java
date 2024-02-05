package programmers.lv2;

class Solution {
    public int solution(String s) {
        int answer = s.length();

        for (int interval = 1; interval < s.length() / 2 + 1; interval++) {
            String now = s.substring(0, interval);
            String str = "";
            int cnt = 1;
            for (int i = interval; i < s.length(); i += interval) {
                String next = s.substring(i, Math.min(i + interval, s.length()));
                if (next.equals(now)) {
                    cnt++;
                    continue;
                }

                str += cnt == 1 ? now : cnt + now;
                now = next;
                cnt = 1;
            }
            str += cnt == 1 ? now : cnt + now;
            answer = Math.min(answer, str.length());
        }

        return answer;
    }
}