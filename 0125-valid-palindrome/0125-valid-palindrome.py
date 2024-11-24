class Solution:
    def isPalindrome(self, s: str) -> bool:
        s= s.strip()
        begin=0
        end= len(s) - 1
        while begin <= end:
            if  s[begin].isalnum() and s[end].isalnum():
                if s[begin].lower() != s[end].lower():
                    return False
                else:
                    begin += 1
                    end -= 1
            else:
                if not s[begin].isalnum():
                    begin += 1
                if not s[end].isalnum():
                    end -= 1
        return True
            
        