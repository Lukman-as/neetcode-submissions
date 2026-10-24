class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) > len(t):
            lets = set(s)
        else:
            lets = set(t)
            
        for let in lets:
            if s.count(let) != t.count(let):
                return False
        
        return True
        