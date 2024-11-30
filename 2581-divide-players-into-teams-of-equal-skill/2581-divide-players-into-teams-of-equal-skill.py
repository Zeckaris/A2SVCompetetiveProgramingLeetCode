class Solution:
    def dividePlayers(self, skill: List[int]) -> int:
        numOfTeams= len(skill) // 2
        target= sum(skill) // numOfTeams
        skill.sort()
        begin= 0
        end= len(skill) - 1
        output=0
        while  begin < end:
            if skill[begin] + skill[end] == target:
                output += (skill[begin] * skill[end])
                begin += 1
                end -= 1
            else:
                return -1
        return output
