class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
       
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

