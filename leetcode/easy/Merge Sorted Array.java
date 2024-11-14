package leetcode.easy;

class Solution {
    public void merge(int[] nums1, int m, int[] nums2, int n) {
        int[] tmp = new int[m];
        for (int i = 0; i < m; i++) {
            tmp[i] = nums1[i];
        }

        int a = 0;
        int b = 0;
        for (int i = 0; i < m + n; i++) {
            if (a >= m) {
                nums1[i] = nums2[b];
                b++;
            } else if (b >= n) {
                nums1[i] = tmp[a];
                a++;
            } else if (tmp[a] < nums2[b]) {
                nums1[i] = tmp[a];
                a++;
            } else {
                nums1[i] = nums2[b];
                b++;
            }
        }
    }
}
