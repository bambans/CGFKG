from rdflib import Graph
from rdflib.query import Result

class RDFQuery:
    def __init__(self, graph:Graph) -> None:
        self.graph = graph
        self.prefixes = {
            'rdf': '<http://www.w3.org/1999/02/22-rdf-syntax-ns#>',
            'owl': '<http://www.w3.org/2002/07/owl#>',
            'rdfs': '<http://www.w3.org/2000/01/rdf-schema#>',
            'xsd': '<http://www.w3.org/2001/XMLSchema#>',
            'mpl2kdl': '<http://ufs.br/ontologies/mpl2kdl#>',
            'cdt': '<http://w3id.org/lindt/custom_datatypes#ucum>',
            'sosa': '<http://www.w3.org/ns/sosa/>',
            'dc': '<http://purl.org/dc/elements/1.1/>',
            'foaf': '<http://xmlns.com/foaf/0.1/>',
            'wsml': '<http://www.wsmo.org/wsml/wsml-syntax#>'
        }

    def prefixes_processor(self) -> str:
        prefixes = ""

        for short, prefix in self.prefixes.items():
            prefixes += f"PREFIX {short}: {prefix}"

        return prefixes

    def query_processor(self, type:str = "SELECT", subject:str = "?s", predicate:str = "?p", object:str = "?o") -> Result:
        """
        It performes a `rdflib.query` in a `rdflib.graph` and returns a `rdflib.query.Result`.
        """
        query =  """
            """+type+""" ?s ?p ?o WHERE{
                """+subject+""" """+predicate+""" """+object+""" .
            }
        """

        return self.graph.query(self.prefixes_processor() + query)
