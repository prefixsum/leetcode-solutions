#!/usr/bin/env python3
"""
Given an array of integers `nums` and an integer `target`, return indices of the two
numbers such that they add up to `target`.

You may assume that each input would have exactly one solution, and you may not use the
same element twice.

You can return the answer in any order.
"""
from typing import Dict, List, Optional, Set, Tuple


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """
        For each element, check if its complement has been seen before. If it
        has been seen, then return it and the current element's indices. Else,
        add it to the dictionary of seen elements with its index as its value.
        """
        # Initialise dictionary of seen elements
        seen = {}
        # Pass over inputs
        for i, n in enumerate(nums):
            # Get complement
            complement = target - n
            # Check if current element's complement has been seen
            if complement in seen:
                # Return current index and the complement's index
                return [seen[complement], i]
            # Add current input to dictionary
            seen[n] = i
        # Return empty list if no pair found
        return []


class Test:
    def test(self):
        """
        Given test case from Leetcode.
        """
        case = [[2, 7, 11, 15], 9]
        expected = [0, 1]

        assert Solution().twoSum(*case) == expected

    def test_last(self):
        """
        Given test case from Leetcode, with one index being the final index.
        """
        case = [[3, 2, 4], 6]
        expected = [1, 2]

        assert Solution().twoSum(*case) == expected

    def test_repeated(self):
        """
        Given test case from Leetcode, with repeated values.
        """
        case = [[3, 3], 6]
        expected = [0, 1]

        assert Solution().twoSum(*case) == expected
