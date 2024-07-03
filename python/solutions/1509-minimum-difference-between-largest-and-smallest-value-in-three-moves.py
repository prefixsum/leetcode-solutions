#!/usr/bin/env python3
"""
You are given an integer array `nums`.

In one move, you can choose one element of `nums` and change it to any value.

Return the minimum difference between the largest and smallest value of `nums` after
performing at most three moves.
"""
import heapq

from typing import Dict, List, Optional, Set, Tuple


class Solution:
    def minDifference(self, nums: List[int]) -> int:
        """
        Consider the sorted list of nums.

        We want to remove some combination of its smallest and largest values so that
        the difference between the smallest value and the largest value is minimised.

        For each n in 0 <= n <= 3, remove the n smallest values and the 3 - n largest
        values from the input array, and calculate the array's difference in each case.
        Find the minimum of these differences.

        This is done trivially by calculating and comparing the following:
        - nums[-4] - nums[0]
        - nums[-3] - nums[1]
        - nums[-2] - nums[2]
        - nums[-1] - nums[3]

        However, consider that we do not require the whole list to be sorted; we need
        only the 4 smallest values, sorted, and the 4 largest values, sorted.

        A heap is perfect for this, reducing our runtime at this point from O(n log n)
        to O(n log 4).

        Importantly, we're able to compare the pairs of elements in O(4) time by
        traversing the heaps linearly, reducing our final runtime from O(n log n + 4) to
        O(n log 4 + 4), or O(n).
        """
        # Generalise problem on k=3
        k = 3
        # Handle case of small input list
        if len(nums) <= k + 1:
            return 0
        # Use two heaps in order to get smallest and largest values
        smallest = heapq.nsmallest(k + 1, nums)
        largest = heapq.nlargest(k + 1, nums)
        # Compare pairwise differences
        best = None
        for i in range(k + 1):
            if not best:
                best = largest[~i] - smallest[i]
            else:
                best = min(best, largest[~i] - smallest[i])
        return best


class Test:
    def test(self):
        """
        Given test case from Leetcode.
        """
        case = [[5, 3, 2, 4]]
        expected = 0

        assert Solution().minDifference(*case) == expected

    def test_non_zero(self):
        """
        Given test case from Leetcode, with a minimum difference larger than 0.
        """
        case = [[1, 5, 0, 10, 14]]
        expected = 1

        assert Solution().minDifference(*case) == expected

    def test_three_values(self):
        """
        Given test case from Leetcode, with three values.
        """
        case = [[3, 100, 20]]
        expected = 0

        assert Solution().minDifference(*case) == expected
