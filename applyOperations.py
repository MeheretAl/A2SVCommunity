def applyOperations(nums: list[int]) -> list[int]:

    for i in range(len(nums)):
        if i < len(nums) - 1 and nums[i] == nums[i+1]:
            nums[i] = nums[i]*2
            nums[i+1] = 0
    i = 0
    for j in range(len(nums)):
        if nums[j] != 0:
            nums[j] , nums[i] = nums[i], nums[j]
            i+=1
        
    return nums

applyOperations([0,1])