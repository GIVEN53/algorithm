package programmers.lv1;

class Solution {
    public String solution(String video_len, String pos, String op_start, String op_end, String[] commands) {
        int videoTotalSec = convertToSec(video_len);
        int now = convertToSec(pos);
        int opStart = convertToSec(op_start);
        int opEnd = convertToSec(op_end);
        
        if (opStart <= now && now <= opEnd) {
                now = opEnd;
            }
        int i = 0;
        while (i < commands.length) {
            String command = commands[i];
            if ("prev".equals(command)) {
                now = doPrev(now);
            } else if ("next".equals(command)) {
                now = doNext(now, videoTotalSec);
            }
            if (opStart <= now && now <= opEnd) {
                now = opEnd;
            }
            i++;
        }
        return convertToMmSs(now);
    }
    
    private int convertToSec(String mmss) {
        String[] separatedMmSs = mmss.split(":");
        int minute = Integer.parseInt(separatedMmSs[0]);
        int second = Integer.parseInt(separatedMmSs[1]);
        return minute * 60 + second;
    }
    
    private int doPrev(int now) {
        now -= 10;
        if (now < 0) {
            return 0;
        }
        return now;
    }
    
    private int doNext(int now, int total) {
        now += 10;
        if (now > total) {
            return total;
        }
        return now;
    }
    
    private String convertToMmSs(int sec) {
        String minute = String.valueOf(sec / 60);
        String second = String.valueOf(sec % 60);
        if (minute.length() == 1) {
            minute = "0" + minute;
        }
        if (second.length() == 1) {
            second = "0" + second;
        }
        return minute + ":" + second;
    }
}
