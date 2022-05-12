import networkx as nx
import pandas as pd
import json
import os
from typing import List


class GraphBuilder:
    def __init__(self, csv_path, characters_combined_json_path):
        """
        Build the network graph of all the characters
        :param csv_path: csv file contains event ID and characters ID
        :param characters_combined_json_path: json file contains all characters ID
        """
        self.csv_path = csv_path
        self.characters_combined_json_path = characters_combined_json_path
        self.data = dict()
        self.characters_dict = dict()
        self.graph = nx.Graph()
        self.read_data()
        self.read_json()
        self.build_graph()

    def read_data(self):
        df = pd.read_csv(self.csv_path)
        for i, info in df.iterrows():
            eventID = info["eventID"]
            characterID = info["characterID"]
            if eventID in self.data.keys():
                self.data[eventID].append(characterID)
            else:
                self.data[eventID] = list()

    def read_json(self):
        json_file = open(self.characters_combined_json_path, "r")
        data = json.load(json_file)
        for i in range(len(data["results"])):
            id = data["results"][i]["id"]
            name = data["results"][i]["name"]
            self.characters_dict[id] = name

    def build_connection(self, node_list: list):
        for i in range(len(node_list) - 1):
            for j in range(i, len(node_list)):
                if (node_list[i], node_list[j]) in self.graph.edges:
                    self.graph[node_list[i]][node_list[j]]["weight"] += 1
                else:
                    self.graph.add_edge(node_list[i], node_list[j], weight=1)

    def build_graph(self):
        for eventID in self.data.keys():
            characters = self.data[eventID]
            self.build_connection(node_list=characters)

    def get_graph(self) -> nx.Graph:
        return self.graph

    def get_characters_dict(self) -> dict:
        return self.characters_dict

    def centralityRank_to_csv(
        self,
        centrality_types: List[str],
        output_path: str,
    ):
        for cent_type in centrality_types:
            centrality = getattr(nx, cent_type)(self.graph)
            centrality = sorted(centrality.items(), key=lambda x: x[1], reverse=True)

            os.makedirs(output_path, exist_ok=True)
            csv_path = os.path.join(output_path, "{}.csv".format(cent_type))
            csv_file = open(csv_path, "w")
            csv_file.write("id,name,score\n")
            for item in centrality:
                id = int(item[0])
                score = item[1]
                name = self.characters_dict[id]
                csv_file.write("{},{},{}\n".format(str(id), name, str(score)))
