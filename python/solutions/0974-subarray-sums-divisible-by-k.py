#!/usr/bin/env python3
"""
Given an integer array `nums` and an integer `k`, return the number of non-empty
subarrays that have a sum divisible by `k`.

A subarray is a contiguous part of an array.
"""
from typing import Dict, List, Optional, Set, Tuple


class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        """
        If `sum([:i]) % k` is equal to `sum([:j]) % k`, then `sum([i:j]) % k` must equal
        to `0`, and therefore, `sum([i:j])` must be a multiple of `k`.

        Iterate over each subarray (i.e., `[:i]` for each `i`), keeping count of the
        number of subarrays for each remainder. At each `i`, calculate the current
        remainder (`[:i] % k`) and increment the result counter by the number of
        subarrays with the same remainder.
        """
        # Track arrays with remainder
        counts = {
            0: 1,  # Account for sum([:i]) % k == 0
        }
        # Initialise counter
        result = 0
        # Iterate over input array
        prefix_sum = 0
        for i in range(len(nums)):
            # Get current remainder
            prefix_sum += nums[i]
            remainder = prefix_sum % k
            # Compare remainder to previous remainders and increment counter
            if remainder not in counts:
                counts[remainder] = 0
            result += counts[remainder]
            # Increment remainder count
            counts[remainder] += 1
        # Return result counter
        return result


class Test:
    def test(self):
        """
        Given test case from Leetcode.
        """
        case = [[4, 5, 0, -2, -3, 1], 5]
        expected = 7

        assert Solution().subarraysDivByK(*case) == expected

    def test_zero(self):
        """
        Given test case from Leetcode, with no valid subarrays.
        """
        case = [[5], 9]
        expected = 0

        assert Solution().subarraysDivByK(*case) == expected
