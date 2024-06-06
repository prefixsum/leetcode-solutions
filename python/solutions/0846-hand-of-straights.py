#!/usr/bin/env python3
"""
Alice has some number of cards and she wants to rearrange the cards into groups so that
each group is of size `groupSize`, and consists of `groupSize` consecutive cards.

Given an integer array `hand` where `hand[i]` is the value written on the `i^th` card
and an integer `groupSize`, return `true` if she can rearrange the cards, or `false`
otherwise.
"""
import collections
from typing import Dict, List, Optional, Set, Tuple


class Solution:
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        """
        Generate a count of each card, and then iteratively subtract staights from this
        count starting with the smallest card.
        """
        # Get count of each card
        counter = collections.Counter(hand)
        # Iterate over cards, sorted by count
        for card in sorted(counter):
            # Skip card if counter now at zero
            if counter[card] == 0:
                continue
            # Attempt to subtract straights starting at card
            straights = counter[card]
            for i in range(groupSize):
                # Check if enough cards to satisfy number of straights
                if counter[card + i] < straights:
                    return False
                # Subtract number of straights from count
                counter[card + i] -= straights
        # If all straights subtracted, return true
        return True


class Test:
    def test(self):
        """
        Given test case from Leetcode.
        """
        case = [[1, 2, 3, 6, 2, 3, 4, 7, 8], 3]
        expected = True

        assert Solution().isNStraightHand(*case) == expected

    def test_falsey(self):
        """
        Given test case from Leetcode, which should return false.
        """
        case = [[1, 2, 3, 4, 5], 4]
        expected = False

        assert Solution().isNStraightHand(*case) == expected
