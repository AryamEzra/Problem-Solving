class Solution:
    def distributeCookies(self, cookies: List[int], k: int) -> int:
        cookies.sort(reverse = True)
        c = len(cookies)
        buckets = [0] * k
        self.minn = float('inf')
        def backtrack(i ,buckets):
            if i >= c:
                self.minn = min(self.minn, max(buckets))
                return

            for j in range(k):
                if buckets[j] + cookies[i] >= self.minn:
                    continue
                    
                buckets[j] += cookies[i]
                backtrack(i+1, buckets)
                buckets[j] -= cookies[i]
        backtrack(0, buckets)
        return self.minn

        
        