class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        #time: O(n)
        #space: O(1)

        l = 0
        r = 1
        min_len = float('inf')
        cur_len = 0
        
        seen = set()
        seen.add(cards[l])
        while r < len(cards):
            if cards[r] not in seen:
                seen.add(cards[r])
                r += 1
            else:
                cur_len = r - l + 1
                min_len = min(cur_len, min_len) 
                seen.remove(cards[l])
                l += 1
        return min_len if min_len != float('inf') else -1


        