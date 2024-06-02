"""

Two Sum
Easy

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
Example 2:

Input: nums = [3,2,4], target = 6
Output: [1,2]
Example 3:

Input: nums = [3,3], target = 6
Output: [0,1]
 

Constraints:

2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.

"""

def twoSum(nums, target):
    result_list = []
    num1 = nums
    for a in nums:
        for b in num1:
            x = a+b
            if(x==target)and(nums.index(a)!=nums.index(b)):
                result_list.append(nums.index(a))
                result_list.append(nums.index(b))
                break
    result_list_sorted = result_list.sort()
    return result_list_sorted


nums = [3,2,4]
target = 6
final_list = []
final_list.append(twoSum(nums, target))
print(final_list)
