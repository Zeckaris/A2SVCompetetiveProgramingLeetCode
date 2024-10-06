class Solution:
    def minChanges(self, n: int, k: int) -> int:
        if k > n:
            return -1
        elif k == n:
            return 0
        
        diff = n - k
        n= bin(n)[2:][::-1]
        diff=bin(diff)[2:][::-1]
        count=0
        for i in range(len(diff)):
            if diff[i] != '1':
                continue
            elif diff[i] == '1' and n[i] == '1':
                print('count ++')
                count += 1
            else:
                return -1
        return count