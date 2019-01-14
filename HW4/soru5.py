"""


graph = {'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['C', 'E'])}


"""

"""
You are given a set of n variables x1, x2, . . . , xn and a set of m1 equality constraints of the form xi = xj
and a set of m2 inequality constraints of the form xi 6= xj . Is it possible to satisfy all of them? For example,
it is impossible to satisfy the constraints: x1 = x2, x2 = x3, x1 6= x3.
Design an algorithm that takes as input the m1 + m2 constraints and decides whether the constraints
can be satisfied. Prove that your algorithm is correct, and provide an analysis of its running time.
Solution
Let G = (V, E) be the following graph: G has a node corresponding to every variable xi
, and there is an
edge (xi
, xj ) if xi = xj is an equality constraint. We do a Depth First Search of G to find all its connected
components. For each node xi
, if it is in the k-th connected component of G, we assign it a mark k.
Now for each inequality constraint xi 6= xj , we check to see if xi and xj occur in different connected
components of G. If there is some inequality constraint xi 6= xj such that xi and xj occur in the same
connected component of G, then we report that the constraints are unsatisfiable. If there is no such constraint,
then we report satisfiable



"""

graph = {'x1': set(['x2','x3']),
         'x2': set(['x3','x4','x1']),
         'x3': set(['x4','x1','x2']),
         'x4': set(['x4','x3','x2'])}


visited = []

def soru(graph,node):
    global visited
    if node not in visited:
        visited.append(node)
        for n in graph[node]:
            soru(graph,n)

soru(graph,'x1')
print(visited)