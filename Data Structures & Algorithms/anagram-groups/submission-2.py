class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        l = defaultdict(list)

        for s in strs:
            f = [0]*26 # frequency array
            
            for c in s:
                f[ord(c)-ord('a')] += 1 #ascii subtract gives 0-26

            l[tuple(f)].append(s)

        return list(l.values())