import json
import itertools
import networkx as nx
import matplotlib.pyplot as plt
from pprint import pprint


keywords = ['attack', 'authority', 'bnp', 'buddhist', 'celebration', 'christian', 'eid', 'ethnic', 'hindu', 'holidays', 'jamaat', 'league', 'minority', 'muslim', 'nationalist', 'opposition', 'pakistan', 'police', 'puja', 'rape', 'shibir', 'vandalism']


def complete_graph_from_list(L, create_using=None):
    G = nx.empty_graph(len(L), create_using)
    edges = itertools.combinations(L, 2)
    G.add_edges_from(edges)
    return G.edges()


# def flattenjson(b, delim):
#     val = {}
#     for i in b.keys():
#         if isinstance(b[i], dict):
#             get = flattenjson(b[i], delim)
#             for j in get.keys():
#                 val[i + delim + j] = get[j]
#         else:
#             val[i] = b[i]

#     return val


all_combos = complete_graph_from_list(keywords)
all_combos_dict = {}
for i in all_combos:
    all_combos_dict[i] = 0


with open("./Scraped data/news_db.json") as infile:
    for row in infile:
        all_data = json.loads(row)
        news_text = all_data['content']
        # print(news_text)
        for i in all_combos_dict.keys():
            if i[0] in news_text and i[1] in news_text:
                all_combos_dict[i] += 1


pprint(all_combos_dict)
# G = nx.Graph()

# for key, value in all_combos_dict.items():
#     G.add_edge(key[0], key[1], weight=value)

# edges = G.edges()
# weights = [G[u][v]['weight'] for u, v in edges]
# # min_max_scalar = preprocessing.MinMaxScaler()
# labels = G.nodes()

# nx.draw(G, pos=None, hold=None, edges=edges, width=weights, with_labels=True)
# plt.show()
