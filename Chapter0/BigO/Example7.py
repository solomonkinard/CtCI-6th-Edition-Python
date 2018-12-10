"""
Example 7
Which of the following are equivalent to 0(N)? Why? • 0(N + P),where P < M
• 0(2N)
. 0(N+logN)
• 0(N + M)
Let's go through these.
• IfP < then we know that N is the dominant term so we can droptheO(P). • 0(2N) isO(N) since we drop constants.
4 8 Cracking the Coding Interview, 6th Edition
array[other] = temp;

• 0(N) dominates 0( log N), so we can drop the 0( log N).
• There is no established relationship between N and M, so we have to keep both variables in there.
Therefore, all but the last one are equivalent to 0( N),
"""