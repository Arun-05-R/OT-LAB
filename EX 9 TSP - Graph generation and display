import numpy as np
import networkx as nx
import matplotlib.pyplot as plt
from itertools import combinations

def generate_random_weighted_graph(n,low,high):
    g = nx.generators.complete_graph(n)
    # add random weights to the graph
    g.add_weighted_edges_from([(a,b,np.random.randint(low,high)) for a,b in g.edges()])
    # creare layout fro plotting and set pos as attribute
    nx.set_node_attributes(g,nx.spring_layout(g),"pos")
    return g

def plot_graph(g,title="",highlight_edges=[]):
    pos = nx.get_node_attributes(g,"pos")
    plt.figure(figsize=(17,17))
    plt.title(title)
    nx.draw(g,pos=pos,labels = {x:x for x in g.nodes},width=2)
    weights = nx.get_edge_attributes(g,"weight")
    # draw labels for edges
    nx.draw_networkx_edge_labels(g,pos,edge_labels=weights,label_pos=.4);

    # highlight highlighted_edges
    nx.draw_networkx_edges(g,pos,edgelist = highlight_edges,edge_color="r",width=3)
    # highlight labels of highlighted edges
    nx.draw_networkx_edge_labels(
        g,
        pos,
        edge_labels={
            e:w
            for e,w in weights.items()
            if e in map(lambda x:tuple(sorted(x)),highlight_edges)
        },
        font_color="r",
        label_pos=.4
    )
    plt.show()

np.random.seed(3)
g = generate_random_weighted_graph(7,1,20)
plot_graph(g,"Graph for TSP")
