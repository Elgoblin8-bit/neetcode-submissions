class Solution:
    def isAnagram(self, s: str, t: str) -> bool:

        sort = "".join(sorted(s))
        sortTwo = "".join(sorted(t))
        if sort == sortTwo:
            return True
        return False

        
