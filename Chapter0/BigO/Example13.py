def fib(n):
  if n<=0:
    return 0
  elif n==1:
    return 1
  return fib(n-1)+fib(n-2)

print(fib(8))

"""
Example 13
The following code computes the Nth Fibonacci number.
1 int fib(int n) {
2 if (n <= 0) return 0;
3 else if (n == 1) return 1;
4 return fib(n - 1) + fib(n - 2);
5}
We can use the earlier pattern we'd established for recursive calls: 0(branchesa ? i l t h ). There are 2 branches per call, and we go as deep as N, therefore the runtime isO(2N).
I
SI
Through some very complicated math, we can actually get a tighter runtime. The time is indeed exponential, but it's actually closer to 0 ( 1 . 6 " ) . The reason that it's not exactly 0 ( 2 N ) is that, at the bottom of the call stack, there is sometimes only one call. It turns out that a lot of the nodes are at the bottom (as is true in most trees), so this single versus double call actually makes a big difference. Saying 0 ( 2 " ) would suffice for the scope of an interview, though (and is still techni- cally correct, if you read the note about big theta on page 39). You might get "bonus points" if you can recognize that it'll actually be less than that.
Cracking the Coding Interview, 6th Edition

VII Big 0
Generally speaking, when you see an algorithm with multiple recursive calls, you're looking at exponential runtime.
"""