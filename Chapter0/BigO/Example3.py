def print_unordered_pairs(arr):
  n = len(arr)
  for i in range(n):
    for j in range(i+1, n):
      print(arr[i], arr[j])

print_unordered_pairs([2,3,4,5,6])

"""
Example 3
This is very similar code to the above example, but now the inner for loop starts at i

We can derive the runtime several ways.

Counting the Iterations
The first time through j runs for N -1 steps. The second time, it's N- 2 steps.Then N-3 steps. And so on. Therefore, the number of steps total is:
(N-l) + (N-2) + (N-3) + ... + 2 + 1
26 Cracking the Coding Interview, 6th Edition
This pattern of for loop is very common. It's important that you know the runtime and that you deeply understand it. You can't rely on just memorizing common runtimes. Deep comprehen- sion is important.
» 1 + 2 + 3 + ...+ H-l = sum of 1 through N-l
The sum ofl throughN-lis (see "Sum of Integers 1 through N" on page 630), so the runtime will be 0(NJ).

What lt Means
Alternatively, we can figure out the runtime by thinking about what the code "means." It iterates through each pair of values for { i , j) where j is bigger than i.
There are N1 total pairs. Roughly half of those wil! have i < j and the remaining half will have i > code goes through roughly w/2 pairs so it does Off^) work.
Visualizing What It Does

The code iterates through the following ( i , j)pairswhenN = 8:
j.This
{0, 1) (0, 2) (0, 3) (0, 4) (0j 5) <0, 6) {0, 7) (1, 2) (1, 3) (1, 4) (1, 5) {1, 6) (1, 7) (2j3)(2,4)(2j5)(2j6) (2, 7) (3j 4) (3j S) (3, 6) (3, 7) (4, 5) <4, 6) (4, 7) (5, 6) (5j 7) (6, 7)
This looks like half of an NxN matrix, which has size (roughly)
Average Work
Therefore, it takes 0(N2) time.
We know that the outer loop runs N times. How much work does the inner loop do? It varies across itera- tions, but we can think about the average iteration.
What is the average value of lj 2, 3, 4, 5, 6, 7, 8, 10? The average value will be in the middle, so it will be roughly 5. (We could give a more precise answer, of course, but we don't need to for big 0.)
What about for 1, 2, 3, . N?Theaverage value in this sequence is N/2.
Therefore, since the inner loop does Yi work on average and it is run N times, the total work is V i ' which
isO(N;).
"""