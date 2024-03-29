"""Problem
Little Egor likes to play with positive integers and their divisors. Bigger the number to play with, 
more the fun! The boy asked you to come up with an algorithm, that could play the following game:

Let's define f(n) as the sum of all odd divisors of n. I.e. f(10) = 1 + 5 = 6 and 
f(21) = 1 + 3 + 7 + 21 = 32. The game is to calculate f(l) + f(l + 1) + ... + f(r - 1) + f(r) 
for the given integers l and r.

Have fun! But be careful, the integers might be quite big.

Input
The first line of the input contains one integer T denoting the number of test cases.
The only line of the test case description contains two positive integers l and r.

Output
For each test case, output the required sum on a separate line."""

# cook your dish here
import math

def f(n):
    result = 0
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            if i % 2 == 1:
                result += i
            if n // i % 2 == 1 and n // i != i:
                result += n // i
    return result

t = int(input())

for _ in range(t):
    l, r = map(int, input().split())
    result = 0
    for i in range(l, r+1):
        result += f(i)
    print(result)
