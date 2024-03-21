class Solution {
    public boolean isHappy(int n) {
        long t = n;
        Set<Long> seen = new HashSet<Long>();
        while (seen.add(t)) {
            t = process(t);
            if (t == 1) {
                return true;
            }
        }
        return false;
    }

    private long process(long n) {
        long res = 0;
        while (n > 0) {
            long rem = n % 10;
            res += rem * rem;
            n /= 10;
        }
        return res;
    }
}