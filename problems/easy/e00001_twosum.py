r"""module docstring
# @filename           :  00001_two_sum.py
# @author             :  Copyright (C) Church.ZHONG
# @date               :  Fri Sep 16 02:02:34 PM HKT 2022
"""

__all__ = ['DATA00001']

DATA00001 = {
    "title": "Two Sum",
    "url": "https://leetcode.com/problems/two-sum",
    "description": r'''
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
 

Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?
''',
    "entry": r'''
class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target) {
        
    }
};
''',
}
