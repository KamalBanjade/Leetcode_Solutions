class Solution(object):
    def isPalindrome(self, x):
        if x <= 0:
            return x == 0
        reversed_num = 0
        temp = x
        while temp > 0:
            reversed_num = reversed_num * 10 + temp % 10
            temp //= 10
        return reversed_num == x