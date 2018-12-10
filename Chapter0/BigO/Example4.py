def print_unordered_pairs(arr_a, arr_b):
  for i in range(len(arr_a)):
    for j in range(len(arr_b)):
      if arr_a[i] < arr_b[j]:
        print(arr_a[i], arr_b[j])

print_unordered_pairs([2,3,4], [5,6,7])

"""
Example 4
This is similar to the above, but now we have two different arrays.

We can break up this analysis. The if-statement within j's for loop is 0 ( 1 ) time since it's just a sequence of constant-time statements.
We now have this:
1 void printUnorderedPairs(int[] arrayA, int[] arrayB) {
CrackingTheCodinglnterview.com j 6th Edition 47
VIjBig0

VII BigO
2
3
4 5} 6} 1>
2 3 4
for (int i = 0j i < arrayA.length; i++) { for (int j = 0; j < arrayB.length; j++) {
for (int k = 0; k < 160800; k++) { System.out.println(arrayA[i] + "," + arrayB[j]);
for (int i = 0; i < arrayA.length; i++) { for (int j = 0; j < arrayB.length; j++) {
/* 0(1) work */
For each element of arrayA, the inner for loop goes through b iterations, where b = tfa = arrayA. length, then the runtime isO(ab),
arrayB. length,
Ifyou said 0(NJ)-then remember your mistake for the future. It's not 0(NJ) because there are two different inputs. Both matter. This is an extremely common mistake.
Examples
What about this strange bit of code?
1 void printUnorderedPairs(int[] arrayAj intjj arrays) {
6} 7> 3} 9}
Nothing has really changed here. 100,000 units of work is still constant, so the runtime is 0 ( a b ) .
"""