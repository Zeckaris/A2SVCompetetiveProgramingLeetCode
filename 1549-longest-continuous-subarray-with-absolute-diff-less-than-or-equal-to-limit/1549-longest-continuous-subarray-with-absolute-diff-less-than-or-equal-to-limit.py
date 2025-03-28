class Solution:
    def longestSubarray(self, nums: List[int], limit: int) -> int:
        begin = 0
        maxWindow = 0
        minDeque = deque()
        maxDeque = deque()

        for end in range(len(nums)):
            while minDeque and nums[minDeque[-1]] > nums[end]:
                minDeque.pop()
            minDeque.append(end)
            while maxDeque and nums[maxDeque[-1]] < nums[end]:
                maxDeque.pop()
            maxDeque.append(end)
            while nums[maxDeque[0]] - nums[minDeque[0]] > limit:
                begin += 1

                if minDeque[0] < begin:
                    minDeque.popleft()
                if maxDeque[0] < begin:
                    maxDeque.popleft()

            maxWindow = max(maxWindow, end - begin + 1)

        return maxWindow