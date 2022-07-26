'''
509. Fibonacci Number

Easy

4600

281

Add to List

Share
The Fibonacci numbers, commonly denoted F(n) form a sequence, called the Fibonacci sequence, such that each number is the sum of the two preceding ones, starting from 0 and 1. That is,

F(0) = 0, F(1) = 1
F(n) = F(n - 1) + F(n - 2), for n > 1.
Given n, calculate F(n).

 

Example 1:

Input: n = 2
Output: 1
Explanation: F(2) = F(1) + F(0) = 1 + 0 = 1.
Example 2:

Input: n = 3
Output: 2
Explanation: F(3) = F(2) + F(1) = 1 + 1 = 2.
Example 3:

Input: n = 4
Output: 3
Explanation: F(4) = F(3) + F(2) = 2 + 1 = 3.
 

Constraints:

0 <= n <= 30
'''
class Solution:
    def fib(self, n: int) -> int:
        count = 1
        print(n)
        
        def fib(num1, num2, count, n):
            if n == 0:
                return 0
            if n == 1:
                return 1
            num_1 = num2
            num_2 = num1 + num2
            count +=1
            print(count)
            if count == n:
                print('equalled count')
                print(num_2)
                return int(num_2)
            else:
                print('another iteration')
                return fib(num_1, num_2, count, n)

        return fib(0, 1, count, n)



'''
Success
Details 
Runtime: 42 ms, faster than 73.86% of Python3 online submissions for Fibonacci Number.
Memory Usage: 14 MB, less than 9.48% of Python3 online submissions for Fibonacci Number.
'''