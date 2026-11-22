class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        index1, index2 = 0, len(numbers) - 1
        result = []
        total = numbers[index1] + numbers[index2]
        while total != target:
        # [2,3,4], target = 6
            if (total > target):
                index2 -= 1
            if(total < target):
                index1 += 1
            total = numbers[index1] + numbers[index2]
        
        result.append(index1 + 1)
        result.append(index2 + 1)
        return result

