def reverse(arr):
  for i in range(len(arr)//2):
    other = len(arr)-i-1
    arr[i], arr[other] = arr[other], arr[i]
    return arr

print(reverse([2,3,4]))

"""
Example 6
The following code reverses an array. What is its runtime? 1 void reverse(int[] array) {

This algorithm runs in 0 ( N ) time. The fact that it only goes through half of the array (in terms of iterations) does not impact the big O time.
"""