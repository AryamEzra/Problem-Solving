class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        #time complexity - O(nlogn) - beacuse of the sorting at the end
        #space complexity - O(n) - beacuse of the hashmap created 
        game = {}

        for winner, loser in matches:
            game[winner] = game.get(winner, 0)
            game[loser] = game.get(loser, 0) + 1
        
        never_lose = []
        lost_one_match = []

        for players, loss in game.items():
            if loss == 0:
                never_lose.append(players)
            elif loss == 1:
                lost_one_match.append(players)
        
        return [sorted(never_lose), sorted(lost_one_match)]




        