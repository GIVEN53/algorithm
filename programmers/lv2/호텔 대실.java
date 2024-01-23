package programmers.lv2;

import java.util.*;

class Solution {
    public int solution(String[][] book_time) {
        List<Reservation> reservations = new ArrayList<>();
        for (String[] bookTime : book_time) {
            reservations.add(new Reservation(getMinute(bookTime[0]), getMinute(bookTime[1])));
        }
        reservations.sort((r1, r2) -> r1.start - r2.start);

        List<Integer> rooms = new ArrayList<>();
        for (Reservation reservation : reservations) {
            boolean matched = false;
            for (int i = 0; i < rooms.size(); i++) {
                if (rooms.get(i) <= reservation.start) {
                    rooms.set(i, reservation.end);
                    matched = true;
                    break;
                }
            }
            if (!matched) {
                rooms.add(reservation.end);
            }
        }

        return rooms.size();
    }

    private int getMinute(String time) {
        String[] t = time.split(":");
        return Integer.parseInt(t[0]) * 60 + Integer.parseInt(t[1]);
    }

    class Reservation {
        static final int CLEAN_TIME = 10;
        int start;
        int end;

        Reservation(int start, int end) {
            this.start = start;
            this.end = end + CLEAN_TIME;
        }
    }
}
