#!/usr/bin/env python3
"""
Given an integer array `nums`, in which exactly two elements appear only once and all
the other elements appear exactly twice. Find the two elements that appear only once.
You can return the answer in any order.

You must write an algorithm that runs in linear runtime complexity and uses only
constant extra space.
"""
from typing import Dict, List, Optional, Set, Tuple


class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        """
        We first take the XOR of all elements, which will give us the XOR of the pair of
        single elements (`a ⊕ b`).

        We can then partition the elements into two distinct sets, where one contains
        `a` and the other contains `b`. This is achieved by taking any set bit in `a ⊕
        b`, as `a` and `b` must have different values at this bit, and then partitioning
        the elements based on if each has that bit set.

        As a shortcut, we only need to calculate the XOR of one set (i.e., `a`), and
        then compute `(a ⊕ b) ⊕ a` which will leave us with `b`.
        """
        # Calculate XOR of all elements
        xor_all = 0
        for n in nums:
            xor_all ^= n
        # Get smallest non-zero bit
        non_zero_bit = xor_all & (xor_all - 1) ^ xor_all
        # Get XOR of elements with the non-zero bit
        xor_set = 0
        for n in nums:
            if n & non_zero_bit:
                xor_set ^= n
        # Form answer
        a = xor_set
        b = xor_all ^ xor_set
        return [a, b]


class Test:
    def test(self):
        """
        Given test case from Leetcode.
        """
        case = [[1, 2, 1, 3, 2, 5]]
        expected = [3, 5]

        assert Solution().singleNumber(*case) == expected

    def test_negative(self):
        """
        Given test case from Leetcode, with a negative value.
        """
        case = [[-1, 0]]
        expected = [-1, 0]

        assert Solution().singleNumber(*case) == expected

    def test_pair(self):
        """
        Given test case from Leetcode, with a pair of values in the input.
        """
        case = [[0, 1]]
        expected = [1, 0]

        assert Solution().singleNumber(*case) == expected
