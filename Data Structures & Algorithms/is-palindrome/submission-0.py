class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        palin = "".join(filter(str.isalnum, s))
        palin = palin.lower()
        start = 0
        opposite = len(palin) - 1
        for char in palin:
            if char != palin[opposite]:
                return False
            opposite -= 1
        return True
