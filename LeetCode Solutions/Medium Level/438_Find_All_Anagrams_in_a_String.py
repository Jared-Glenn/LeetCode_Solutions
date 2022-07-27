'''
438. Find All Anagrams in a String

Medium

8099

265

Add to List

Share
Given two strings s and p, return an array of all the start indices of p's anagrams in s. You may return the answer in any order.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

 

Example 1:

Input: s = "cbaebabacd", p = "abc"
Output: [0,6]
Explanation:
The substring with start index = 0 is "cba", which is an anagram of "abc".
The substring with start index = 6 is "bac", which is an anagram of "abc".
Example 2:

Input: s = "abab", p = "ab"
Output: [0,1,2]
Explanation:
The substring with start index = 0 is "ab", which is an anagram of "ab".
The substring with start index = 1 is "ba", which is an anagram of "ab".
The substring with start index = 2 is "ab", which is an anagram of "ab".
 

Constraints:

1 <= s.length, p.length <= 3 * 104
s and p consist of lowercase English letters.
'''
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        if len(p) > len(s):
            return []
        sCount, pCount = {}, {}
        for i in range(len(p)):
            sCount[s[i]] = 1 + sCount.get(s[i], 0)
            pCount[p[i]] = 1 + pCount.get(p[i], 0)
        
        if sCount == pCount:
            res = [0]
        else:
            res = []
        
        l = 0
        for r in range(len(p), len(s)):
            sCount[s[r]] = 1 + sCount.get(s[r], 0)
            sCount[s[l]] -= 1
                   
            if sCount[s[l]] == 0:
                sCount.pop(s[l])   
            l += 1
            
            if sCount == pCount:
                res.append(l)
        
        return res

        
        #main = list(s)
        #sub = list(p)
        #ana_len = len(sub)
        #upper_range = -1*(ana_len-1)
        #
        #final_list = []
        #
        #if ana_len == 1:
        #    for x, letter in enumerate(main):
        #        if letter in sub:
        #            final_list.append(x)
        #else:
        #    for x, letter in enumerate(main[:upper_range]):
        #        holder = sub.copy()
        #        if letter in holder:
        #            holder.remove(letter)
        #            for y in range(ana_len):
        #                if len(holder) == 0:
        #                    final_list.append(x)
        #                elif main[x+y+1] in holder:
        #                    holder.remove(main[x+y+1])
        #                else:
        #                    break
        #
        #final_list.sort()
        #
        #return final_list
'''
Success
Details 
Runtime: 194 ms, faster than 57.95% of Python3 online submissions for Find All Anagrams in a String.
Memory Usage: 15.2 MB, less than 33.28% of Python3 online submissions for Find All Anagrams in a String.
'''