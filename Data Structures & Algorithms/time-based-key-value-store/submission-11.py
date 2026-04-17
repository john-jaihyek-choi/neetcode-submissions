class TimeMap:
    def __init__(self):
        self.people = defaultdict(list[str, int])
    
    def set(self, key: str, value: str, timestamp: int) -> None:
        self.people[key].append([value, timestamp])
        return 

    def get(self, key: str, timestamp: int) -> str:
        timestamps = self.people[key]

        l, r = 0, len(timestamps) - 1
        current_latest=''
        while l <= r:
            m = (r + l) // 2
            val, time = timestamps[m]

            if time <= timestamp:
                current_latest = val

            if time == timestamp:
                return val
            elif time < timestamp:
                l = m + 1
            else:
                r = m - 1

        return current_latest
