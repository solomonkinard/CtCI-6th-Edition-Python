def is_prime(n):
  for x in range(2, int(n**0.5)+1):
    if n % x == 0:
      return False
  return True

print(['{} {}'.format(x, is_prime(x)) for x in range(90, 100)])

"""
Example 10
The following method checks if a number is prime by checking for divisibility on numbers less than it. It only needs to go up to the square root of n because if n is divisible by a number greater than its square root then it's divisible by something smaller than it.
For example, while 33 is divisible by 11 (which is greater than the square root of 33), the "counterpart" to 11 is 3 (3 * 11 = 33). 33 will have already been eliminated as a prime number by 3.
What is the time complexity of this function?
7 return true;
50 SI Cracking the Coding Interview, 6th Edition


Many people get this question wrong. If you're careful about your logic, it's fairly easy.
The work inside the for loop is constant. Therefore, we just need to know how many iterations the for loop goes through in the worst case.
The for loop will startwhen x = 2 and end when x * x = n.Or, in otherwords, it stops when x = s/n (when x equals the square root of n).
This for loop is really something like this:

if (n < 0) { return -1;
4 5 6
} else if (n == 0) { return 1;
> else {
return n * factorial(n - 1);
for (int x = 2; x <= sqrt(n); x++) { if (n % x == 0) {
return false;
7 return true;

This runs in 0(^n) time.
"""