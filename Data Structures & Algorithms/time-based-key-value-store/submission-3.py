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
            res = ""
            values = self.hm[key]
            # [1, 3, 6, 8]
            l, r = 0, len(values) - 1
            while l <= r:
                m = (l + r) // 2
                currM = values[m][1]
                if currM < timestamp:
                    res = values[m][0]
                    l = m + 1
                elif currM > timestamp:
                    r = m - 1
                else:
                    res = values[m][0]
                    break
            
            return res






        
