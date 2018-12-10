def foo(arr):
  total = 0
  product = 1
  for i in arr:
    total += i
  for i in arr:
    product *= i
  print(total, product)

foo([2,3,4])

"""
Example 1
What is the runtime of the this code?

This will takeO(N) time. The fact that we iterate through the array twice doesn't matter.
"""
