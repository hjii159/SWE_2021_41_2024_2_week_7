from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:
    # Your Codes
    ## Do not use input() or print() in your function
    ## Inputs (nums, target) will given as arguments and the output as
    ## return value
    for i in range(len(nums)-1):
        for j in range(i+1, len(nums)):
            if nums[i] == target-nums[j]:
                ret = [i, j]
                #print(f"i: {nums[i]}[{i}], j: {nums[j]}[{j}]")
                break
        if ret:
            break
    return ret

"""
def main():
    nums = [3, 3]
    target = 6
    print(twoSum(nums, target))

main()
"""
