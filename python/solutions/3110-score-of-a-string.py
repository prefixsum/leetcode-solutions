#!/usr/bin/env python3
"""
You are given a string `s`. The score of a string is defined as the sum of the absolute
difference between the ASCII values of adjacent characters.

Return the score of `s`.
"""
from typing import Dict, List, Optional, Set, Tuple


class Solution:
    def scoreOfString(self, s: str) -> int:
        """
        Initialise a tracker. Iterate over each character, incrementing the result by
        the absolute difference to the next character.
        """
        result = 0
        for i in range(len(s) - 1):
            result += abs(ord(s[i]) - ord(s[i + 1]))
        return result


class Test:
    def test(self):
        """
        Given test case from Leetcode.
        """
        case = ["hello"]
        expected = 13

        assert Solution().scoreOfString(*case) == expected

    def test_alphabet(self):
        """
        Given test case from Leetcode, ranging across the entire alphabet.
        """
        case = ["zaz"]
        expected = 50

        assert Solution().scoreOfString(*case) == expected
