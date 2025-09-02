class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        
        p = ""
        l = [len(i) for i in strs]
        r = min(l)
        good = True
        for i in range(r):
            for j in range(1, len(strs)):
                if strs[0][i] != strs[j][i]:
                    good = False
                    break
            if good:
                p += strs[0][i]
            else: 
                break
        return p
