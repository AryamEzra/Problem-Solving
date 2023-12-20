class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # time complexity: O(n) -> 2n
        # space complexity: O(n) -> 3n

        ans = "".join(str(i) for i in digits)
        ans = int(ans) + 1
        ans = str(ans)
        ans = [int(i) for i in ans]
        return ans


        