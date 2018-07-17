

from core.himesis import Himesis, HimesisPostConditionPattern
import cPickle as pickle
from uuid import UUID

class HTopClass2TableRHS(HimesisPostConditionPattern):
    def __init__(self):
        """
        Creates the himesis graph representing the AToM3 model HTopClass2TableRHS.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HTopClass2TableRHS, self).__init__(name='HTopClass2TableRHS', num_nodes=5, edges=[])
        
        # Add the edges
        self.add_edges([(4, 0), (3, 1), (2, 3), (2, 4)])
        # Set the graph attributes
        self["mm__"] = pickle.loads("""(lp1
S'MT_post__CD2RDBMSMetaModel'
p2
aS'MoTifRule'
p3
a.""")
        self["MT_action__"] = """#===============================================================================
# This code is executed after the rule has been applied.
# You can access a node labelled n matched by this rule by: PostNode('n').
# To access attribute x of node n, use: PostNode('n')['x'].
#===============================================================================

pass
"""
        self["name"] = """"""
        self["GUID__"] = UUID('772d2291-465f-4976-ba63-96c042623685')
        
        # Set the node attributes
        self.vs[0]["mm__"] = """MT_post__Table"""
        self.vs[0]["MT_label__"] = """2"""
        self.vs[0]["MT_post__name"] = pickle.loads("""V\u000a#===============================================================================\u000a# You can access the value of the current node's attribute value by: attr_value.\u000a# If the current node shall be created you MUST initialize it here!\u000a# You can access a node labelled n by: PreNode('n').\u000a# To access attribute x of node n, use: PreNode('n')['x'].\u000a# Note that the attribute values are those before the match is rewritten.\u000a# The order in which this code is executed depends on the label value of the encapsulating node.\u000a# The given action must return the new value of the attribute.\u000a#===============================================================================\u000a\u000areturn PreNode('1')['name']\u000a
p1
.""")
        self.vs[0]["GUID__"] = UUID('8605e1e5-bf8e-4d72-8747-eb7ef1d953fc')
        self.vs[1]["mm__"] = """MT_post__Clazz"""
        self.vs[1]["MT_label__"] = """1"""
        self.vs[1]["MT_post__is_persistent"] = """
#===============================================================================
# You can access the value of the current node's attribute value by: attr_value.
# If the current node shall be created you MUST initialize it here!
# You can access a node labelled n by: PreNode('n').
# To access attribute x of node n, use: PreNode('n')['x'].
# Note that the attribute values are those before the match is rewritten.
# The order in which this code is executed depends on the label value of the encapsulating node.
# The given action must return the new value of the attribute.
#===============================================================================

return attr_value
"""
        self.vs[1]["MT_post__name"] = pickle.loads("""V\u000a#===============================================================================\u000a# You can access the value of the current node's attribute value by: attr_value.\u000a# If the current node shall be created you MUST initialize it here!\u000a# You can access a node labelled n by: PreNode('n').\u000a# To access attribute x of node n, use: PreNode('n')['x'].\u000a# Note that the attribute values are those before the match is rewritten.\u000a# The order in which this code is executed depends on the label value of the encapsulating node.\u000a# The given action must return the new value of the attribute.\u000a#===============================================================================\u000a\u000areturn attr_value\u000a
p1
.""")
        self.vs[1]["GUID__"] = UUID('52241dfa-a743-4205-b401-b9ad7b5bf60e')
        self.vs[2]["mm__"] = """MT_post__GenericNode"""
        self.vs[2]["MT_label__"] = """3"""
        self.vs[2]["GUID__"] = UUID('c382757d-ccb2-4df3-ac75-206bf005571c')
        self.vs[3]["mm__"] = """MT_post__GenericEdge"""
        self.vs[3]["MT_label__"] = """4"""
        self.vs[3]["GUID__"] = UUID('ca02ea46-72dc-4bb5-8efc-636c5cc732e4')
        self.vs[4]["mm__"] = """MT_post__GenericEdge"""
        self.vs[4]["MT_label__"] = """5"""
        self.vs[4]["GUID__"] = UUID('2625d00b-5065-4d65-b02f-e697104fee03')

        from HTopClass2TableLHS import HTopClass2TableLHS
        self.pre = HTopClass2TableLHS()
    
    def set_name2(self, attr_value, PreNode, graph):
        
        #===============================================================================
        # You can access the value of the current node's attribute value by: attr_value.
        # If the current node shall be created you MUST initialize it here!
        # You can access a node labelled n by: PreNode('n').
        # To access attribute x of node n, use: PreNode('n')['x'].
        # Note that the attribute values are those before the match is rewritten.
        # The order in which this code is executed depends on the label value of the encapsulating node.
        # The given action must return the new value of the attribute.
        #===============================================================================
        
        return PreNode('1')['name']


    def action(self, PostNode, graph):
        """
            Executable constraint code. 
            @param PostNode: Function taking an integer as parameter
                             and returns the node corresponding to that label.
        """
        #===============================================================================
        # This code is executed after the rule has been applied.
        # You can access a node labelled n matched by this rule by: PostNode('n').
        # To access attribute x of node n, use: PostNode('n')['x'].
        #===============================================================================
        
        pass

    def execute(self, packet, match):
        """
            Transforms the current match of the packet according to the rule %s.
            Pivots are also assigned, if any.
            @param packet: The input packet.
            @param match: The match to rewrite.
        """
        graph = packet.graph
        
        # Build a dictionary {label: node index} mapping each label of the pattern to a node in the graph to rewrite.
        # Because of the uniqueness property of labels in a rule, we can store all LHS labels
        # and subsequently add the labels corresponding to the nodes to be created.
        labels = match.copy()
        
        #===============================================================================
        # Update attribute values
        #===============================================================================
        
        #===============================================================================
        # Create new nodes
        #===============================================================================
        # Table2
        new_node = graph.add_node()
        labels['2'] = new_node
        graph.vs[new_node][Himesis.Constants.META_MODEL] = 'Table'
        try:
            graph.vs[new_node]['name'] = self.set_name2(None, lambda i: graph.vs[match[i]], graph)
        except Exception, e:
            raise Exception('An error has occurred while computing the value of the attribute \'name\'', e)
        # GenericEdge4
        new_node = graph.add_node()
        labels['4'] = new_node
        graph.vs[new_node][Himesis.Constants.META_MODEL] = 'GenericEdge'
        # GenericEdge5
        new_node = graph.add_node()
        labels['5'] = new_node
        graph.vs[new_node][Himesis.Constants.META_MODEL] = 'GenericEdge'
        # GenericNode3
        new_node = graph.add_node()
        labels['3'] = new_node
        graph.vs[new_node][Himesis.Constants.META_MODEL] = 'GenericNode'
        
        #===============================================================================
        # Create new edges
        #===============================================================================
        # GenericEdge5 -> Table2
        graph.add_edges((labels['5'], labels['2']))
        # GenericNode3 -> GenericEdge4
        graph.add_edges((labels['3'], labels['4']))
        # GenericNode3 -> GenericEdge5
        graph.add_edges((labels['3'], labels['5']))
        # GenericEdge4 -> Clazz1
        graph.add_edges((labels['4'], labels['1']))
        
        #===============================================================================
        # Set the output pivots
        #===============================================================================
        
        #===============================================================================
        # Perform the post-action
        #===============================================================================
        try:
            self.action(lambda i: graph.vs[labels[i]], graph)
        except Exception, e:
            raise Exception('An error has occurred while applying the post-action', e)
        #===============================================================================
        # Finally, delete nodes (this will automatically delete the adjacent edges)
        #===============================================================================
    
