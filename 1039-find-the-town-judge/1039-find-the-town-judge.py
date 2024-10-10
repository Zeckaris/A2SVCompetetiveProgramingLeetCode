class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        canBeAJudge = set(range(1, n + 1))
        trustedByPeople = {}
        for i in trust:
            if i[0] in canBeAJudge:
                canBeAJudge.remove(i[0])
            if i[1] in trustedByPeople:
                trustedByPeople[i[1]] += 1
            else:
                trustedByPeople[i[1]] = 1

      
        if len(canBeAJudge) == 1:
            a = next(iter(canBeAJudge)) 
            
            if trustedByPeople.get(a, 0) == n - 1:
                return a
            else:
                return -1
        else:
            return -1
