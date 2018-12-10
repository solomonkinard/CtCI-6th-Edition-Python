def factorial(n):
  if n<0:
    return -1
  elif n==0:
    return 1
  else:
    return n*factorial(n-1)

print(factorial(5))

"""
Example 11
The following code computes n! (n factorial). What is its time complexity?
1
int factorial(int n) {
8} 9>
This isjust a straight recursion from n ton-1 to n-2down to 1. It wilt take 0(n) time.
"""