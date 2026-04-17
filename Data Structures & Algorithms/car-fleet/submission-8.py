class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # stack to store the fleet of cars
            # car_fleet = [ eta1, ... ]
        # list to store the position and speed pair in the reversed
            #          c1     c2
            # road = [(1,3), (4,2)]

        car_fleet = []
        road = list(zip(position, speed))
        road.sort(reverse=True)

        # destination/target
        # position
        # speed
        # distance_remaining
            # target - position
        # eta
            # distance_remaining / speed

        for position, speed in road:
            distance_remaining = target - position
            eta = distance_remaining / speed

            if car_fleet and eta <= car_fleet[-1]:
                continue

            car_fleet.append(eta)
        print(car_fleet)
        return len(car_fleet)