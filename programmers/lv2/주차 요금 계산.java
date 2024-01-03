package programmers.lv2;

import java.util.*;

class Solution {
    private Map<String, String> parkingLot = new HashMap<>();
    private Map<String, Integer> parkingMinutes = new HashMap<>();

    public int[] solution(int[] fees, String[] records) {
        for (String record : records) {
            String[] r = record.split(" ");
            String time = r[0];
            String carNumber = r[1];
            String inOrOut = r[2];

            if (inOrOut.equals("IN")) {
                parkingLot.put(carNumber, time);
            } else if (inOrOut.equals("OUT")) {
                int parkingMinute = calculateParkingMinute(parkingLot.get(carNumber), time);
                parkingMinutes.put(carNumber, parkingMinutes.getOrDefault(carNumber, 0) + parkingMinute);
                parkingLot.remove(carNumber);
            }
        }

        for (String carNumber : parkingLot.keySet()) {
            int parkingMinute = calculateParkingMinute(parkingLot.get(carNumber), "23:59");
            parkingMinutes.put(carNumber, parkingMinutes.getOrDefault(carNumber, 0) + parkingMinute);
        }

        String[] carNumbers = parkingMinutes.keySet().toArray(new String[0]);
        Arrays.sort(carNumbers);

        int[] answer = new int[carNumbers.length];
        for (int i = 0; i < carNumbers.length; i++) {
            int parkingMinute = parkingMinutes.get(carNumbers[i]);
            int fee = calculateParkingFee(fees, parkingMinute);
            answer[i] = fee;
        }
        return answer;
    }

    private int calculateParkingMinute(String in, String out) {
        String[] inTime = in.split(":");
        int inHour = Integer.parseInt(inTime[0]);
        int inMinute = Integer.parseInt(inTime[1]);

        String[] outTime = out.split(":");
        int outHour = Integer.parseInt(outTime[0]);
        int outMinute = Integer.parseInt(outTime[1]);

        int h = outHour - inHour;
        int m = outMinute - inMinute;
        if (inMinute > outMinute) {
            h--;
            m = 60 - inMinute + outMinute;
        }

        return h * 60 + m;
    }

    private int calculateParkingFee(int[] fees, int parkingMinute) {
        int baseTime = fees[0];
        int baseRate = fees[1];
        int unitTime = fees[2];
        int unitRate = fees[3];

        if (parkingMinute <= baseTime) {
            return baseRate;
        }
        parkingMinute -= baseTime;
        if (parkingMinute % unitTime == 0) {
            return baseRate + parkingMinute / unitTime * unitRate;
        }

        return baseRate + (parkingMinute / unitTime + 1) * unitRate;
    }
}