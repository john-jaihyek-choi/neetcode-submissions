class TimeMap:
    def __init__(self):
        self.people = defaultdict(list[str, int])
    
    def set(self, key: str, value: str, timestamp: int) -> None:
        self.people[key].append([value, timestamp])
        return 

    def get(self, key: str, timestamp: int) -> str:
        res, timestamps = "", self.people[key]

        l, r = 0, len(timestamps) - 1
        while l <= r:
            m = (r + l) // 2
            val, time = timestamps[m]

            if time <= timestamp:
                res = val
                l = m + 1
            else:
                r = m - 1

        return res
