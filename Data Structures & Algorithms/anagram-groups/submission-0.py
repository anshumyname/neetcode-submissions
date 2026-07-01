class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = []
        seen = {}
        for s in strs:
            a = tuple(sorted(s))
            if a not in seen.keys():
                seen[a]= [s]
            else:
                seen[a].append(s)

        return list(seen.values())