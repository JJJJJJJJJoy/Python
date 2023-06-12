class Solution:
    def isPalindrome(self, x: int) -> bool:

        if x < 0:
            return False
        a = 0
        b = x
        while x > 0:
            a = a * 10 + x % 10
            x //= 10
        return a == b
        print(True)