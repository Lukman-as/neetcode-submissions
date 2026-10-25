class Solution:
    def isPalindrome(self, s: str) -> bool:
        # check = ""
        # for c in s:
        #     if c.isalnum():
        #         check += c
        # reverse = [""]*len(check)
        # for i, c in enumerate(check):
        #     reverse[len(check) - 1 - i] = c
        
        # return check.lower() == ''.join(reverse).lower()
        l = 0
        r = len(s) - 1

        while l < r:
            if not s[l].isalnum():
                l+=1
                continue
            
            if not s[r].isalnum():
                r-=1
                continue
            
            if s[l].lower() != s[r].lower():
                return False
            else:
                l+=1
                r-=1
        return True 

        