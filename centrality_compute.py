import networkx as nx
from graphBuilder.graph_build import GraphBuilder

csv_path = "./data/events/CSV/events_characters/event2characters.csv"

graph_builder = GraphBuilder(csv_path=csv_path)


if __name__ == "__main__":
    graph = graph_builder.get_graph()
    centrality = nx.betweenness_centrality(graph)

    centrality = sorted(centrality.items(), key=lambda x: x[1], reverse=True)
    print(centrality)
