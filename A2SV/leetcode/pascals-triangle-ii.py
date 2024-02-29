class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        def pascalsTriange(n):
            if n == 0:
                return [1]
            elif n == 1:
                return [1,1]
            else:
                prev_arr = pascalsTriange(n-1)
                cur_arr = [1]
                for i in range((len(prev_arr))-1):
                    cur_arr.append(prev_arr[i] + prev_arr[i+1])
                cur_arr += [1]
            return cur_arr

        return pascalsTriange(rowIndex)

        