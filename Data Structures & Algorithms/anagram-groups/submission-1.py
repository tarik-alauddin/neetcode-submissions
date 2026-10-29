class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        l = defaultdict(list)

        for s in strs:
            sort = "".join(sorted(s))

            l[sort].append(s)

        return list(l.values())