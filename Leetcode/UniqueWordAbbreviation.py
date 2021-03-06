__author__ = 'Michael'
"""
An abbreviation of a word follows the form <first letter><number><last letter>. Below are some examples of word abbreviations:

a) it                      --> it    (no abbreviation)

     1
b) d|o|g                   --> d1g

              1    1  1
     1---5----0----5--8
c) i|nternationalizatio|n  --> i18n

              1
     1---5----0
d) l|ocalizatio|n          --> l10n
Assume you have a dictionary and given a word, find whether its abbreviation is unique in the dictionary. A word's abbreviation is unique if no other word from the dictionary has the same abbreviation.

Example:
Given dictionary = [ "deer", "door", "cake", "card" ]

isUnique("dear") -> false
isUnique("cart") -> true
isUnique("cane") -> false
isUnique("make") -> true

"""
from collections import defaultdict


@profile
def abbreviate(word):
    if len(word) <= 2:
        return word

    in_between = len(word[1:-1])
    return ''.join([word[0], str(in_between), word[-1]])


class ValidWordAbbr:
    @profile
    def __init__(self, dictionary):
        """
        initialize your data structure here.
        :type dictionary: List[str]
        """
        self.dict3 = defaultdict(int)
        self.dict2 = defaultdict(int)
        for word in dictionary:
            self.dict2[abbreviate(word)] += 1
            self.dict3[word] += 1

    @profile
    def isUnique(self, word):
        """
        check if a word is unique.
        :type word: str
        :rtype: bool
        """
        # print("Word: {} Abbreviation: {}".format(word, abbreviate(word)))
        if word not in self.dict3.keys():
            return self.dict2[abbreviate(word)] == 0
        else:
            return self.dict2[abbreviate(word)] == self.dict3[word]



            # Your ValidWordAbbr object will be instantiated and called as such:
            # vwa = ValidWordAbbr(dictionary)
            # vwa.isUnique("word")
            # vwa.isUnique("anotherWord")


test1 = ["deer", "door", "cake", "card"]
vwa = ValidWordAbbr(test1)

vwa.isUnique("dear")
vwa.isUnique("cart")
vwa.isUnique("cane")
vwa.isUnique("make")
vwa.isUnique("card")

from unittest import TestCase

test1 = ["deer", "door", "cake", "card"]


class TestValidWordAbbr(TestCase):
    def test_isUnique(self):
        vwa = ValidWordAbbr(test1)
        print(vwa.dict2)
        self.assertFalse(vwa.isUnique("dear"))
        self.assertTrue(vwa.isUnique("cart"))
        self.assertFalse(vwa.isUnique("cane"))
        self.assertTrue(vwa.isUnique("make"))
        self.assertTrue(vwa.isUnique("card"))
