class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        car_fleet = []
        road = list(zip(position, speed))
        road.sort()

        for i in range(len(road) - 1, -1, -1):
            car = road[i]
            time_remaining = (target - car[0]) / car[1]

            if car_fleet and car_fleet[-1] >= time_remaining:
                continue
            car_fleet.append(time_remaining)

        return len(car_fleet)