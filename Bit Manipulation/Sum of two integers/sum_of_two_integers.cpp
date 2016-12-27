class Solution {
public:
    int getSum(int a, int b) {
        if (b == 0) return a;
        int sum = a ^ b;//不考虑进位
        int carry = (a & b) << 1;//只考虑进位
        return getSum(sum, carry);
    }
};