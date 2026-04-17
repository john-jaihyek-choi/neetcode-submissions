class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        car_fleet = []
        road = list(zip(position, speed))
        road.sort(reverse=True)

        # distance_remaining = target - postion[i]
        # time_remaining = distance_remaining / speed[i]

        for position, speed in road:
            distance_remaining = target - position
            time_remaining = distance_remaining / speed

            if car_fleet and car_fleet[-1] >= time_remaining:
                continue
            
            car_fleet.append(time_remaining)


        return len(car_fleet)