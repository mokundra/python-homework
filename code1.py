class Solution:
    def summaryRanges(self, nums: list[int]) -> list[str]:
        n=len(nums)
        if n==0:
            return []
        res=[]
        cur=nums[0]
        for i in range(1,n):
            if nums[i]==nums[i-1]+1:
                continue
            else:
                if cur==nums[i-1]:
                    res.append(str(cur))
                else:
                    res.append(f"{cur}->{nums[i-1]}")
                cur=nums[i]
        if cur==nums[-1]:
            res.append(str(cur))
        else:
            res.append(f"{cur}->{nums[-1]}")

        return res
