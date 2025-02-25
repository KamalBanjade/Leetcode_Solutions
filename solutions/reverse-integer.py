class Solution(object):
    def reverse(self, x):
        sign = 1 if x >= 0 else -1
        x = abs(x)
        
        reversed_num = 0
        while x:
            reversed_num = reversed_num * 10 + x % 10
            x //= 10
            if reversed_num > 2147483647:
                return 0
        
        return sign * reversed_num if reversed_num <= 2147483647 else 0