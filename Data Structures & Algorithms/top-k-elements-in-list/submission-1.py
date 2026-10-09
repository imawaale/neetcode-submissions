class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        groups = {}
        for key in nums:
            if key not in groups:
                groups[key] = 0
            groups[key] += 1
        topk = sorted(groups, key=groups.get, reverse=True)[:k]
        return topk

        
            