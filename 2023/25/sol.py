import graphviz
import networkx

ex = """
jqt: rhn xhk nvd
rsh: frs pzl lsr
xhk: hfx
cmg: qnr nvd lhk bvb
rhn: xhk bvb hfx
bvb: xhk hfx
pzl: lsr hfx nvd
qnr: nvd
ntq: jqt hfx bvb xhk
nvd: lhk
lsr: lhk
rzs: qnr cmg lsr rsh
frs: qnr lhk lsr
"""

"""
Originally was using graphviz and manually finding min cut, but was having issues
 calculating the connected components manually.

NetworkX is so OP for this one.
"""
with open("input.txt") as f:
  debug = int(input("Debug? 0 for no, 1 for test case: "))
  view = int(input("View Graph? "))
  src = ex if debug != 0 else f.read()
  lines = [[n[:3] for n in l.split(" ")] for l in src.strip().split("\n")]

  dot = graphviz.Digraph(engine="neato")

  edges = []
  for l in lines:
    dot.node(str(l[0]), str(l[0]))
    root = l[0]
    for out_edge in l[1:]:
      dot.node(str(out_edge), str(out_edge))
      dot.edge(str(l[0]), str(out_edge))
      edges.append((root, out_edge))
  dot.render(directory='aoc_graph', view=(view == 1))

  # Use diagram to find edges to cut
  edges_to_cut = [("hfx", "pzl"), ("bvb", "cmg"), ("nvd", "jqt")] if debug else [("fjn", "mzb"), ("sjr", "jlt"), ("mhb", "zqp")]

  graph = networkx.Graph()
  for l in lines:
    graph.add_edges_from([(l[0], val) for val in l[1:]])

  # there will ony ever be 3 edges in the min cut
  cut = networkx.minimum_edge_cut(graph)
  graph.remove_edges_from(cut)

  groups = networkx.connected_components(graph)
  count = 1
  for g in groups:
    count *= len(g)
  print("SOL:", count)
