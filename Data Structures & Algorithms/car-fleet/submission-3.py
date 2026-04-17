class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        car_fleet = [] # O(1)
        road = list(zip(position, speed)) # O(n)
        road.sort() # O(n log n)

        for i in range(len(road) - 1, -1, -1): # O(n)
            car = road[i] # O(1)
            time_remaining = (target - car[0]) / car[1] # O(1)

            car_fleet.append(time_remaining) # O(1)

            if len(car_fleet) >= 2 and car_fleet[-1] <= car_fleet[-2]: # O(1)
                car_fleet.pop()

        return len(car_fleet) # O(1)