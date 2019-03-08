class UndirectedGraphNode:
    def __init__(self, x):
        self.label = x
        self.neighbors = []

    @staticmethod
    def deserialize(data):
        data = data[1:-1]
        nodes = [node[0] for node in data.split('#')]
        mapping = {}
        for node in nodes:
            mapping[node] = UndirectedGraphNode(node)
        graph = []
        data = data.split('#')
        for node_str in data:
            node_list = node_str.split(',')
            base = mapping[node_list[0]]
            for nb in node_list[1:]:
                base.neighbors.append(mapping[nb])
            graph.append(base)

        return graph

    @staticmethod
    def serialize(graph):
        ser = ''
        for node in graph:
            tmp = str(node.label)
            for nb in node.neighbors:
                tmp += ',' + str(nb.label)
            ser += '#' + tmp
        return '{' + ser[1:] + '}'


if __name__ == "__main__":
    graph = UndirectedGraphNode.deserialize("{1,2,3,4#2,1,3#3,1#4,1,5#5,4}")
    print UndirectedGraphNode.serialize(graph)