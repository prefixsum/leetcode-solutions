#!/usr/bin/env python3
"""
Given an integer array `arr`, return `true` if there are three consecutive odd numbers
in the array. Otherwise, return `false`.
"""
from typing import Dict, List, Optional, Set, Tuple


class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        """
        Iterate over the array, keeping count of successive odd numbers. If the counter
        ever reaches 3, return True. Otherwise, return False.
        """
        # Initialise counter
        counter = 0
        # Iterate over input array
        for n in arr:
            # Case of odd number
            if n % 2:
                # Increment counter and check current result
                counter += 1
                if counter == 3:
                    return True
            # Case of even number
            else:
                # Reset counter
                counter = 0
        # Consecutive odds not found
        return False


class Test:
    def test(self):
        """
        Given test case from Leetcode.
        """
        case = [[2, 6, 4, 1]]
        expected = False

        assert Solution().threeConsecutiveOdds(*case) == expected

    def test_truthy(self):
        """
        Given test case from Leetcode, expected to return True.
        """
        case = [[1, 2, 34, 3, 4, 5, 7, 23, 12]]
        expected = True

        assert Solution().threeConsecutiveOdds(*case) == expected
