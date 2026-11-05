def order_crossover(p1,p2):
    start = np.random.randint(0,len(p1)-1)
    end = np.random.randint(start+1,len(p1) if start !=0 else len(p1)-1)
    def fill_blanks(p1,p2,s,e):

        unvisited_nodes = p2.copy()
        for node in p1[s:e]:
            unvisited_nodes.remove(node)

        c = p1.copy()
        for i in range(len(p1)):
            if i<s or i>=e:
                c[i] = unvisited_nodes.pop(0)
        return c

    c1 = fill_blanks(p1,p2,start,end)
    c2 = fill_blanks(p2,p1,start,end)
    return c1,c2

np.random.seed(2)
n_population = 8
population = [shortest_edge_initialization(g, closed_tour=False) for _ in range(n_population)]
selected_population =  roulette_wheel_selection(inv_path_length,population)
parents = selected_population[:2]
print(parents)
print(order_crossover(*parents))
