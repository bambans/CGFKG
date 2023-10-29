from ast import AST
from rdflib import Graph
from cgfkg.rdf_query import RDFQuery
from ast import AST, Tuple, Call, ImportFrom, arguments, Str
from cgfkg.classToToken import astToTokenList

class Graph_processor:
    def __init__(self, graph:Graph, token_list:dict = astToTokenList, DEBUG = False) -> None:
        self.graph = graph
        self.token_list = token_list
        self.ASTlist = {}
        self.load_AST(list=self.ASTlist)
        self.fields_filter = {'kind', 'ctx'}
        self.arguments_d = []
        self.defaults_d = []

        query_processor_class = RDFQuery(self.graph)
        self.query_processor = query_processor_class.query_processor

        self.DEBUG = DEBUG

    def load_AST(self, node:AST = AST, list:dict = {}):
        """
        This function maps all AST nodes into a dictionary in which we can get an object class inherit from <class 'ast'>.
        
        Ex.:
        - `ASTlist['AST'] => <class 'ast.AST'>`; 
        - `ASTlist['ExceptHandler'] => <class 'ast.ExceptHandler'>`.
        """
        list[node.__name__] = node
        subclasses = node.__subclasses__()
        for subclass in subclasses:
            self.load_AST(node = subclass, list = list)

    def _get_AST_object(self, node:str) -> AST:
        if node == 'NoneStmt':
            return ''
        else:
            return self.ASTlist[node]

    def get_token(self, object, kind:str = 'tokenValue') -> str:
        """
        Object is usually subject.o.fragment
        Type can be 'tokenValue' or `field`
        """
        return self.token_list[self._get_AST_object(object)][kind]

    def run(self, graphNode:AST = None, block_level:int = 0):
        """
        This function walks recursively on the given RDFS graph. For each graph node, its type is tested and, from searching on `ASTlist`, it becomes possible to performe a new query for this node by each node field (described by the AST).
        
        This function needs these following arguments:
        - `graphNode`: graph node for which will be performed its fields searching and the recursive subqueries;
        - `graph:Graph`: graph object in which will be performed all SPARQL queries.
        """
        try:
            for subject in self.query_processor(subject = "mpl2kdl:" + graphNode.fragment, predicate="rdf:type"):

                level = block_level
                
                token = self.get_token(object = subject.o.fragment)

                if(token != ''):
                    print(level*'\t', end="")
                    print(token if token != '' else '', end="")

                ast_object = self._get_AST_object(subject.o.fragment)

                fields = ast_object._fields

                if len(fields) > 0:

                    for field in fields:

                        if field in self.fields_filter: continue

                        # observar o 'body' como marcador de bloco
                        if field == 'body': level += 1

                        objects = self.query_processor(subject = "mpl2kdl:" + graphNode.fragment, predicate = "mpl2kdl:_" + field)

                        if len(objects) > 0:

                            field_open = self.get_token(object = subject.o.fragment, kind = field)['open']
                            print(field_open if field_open != '' else '', end="")

                            for index, object in enumerate(objects):

                                value = self.run(graphNode = object.o, block_level = level)

                                if ast_object is arguments and field == "args":
                                    for arg in self.query_processor(subject = "mpl2kdl:" + object.o.fragment, predicate="mpl2kdl:_arg"):
                                        self.arguments_d.append(arg.o)

                                if ast_object is arguments and field == "defaults":
                                    for default in self.query_processor(subject = "mpl2kdl:" + object.o.fragment, predicate="mpl2kdl:_value"):
                                        self.defaults_d.append(default.o)

                                    range_diff = abs(len(self.arguments_d) - len(self.defaults_d))

                                    for i in range(len(self.defaults_d) -1, -1, -1):
                                        if i != 0:
                                            print(f"{self.arguments_d[i+range_diff]} = {self.defaults_d[i]}", end=", ")
                                        else:
                                            print(f"{self.arguments_d[i+range_diff]} = {self.defaults_d[i]}", end="")

                                if isinstance(ast_object, Str):
                                    if value is not None:
                                        if "\n" in value:
                                            print(f"""{value}""", end="")
                                        elif '"' in value:
                                            print(f'{value}', end="")
                                        elif "'" in value:
                                            print(f"{value}", end="")
                                        else:
                                            print(value, end="")
                                    else:
                                        print('', end="")
                                else:
                                    print(value if value is not None else '', end="")
                                
                                # se houver mais de uma iteração, colocar as vírgulas
                                if (ast_object is Tuple and index != len(objects)-1) or (ast_object is ImportFrom and field == 'names' and len(objects) > 1 and index != len(objects)-1) or (ast_object is Call and field == 'args' and index != len(objects)-1) or (ast_object is arguments and field == 'args' and index != len(objects)-1):
                                    # Para as tuplas é mais fácil, mas no caso abaixo, tenho que estudar outra alternativa:
                                    # ast_object is alias and field == 'name' and len(objects) > 1 and index != len(objects)-1
                                    print(', ', end='')

                            field_close = self.get_token(object = subject.o.fragment, kind = field)['close']
                            print(field_close if field_close != '' else '', end="")

                        else:
                            # resolver o caso do 'as' no ImportFrom
                            if field in self.fields_filter:
                                field_open = self.get_token(object = subject.o.fragment, kind = field)['open']
                                print(field_open if field_open != '' else '', end="")
                                
                                field_close = self.get_token(object = subject.o.fragment, kind = field)['close']
                                print(field_close if field_close != '' else '', end="")

                        if field == 'body': level -= 1

                        block_level = level

                        self.defaults_d = []
        except:
            if self.DEBUG: print('\n{\n', f'\tGraphNode: {graphNode}\n', f'\tBlockLevel: {block_level}\n','\n}\n')

            if graphNode == 'None':
                # Aparentemente, os termos que são da classe rdflib.term.literal possuem conversão implícita para tipos como 'string' e, sendo assim, é possível diferenciar None (NoneType) de 'None' (String)
                #     # Estou forçando a variável graphNone, quando 'None', a receber None (NoneType)
                graphNode = None
                
                return graphNode
            else:
                return graphNode
            
        if self.DEBUG: print('\n{\n', f'\tGetAstObject: {ast_object}\n', f'\tField: {field}\n', f'\tObjectO: {object.o}\n', f'\tValue: {value}\n', f'\tValueClass: {value.__class__}\n', f'\tBlockLevel: {level}\n','\n}\n')
