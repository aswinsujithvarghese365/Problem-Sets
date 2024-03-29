/* Problem
The National Championships are starting soon. There are 4 race categories, numbered from 1 to 4, 
that Chef is interested in. Chef is participating in exactly 2 of these categories.

Chef has an arch-rival who is, unfortunately, the only person participating who is better than Chef, 
i.e, Chef can't defeat the arch-rival in any of the four race categories but can defeat anyone else. 
Chef's arch-rival is also participating in exactly 2 of the four categories. Chef hopes to not fall 
into the same categories as that of the arch-rival.

Given X,Y,A,B where X,Y are the races that Chef participates in, and A,B are the races that Chef's 
arch-rival participates in, find the maximum number of gold medals (first place) that Chef can win.

Input Format
The first line of input contains an integer T, denoting the number of testcases. The description of 
T testcases follows.
Each testcase consists of a single line containing four space-separated integers — the values of 
X,Y,A, and B respectively.

Output Format
For each testcase, print a single line containing one integer — the maximum number of gold medals that Chef can win. */

#include <iostream>
using namespace std;

int main() {
	int n;
	int X, Y, A, B;
	int medals = 0;
	cin>>n;
	for(int i = 0; i < n; i++){
	    cin>>X>>Y>>A>>B;
	    if(X!=A && X!=B){
	        medals++;
	    }
	    if(Y!=A && Y!=B){
	        medals++;
	    }
	    cout<<medals<<"\n";
	    medals = 0;
	}
	return 0;
}
