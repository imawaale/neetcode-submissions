class Solution:

    def encode(self, strs: List[str]) -> str:
        results = []
        for s in strs:
            n = len(s)
            results.append(f"{n}#{s}")
        return "".join(results)

    def decode(self, s: str) -> List[str]:
        results = []
        i = 0
        while i < len(s):
            j = i 
            while s[j] != "#":
                j += 1
            length = int(s[i:j])

            start = j + 1
            end = start + length
            results.append(s[start:end])

            i = end
        return results
                

