class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        #time: O(n)
        #space: O(1)

        white_count = 0
        left = 0
        res = float('inf')
        for right in range(len(blocks)):
            if blocks[right] == "W":
                white_count += 1
            if right - k >= 0 and blocks[right - k] == "W":
                white_count -= 1
            if right - k + 1 >= 0:
                res = min(res, white_count)
        return res   


        