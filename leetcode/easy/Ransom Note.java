package leetcode.easy;

import java.util.*;

class Solution {
    public boolean canConstruct(String ransomNote, String magazine) {
        Map<Character, Integer> magazineCounts = new HashMap<>();
        for (int i = 0; i < magazine.length(); i++) {
            char m = magazine.charAt(i);
            magazineCounts.put(m, magazineCounts.getOrDefault(m, 0) + 1);
        }

        for (int i = 0; i < ransomNote.length(); i++) {
            char r = ransomNote.charAt(i);
            if (!magazineCounts.containsKey(r) || magazineCounts.get(r) == 0) {
                return false;
            }
            magazineCounts.put(r, magazineCounts.get(r) - 1);
        }

        return true;
    }
}
