from collections import defaultdict

def has_cycle(g):
    try:
        nx.find_cycle(g)
    except nx.NetworkXNoCycle:
        return False
    return True

def get_path_from_edges(edges,closed_tour=False):
    path_graph = nx.Graph(edges)
    # if it is an open tour start from a node with a single degree
    curr = min(path_graph.nodes,key=path_graph.degree)
    path,visited = [curr],{curr}
    while len(path)<len(path_graph):
        curr = (set(path_graph.neighbors(curr))-visited).pop()
        visited.add(curr)
        path.append(curr)
    if closed_tour:
        path.append(path[0])
    return path

def shortest_edge_initialization(g, closed_tour = False):
    edge_list = set(g.edges)
    times_visited  = defaultdict(int)
    tour = set()
    max_tour_len = len(g) if closed_tour else len(g)-1
    key = nx.get_edge_attributes(g,"weight").get
    while len(tour)<max_tour_len:
        u,v = min(edge_list, key=key)
        times_visited[u]+=1
        times_visited[v]+=1
        tour.add((u,v))

        # removing edges that not satisfying the conditions
        edge_list.remove((u,v))

        for u,v in set(edge_list):
            if (
                # closed loop condition
                (has_cycle(nx.Graph(tour|{(u,v)})) and len(tour) != len(g)-1)
                # not more than two edges condition
                or times_visited[u] ==2 or times_visited[v] ==2

            ):
                edge_list.remove((u,v))

    return get_path_from_edges(tour,closed_tour=closed_tour)

np.random.seed(1)
print(shortest_edge_initialization(g))
print(shortest_edge_initialization(g, closed_tour=True))
