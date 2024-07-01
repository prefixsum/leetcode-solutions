#!/usr/bin/env python3
"""
A school is trying to take an annual photo of all the students. The students are asked
to stand in a single file line in non-decreasing order by height. Let this ordering be
represented by the integer array `expected` where `expected[i]` is the expected height
of the `i^th` student in line.

You are given an integer array `heights` representing the current order that the
students are standing in. Each `heights[i]` is the height of the `i^th` student in line
(0-indexed).

Return the number of indices where `heights[i] != expected[i]`.
"""
from typing import Dict, List, Optional, Set, Tuple


class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        """
        Build a sorted list, and iterate over both while counting their differences.
        """
        # Generate sorted list of heights
        expected = sorted(heights)
        # Initialise counter
        result = 0
        # Iterate over heights
        for i in range(len(heights)):
            # Increment counter if mismatch
            if heights[i] != expected[i]:
                result += 1
        # Return counter
        return result


class Test:
    def test(self):
        """
        Given test case from Leetcode.
        """
        case = [[1, 1, 4, 2, 1, 3]]
        expected = 3

        assert Solution().heightChecker(*case) == expected

    def test_all(self):
        """
        Given test case from Leetcode, where all heights mismatch.
        """
        case = [[5, 1, 2, 3, 4]]
        expected = 5

        assert Solution().heightChecker(*case) == expected

    def test_none(self):
        """
        Given test case from Leetcode, where no heights are out of order.
        """
        case = [[1, 2, 3, 4, 5]]
        expected = 0

        assert Solution().heightChecker(*case) == expected
