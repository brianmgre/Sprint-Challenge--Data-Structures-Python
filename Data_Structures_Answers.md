Add your answers to the questions below.

1. What is the runtime complexity of your `depth_first_for_each` method?

O(n) where n is number of nodes. The time complexity depend directly on long it takes to vist each node. If our tree has 5 nodes it would take O(5)

2. What is the space complexity of your `depth_first_for_each` function?

O(n), the same as the runtime complexity. The worst case is that n is the max dept of the tree. For my iterative solution it is the same O(n), because worst all nodes would be entered into the stack.

3. What is the runtime complexity of your `breadth_first_for_each` method?

O(n), n is the number of nodes. The number of nodes dictates n. The same as depth-first-search(dfs)

4. What is the space complexity of your `breadth_first_for_each` method?

O(n) this is the same as dfs' space complecity. The worst case is all nodes end in the queue. For 10 nodes it would be O(10)

5. What is the runtime complexity of the provided code in `names.py`?

O(n^2) this is because of the two nested for loops. The outer loop only runs n times, but the inner loop runs x times. This results in O(n^2)

6. What is the space complexity of the provided code in `names.py`?

O(n) because the amount of items to loop over are constant

7. What is the runtime complexity of your optimized code in `names.py`?

Both of the for loops are O(n). They are not nested therefore n is the number of names.

8. What is the space complexity of your optimized code in `names.py`?

hashtable is O(n), and so are both for loops. So my optimized code is O(n)
