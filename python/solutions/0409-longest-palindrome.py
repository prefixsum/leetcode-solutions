#!/usr/bin/env python3
"""
Given a string `s` which consists of lowercase or uppercase letters, return the length
of the longest palindrome that can be built with those letters.

Letters are case sensitive, for example, `"Aa"` is not considered a palindrome.
"""
from typing import Dict, List, Optional, Set, Tuple


class Solution:
    def longestPalindrome(self, s: str) -> int:
        """
        Palindromes are constructed with pairs of letters, and well as an optional,
        single letter in the middle.

        Our approach is to add new characters to a set "seen", or if the character is
        already in the set, to remove it and then increment the result counter by two.

        Finally, we increment the counter a final time if there are any characters
        remaining in the set, and then return the counter.
        """
        # Initialise result counter
        counter = 0
        # Initialise tracker of seen characters
        seen = set()
        for c in s:
            # Case of current character forms pair
            if c in seen:
                seen.remove(c)
                counter += 2
            # Case of current character is singleton
            else:
                seen.add(c)
        # Adjust for remaining singleton in palindrome
        if seen:
            counter += 1
        # Return result, which is length of palindrome
        return counter


class Test:
    def test(self):
        """
        Given test case from Leetcode.
        """
        case = ["abccccdd"]
        expected = 7

        assert Solution().longestPalindrome(*case) == expected

    def test_singleton(self):
        """
        Given test case from Leetcode, with one character.
        """
        case = ["a"]
        expected = 1

        assert Solution().longestPalindrome(*case) == expected
