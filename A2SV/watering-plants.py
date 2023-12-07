class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        full_capa = capacity
        steps = 0
        for i in range(len(plants)):
            if plants[i] <= capacity:
                steps += 1
                capacity -= plants[i]
            else:
                capacity = full_capa
                steps += 1
                capacity -= plants[i]
                steps += (i*2)
        return steps


        