package leetcode.easy;

import java.util.Arrays;

class Solution {
    public int removeElement(int[] nums, int val) {
        int k = 0;
        for (int i = 0; i < nums.length; i++) {
            if (nums[i] != val) {
                k++;
            } else if (nums[i] == val) {
                nums[i] = 51;
            }
        }
        Arrays.sort(nums);
        return k;
    }
}