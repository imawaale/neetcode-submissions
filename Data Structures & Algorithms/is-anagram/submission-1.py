class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        dictS = {} 
        dictT = {}

        for char in s:
            if char not in dictS:
                dictS[char] = 0
            dictS[char] += 1

        for char in t:
            if char not in dictT:
                dictT[char] = 0
            dictT[char] += 1

        return dictT == dictS