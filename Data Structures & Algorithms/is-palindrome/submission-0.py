class Solution:
    def isPalindrome(self, s: str) -> bool:
        check = ""
        for c in s:
            if c.isalnum():
                check += c
        reverse = [""]*len(check)
        for i, c in enumerate(check):
            reverse[len(check) - 1 - i] = c
        
        return check.lower() == ''.join(reverse).lower()
            

        