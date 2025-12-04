from collections import deque, defaultdict

def topological_sort(graph):
    in_degree = {node: 0 for node in graph}
    for node in graph:
        for neighbor in graph[node]:
            in_degree[neighbor] += 1

    queue = deque([node for node in graph if in_degree[node] == 0])

    topo_order = []

    while queue:
        node = queue.popleft()
        topo_order.append(node)

        for neighbor in graph[node]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)


    if len(topo_order) != len(graph):
        raise ValueError("Graph is not a DAG – it contains a cycle")

    return topo_order


if __name__ == "__main__":
    graph = {
        "IP":   ["DS"],        # Intro to Programming -> Data Structures
        "DM":   ["ALG"],       # Discrete Math -> Algorithms
        "DS":   ["ALG", "DB"], # Data Structures -> Algorithms, Databases
        "ALG":  ["ML", "COMP"],# Algorithms -> ML, Compilers
        "CA":   ["OS", "COMP"],# Comp. Architecture -> OS, Compilers
        "OS":   ["NET"],       # OS -> Networks
        "DB":   ["ML"],        # Databases -> ML
        "NET":  [],            # Networks -> no outgoing deps
        "COMP": [],            # Compilers -> no outgoing deps
        "ML":   []             # Machine Learning -> no outgoing deps
    }

    order = topological_sort(graph)
    print("One valid course order:", order)

    """
        Time Complexity:
            O(V + E)
        Space Complexity:
            O(V + E) 
        """
