class Solution:
    def maxSumRangeQuery(self, nums: List[int], requests: List[List[int]]) -> int:
        #time: O(n)
        #space: O(n)

        MOD = 10**9 + 7
        n = len(nums)
        
        freq = [0] * n
        for start, end in requests:
            freq[start] += 1
            if end + 1 < n:
                freq[end + 1] -= 1

        for i in range(1, n):
            freq[i] += freq[i - 1]

        nums.sort(reverse=True)
        freq.sort(reverse=True)

        result = 0
        for num, f in zip(nums, freq):
            result = (result + num * f) % MOD

        return result


        
        # n = len(nums)
        # pos = [idx for start, end in requests for idx in range(start, end+1)]

        # freq_counter = Counter(pos)
        # sorted_freq_counter = dict(sorted(freq_counter.items(), key=itemgetter(1), reverse=True))
        
        # nums.sort(reverse = True)

        # max_per = [0] * n
        # for i, (idx, freq) in enumerate(sorted_freq_counter.items()):
        #     max_per[idx] = nums[i]
        # print(max_per)
        # arr = [0] * (n)
        # cur = 0
        
        # for first,last in requests:
        #     arr[first] += 1
        #     arr[last + 1] -= 1
        
        # for i in range(1, len(arr)):
        #     arr[i] += arr[i-1] 

        # res = [0] * n

        # for i in range(n):
        #     res[i] = max_per[i] + arr[i]

        # for i in range(n):
        #     res[i] += res[i - 1]

        # return res[-1]
