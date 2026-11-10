class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        if len(nums) < 2:
            return False
        checked = set()
        for num in nums:
            if num in checked:
                return True
            checked.add(num)
        return False  
            
