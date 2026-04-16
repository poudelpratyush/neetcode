from collections import defaultdict
class TimeMap:

    def __init__(self):
        self.hm = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.hm[key].append([value, timestamp])
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.hm or self.hm[key][0][1] > timestamp:
            return ""
        else:
            values = self.hm[key]
            for i in range(len(values) - 1, -1, -1):
                if values[i][1] <= timestamp:
                    return values[i][0]


        
