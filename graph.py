class Graph(object):

    def __init__(self):
        self.nodes = []
        self.count = 0

    def add_node(self,node):
        node.id = self.count #id is index in self.nodes
        self.count += 1
        self.nodes.append(node)

    def get_node(self, id):
        return self.nodes[id]

    def connect(self, node1, node2, directed=False, weight=None, edge_data=None):
        node1.connect_to(node2, weight, edge_data)
        if not directed:
            node2.connect_to(node1, weight, edge_data)

    def is_connected(node1, node2, two_way=False):
        if not two_way:
            return node1.is_connected(node2)
        else:
            return node1.is_connected(node2) and node2.is_connected(node1)

    def get_nodes(self, ids):
        return [node for node in self.nodes if node.id in ids]

    def __str__(self):
        s = ''
        for node in self.nodes:
            s += format('node %d\t- ' % (node.id))
            for edge in node.edges:
                s += str(edge.to.id) + " "
            s += '\n'
        return s


class Node(object):

    def __init__(self, data):
        self.data = data
        self.edges = []
        self.id = -1

    def connect_to(self,other, weight=None, edge_data=None):
        self.edges.append(Edge(other,weight,edge_data))


class Edge(object):

    def __init__(self,cell_to, weight=None,data=None,):
        self.to = cell_to
        self.data = data
        self.weight = weight

def main():
    g = Graph()
    g.add_node(Node(1))
    g.add_node(Node(2))
    g.add_node(Node(1))
    g.connect(g.get_node(0), g.get_node(1))
    n = g.get_node(0)
    n.connect_to(g.get_node(2))

    print(g)

if __name__ == '__main__':
    main()
