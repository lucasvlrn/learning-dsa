def bubble_sort(nums):
    size = len(nums)
    for _ in nums:
        is_sorted = True
        print(nums)
        for j in range(size-1):
           if nums[j] > nums[j+1]:
                is_sorted = False
                pot = nums[j]
                nums[j] = nums[j+1]
                nums[j+1] = pot
        if is_sorted:
            return




# bubble_sort([5,4,3,2,1])
# bubble_sort([1,2,3,4,5])
bubble_sort([1,2,5,4,3])