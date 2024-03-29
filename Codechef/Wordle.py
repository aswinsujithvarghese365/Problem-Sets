"""Problem
Chef invented a modified wordle. There is a hidden word S and a guess word T, both of length 5.
Chef defines a string M to determine the correctness of the guess word. For the i-th index:
If the guess at the i-th index is correct, the i-th character of M is G.
If the guess at the i-th index is wrong, the i-th character of M is B.
Given the hidden word S and guess T, determine string M.

Input Format
First line will contain T, number of test cases. Then the test cases follow.
Each test case contains of two lines of input.
First line contains the string S - the hidden word.
Second line contains the string T - the guess word.

Output Format
For each test case, print the value of string M.

You may print each character of the string in uppercase or lowercase (for example, the strings 
BgBgB, BGBGB, bgbGB and bgbgb will all be treated as identical)."""

# cook your dish here
T=int(input())
for i in range(T):
    l1=str(input())
    l2=str(input()) 
    for j in range(len(l1)):
        if(l1[j]==l2[j]):
            print("G",end="")
        else:
            print("B",end="")
    print("\n")
