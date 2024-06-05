#!/usr/bin/env python3
"""
Given a string array `words`, return an array of all characters that show up in all
strings within the `words` (including duplicates). You may return the answer in any
order.
"""
from typing import Dict, List, Optional, Set, Tuple


class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        """
        Start with a counter of each character in the first word. For each word, replace
        the counter with the intersection of the word's characters and the counter, with
        each remaining character's count being the minimum of the old and new counts.
        """
        # Handle empty case
        if len(words) == 0:
            return []
        # Handle case of single word
        if len(words) == 1:
            return [c for c in words[0]]
        # Initialise counter for all words
        counter = {}
        # Count letters in first word
        for c in words[0]:
            if c not in counter:
                counter[c] = 0
            counter[c] += 1
        # Iterate over words
        for word in words[1:]:
            # Count letters in current word
            word_counter = {}
            for c in word:
                if c not in word_counter:
                    word_counter[c] = 0
                word_counter[c] += 1
            # Get intersection of counters with their minimum as count
            new_counter = {}
            for k, v in counter.items():
                if k in word_counter:
                    new_counter[k] = min(counter[k], word_counter[k])
            # Replace counter with intersection
            counter = new_counter
        # Generate list of shared characters with duplicates
        result = []
        for k, v in counter.items():
            result.extend([k for _ in range(v)])
        return result


class Test:
    def test(self):
        """
        Given test case from Leetcode.
        """
        case = [["bella", "label", "roller"]]
        expected = ["e", "l", "l"]

        assert Solution().commonChars(*case) == expected

    def test_unique(self):
        """
        Given test case from Leetcode, with each common character appearing once.
        """
        case = [["cool", "lock", "cook"]]
        expected = ["c", "o"]

        assert Solution().commonChars(*case) == expected
