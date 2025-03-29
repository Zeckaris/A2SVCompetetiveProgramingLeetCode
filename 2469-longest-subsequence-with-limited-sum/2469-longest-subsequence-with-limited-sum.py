class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        #use prefix sum
        psum=[0]
        ans=[]
        nums.sort()
        for i in nums:
            psum.append(psum[-1] + i)
        
        for i in queries:
            found=False
            for j in range(len(psum) - 1, 0, -1):
                if psum[j] <= i:
                    ans.append(j)
                    found=True
                    break
            if not found:
                ans.append(0)
            
                
        return ans
            
      
             




        