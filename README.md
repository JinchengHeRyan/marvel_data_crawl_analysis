# STATS 401 Data Visualization Proj 2

## Marvel data crawling and analysis

### Team Member: [@Yixuan Li](https://github.com/austenoooo), [@Ziang Zhou](https://github.com/realzza), [@Jincheng He](https://github.com/JinchengHeRyan)

--------------------

Code in `marvel/` directory is referenced from [here](https://github.com/wrap-away/Marvel-API/tree/master/marvel).

#### Visualization Description:

In this graph, we visualized the network of marvel characters connection. Each node in this graph is a character, and
the edge between two nodes represents these two characters have a connection. Here the definition of two characters
having the connection is that these two characters both appear in at least one certain event. The weight of the edge is
the number of events that these two characters both appear.

To better visualize the graph and make it clearer, we randomized the edges of being showed. Originally there are 55256
edges, we chose the random rate to be 0.02, which means the graph only reveals 1105 edges.

By using this graph, we can compute different types of centrality such as betweenness centrality or closeness
centrality.

[[data](./data/events/CSV/events_characters/event2characters.csv)] | [[crawling code](./events_crawl.py)]
| [[visualization code](./network_vis.py)]
