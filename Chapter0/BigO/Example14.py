def allFib(n):
  for i in range(n):
    print('{}: {}'.format(i, fib(i)))

def fib(n):
  if n<=0:
    return 0
  elif n==1:
    return 1
  return fib(n-1)+fib(n-2)

allFib(8)

"""
Example 14
The following code prints all Fibonacci numbers from 0 to n.What is its time complexity?
1
2
3 4> 5}
6
7
8
9
10 11 >
7 8 9 10 11 12 13
int fib(int n, int[] memo) {
if (n <= 0) return 0;
else if (n == 1) return 1;
else if (memo[n] > 0) return memo[n];
memo[n] = fib(n - 1, memo) + fib(n - 2, memo);
CrackingTheCodinglnterview.com | 16th Edition
void allFib(int n) {
for (int i = 8; i < n; i++) {
System.out.printlnfi +
" + fib(l));
else if (n =* 1) return 1; return fib(n - 1) + fib(n - 2);
int fib(int n) {
if (n <= 6) return 0;
Many people will rush to concluding that since f i b ( n ) takes 0 ( 2 " ) time and it's called n times, then it's 0(n2n).
Not so fast. Can you find the error in the logic?
The error is that the n is changing. Yes, f i b ( n ) takes 0(2") time, but it matters what that value of n is.
Instead, let's walk through each call.
1
fib(l) -> 2 steps 2
fib(2) -> 2 steps J
fib(3) -> 2 steps fib(4) -> 2' steps
fib(n) -> 2" steps
Therefore, the total amount of work is:
21 +2J +23 +24 +...+2"
As we showed on page 44, this is 2P*1. Therefore, the runtime to compute the first n Fibonacci numbers (using this terrible algorithm) is still 0 ( 2 n ) .
"""