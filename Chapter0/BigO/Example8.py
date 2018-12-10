"""
Example 8
Suppose we had an algorithm that took in an array of strings, sorted each string, and then sorted the full array. What would the runtime be?
Many candidates will reason the following: sorting each string is 0(N log N) and we have to do this for each string, so that's 0(N*N l o g N). We also have to sort this array, so that's an additional 0(W l o g M) work.Therefore, the total runtime is 0(N2 log N + N log N), which isjust 0(N; log N).
This is completely incorrect. Did you catch the error?
The problem is that we used N in two different ways. In one case, it's the length ofthe string (which string?). And in another case, it's the length of the array.
In your interviews, you can prevent this error by either not using the variable "N"at all, or by only using it when there is no ambiguity as to what N could represent.
In fact, I wouldn't even use a and b here, or m and n. It's too easy to forget which is which and mix them up. An 0 ( a : ) runtime is completely different from an 0 ( a * b ) runtime.
Let's define new terms—and use names that are logical.
• Let S be the length of the longest string.
• Let a be the length of the array. Now we can work through this in parts:
• Sorting each string isO(s l o g s),
• We have to do this for every string (and there are a strings), so that's 0( a*s
log s).
• Now we have to sort all the strings. There a re a strings, so you'll may be inclined to say that this takes 0( a
l o g a) time. This is what most candidates would say. You should also take into account that you need to compare the strings. Each string comparison takes 0 ( s ) time.There are 0 ( a l o g a) comparisons, therefore this will takeO(a*s log a)time.
If you add up these two parts, you get 0(a*s( log a + log s)). This is it. There is no way to reduce it further.
Example?
The following simple code sums the values of all the nodes in a balanced binary search tree. What is its runtime?
1
2
3
4}
5 return sum(node,left) + node.value + sum(node.right); 6>
lust because it's a binary search tree doesn't mean that there is a log in it! We can look at this two ways.
CrackingTheCodinglnterview.com j 6th Edition 47
int sum(Node node) { if (node == null) {
return 0;
VI j Big 0

VI I Big O
What It Means
The most straightforward way is to think about what this means. This code touches each node in the tree once and does a constant time amount of work with each "touch" (excluding the recursive calls).
Therefore, the runtime will be linear in terms of the number of nodes. If there are N nodes, then the runtime isO(N).
Recursive Pattern
On page 44, we discussed a pattern for the runtime of recursive functions that have multiple branches.
Let's try that approach here.
We said that the runtime of a recursive function with multiple branches is typically (^branches'3*1101). There are two branches at each call, so we're looking at 0 (2dc*rth).
At this point many people might assume that something went wrong since we have an exponential algo- rithm—that something in our logic is flawed or that we've inadvertently created an exponential time algo- rithm (yikesl).
The second statement is correct. We do have an exponential time algorithm, but it's not as bad as one might think. Consider what variable it's exponential with respect to.
What is depth?The tree is a balanced binary search tree. Therefore, if there are N total nodes, then depth is roughly l o g N.
By the equation above, we get 0 (2l c | N).
Recall what l o g 2 means:
2" = Q ~> logjQ = P
What is 2lag N? There is a relationship between 2 and log, so we should be able to simplify this.
LetP = 2lt>e N. By the definition of logj, we can write this as logjP = log; It This means that P = N.
Let P = 2loeN
-> log: P = log^N
-> P = N
-> 2loe N = N
Therefore, the runtime of this code is 0 ( N ) , where N is the number of nodes.
"""