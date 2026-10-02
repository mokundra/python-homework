class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        n=len(intervals)
        intervals.sort()
        res=[intervals[0]]
        for i in range(1,n):
            last=res[-1]
            cur=intervals[i]
            if cur[0]<=last[1]:
                last[1]=max(last[1],cur[1])
            else:
                res.append(cur)
        return res
