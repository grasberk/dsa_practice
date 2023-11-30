Given a non-empty array of integers nums, every element appears twice except for one. Find that single one.

You must implement a solution with a linear runtime complexity and use only constant extra space.

Example 1:

Input: nums = [2,2,1]
Output: 1
Example 2:

Input: nums = [4,1,2,1,2]
Output: 4
Example 3:

Input: nums = [1]
Output: 1
 

Constraints:

1 <= nums.length <= 3 * 104
-3 * 104 <= nums[i] <= 3 * 104
Each element in the array appears twice except for one element which appears only once.

Each project submission must have at least four seperate commits
* One: Summarize the problem in your own words, explaining as clearly as possible
        1. an array that is not empty contains numbers. In the list of numbers every number is repeating except for one number. Find the number that does not repeat.
* Two: Write test cases for example inputs and outputs
    [2,2,1]
    expected_result: 1
    results: 
    assertEqual(expected_result, results)
    [2,2,2]
    expected_result: 
    result:
    assertEqual(expected_result, results)
    [1,2,3]
    expected_result: 1,2,3
    result
    assertEqual(expected_result, results)
* Three: Pseudocode your plan in comments
    iterate through each element in the list and to a list of unique elements, if it repeats add one to the counter, after list is iterated and each value is assigned a counter, the value with counter of 1 is the desired result 
* Four (and above): Commit your code as you go until you solution is complete

