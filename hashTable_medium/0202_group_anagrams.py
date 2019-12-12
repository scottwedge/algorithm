"""
49. Group Anagrams
Medium

2292

138

Favorite

Share
Given an array of strings, group anagrams together.

Example:

Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
Note:

All inputs will be in lowercase.
The order of your output does not matter.
"""
class Solution:
    def groupAnagrams(self, strs):
        hash = {}
        for i in strs:
            li = list(i)
            li.sort()
            k = "".join(li)
            if not hash.get(k, None):
                hash[k] = [i]
            else:
                hash[k].append(i)
        return hash.values()
