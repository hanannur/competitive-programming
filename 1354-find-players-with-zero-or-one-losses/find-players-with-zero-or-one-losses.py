from collections import Counter
class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        loss_count = Counter()
        players = set()
        
        for winner, loser in matches:
            loss_count[loser] += 1
            players.add(winner)
            players.add(loser)
        
        zero_loss = []
        one_loss = []
        
        for player in players:
            if loss_count[player] == 0:
                zero_loss.append(player)
            elif loss_count[player] == 1:
                one_loss.append(player)
                
        return [sorted(zero_loss), sorted(one_loss)]
