import networkx as nx
import pandas as pd
import json
import os


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

    def centralityRank_to_csv(
        self, characters_combined_json_path: str, output_path: str
    ):
        json_file = open(characters_combined_json_path, "r")
        data = json.load(json_file)
        characters_dict = dict()
        for i in range(len(data["results"])):
            id = data["results"][i]["id"]
            name = data["results"][i]["name"]
            characters_dict[id] = name

        self.get_graph()
        centrality = nx.betweenness_centrality(self.graph)
        centrality = sorted(centrality.items(), key=lambda x: x[1], reverse=True)

        os.makedirs(output_path, exist_ok=True)
        csv_path = os.path.join(output_path, "centrality_rank.csv")
        csv_file = open(csv_path, "w")
        csv_file.write("id,name,score\n")
        for item in centrality:
            id = int(item[0])
            score = item[1]
            name = characters_dict[id]
            csv_file.write("{},{},{}\n".format(str(id), name, str(score)))