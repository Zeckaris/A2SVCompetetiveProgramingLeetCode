class Solution:
    def countBits(self, n: int) -> List[int]:
        ans=[0]
        for i in range(1,n + 1):
            count=0
            k=i
            while k:
                count += k & 1
                k= k >> 1
            ans.append(count)
        return ans


        