class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        


        p1 = [0, 0]  # left_score
        p2 = [0, 0] # right_score
        def scoreCalc(s, e, turn):
            if s == e:
                if turn:
                    return [nums[s], 0]
                return [0, nums[s]]
            
            if turn:
                left_score = scoreCalc(s + 1, e, not turn)
                right_score = scoreCalc(s, e - 1, not turn)

                left_score[0] += nums[s]
                right_score[0] += nums[e]
                if left_score[0] > right_score[0]:
                    return left_score
                else:
                    return right_score
                
                
            else:
                left_score = scoreCalc(s + 1, e, not turn)
                right_score = scoreCalc(s, e - 1, not turn)

                left_score[1] += nums[s]
                right_score[1] += nums[e]

                if left_score[1] > right_score[1]:
                    return left_score
                else:
                    return right_score 
            
        var =  scoreCalc(0, len(nums)-1,True)
        return var[0] >= var[1]




        #(pl-(p2-(pl-(p2-(pl-(p2-(pl-))))))) - onw score approch
        # def solve(left, right):
        #     if left == right:
        #         return nums[left]
        #     left_score = nums[left] - solve(left + 1, right)
        #     right_score = nums[right] - solve(left, right - 1)

        #     return left_score >= right_score
        # return solve(0, len(nums) - 1) >= 0

        # def scoreCalc(s, e, turn):
        #     if s == e:
        #         if turn:
        #             return [nums[s], 0]
        #         return [0, nums[s]]
            
        #     score = [0, 0]

        #     if turn:
        #         temp = scoreCalc(s + 1, e, not turn)
        #         temp2 = scoreCalc(s, e - 1, not turn)

        #         score[0] += max(nums[s] + temp[0], temp2[1] + nums[e])
        #         print(temp)
        #         print(temp2) 
        #     else:
        #         temp = scoreCalc(s + 1, e, not turn)
        #         temp2 = scoreCalc(s, e - 1, not turn)

        #         score[1] += max(nums[s] + temp[0], temp2[1] + nums[e])
        #         print(temp)
        #         print(temp2)  
            
        #     return score

        # val = scoreCalc(0, len(nums)-1,True)
        
        # return val[1] <= val[0]
