class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        diff= start ^ goal
        count=0
        while diff:
            count += diff & 1
            diff = diff >> 1
        return count