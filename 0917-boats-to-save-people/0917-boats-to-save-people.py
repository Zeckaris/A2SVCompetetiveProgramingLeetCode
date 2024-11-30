class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        numOfBoats=0
        begin=0
        end=len(people) - 1
        people.sort()
        while begin <= end:
            if people[begin] + people[end] <= limit:
                numOfBoats += 1
                begin += 1
                end -= 1
            elif people[begin] + people[end] > limit:
                numOfBoats += 1
                end -= 1
        return numOfBoats



       
            
            

        
           