def twoSum(nums: List[int], target: int) -> List[int]:
    d=dict()
    for item in range(len(nums)):
        summ = target - nums[item]
        if summ in d:
            print(d)
            return d[summ], item
        else:
            d.update({nums[item]: item })
            item+1
        return []
                