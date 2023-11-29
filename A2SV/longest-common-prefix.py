class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = []

        strs.sort()
        min_length = min(len(s) for s in strs)

        for i in range(min_length):
            char = strs[0][i]
            if all(s[i] == char for s in strs):
                prefix += char
            else:
                break
        return "".join(prefix)

        