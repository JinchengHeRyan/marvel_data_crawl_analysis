import networkx as nx
import pandas as pd


class GraphBuilder:
    def __init__(self, csv_path):
        self.csv_path = csv_path
        self.data = dict()
        self.graph = nx.Graph()

    def read_data(self):
        df = pd.read_csv(self.csv_path)
        for i, info in df.iterrows():
            eventID = info["eventID"]
            characterID = info["characterID"]
            if eventID in self.data.keys():
                self.data[eventID].append(characterID)
            else:
                self.data[eventID] = list()

    def build_connection(self, node_list: list):
        for i in range(len(node_list) - 1):
            for j in range(i, len(node_list)):
                if (node_list[i], node_list[j]) in self.graph.edges:
                    self.graph[node_list[i]][node_list[j]]["weight"] += 1
                else:
                    self.graph.add_edge(node_list[i], node_list[j], weight=1)

    def get_graph(self) -> nx.Graph:
        self.read_data()
        for eventID in self.data.keys():
            characters = self.data[eventID]
            self.build_connection(node_list=characters)
        return self.graph
