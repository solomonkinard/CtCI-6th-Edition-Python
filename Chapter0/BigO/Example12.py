def permutation(s):
  def permutation(s, p):
    if len(s)==0:
      print(p)
    else:
      for i in range(len(s)):
        rem = s[0:i]+s[i+1:]
        permutation(rem, p+s[i])
  permutation(s, '')

permutation('abcdefghi')

"""
Example 12
This code counts all permutations of a string.
1 void permutation(String str) {
2
3> 4
5
6
7
8
9
IS
11
12 > 13 >
14 >
This is a (very!) tricky one. We can think about this by looking at how many times permutation gets called and how long each call takes. We'll aim for getting as tight of an upper bound as possible.
CrackingTheCodinglnterview.com | 6th Edition 51
permutation(str, '"');
void permutation(String str, String prefix) { if (str.lengthQ == 0) {
System.out.println(prefix); > else {
for (int i = 0; i < str.lengthQ; i++) {
String rem = str.substring(0, i) + str.substring(i + 1); perrriut3tion(rem, prefix + str.charAt(i));
VII Big 0

VI I Big O
How many times does permutation get called in its base case?
If we were to generate a permutation, then we woutd need to pick characters for each "slot," Suppose we had 7 characters in the string. In the first slot, we have 7 choices. Once we pick the letter there, we have 6 choices for the next slot, (Note that this is 6 choices for each of the 7 choices earlier.) Then 5 choices for the next slot,and soon.
Therefore, the total number of options is 7 * 6 * 5 * 4 * 3 * 2 * 1, which is also expressed as 7! (7 factorial).
This tells us that there are n! permutations. Therefore, p e r m u t a t i o n is called n I times in its base case (when p r e f i x is the full permutation).
How many times does permutation get called before its base case?
But, of course, we also need to consider how many times lines 9 through 12 are hit. Picture a large call tree representing all the calls. There are n I leaves, as shown above. Each leaf is attached to a path of length n. Therefore, we know there will be no more than n * n! nodes {function calls) in this tree.
How long does each function call take?
Executing line 7 takes 0 ( n ) time since each character needs to be printed.
Line 10 and line 11 will also take 0 ( n ) time combined, due to the string concatenation. Observe that the sum of the lengths of rem, prefix, and str. charAt( i) will always be n.
Each node in our call tree therefore corresponds to 0 ( n ) work.
What is the total runtime?
Since we are calling permutation 0( n * n!) times (as an upper bound), and each one takes 0(n) time, the totai runtime will not exceed 0(nJ * n ! ).
Through more complex mathematics, we can derive a tighter runtime equation (though not necessarily a nice closed-form expression). This would almost certainly be beyond the scope of any normal interview.
"""