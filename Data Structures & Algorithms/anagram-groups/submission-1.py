class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        result = []
        buckets = defaultdict(list)

        for str in strs:
            sortedstr = "".join(sorted(str))
            buckets[sortedstr].append(str)
        
        for bucketList in buckets:
            result.append(buckets[bucketList])
        return result



