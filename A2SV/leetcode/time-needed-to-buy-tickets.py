class Solution:
    def timeRequiredToBuy(self, tickets: List[int], k: int) -> int:
        pos = k
        time = 0
        tickets = deque(tickets)

        while tickets and tickets[pos] != 0:
            print(pos)
            tickets[0] -= 1
            time += 1
            if tickets[0] != 0:
                tmp = tickets.popleft()
                tickets.append(tmp)
            else:
                if pos == 0:
                    break
                tickets.popleft()
                
            if pos != 0:
                pos -= 1
            else:
                pos = len(tickets) - 1
            
        return time
        
        