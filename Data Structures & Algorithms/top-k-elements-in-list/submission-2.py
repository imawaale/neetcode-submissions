class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        groups = {}
        counts = [ [] for _ in range(len(nums) + 1)]
        for key in nums:
            if key not in groups:
                groups[key] = 0
            groups[key] += 1
        
        for num, freq in groups.items():
            counts[freq].append(num) 

        results = []
        for i in range(len(nums), 0, -1):
            for n in counts[i]:
                results.append(n)
                if len(results) == k:
                    return results
        

        
            