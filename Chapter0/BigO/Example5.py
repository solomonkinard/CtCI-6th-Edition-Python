def print_unordered_pairs(arr_a, arr_b):
  for i in range(len(arr_a)):
    for j in range(len(arr_b)):
      for k in range(10**5):
        print(arr_a[i], arr_b[j])

print_unordered_pairs([2,3,4], [5,6,7])

"""
ExampleS
What about this strange bit of code?
1
For each element of arrayA, the inner for loop goes through b iterations, where b Ifa = arrayA.length,thentheruntimeisO(ab).
void printUnorderedPairs(int[] arrayA, int[] arrayB) { for (int i = e; i < arrayA.length; i++) {
for (int j = e; j < arrayB.length; j++) { for (int k =e; k <1eeeee; k++) {
System.out.println(arrayA[i] + ",. + arrayB[j]);
Nothing has really changed here. 100,000 units of work is still constant, so the runtime is O( ab) .
"""