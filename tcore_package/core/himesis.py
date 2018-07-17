
import uuid, os.path, copy, cPickle as pickle    # Pickle is used to save the attribute values as pickled strings
import igraph as ig
import util.misc as misc
from epsilon_parser import EpsilonParser
from util.misc import indent_text


class HConstants:
    GUID = 'GUID__'
    META_MODEL = 'mm__'
    MT_LABEL = 'MT_label__'
    MT_CONSTRAINT = 'MT_constraint__'
    MT_ACTION = 'MT_action__'
    MT_SUBTYPE_MATCH = 'MT_subtypeMatching__'
    MT_SUBTYPES = 'MT_subtypes__'
    MT_DIRTY = 'MT_dirty__'
    MT_PIVOT_IN = 'MT_pivotIn__'
    MT_PIVOT_OUT = 'MT_pivotOut__'
    MT_PRECOND_PREFIX = 'MT_pre__'
    MT_POSTCOND_PREFIX = 'MT_post__'



class Himesis(ig.Graph):
    """
        Creates a typed, attributed, directed, multi-graph.
        @param num_nodes: the total number of nodes. If not known, you can add more vertices later
        @param edges: the list of edges where each edge is a tuple representing the ids of the source and target nodes
    """
    Constants = HConstants
    EDGE_LIST_THRESHOLD = 10**3
    
    @staticmethod
    def standardize_name(name):
        """
            Converts the given name into a standard Himesis name.
            @param name: The name of the Himesis graph
        """
        if name.startswith('H'):
            return name
        return 'H%s%s' % (name[0].capitalize(), name[1:])
    
    @staticmethod
    def is_RAM_attribute(attr_name):
        return (attr_name.startswith(Himesis.Constants.MT_PRECOND_PREFIX)
                or attr_name.startswith(Himesis.Constants.MT_POSTCOND_PREFIX))
    
    @staticmethod
    def to_non_RAM_attribute(attr_name):
        if attr_name.startswith(Himesis.Constants.MT_PRECOND_PREFIX):
            return attr_name[len(Himesis.Constants.MT_PRECOND_PREFIX):]
        elif attr_name.startswith(Himesis.Constants.MT_POSTCOND_PREFIX):
            return attr_name[len(Himesis.Constants.MT_POSTCOND_PREFIX):]
        else:
            return attr_name
    
    def __init__(self, name='', num_nodes=0, edges=[]):
        """
            Creates a typed, attributed, directed, multi-graph.
            @param num_nodes: the total number of nodes. If not known, you can add more vertices later
            @param edges: the list of edges where each edge is a tuple representing the ids of the source and target nodes
        """
        ig.Graph.__init__(self, directed=True, n=num_nodes, edges=edges)
        if not name:
            name = self.__class__.__name__
        self.name = Himesis.standardize_name(name)
        
        # Set universally unique identifiers for the graph and each node
        if not hasattr(self, 'is_compiled'):
            self.is_compiled = False    # this instance is not yet compiled
            self[Himesis.Constants.GUID] = uuid.uuid4()
            for n in self.node_iter():
                self.vs[n][Himesis.Constants.GUID] = uuid.uuid4()
        # A fast lookup of the node's index by its guid
        self.nodes_id = {}
        
        # The following attributes are used by the compiler
        self.execute_body = ''          # holds the content of the execute method
        self.execute_parameters = []    # holds the arguments of the execute method
        self.execute_doc = ''           # holds the docstring of the execute method
        self.init_params = []           # If any further parameters are required for instantiating a sub-class
        self.import_name = 'Himesis'    # holds the name of the super-class (one of those in this module) of this instance
    
    def copy(self):
        cpy = ig.Graph.copy(self)
        cpy.nodes_id = copy.deepcopy(self.nodes_id)
        cpy.execute_body = copy.deepcopy(self.execute_body)
        cpy.execute_parameters = copy.deepcopy(self.execute_parameters)
        cpy.execute_doc = copy.deepcopy(self.execute_doc)
        cpy.init_params = copy.deepcopy(self.init_params)
        cpy.import_name = copy.deepcopy(self.import_name)
        cpy.is_compiled = copy.deepcopy(self.is_compiled)
        cpy.name = copy.deepcopy(self.name)
        return cpy
    
    def __copy__(self):
        return self.copy()
    
    def __deepcopy__(self, memo):
        return self.__copy__()
    
    def __str__(self):
        s = super(Himesis, self).__str__()
        return self.name + ' ' + s[s.index('('):] + ' ' + str(self[Himesis.Constants.GUID])
    
    def get_id(self):
        """
            Returns the unique identifier of the graph
        """
        return self[Himesis.Constants.GUID]
    
    def node_iter(self):
        """
            Iterates over the nodes in the graph, by index
        """
        return xrange(self.vcount())
    
    def edge_iter(self):
        """
            Iterates over the edges in the graph, by index
        """
        return xrange(self.ecount())
    
    def add_node(self):
        new_node = self.vcount()
        self.add_vertices(1)
        id = uuid.uuid4()
        self.vs[new_node][Himesis.Constants.GUID] = id
        self.nodes_id[id] = new_node
        return new_node
    
    def delete_nodes(self, nodes):
        self.delete_vertices(nodes)
        # Regenerate the lookup because node indices have changed
        self.nodes_id = dict([(self.vs[node][Himesis.Constants.GUID], node) for node in self.node_iter()])
    
    def get_node(self, id):
        """
            Retrieves the node instance with the specified label.
            @param label: The label of the node.
        """
        if len(self.nodes_id) < self.vcount():
            self.nodes_id = dict([(self.vs[node][Himesis.Constants.GUID], node) for node in self.node_iter()])
        if id in self.nodes_id:
            return self.nodes_id[id]
        else:
            #TODO: This should be a TransformationLanguageSpecificException
            raise Exception('No node was found with the given id')
    
    def draw(self, visual_style={}, label=None, show_guid=False, show_id=False, debug=False, width=600, height=900):
        """
        Visual graphic rendering of the graph.
        @param label: The attribute to use as node label in the figure.
                      If not provided, the index of the node is used.
        @param visual_style: More drawing options
        (see http://igraph.sourceforge.net/doc/python/igraph.Graph-class.html#__plot__ for more details).
        """
        if 'layout' not in visual_style:
            visual_style["layout"] = 'fr'
        if 'margin' not in visual_style:
            visual_style["margin"] = 10
        
        # Set the labels
        if not label:
            if show_guid:
                visual_style["vertex_label"] = [str(self.vs[i][Himesis.Constants.GUID])[:4] for i in self.node_iter()]
            elif show_id:
                visual_style["vertex_label"] = [str(i) for i in self.node_iter()]
            else:
                visual_style["vertex_label"] = [''] *  self.vcount()
        else:
            try:
                visual_style["vertex_label"] = self.vs[label]
                for n in self.node_iter():
                    if not visual_style["vertex_label"][n]:
                        visual_style["vertex_label"][n] = self.vs[n][Himesis.Constants.META_MODEL]
                        if debug:
                            visual_style["vertex_label"][n] = str(n) + ':' + visual_style["vertex_label"][n] 
                    elif debug:
                        visual_style["vertex_label"][n] = str(n) + ':' + visual_style["vertex_label"][n]
            except:
                raise Exception('%s is not a valid attribute' % label)
        
        return ig.plot(self, bbox=(0, 0, width, height), **visual_style)
    
    def _compile_additional_info(self, file):
        s = ''
        if self.execute_body:
            s = '''
    def execute(self'''
            if self.execute_parameters:
                params = ', %s' * len(self.execute_parameters)
                s += params % tuple(self.execute_parameters)
            s += '''):
%s
    '''
            file.write(s % indent_text(self.execute_doc + self.execute_body, 2))
        
    def __compile_attribute(self, access, value):
        """
        Dump the initialization of the attribute:
        - for string, int, float, and bool types write the value directly;
        - for reference to another Himesis graph, call the constructor;
        - for all other types, dump the pickled value.
        @param access: the access to the attribute
        @param value: the value to set the attribute to
        """
        if isinstance(value, str):
            return '''
        %s = """%s"""''' % (access, value)
        elif isinstance(value, int) or isinstance(value, float) or isinstance(value, bool):
            return '''
        %s = %s''' % (access, value)
        elif isinstance(value, uuid.UUID):
            return '''
        %s = UUID('%s')''' % (access, str(value))
        elif isinstance(value, Himesis):
            graphClass = value.name
            return '''
        from %s import %s
        %s = %s()''' % (graphClass, graphClass, access, graphClass)
        else:
            return '''
        %s = pickle.loads("""%s""")''' % (access, pickle.dumps(value))
    
    def compile(self, file_path):
        """
        Compiles the graph into a Python file.
        Compilation is recursive: i.e., all sub-graphs are also compiled.
        @param file_path: The path of the output file.
        """
        
        # Make sure the directory exists
        # If the path contains the output file name, it will be replaced by the default one
        if os.path.isfile(file_path):
            file_path = os.path.dirname(file_path)
        if not os.path.isdir(file_path):
            e = IOError(2, 'Output path does not exist')
            e.filename = file_path
            raise e
        
        subgraphs = []      # references to Himesis sub-graphs of this graph
        
        #with open(file, 'w') as file:
        file = open(os.path.join(file_path, self.name + '.py'), 'w')
        if True:
            # Save the nodes in increasing order of the occurrence of its meta-model:
            # First build a dictionary {meta-model element: number of nodes of that type}
            meta_models = {}
            if self.vcount() > 0:
                tmp = self.vs[Himesis.Constants.META_MODEL]
                for mm in tmp:
                    if mm not in meta_models:
                        meta_models[mm] = tmp.count(mm)
                del tmp
            # Then, sort the node indices such that the node that has the least frequent type is in the beginning
            # We save the list as an object attribute, because it might be used by a sub-class' compiler
            self.ordered_nodes = sorted(self.node_iter(),
                                   key=lambda v: meta_models[self.vs[v][Himesis.Constants.META_MODEL]])
            
            file.write('''

from core.himesis import Himesis''')
            if self.import_name != 'Himesis':
                file.write(''', %s''' % self.import_name)
            
            init_params = ''
            init_params_values = ''
            if len(self.init_params) > 0:
                init_params = reduce(lambda p1, p2: p1 + p2,
                                    map(lambda p: ', %s' % p,
                                        self.init_params))
                init_params_values = reduce(lambda p1, p2: p1 + p2,
                                            map(lambda p: ', %s=%s' % (p, p),
                                                self.init_params))
            file.write('''
import cPickle as pickle
from uuid import UUID

class %s(%s):
    def __init__(self%s):
        """
        Creates the himesis graph representing the AToM3 model %s.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(%s, self).__init__(name='%s', num_nodes=%d, edges=[]%s)
''' % (self.name,
       self.import_name,
       init_params,
       self.name,
       self.name,
       self.name,
       self.vcount(),
       init_params_values))
            
            # Add the edges
            file.write('''        
        # Add the edges''')
            edge_list = []
            # Determines if it's possible to provide the edges as a single list
            # Because it's faster than adding each edge individually.
            # However, due to Python limitations, the edge list is specified one 1 line
            # So for bigger graphs, we need to add edges in groups.
            if self.ecount() < Himesis.EDGE_LIST_THRESHOLD:
                edge_list = self.get_edgelist()
                # Order the edge list
                for i in range(len(edge_list)):
                    edge_list[i] = (self.ordered_nodes.index(edge_list[i][0]),
                                    self.ordered_nodes.index(edge_list[i][1]))
                file.write('''
        self.add_edges(%s)''' % str(edge_list))
            else:
                pitch = 0
                while pitch < self.ecount():
                    edgeId = pitch
                    edge_list = []
                    while edgeId - pitch < Himesis.EDGE_LIST_THRESHOLD and edgeId < self.ecount():
                        # Using the new order of nodes
                        edge = (self.ordered_nodes.index(self.es[edgeId].source),
                                self.ordered_nodes.index(self.es[edgeId].target))
                        edge_list.append(edge)
                        edgeId += 1
                    file.write('''
        self.add_edges(%s)''' % str(edge_list))
                    pitch += Himesis.EDGE_LIST_THRESHOLD
                file.write('''
        ''')
            
            # Set the graph attributes
            file.write('''
        # Set the graph attributes''')
            for attr in self.attributes():
                value = self[attr]
                access = 'self["%s"]' % attr
                file.write(self.__compile_attribute(access, value))
                if isinstance(value, Himesis):
                    subgraphs.append(value)
            
            # Set node attributes
            file.write('''
        
        # Set the node attributes''')
            # Compile the node attributes, always in the reight order
            for new_node_index, old_node_index in enumerate(self.ordered_nodes):
                for attr in self.vs[old_node_index].attribute_names():
                    if self.vs[old_node_index][attr] is not None:
                        value = self.vs[old_node_index][attr]
                        access = 'self.vs[%d]["%s"]' % (new_node_index, attr)
                        file.write(self.__compile_attribute(access, value))
                        if isinstance(value, Himesis):
                            subgraphs.append(value)
            
            file.write('\n')
            self._compile_additional_info(file)
            file.write('\n')
        
        file.close()
        
        for sg in subgraphs:
            sg.compile(file_path)
        
        return file.name
   
    def execute(self, *args):
        raise AttributeError('This method is not implemented')


class HimesisPattern(Himesis):
    def __init__(self, name='', num_nodes=0, edges=[]):
        super(HimesisPattern, self).__init__(name, num_nodes, edges)
        self.nodes_label = {}
        self.nodes_pivot_out = {}
    
    def get_node_with_label(self, label):
        """
            Retrieves the index of the node with the specified label.
            @param label: The label of the node.
        """
        if not self.nodes_label:
            self.nodes_label = dict([(self.vs[i][Himesis.Constants.MT_LABEL], i) for i in self.node_iter()])
        if label in self.nodes_label:
            return self.nodes_label[label]
    
    def get_pivot_out(self, pivot):
        """
            Retrieves the index of the pivot node
            @param pivot: The label of the pivot.
        """
        if not self.nodes_pivot_out and Himesis.Constants.MT_PIVOT_OUT in self.vs.attribute_names():
            self.nodes_pivot_out = dict([(i, self.vs[i][Himesis.Constants.MT_PIVOT_OUT]) for i in self.node_iter()])
        if pivot in self.nodes_pivot_out:
            return self.nodes_pivot_out[pivot]


class HimesisPreConditionPattern(HimesisPattern):
    def __init__(self, name='', num_nodes=0, edges=[]):
        super(HimesisPreConditionPattern, self).__init__(name, num_nodes, edges)
        self.import_name = 'HimesisPreConditionPattern'
        self.nodes_pivot_in = {}
    
    def get_pivot_in(self, pivot):
        """
            Retrieves the index of the pivot node
            @param pivot: The label of the pivot.
        """
        if not self.nodes_pivot_in and Himesis.Constants.MT_PIVOT_IN in self.vs.attribute_names():
            self.nodes_pivot_in = dict([(self.vs[i][Himesis.Constants.MT_PIVOT_IN], i) for i in self.node_iter()])
        if pivot in self.nodes_pivot_in:
            return self.nodes_pivot_in[pivot]
    
    def constraint(self, PreMatch, graph):
        """
        If a constraint shall be specified, the corresponding Himesis graph must override this method.
        The condition must be specified in the pattern graph and not the input graph.
        By default, the constraint evaluates to True.
        @param PreMatch: The current match, before the rewriting.
        @param graph: The whole input graph.
        """
        return True
    
    def get_attr_constraint_name(self, node, attr_name):
        """
            Returns the name of the method to call to evaluate the constraint of the given attribute.
            @param attr_name: The name of the attribute.
        """
        return 'eval_%s%s' % (Himesis.to_non_RAM_attribute(attr_name), self.vs[node][Himesis.Constants.MT_LABEL])
    
    def _compile_additional_info(self, file):
        """
        Compiles the constraint code into a callable method.
        @param file: The output file.
        """
        
        # Attribute constraints code
        for v in self.node_iter():
            for attr in self.vs[v].attribute_names():
                if not self.vs[v][attr]:
                    # There is no action for this attribute
                    continue
                if Himesis.is_RAM_attribute(attr):
                    file.write('''
    def %s(self, attr_value, this):
%s

''' % (self.get_attr_constraint_name(v, attr), misc.indent_text(EpsilonParser().to_python(self.vs[v][attr]), 2)))
        
        # The constraint code
        code = 'return True'
        if Himesis.Constants.MT_CONSTRAINT in self.attributes() and self[Himesis.Constants.MT_CONSTRAINT]:
            code = EpsilonParser().to_python(self[Himesis.Constants.MT_CONSTRAINT])
        file.write('''
    def constraint(self, PreNode, graph):
        """
            Executable constraint code. 
            @param PreNode: Function taking an integer as parameter
                            and returns the node corresponding to that label.
        """
%s
''' %  misc.indent_text(code, 2))



class HimesisPreConditionPatternLHS(HimesisPreConditionPattern):
    def __init__(self, name='', num_nodes=0, edges=[]):
        super(HimesisPreConditionPatternLHS, self).__init__(name, num_nodes, edges)
        self.import_name = 'HimesisPreConditionPatternLHS'
        self.NACs = []
    
    def _compile_additional_info(self, file):
        """
        Compiles the constraint code into a callable method and links to NACs.
        @param file: The output file.
        """
        
        # The NACs
        if len(self.NACs) > 0:
            file.write('''
        
        # Load the NACs''')
            if self.is_compiled:
                # self.NACs is a list of Himesis graphs
                for NAC in self.NACs:
                    NAC_name = NAC.__class__.__name__
                    file.write("""
        from %s import %s""" % (NAC_name, NAC_name))
                file.write('''
        self.NACs = %s
''' % str(map(lambda NAC: '%s(LHS=self)' % Himesis.standardize_name(NAC.__class__.__name__),
                    self.NACs)).replace("'", ""))
            
            else:
                # self.NACs = ['NAC1', 'NAC2', ..., 'NACn']
                for NAC_name in self.NACs:
                    file.write("""
        from %s import %s""" % (Himesis.standardize_name(NAC_name), Himesis.standardize_name(NAC_name)))
                file.write('''
        self.NACs = %s
''' % str(map(lambda NAC: '%s(LHS=self)' % Himesis.standardize_name(NAC), self.NACs)).replace("'", ""))
        
        super(HimesisPreConditionPatternLHS, self)._compile_additional_info(file)



class HimesisPreConditionPatternNAC(HimesisPreConditionPattern):
    def __init__(self, LHS, name='', num_nodes=0, edges=[]):
        super(HimesisPreConditionPatternNAC, self).__init__(name, num_nodes, edges)
        self.LHS = LHS
        self.bridge = None
        self.init_params.append('LHS')
        self.import_name = 'HimesisPreConditionPatternNAC'
    
    def _compile_additional_info(self, file):
        """
        Compiles the bridge between this NAC and its LHS.
        @param file: The output file.
        """
        
        # Re-compile the bridge even if the NAC was already compiled, to ensure consistency between the 3 graphs
        self.bridge = self.compute_bridge()
        self.bridge.name = self.name + 'Bridge'
        self.bridge.compile(file.name)
        
        file.write("""
        
        # Load the bridge between this NAC and its LHS
        from %s import %s""" % (self.bridge.name, self.bridge.name))
        file.write('''
        self.bridge = %s()
''' % self.bridge.name)
        
        super(HimesisPreConditionPatternNAC, self)._compile_additional_info(file)
    
    def compute_bridge(self):
        """
            Creates a HimesisPreConditionPattern defined as the intersection of graph with this instance.
            This is called the 'bridge'.
            From a topological point of view, this method computes the largest common subgraph of these two graphs.
            However, the similarity of nodes of the bridge relies on the meta-model type of the nodes. 
            Furthermore, every attribute value is the conjunction of the constraints defined in each graph.
        """
        # G1 is the smallest graph and G2 is the bigger graph
        G1 = self
        G2 = self.LHS
        if G1.vcount() > G2.vcount():
            # Swap
            G1, G2 = G2, G1
        # The bridge
        G = HimesisPreConditionPattern()
        # We don't need to actually solve the largest common subgraph (LCS) problem
        # because we assume that the nodes are labelled uniquely in each graph
        # and that if a label is in G1 and in G2, then it will be in G
        Labels2 = G2.vs[Himesis.Constants.MT_LABEL]
        for label in G1.vs[Himesis.Constants.MT_LABEL]:
            if label in Labels2:
                # Get the corresponding node from G1 
                v1 = G1.vs.select(lambda v : v[Himesis.Constants.MT_LABEL] == label)
                if len(v1) == 1:
                    v1 = v1[0]
                elif len(v1) == 0:
                    raise Exception('Label does not exist: ' + str(label))
                else:
                    raise Exception('Label is not unique: ' + str(label))
                # Get the corresponding node from G2 
                v2 = G2.vs.select(lambda v : v[Himesis.Constants.MT_LABEL] == label)
                if len(v2) == 1:
                    v2 = v2[0]
                elif len(v2) == 0:
                    raise Exception('Label does not exist: ' + str(label))
                else:
                    raise Exception('Label is not unique: ' + str(label))
                new_node = G.add_node()
                # Now do a conjunction of the attributes
                for attr in v1.attribute_names():
                    G.vs[new_node][attr] = v1[attr]
                for attr in v2.attribute_names():
                    # The attribute is not in v1
                    if attr not in G.vs[new_node].attribute_names():
                        G.vs[new_node][attr] = v2[attr]
                    # Ignore the GUID attribute, it will be automatically set at run-time
                    elif attr == Himesis.Constants.GUID:
                        continue
                    elif Himesis.is_RAM_attribute(attr):
                        if not v2[attr]:
                            # There is no constraint for this attribute
                            continue
                        # The attribute constraint code is the conjunction of the LHS constraint
                        # with the NAC constraint for this attribute
                        s = '''from %s import %s
from %s import %s''' % (G1.name, G1.name, G2.name, G2.name)
                        if G1 == self:
                            s += ('''
lhs = %s()''' % G2.name) + '''
return %s(lhs).%s(attr_value, this) and %s().%s(attr_value, this)'''
                        else:
                            s += ('''
lhs = %s()''' % G1.name) + '''
return %s().%s(attr_value, this) and %s(lhs).%s(attr_value, this)'''
                        G.vs[new_node][attr] = s % (G1.name, G1.get_attr_constraint_name(v1.index, attr),
                                                    G2.name, G2.get_attr_constraint_name(v2.index, attr))
                    elif v1[attr] != v2[attr]:
                        #TODO: This should be a TransformationLanguageSpecificException
                        raise Exception('Unable to conjunct \'%s\' while computing the bridge' % attr)
                    #else: v1[attr] == v2[attr], so we don't need to do anything more 
        # Now add the edges
        # We only need to go through the edges of the smaller graph
        for e in G1.edge_iter():
            src_label = G1.vs[G1.es[e].source][Himesis.Constants.MT_LABEL]
            trg_label = G1.vs[G1.es[e].target][Himesis.Constants.MT_LABEL]
            src = G.vs.select(lambda v : v[Himesis.Constants.MT_LABEL] == src_label)
            trg = G.vs.select(lambda v : v[Himesis.Constants.MT_LABEL] == trg_label)
            if len(src) == len(trg) == 1:
                src = src[0]
                trg = trg[0]
                G.add_edges((src.index, trg.index))
            elif len(src) == 0 :
#                raise Exception('Label does not exist :: '+str(src_label))
                pass
            elif len(trg) == 0 :
#                raise Exception('Label does not exist :: '+str(tgt_label))
                pass
            elif len(src) > 1 :
                raise Exception('Label is not unique: ' + str(src_label))
            elif len(trg) > 1 :
                raise Exception('Label is not unique: ' + str(trg_label))        
        return G



class HimesisPostConditionPattern(HimesisPattern):
    def __init__(self, name='', num_nodes=0, edges=[]):
        super(HimesisPostConditionPattern, self).__init__(name, num_nodes, edges)
        self.pre = None
        self.import_name = 'HimesisPostConditionPattern'
    
    def action(self, MTpre, MTpost):
        """
        If an action shall be specified, the corresponding Himesis graph must override this method.
        The action must be specified in the pattern graph and not the input graph.
        """
        pass
    
    def get_attr_action_name(self, node, attr_name):
        """
            Returns the name of the method to call to execute the action of the given attribute.
            @param attr_name: The name of the attribute.
        """
        return 'set_%s%s' % (Himesis.to_non_RAM_attribute(attr_name), self.vs[node][Himesis.Constants.MT_LABEL])
    
    # This method must be overridden by every sub-class.
    # There lies the code of the rewriting part of the rule.
    def execute(self, packet):
        pass
    
    def compile(self, file_path, pre_label_MM_mapping={}):
        """
        Compiles the graph down to a file in an executable format.
        @param file_path: The path of the output file.
        @param pre_label_MM_mapping: If this instance was not yet compiled,
                                     you must specify the mapping from the pre-condition pattern in the form:
                                     {label: meta-model name}.
        """
        assert(self.is_compiled or (not self.is_compiled and pre_label_MM_mapping),
               'The mapping {label: meta-model name} of the pre-condition pattern must be specified')
        # Augment the graph with the following attribute just for compilation purposes
        self.pre_label_MM_mapping = pre_label_MM_mapping
        return super(HimesisPostConditionPattern, self).compile(file_path)
    
    def attribute_is_specified(self, code):
        """
            Detects if some action code in the attribute is specified and actually does something
            @param code: The action code.
        """
        for line in code.splitlines():
            if line != '' and not line.startswith('#') and line != 'return attr_value':
                # Returns true also if there is code after return attr_value 
                return True
        return False
    
    def _compile_additional_info(self, file):
        """
        Compiles the execute and action codes into callable methods as well as the pointer to the pre-condition pattern. 
        @param file: The output file
        """
        if self.is_compiled:
            # self.pre is a Himesis graph
            file.write('''
        from %s import %s
        self.pre = %s()
    ''' % tuple([self.pre.__class__.__name__] * 3))
        else:
            # self.pre = "precondition name"
            file.write('''
        from %s import %s
        self.pre = %s()
    ''' % tuple([Himesis.standardize_name(self.pre)] * 3))
        
        # Attributes action code
        for v in self.node_iter():
            for attr in self.vs[v].attribute_names():
                if not self.vs[v][attr]:
                    # There is no action for this attribute
                    continue
                if Himesis.is_RAM_attribute(attr):
                    code = self.vs[v][attr]
                    if self.attribute_is_specified(code):
                        file.write('''
    def %s(self, attr_value, PreNode, graph):
%s

''' % (self.get_attr_action_name(v, attr), misc.indent_text(EpsilonParser().to_python(code), 2)))
        
        # The action code
        code = 'pass'
        if Himesis.Constants.MT_ACTION in self.attributes() and self[Himesis.Constants.MT_ACTION]:
            code = EpsilonParser().to_python(self[Himesis.Constants.MT_ACTION])
        file.write('''
    def action(self, PostNode, graph):
        """
            Executable constraint code. 
            @param PostNode: Function taking an integer as parameter
                             and returns the node corresponding to that label.
        """
%s
''' % misc.indent_text(code, 2))
        
        # The execute method
        self.set_execute_body()
        assert(len(self.execute_body) > 0, 'The execute method has no body')
        self.execute_parameters = ['packet', 'match'] 
        self.execute_doc = '''"""
    Transforms the current match of the packet according to the rule %s.
    Pivots are also assigned, if any.
    @param packet: The input packet.
    @param match: The match to rewrite.
"""
'''
        super(HimesisPostConditionPattern, self)._compile_additional_info(file)
    
    def set_execute_body(self):
        """
        Compiles the body of the execute method.
        """
        
        def set_attributes(node, index, has_old_values):
            transformationCode = []
            for attrName in self.vs[node].attribute_names():
                if Himesis.is_RAM_attribute(attrName):
                    attr = self.vs[node][attrName]
                    if not attr:
                        # No action to perform for this attribute
                        continue
                    attrName = Himesis.to_non_RAM_attribute(attrName)
                    if self.attribute_is_specified(attr):
                        old_value = 'None'
                        if has_old_values:
                            old_value = "graph.vs[%s]['%s']" % (index, Himesis.to_non_RAM_attribute(attrName))
                        #TODO: This should be a TransformationLanguageSpecificException
                        transformationCode.append("""try:
    graph.vs[%s]['%s'] = self.%s(%s, lambda i: graph.vs[match[i]], graph)
except Exception, e:
    raise Exception('An error has occurred while computing the value of the attribute \\'%s\\'', e)
""" \
    % (index, Himesis.to_non_RAM_attribute(attrName),
       self.get_attr_action_name(node, attrName),
       old_value, attrName))
            return ''.join(transformationCode)
        
        
        LHS_labels = {}     # {label: meta-model name}
        if self.is_compiled and Himesis.Constants.MT_LABEL in self.pre.vs.attribute_names():
            LHS_labels = dict([(label, self.pre.vs[self.pre.get_node_with_label(label)][Himesis.Constants.META_MODEL])
                               for label in self.pre.vs[Himesis.Constants.MT_LABEL]])
        else:
            LHS_labels = self.pre_label_MM_mapping  # This was initialized in the overridden compile method
        RHS_labels = []
        if Himesis.Constants.MT_LABEL in self.vs.attribute_names():
            RHS_labels += self.vs[Himesis.Constants.MT_LABEL]
        
        # Update attributes
        transformationCode = ["""graph = packet.graph

# Build a dictionary {label: node index} mapping each label of the pattern to a node in the graph to rewrite.
# Because of the uniqueness property of labels in a rule, we can store all LHS labels
# and subsequently add the labels corresponding to the nodes to be created.
labels = match.copy()

#===============================================================================
# Update attribute values
#===============================================================================
"""]
        for label in LHS_labels:
            rhsNode = self.get_node_with_label(label)
            if rhsNode is None: continue        # not in the interface graph (LHS n RHS)
            updateCode = set_attributes(rhsNode, "labels['%s']" % label, has_old_values=True)
            if len(updateCode) > 0:
                transformationCode.append("""# %s%s
%s""" % (Himesis.to_non_RAM_attribute(self.vs[rhsNode][Himesis.Constants.META_MODEL]), label, updateCode))
                # Only set the dirty flag if there was a modification in the attributes
                transformationCode.append("""
graph.vs[labels['%s']][Himesis.Constants.MT_DIRTY] = True
""" % label)
        
        # Create new nodes
        transformationCode.append("""
#===============================================================================
# Create new nodes
#===============================================================================
""")
        new_labels = []
        for label in RHS_labels:
            rhsNode = self.get_node_with_label(label)
            if label not in LHS_labels:
                new_labels += [label]
                className = Himesis.to_non_RAM_attribute(self.vs[rhsNode][Himesis.Constants.META_MODEL])
                transformationCode.append("""# %s%s
new_node = graph.add_node()
labels['%s'] = new_node
graph.vs[new_node][Himesis.Constants.META_MODEL] = '%s'
""" % (className, label, label, className))
                transformationCode += set_attributes(rhsNode, 'new_node', has_old_values=False)
        
        # Link the new nodes
        transformationCode.append("""
#===============================================================================
# Create new edges
#===============================================================================
""")
        visited_edges = []
        for label in sorted(new_labels):
            for edge in self.es.select(lambda e: (e.index not in visited_edges and
                                                  (label == self.vs[e.source][Himesis.Constants.MT_LABEL]
                                                   or label == self.vs[e.target][Himesis.Constants.MT_LABEL]))):
                src_label = self.vs[edge.source][Himesis.Constants.MT_LABEL]
                tar_label = self.vs[edge.target][Himesis.Constants.MT_LABEL]
                transformationCode.append("""# %s%s -> %s%s
graph.add_edges((labels['%s'], labels['%s']))
""" % (Himesis.to_non_RAM_attribute(self.vs[edge.source][Himesis.Constants.META_MODEL]),
       src_label,
       Himesis.to_non_RAM_attribute(self.vs[edge.target][Himesis.Constants.META_MODEL]),
       tar_label,
       src_label,
       tar_label))
                visited_edges.append(edge.index)
        
        # Set the output pivots
        transformationCode.append("""
#===============================================================================
# Set the output pivots
#===============================================================================
""")
        if Himesis.Constants.MT_PIVOT_OUT in self.vs.attribute_names():
            for node in self.vs.select(lambda v: v[Himesis.Constants.MT_PIVOT_OUT]):
                node = node.index
                label = self.vs[node][Himesis.Constants.MT_LABEL]
                transformationCode.append(
"""# %s%s
packet.global_pivots['%s'] = graph.vs[labels['%s']][Himesis.Constants.GUID]
""" % (Himesis.to_non_RAM_attribute(self.vs[node][Himesis.Constants.META_MODEL]), label, self.vs[node][Himesis.Constants.MT_PIVOT_OUT], label))
        #TODO: This should be a TransformationLanguageSpecificException
        transformationCode.append("""
#===============================================================================
# Perform the post-action
#===============================================================================
try:
    self.action(lambda i: graph.vs[labels[i]], graph)
except Exception, e:
    raise Exception('An error has occurred while applying the post-action', e)""")
        
        # Delete nodes (and edges)
        transformationCode.append("""
#===============================================================================
# Finally, delete nodes (this will automatically delete the adjacent edges)
#===============================================================================
""")
        labels_to_delete = []
        for label in LHS_labels:
            if label not in RHS_labels:
                labels_to_delete.append(label)
        if len(labels_to_delete) > 0:
            transformationCode.append("""# %s
graph.delete_nodes(%s)
""" % (reduce(lambda l1,l2: l1 + ', ' + l2, map(lambda lbl: '%s%s' % (LHS_labels[lbl], lbl), labels_to_delete)),
       str(map(lambda lbl: 'labels["%s"]' % lbl, labels_to_delete)).replace("'", "")))
        
        # Save the code in the body of the execute method
        self.execute_body = ''.join(transformationCode)

