def allFib(n):
  memo = [0]*(n+1)
  def fib(n):
    if n<=0:
      return 0
    elif n==1:
      return 1
    elif memo[n]>0:
      return memo[n]
    memo[n] = fib(n-1)+fib(n-2)
    return memo[n]
  for i in range(n):
    print('{}: {}'.format(i, fib(i)))

allFib(9)

"""
Example 15
The following code prints all Fibonacci numbers from 0 to n. However, this time, it stores (i.e., caches) previ- ously computed values in an Integer array. If it has already been computed. It just returns the cache. What is its runtime?
1 void allFib(int n) {
2
3
4 5> 6}
int[] memo = new int[n + 1]; for (int i * 0; i < n; 1++) {
System.out.println(i +
" + fib(ij memo));
51

VI I BigO
14 return memo[n];
15 }
Let's walk through what this algorithm does. fib(l) -> return 1
fib<2)
fib(l) -> return 1 fib(0) -> return 0 store 1 at memo[2]
fib(3)
fib(2) -> lookup memo[2] -> return 1 flb(l) -> return 1
store 2 at rrtemo[3]
fib(4)
fib(3) -> lookup memo[3] -> return 2 fib(2) -> lookup mema[2] -> return 1 store 3 at memo[4]
fib(S)
fib(4) -> lookup meroo[4] -> return 3 fib(3) -> lookup me[tto[3] -> return 2 store 5 at memo[S]
At each call to fib(i), we have alreadycomputed and stored the values for fib(i-l) and fib(i-2). We just took up those values, sum them, store the new result, and return. This takes a constant amount of time.
We're doing a constant amount of work N times, so thisisO(n) time.
This technique, called memoization, is a very common one to optimize exponential time recursive algo- rithms.
"""