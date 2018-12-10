def powersOf2(n):
  if n<1:
    return 0
  elif n==1:
    print(1)
    return 1
  else:
    prev = powersOf2(n//2)
    curr = prev*2
    print(curr)
    return curr

powersOf2(8)

"""
Example 16
The following function prints the powers of 2 from 1 through n (inclusive). For example, if n is 4, it would print 1,2, and 4, What is its runtime?
1 int powers0f2(int n) {
2
3 4 5 6 7 8 9 10 11
if (n < 1) { return 0;
} else if (n == 1) { System.out,println(l)j return lj
} else {
int prev = powers0f2(n / 2); int curr = prev * 2; System,out,println(curr); return currj
12 >} 13
There are several ways we couid compute this runtime.
What It Does
Let's walkthrough a call like powersOf2(50),
powersOf2(50)
-> powersOf2(25)
"""