## algo/hacking-part-2 
#### Author: Agent Harrison
#### 25 solves / 484 points

Eljimike is back at it again with his weird hacking contests. Can you help him this time?

nc hacking-pt2.hsctf.com 1337


Flag: flag{eLjMiKe_Is_PrOuD_oF_yOu}


Once again, we are diving into graph theory. This time we can model the problem with a connected undirected graph and the conditions set by Eljmike translate into finding what is called the minimum spanning tree. This is basically the graph with the minimum total weight that has no cycles and is fully connected. While there are many famous algorithms to find the MST, I will describe how one can derive the result themselves. To begin, note that to satisfy the connected requirement we must have atleast V-1 edges connected the V nodes. From here we might wonder if a greedy algorithm works. we could start with a graph with no edges and for V-1 iterations we could try to add the minimum weighted connection. The only concern here is the no cycle part and making sure we stay connected. Here comes the second insight: if there are no cycles in a graph with V-1 edges and V nodes, it must be connected. You can try to reason this out if you are unsure by drawing some examples. Thus, only one modification is needed: every time we try to add an edge we must check that no cycles form. This is the algorithm used in the solution! The only tweak here is that the step of making sure no cycles form is done in O(log n) time by using a data structure called a Disjoint Set Union (DSU). You can search this up to learn more about how it works! An implementation of this solution is once again in the grader. 

As a sidenote, for the negative one people reading this and wondering how the graph is generated, the algorithm used to generate the graph starts with a Prüfer sequence and uses it to generate a connected graph. From there random nodes are inserted. For more details search these terms up and see the grader for the implementation! 