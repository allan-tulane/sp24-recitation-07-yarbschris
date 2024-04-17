from collections import defaultdict

def make_undirected_graph(edge_list):
    """ Makes an undirected graph from a list of edge tuples. """
    graph = defaultdict(set)
    for e in edge_list:
        graph[e[0]].add(e[1])
        graph[e[1]].add(e[0])
    return graph


def reachable(graph, start_node):
    """
    Returns:
      the set of nodes reachable from start_node
    """
    result = set([start_node])
    frontier = set([start_node])
    while len(frontier) != 0:
        while len(frontier) != 0:
            currentNode = frontier.pop()  # remove and get an element from the frontier
            for neighbor in graph[currentNode]:
                if neighbor not in result:
                    frontier.add(neighbor)
                    result.add(neighbor)
    return result





def connected(graph):
    result = False
    if not graph:
        return True
    if len(reachable(graph, next(iter(graph)))) == len(graph):
        result = True
    return result




def n_components(graph):
    """
    Returns:
      the number of connected components in an undirected graph
    """
    visited = set()
    connectionCount = 0

    for node in graph:
        if node in visited:
            continue
        else:
            reachableNodes = reachable(graph, node)
            visited.update(reachableNodes)
            connectionCount += 1
    return connectionCount



