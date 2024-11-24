class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        elements= set()
        for val in arr:
            if val * 2 in elements or (val % 2 == 0 and val // 2 in elements):
                return True
            elements.add(val)
            
        return False
            




        