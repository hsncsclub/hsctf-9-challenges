## algo/hacking 
#### Author: Agent Harrison
#### 37 solves / 475 points

Help Eljmike organize his hacking contest! nc hacking.hsctf.com 1337

Flag: flag{cOnGrAtS_yOu_ArE_nOw_A_hAcKeR}


The way each participant chooses another hacker to hack can be modelled via a directed graph. From here, the conditions to lose/be eliminated are equivalent to having cycles in the graph. Thus, the problem translates to counting the number of nodes in a cycle with the added condition that each node only reaches out to one other node. By running a dfs from each node, we can easily find these cycles by checking if we revisit a node and then rerun the dfs to find out the length of the cycle. In doing so, we have developed an O(n) algo that satisfies the time constraints. The grader implements this idea to check each response as well. 