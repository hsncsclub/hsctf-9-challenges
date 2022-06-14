from random import randint, sample

class DSU: 
    
    def __init__(self, total):
        self.parent = list(range(total))
        self.rank = [1]*total
        
    def find(self, i):
        if self.parent[i] == i: 
            return i
        else: 
            self.parent[i] = self.find(self.parent[i])
            return self.parent[i]
    
    def union(self, i, j, use_rank = True):
        irep, jrep = self.find(i), self.find(j)
        
        if use_rank: 
            if self.rank[irep] == self.rank[jrep]: 
                self.parent[jrep] = irep
                self.rank[irep] += 1

            elif self.rank[jrep] < self.rank[irep]:
                self.parent[jrep] = irep

            else: 
                self.parent[irep] = jrep
        else: 
            self.parent[irep] = jrep

def solve(graph, V):
    graph = sorted(graph, key = lambda edge: edge[2])
    tree = DSU(V)
    result = []
    
    for edge in graph:
        if tree.find(edge[0]) != tree.find(edge[1]): 
            result.append(edge)
            tree.union(edge[0], edge[1])
        if len(result) == V-1:
            break
            
    return sum([edge[2] for edge in result])    

def generate(V, M):

    def hash_edge(e): 
        return e[0]*V+e[1]

    def break_edge(val): 
        return [val//V, val%V]

    connections = []

    p_seq = [randint(0, V-1) for x in range(V-2)]
    degrees = [1]*V

    for node in p_seq: 
        degrees[node] += 1

    for k in p_seq: 
        for m in range(V): 
            if degrees[m] == 1: 
                connections.append([k, m, randint(1, 1000)])
                degrees[k] -=1
                degrees[m] -=1
                break

    left = [i for i in range(V) if degrees[i] != 0]
    connections.append([left[0], left[1], randint(1, 1000)])

    M -= V - 1

    used_edges = set([hash_edge(c) for c in connections])
    left_edges = [i for i in range(1, V**2) if i not in used_edges and i//V != i%V]

    for val in sample(left_edges, M):
        a, b = break_edge(val)
        connections.append([a, b, randint(1, 1000)])

    adj_list = [[] for _ in range(V)]
    for c in connections: 
        adj_list[c[0]].append([c[1]+1, c[2]])
        
    return adj_list, connections

for case, nV in enumerate([10, 50, 100, 200, 250]): 
    show, internal = generate(nV, randint(nV*2, (nV-2)**2))
    sol = solve(internal, nV)
    
    print(f"Test case: {case+1}")
    print(nV)
    for part in show: 
        for a, b in part: 
            print(f"{a},{b} ", end = "")
            
        print()
            
    if int(input("Answer: ")) == sol: 
        print("Congrats, onto the next case: \n")
    else: 
        print("Boohoo Eljmike is disappointed in you ?:(")
        break 
else: 
    print("flag{eLjMiKe_Is_PrOuD_oF_yOu}")