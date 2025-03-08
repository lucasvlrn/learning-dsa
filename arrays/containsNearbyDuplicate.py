def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
    counter={}
    for item in range(len(nums)):
        if nums[item] in counter:
            if abs(item - counter[nums[item]]) <= k:
                print(item, counter[nums[item]])
                return True  
            counter.update({nums[item]: item})
        counter.update({nums[item]: item})
                
    return False