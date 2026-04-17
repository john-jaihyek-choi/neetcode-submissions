class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        """
        Intuition:
            - Bruteforce:
                - compute distance between origin and every coordinate in points[i]
                - sort the list of distance in increasing order
                - return last kth elements from the sorted list
        """
        origin = [0, 0]
        distances = []
        for point in points:
            distance = self.calcDistance(origin, point)
            distances.append(tuple([distance, [point[0], point[1]]]))
        
        distances.sort()

        return [item[1] for item in distances[:k]]

    def calcDistance(self, coord1: List[int], coord2: List[int]) -> float:
        return math.sqrt(pow(coord1[0] - coord2[0], 2) + pow(coord1[1] - coord2[1], 2))
        