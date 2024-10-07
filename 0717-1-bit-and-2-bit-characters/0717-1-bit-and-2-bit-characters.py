class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
       
        isTwoBitPart=False
        for i in range(len(bits)):
            if bits[i] == 1 and isTwoBitPart == False:
                isTwoBitPart= True
            elif bits[i] == 1 and isTwoBitPart == True:
                isTwoBitPart = False
            elif i == len(bits) - 1:
                if isTwoBitPart== True:
                    return False
                else:
                    return True
            elif bits[i] == 0  and isTwoBitPart == True:
                isTwoBitPart= False