#!/usr/bin/env python3
"""
Given an integer array `nums` and an integer `k`, return `true` if `nums` has a good
subarray or `false` otherwise.

A good subarray is a subarray where:

- Its length is at least two, and
- The sum of the elements of the subarray is a multiple of `k`.

Note that:

- A subarray is a contiguous part of the array.
- An integer `x` is a multiple of `k` if there exists an integer `n` such that
`x = n * k`. `0` is always a multiple of `k`.
"""
from typing import Dict, List, Optional, Set, Tuple


class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        """
        If `sum([:i]) % k` is equal to `sum([:j]) % k`, then `sum([i:j]) % k` must equal
        to `0`, and therefore, `sum([i:j])` must be a multiple of `k`.

        Iterate over each subarray (i.e., `[:i]` for each `i`), keeping track of the
        smallest `i` at which each remainder can be formed from the subarray `[:i]`. At
        each `i`, check if the current remainder (`[:i] % k`) is equal to any previous
        remainders. If so, and if their respective indices have a difference of 2 or
        more, then a valid subarray has been found.
        """
        # Initialise tracker of sum([:i]) remainders
        remainders = {
            0: -1,  # Account for sum([:i]) % k == 0
        }
        # Iterate over input array
        prefix_sum = 0
        for i, n in enumerate(nums):
            # Get current remainder
            prefix_sum += n
            remainder = prefix_sum % k
            # Compare remainder to previous remainders, returning True if match found
            if remainder in remainders and i - remainders[remainder] > 1:
                return True
            # Add remainder to tracker, without replacing existing index for remainder
            if remainder not in remainders:
                remainders[remainder] = i
        # Return False if no match found
        return False


class Test:
    def test(self):
        """
        Given test case from Leetcode.
        """
        case = [[23, 2, 4, 6, 7], 6]
        expected = True  # [2, 4]

        assert Solution().checkSubarraySum(*case) == expected

    def test_all(self):
        """
        Given test case from Leetcode, where the solution derives from the full input.
        """
        case = [[23, 2, 6, 4, 7], 6]
        expected = True  # [23, 2, 6, 4, 7]

        assert Solution().checkSubarraySum(*case) == expected

    def test_falsey(self):
        """
        Given test case from Leetcode, expected to return False.
        """
        case = [[23, 2, 6, 4, 7], 13]
        expected = False

        assert Solution().checkSubarraySum(*case) == expected
