class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        freqCounts = Counter(nums)
        # nums=[1,1,1,2,2,3] k=2
        minheap = [(val, key) for key, val in freqCounts.items()]
        heapq.heapify(minheap)
        while len(minheap) > k:
            heapq.heappop(minheap)

        result = []
        for ele in minheap:
            result.append(ele[1])
        return result



