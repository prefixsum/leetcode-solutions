#!/usr/bin/env python3
"""
Write a function that reverses a string. The input string is given as an array of
characters `s`.

You must do this by modifying the input array in-place with `O(1)` extra memory.
"""
from typing import Dict, List, Optional, Set, Tuple


class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Initialise a left pointer and a right pointer. Swap their values, and then
        increment and decrement them respectively, until they meet or cross.
        """
        # Initialise pointers
        left = 0
        right = len(s) - 1
        # Iterate over list in each direction
        while left < right:
            # Swap values
            s[left], s[right] = s[right], s[left]
            # Move pointers
            left += 1
            right -= 1
        # Return list
        return s


class Test:
    def test(self):
        """
        Given test case from Leetcode.
        """
        case = [["h", "e", "l", "l", "o"]]
        expected = ["o", "l", "l", "e", "h"]

        assert Solution().reverseString(*case) == expected

    def test_capital(self):
        """
        Given test case from Leetcode, with a capital letter.
        """
        case = [["H", "a", "n", "n", "a", "h"]]
        expected = ["h", "a", "n", "n", "a", "H"]

        assert Solution().reverseString(*case) == expected
