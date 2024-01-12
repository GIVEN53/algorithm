package programmers.lv1;

class Solution {
    private int currentHealth;
    private int sec = 1;
    private int successStreak;

    public int solution(int[] bandage, int health, int[][] attacks) {
        currentHealth = health;
        int i = 0;
        while (i < attacks.length) {
            if (sec == attacks[i][0]) {
                attackByMonster(attacks[i][1]);
                i++;
            } else {
                recover(bandage, health);
            }

            if (currentHealth <= 0) {
                return -1;
            }
            sec += 1;
        }
        return currentHealth;
    }

    private void attackByMonster(int damage) {
        currentHealth -= damage;
        successStreak = 0;
    }

    private void recover(int[] bandage, int health) {
        currentHealth += bandage[1];
        successStreak++;
        if (successStreak == bandage[0]) {
            currentHealth += bandage[2];
            successStreak = 0;
        }

        if (currentHealth >= health) {
            currentHealth = health;
        }
    }
}
