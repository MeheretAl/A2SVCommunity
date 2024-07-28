def getConcatenation( nums: list[int]) -> list[int]:
    size = len(nums)
    ans = [0]*(2*size)
    for i in range(size):
        ans[i] = nums[i]
        ans[i+size] = nums[i]
    
    return ans