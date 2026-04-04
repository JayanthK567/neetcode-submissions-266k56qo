class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        seen = dict()
        if len(s) != len(t):
            return False
        for char in s:
            seen[char] = seen.get(char,0)+1
        for char in t:
            seen[char] = seen.get(char,0)-1
        for val in seen.values():
            if val != 0:
                return False
        return True
