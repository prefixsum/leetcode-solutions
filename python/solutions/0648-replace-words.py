#!/usr/bin/env python3
"""
In English, we have a concept called root, which can be followed by some other word to
form another longer word - let's call this word derivative. For example, when the root
`"help"` is followed by the word `"ful"`, we can form a derivative `"helpful"`.

Given a `dictionary` consisting of many roots and a `sentence` consisting of words
separated by spaces, replace all the derivatives in the sentence with the root forming
it. If a derivative can be replaced by more than one root, replace it with the root that
has the shortest length.

Return the `sentence` after the replacement.
"""
from typing import Dict, List, Optional, Set, Tuple


class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        """
        Turn the dictionary into a set. For each word in the sentence, check if each
        root (i.e., each substring starting at 0) is in the set. If so, replace the word
        with the root, and then continue to the next word.
        """
        # Turn dictionary into set of roots
        roots = set(dictionary)
        # Iterate over words in sentence
        words = sentence.split(" ")
        for i in range(len(words)):
            # Get current word
            word = words[i]
            # Check if word can be replaced by roots of increasing size
            for j in range(len(word)):
                # Case of root not in dictionary
                if word[:j] not in roots:
                    continue
                # Case of root valid
                words[i] = word[:j]
                break
        # Reform words in sentence and return
        return " ".join(words)


class Test:
    def test(self):
        """
        Given test case from Leetcode.
        """
        case = [["cat", "bat", "rat"], "the cattle was rattled by the battery"]
        expected = "the cat was rat by the bat"

        assert Solution().replaceWords(*case) == expected

    def test_last(self):
        """
        Given test case from Leetcode, with one index being the final index.
        """
        case = [["a", "b", "c"], "aadsfasf absbs bbab cadsfafs"]
        expected = "a a b c"

        assert Solution().replaceWords(*case) == expected
