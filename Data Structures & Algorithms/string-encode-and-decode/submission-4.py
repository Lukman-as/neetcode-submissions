class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return "Null"
        result = ""
        for i, s in enumerate(strs):
            result+=s
            if i != len(strs) - 1:
                result+="+_"
        return result

    def decode(self, s: str) -> List[str]:
        if s == "Null":
            return []
            
        return s.split("+_")
