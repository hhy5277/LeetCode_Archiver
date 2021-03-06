class Solution:
    def smallestRepunitDivByK(self, K: int) -> int:
        n = 0
        for i in range(1, K + 1):
            n = n * 10 + 1
            n %= K
            if n == 0:
                return i
        return -1
