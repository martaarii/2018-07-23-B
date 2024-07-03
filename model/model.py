import networkx as nx

from database.DAO import DAO


class Model:
    def __init__(self):
        self.grafo = nx.Graph()
        self.nodi = DAO.getAllStates()
        self.idMap = {}
        for n in self.nodi:
            self.idMap[n.id] = n
        self.edges = DAO.getAllNeigh(self.idMap)

    def creaGrafo(self, a, x):
        self.grafo.add_nodes_from(self.nodi)
        self.grafo.add_edges_from(self.edges)
        print(f"nodi: {self.grafo.nodes}, archi: {self.grafo.edges}")
        for e in self.edges:
            self.grafo[e[0]][e[1]]["weight"] = DAO.getPeso(e[0].id, e[1].id, a, x)[0]

    def sommaPesi(self):
        string = ""
        for n in self.nodi:
            string += n.id
            string += " "
            peso = 0
            for nei in self.grafo.neighbors(n):
                p = self.grafo[n][nei]['weight']
                peso += p
            string += str(peso)
            string += "\n"
        return string
    def stampa(self):
        return f"nodi: {len(self.grafo.nodes)}, archi: {len(self.grafo.edges)}"