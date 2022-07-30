'''
49. Group Anagrams

Medium

10687

344

Add to List

Share
Given an array of strings strs, group the anagrams together. You can return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

Example 1:

Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
Example 2:

Input: strs = [""]
Output: [[""]]
Example 3:

Input: strs = ["a"]
Output: [["a"]]
 

Constraints:

1 <= strs.length <= 104
0 <= strs[i].length <= 100
strs[i] consists of lowercase English letters.
'''
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        res = defaultdict(list)
        
        for word in strs:
            count = [0] * 26
            
            for letter in word:
                count[ord(letter) - ord("a")] += 1
                
            res[(tuple(count))].append(word)
                 
        return res.values()

'''
Success
Details 
Runtime: 123 ms, faster than 80.24% of Python3 online submissions for Group Anagrams.
Memory Usage: 19.9 MB, less than 9.67% of Python3 online submissions for Group Anagrams.
'''