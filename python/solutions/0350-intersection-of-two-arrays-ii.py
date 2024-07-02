#!/usr/bin/env python3
"""
Given two integer arrays `nums1` and `nums2`, return an array of their intersection.
Each element in the result must appear as many times as it shows in both arrays and you
may return the result in any order.
"""
from typing import Dict, List, Optional, Set, Tuple


class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """
        Generate a counter for each array. Initialise a result list, and for each shared
        key, take its minimum count between the two counters and add the key to the
        result list this many times.
        """
        # Generate counter for first input array
        counter1 = {}
        for n in nums1:
            if n not in counter1:
                counter1[n] = 0
            counter1[n] += 1
        # Generate counter for second input array
        counter2 = {}
        for n in nums2:
            if n not in counter2:
                counter2[n] = 0
            counter2[n] += 1
        # Generate result list
        result = []
        for k, v in counter1.items():
            # Handle case of non-shared key
            if k not in counter2:
                continue
            # Get minimum count of each shared key
            result.extend([k] * min(counter1[k], counter2[k]))
        return result


class Test:
    def test(self):
        """
        Given test case from Leetcode.
        """
        case = [[1, 2, 2, 1], [2, 2]]
        expected = [2, 2]

        assert Solution().intersect(*case) == expected

    def test_singletons(self):
        """
        Given test case from Leetcode, with duplicate elements in one array only.
        """
        case = [[4, 9, 5], [9, 4, 9, 8, 4]]
        expected = [4, 9]

        assert Solution().intersect(*case) == expected
