def print_pairs(arr):
  for i in arr:
    for j in arr:
      print(i, j)

print_pairs([2,3,4])

"""
Example 2
What is the runtime of this code?

The inner for loop hasO(N) iterations and it is called N times. Therefore, the runtime isO(N2)-
Another way we can see this is by inspecting what the "meaning" of the code is. It is printing all pairs (two- element sequences). There are 0(N3) pairs; therefore, the runtime isO(NJ).
"""