def findGCD(nums: list[int]) -> int:
    small = min(nums)
    large = max(nums)

    while small:
        large, small = small, large % small

    return large

print(findGCD([2,5,6,9,10]))
print(findGCD([7,5,6,8,3]))
print(findGCD([3,3]))