from graphBuilder.graph_build import GraphBuilder

csv_path = "./data/events/CSV/events_characters/event2characters.csv"

graph_builder = GraphBuilder(csv_path=csv_path)


if __name__ == "__main__":
    graph_builder.centralityRank_to_csv(
        characters_combined_json_path="./data/characters/JSON/combined/combined.json",
        output_path="./data/characters/centrality/",
        centrality_types=["closeness_centrality", "betweenness_centrality"],
    )
