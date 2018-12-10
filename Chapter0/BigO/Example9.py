def asum(node):
  if not node:
    return 0
  return asum(node.left) + node.value + asum(node.right)

class Node:
  def __init__(self, value):
    self.value = value
    self.left = self.right = None

node = Node(2)
node.left = Node(3)
node.right = Node(4)
print(asum(node))

"""
Example 9
The following simple code sums the values of all the nodes in a balanced binary search tree. What is its runtime?
return a;
Just because it's a binary search tree doesn't mean that there is a log in it! We can look at this two ways.
int sum(Node node) { if (node == nUll) {
1
2
3
4}
5 return sum(node.left) + node.value + sum(node.right); 6}
CrackingTheCodinglnterview.com 16th Edition 49
VII BigO
   VII BigO
What It Means
The most straightforward way is to think about what this means. This code touches each node in the tree once and does a constant time amount of work with each "touch" (excluding the recursive calls).
Therefore, the runtime will be linear in terms of the number of nodes. If there are N nodes, then the runtime isO(N) .
Recursive Pattern
On page 44, we discussed a pattern for the runtime of recursive functions that have multiple branches. Let's try that approach here.
We said that the runtime of a recursive function with multiple branches is typically O(branchesdePth). There are two branches at each call, so we're looking at 0 (2dePth ) .
At this point many people might assume that something went wrong since we have an exponential algo- rithm-that something in our logic is flawed or that we've inadvertently created an exponential time algo- rithm (yikes!).
The second statement is correct. We do have an exponential time algorithm, but it's not as bad as one might think. Consider what variable it's exponential with respect to.
What is depth? The tree is a balanced binary search tree. Therefore, if there are N total nodes, then depth isroughlylog N.
Bytheequationabove,weget0(210g N).
Recall what log2 means:
2P =Q->log2Q=P
What is 210g N? There is a relationship between 2 and log, so we should be able to simplify this.
Let P = 210g N. By the definition of log2' we can write this as lo g l = log2N.This means that P N.
Let P =210g N
- > l o g l = l o g 2N
-> P =N _> 210g N = N
Therefore, the runtime of this code is O( N), where N is the number of nodes.
"""