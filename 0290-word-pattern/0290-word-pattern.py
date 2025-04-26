class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s=s.split()
        if len(pattern)!=len(s) or len(set(s))!=len(set(pattern)):
            return False
        d={}
        for i in range(len(s)):
            if pattern[i] in d:
                if d[pattern[i]]!=s[i] :
                    return False
            else:
                d[pattern[i]]=s[i]
        return True