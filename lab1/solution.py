class Solution:
    def insert(
        self, intervals: list[list[int]], newInterval: list[int]
    ) -> list[list[int]]:
        res = []

        if len(intervals) == 0 or len(newInterval) == 0:
            raise ValueError
        if len(newInterval) != 2:
            raise IndexError
        if len(intervals) > 10000:
            raise IndexError
        for g in range(len(newInterval)):
            if newInterval[g] < 0 or newInterval[g] > 100000:
                raise ValueError
        for i in range(len(intervals)):
            if len(intervals[i]) > 2:
                raise IndexError
            if intervals[i][0] < 0 or intervals[i][1] < 0 or intervals[i][0] > 100000 or intervals[i][1] > 100000:
                raise ValueError
            if newInterval[1] < intervals[i][0]:
                res.append(newInterval)
                return res + intervals[i:]
            elif newInterval[0] > intervals[i][1]:
                res.append(intervals[i])
            else:
                newInterval = [
                    min(newInterval[0], intervals[i][0]),
                    max(newInterval[1], intervals[i][1]),
                ]
        res.append(newInterval)
        return res
