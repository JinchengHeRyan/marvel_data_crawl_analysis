import plotly.graph_objects as go
from graphBuilder.graph_build import GraphBuilder
import networkx as nx
import plotly.express as px
import chart_studio.plotly as py
import chart_studio.tools as tls
import random

csv_path = "./data/events/CSV/events_characters/event2characters.csv"
combined_json_path = "./data/characters/JSON/combined/combined.json"
graph_builder = GraphBuilder(
    csv_path=csv_path, characters_combined_json_path=combined_json_path
)

G = graph_builder.get_graph()
characters_list = graph_builder.get_characters_dict()

pos_ = nx.spring_layout(G)

edge_x = []
edge_y = []

random_rate = 0.02

for edge in random.choices(list(G.edges()), k=int(len(G.edges()) * random_rate)):
    x0, y0 = pos_[edge[0]]
    x1, y1 = pos_[edge[1]]
    edge_x.append(x0)
    edge_x.append(x1)
    edge_x.append(None)
    edge_y.append(y0)
    edge_y.append(y1)
    edge_y.append(None)

edge_trace = go.Scatter(
    x=edge_x,
    y=edge_y,
    line=dict(width=0.5, color="#888"),
    hoverinfo="none",
    mode="lines",
    opacity=1,
)

node_x = []
node_y = []
for node in G.nodes():
    x, y = pos_[node]
    node_x.append(x)
    node_y.append(y)

node_trace = go.Scatter(
    x=node_x,
    y=node_y,
    mode="markers",
    hoverinfo="text",
    marker=dict(
        showscale=True,
        # colorscale options
        #'Greys' | 'YlGnBu' | 'Greens' | 'YlOrRd' | 'Bluered' | 'RdBu' |
        #'Reds' | 'Blues' | 'Picnic' | 'Rainbow' | 'Portland' | 'Jet' |
        #'Hot' | 'Blackbody' | 'Earth' | 'Electric' | 'Viridis' |
        colorscale=px.colors.diverging.Picnic,
        # reversescale=True,
        color=[],
        size=10,
        colorbar=dict(
            thickness=15, title="Node Connections", xanchor="left", titleside="right"
        ),
        # line_width=2,
    ),
)

node_adjacencies = []
node_text = []
for node, adjacencies in enumerate(G.adjacency()):
    node_adjacencies.append(len(adjacencies[1]))
    node_text.append(
        "{}, # of connections: ".format(characters_list[adjacencies[0]])
        + str(len(adjacencies[1]))
    )

node_trace.marker.color = node_adjacencies
node_trace.text = node_text
fig = go.Figure(
    data=[edge_trace, node_trace],
    layout=go.Layout(
        title="<br>Marvel characters network visualization",
        font=dict(color="white"),
        titlefont_size=16,
        showlegend=False,
        hovermode="closest",
        margin=dict(b=20, l=5, r=5, t=40),
        annotations=[
            dict(
                text="Marvel data visualization",
                font=dict(color="white", size=14),
                showarrow=False,
                xref="paper",
                yref="paper",
                x=0.005,
                y=-0.002,
            )
        ],
        xaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
        yaxis=dict(showgrid=False, zeroline=False, showticklabels=False),
        paper_bgcolor="rgb(0,0,0)",
        plot_bgcolor="rgb(0,0,0)",
    ),
)
fig.show()
fig.write_html("./index.html")

# Upload to chart studio
py.plot(fig, filename="marvel_network_vis", auto_open=True)

print(tls.get_embed("https://plotly.com/~delteforce23/7"))
