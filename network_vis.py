from graphBuilder.graph_build import GraphBuilder
from visualization.network_visualizer import network_visualizer
import chart_studio.plotly as py
import chart_studio.tools as tls

csv_path = "./data/events/CSV/events_characters/event2characters.csv"
combined_json_path = "./data/characters/JSON/combined/combined.json"
graph_builder = GraphBuilder(
    csv_path=csv_path, characters_combined_json_path=combined_json_path
)

net_vis = network_visualizer(graph_builder=graph_builder, edge_random=0.02)

if __name__ == "__main__":
    fig = net_vis.get_fig()
    fig.show()
    fig.write_html("./index.html")

    # Upload to chart studio, need credential file
    py.plot(fig, filename="marvel_network_vis", auto_open=True)
    print(tls.get_embed("https://plotly.com/~delteforce23/7"))
