from rdflib import Graph
from cgfkg.graph_processor import Graph_processor
from cgfkg.rdf_query import RDFQuery
from ast import AST
from sys import argv

class CGFKG:
    def __init__(self, graph_address:str, format:str = 'xml') -> None:
        # Graph instance
        self.graph = Graph()
        self.graph_aloc(graph_address, format)
        self.graph_processor = Graph_processor(self.graph)

        query_processor_class = RDFQuery(self.graph)
        self.query_processor = query_processor_class.query_processor

        self.Recursive()

    def graph_aloc(self, graph_address:str, format:str) -> None:
        self.graph.parse(location=graph_address, format=format)

    def ASTRecursive(self, node:AST = AST, level:int = 0) -> bool:
        """
        In a recursive walking on AST, it performes `GraphRecursive()` for first leaf, which should be the "Module" one.
        """
        subclasses = node.__subclasses__()
        for subclass in subclasses:
            if self.ASTRecursive(node = subclass, level = level+1):
                return True
            else:
                return False
        if level > 1:
            try:
                for subject in self.query_processor(predicate = "rdf:type", object = "mpl2kdl:" + node.__name__):
                    for field in node._fields:
                        for object in self.query_processor(subject = "mpl2kdl:" + subject.s.fragment, predicate = "mpl2kdl:_" + field):
                            self.graph_processor.run(graphNode = object.o)
                return True
            except:
                return False

    def Recursive(self, node:AST = AST) -> bool:
        """
        This function get the original name of the file and dispatches `ASTRecursive`.
        """

        self.graph_processor.load_AST()

        # Get the original file name
        results = self.query_processor(predicate="wsml:ontologyID")
        for row in results:
            ontologyID = row.o.fragment
            break
            
        print(f"# -------------------------- {ontologyID}.py -------------------------")
        ret = self.ASTRecursive(node = node)
        print("# -----------------------------------------------------------------------", end='\n')

        return ret
