class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        res = list(s)

        for start in range(0, len(s), 2*k):
            end = start + k
            res[start:end] = reversed(res[start:end])

        return "".join(res)

    