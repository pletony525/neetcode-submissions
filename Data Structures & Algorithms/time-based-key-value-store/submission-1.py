class TimeMap:
    #key, value map
    #time, key
    def __init__(self):
        self.keyMap = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.keyMap:
            values = []
            values.append((value, timestamp))
            self.keyMap[key] = values
        else:
            self.keyMap[key].append((value, timestamp))

    def get(self, key: str, timestamp: int) -> str:
        values = self.keyMap.get(key, [])
        return self.binary_search(values, timestamp)

    
    def binary_search(self, values: list, timestamp: int):
        l, r = 0, len(values) - 1
        result = ""
        while l <= r:
            m = (l + r) // 2
            timeVal = values[m][1]
            if timeVal <= timestamp:
                result = values[m][0]
                l = m + 1
            else:
                r = m - 1
        return result




        
