#!/usr/bin/env python3
"""
You are given two strings `s` and `t` consisting of only lowercase English letters.

Return the minimum number of characters that need to be appended to the end of `s` so
that `t` becomes a subsequence of `s`.

A subsequence is a string that can be derived from another string by deleting some or no
characters without changing the order of the remaining characters.
"""
from typing import Dict, List, Optional, Set, Tuple


class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        """
        Initialise a pointer each on `s` and `t`. Seek the pointer forwards on `s`, and
        if its value matches the current value on `t`, push the `t` pointer forwards by
        one. After this pass, the result is the number of characters remaining on `t`
        after its pointer.
        """
        # Initialise pointer on t
        ptr_t = 0
        # Seek forwards
        for ptr_s in range(len(s)):
            # Check match
            if s[ptr_s] == t[ptr_t]:
                ptr_t += 1
            # Check if t exhausted
            if ptr_t == len(t):
                return 0
        # Return characters remaining in t
        return len(t) - ptr_t


class Test:
    def test(self):
        """
        Given test case from Leetcode.
        """
        case = ["coaching", "coding"]
        expected = 4

        assert Solution().appendCharacters(*case) == expected

    def test_zero(self):
        """
        Given test case from Leetcode, with t already a subsequence of s.
        """
        case = ["abcde", "a"]
        expected = 0

        assert Solution().appendCharacters(*case) == expected

    def test_all(self):
        """
        Given test case from Leetcode, with all of t needing to be appended to s.
        """
        case = ["z", "abcde"]
        expected = 5

        assert Solution().appendCharacters(*case) == expected
