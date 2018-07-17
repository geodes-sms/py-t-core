

from core.himesis import Himesis, HimesisPostConditionPattern
import cPickle as pickle

class HNewRuleRHS(HimesisPostConditionPattern):
    def __init__(self):
        """
        Creates the himesis graph representing the AToM3 model HNewRuleRHS.
        """
        # Create the himesis graph
        EDGE_LIST = [(2, 0), (0, 4), (4, 1), (1, 3)]
        
        super(HNewRuleRHS, self).__init__(name='HNewRuleRHS', num_nodes=5, edges=EDGE_LIST)
        self.is_compiled = True    # now this instance has been compiled

        # Set the graph attributes
        self["MT_action__"] = pickle.loads("""S"#===============================================================================@n# This code is executed after the rule has been applied.@n# You can access a node labelled n matched by this rule by: PostNode('n').@n# To access attribute x of node n, use: PostNode('n')['x'].@n#===============================================================================@n@npass@n"
p1
.""").replace("@n", "\n")
        self["name"] = pickle.loads("""S'HNewRuleRHS'
p1
.""")
        self["GUID__"] = pickle.loads("""ccopy_reg
_reconstructor
p1
(cuuid
UUID
p2
c__builtin__
object
p3
NtRp4
(dp5
S'int'
p6
L216252046786439829870692571573926113871L
sb.""")
        # Set the node attributes
        self.vs[0]["mm__"] = pickle.loads("""S'MT_post__next'
p1
.""")
        self.vs[0]["MT_label__"] = pickle.loads("""S'5'
.""")
        self.vs[0]["GUID__"] = pickle.loads("""ccopy_reg
_reconstructor
p1
(cuuid
UUID
p2
c__builtin__
object
p3
NtRp4
(dp5
S'int'
p6
L265398458179928414982637964388342547225L
sb.""")
        self.vs[1]["mm__"] = pickle.loads("""S'MT_post__next'
p1
.""")
        self.vs[1]["MT_label__"] = pickle.loads("""S'6'
.""")
        self.vs[1]["GUID__"] = pickle.loads("""ccopy_reg
_reconstructor
p1
(cuuid
UUID
p2
c__builtin__
object
p3
NtRp4
(dp5
S'int'
p6
L114621590887504245237000617794008652191L
sb.""")
        self.vs[2]["mm__"] = pickle.loads("""S'MT_post__Process'
p1
.""")
        self.vs[2]["MT_label__"] = pickle.loads("""S'1'
.""")
        self.vs[2]["MT_post__name"] = pickle.loads("""S"@n#===============================================================================@n# You can access the value of the current node's attribute value by: attr_value.@n# You can access a matched node labelled n by: PreNode('n').@n# To access attribute x of node n, use: PreNode('n')['x'].@n# Note that the attribute values are those before the match is rewritten.@n# The order in which this code is executed depends on the label value of the encapsulating node.@n# The given action must return the new value of the attribute.@n#===============================================================================@n@nreturn attr_value@n"
p1
.""").replace("@n", "\n")
        self.vs[2]["GUID__"] = pickle.loads("""ccopy_reg
_reconstructor
p1
(cuuid
UUID
p2
c__builtin__
object
p3
NtRp4
(dp5
S'int'
p6
L212607478986061461350152077805400419080L
sb.""")
        self.vs[3]["mm__"] = pickle.loads("""S'MT_post__Process'
p1
.""")
        self.vs[3]["MT_label__"] = pickle.loads("""S'2'
.""")
        self.vs[3]["MT_post__name"] = pickle.loads("""S"@n#===============================================================================@n# You can access the value of the current node's attribute value by: attr_value.@n# You can access a matched node labelled n by: PreNode('n').@n# To access attribute x of node n, use: PreNode('n')['x'].@n# Note that the attribute values are those before the match is rewritten.@n# The order in which this code is executed depends on the label value of the encapsulating node.@n# The given action must return the new value of the attribute.@n#===============================================================================@n@nreturn attr_value@n"
p1
.""").replace("@n", "\n")
        self.vs[3]["GUID__"] = pickle.loads("""ccopy_reg
_reconstructor
p1
(cuuid
UUID
p2
c__builtin__
object
p3
NtRp4
(dp5
S'int'
p6
L256358921611709246543309184649991082021L
sb.""")
        self.vs[4]["mm__"] = pickle.loads("""S'MT_post__Process'
p1
.""")
        self.vs[4]["MT_label__"] = pickle.loads("""S'4'
.""")
        self.vs[4]["MT_post__name"] = pickle.loads("""S"@n#===============================================================================@n# You can access the value of the current node's attribute value by: attr_value.@n# You can access a matched node labelled n by: PreNode('n').@n# To access attribute x of node n, use: PreNode('n')['x'].@n# Note that the attribute values are those before the match is rewritten.@n# The order in which this code is executed depends on the label value of the encapsulating node.@n# The given action must return the new value of the attribute.@n#===============================================================================@n@nvs = graph.vs.select(mm__ = 'Process')@nmaxId = -1@nfor v in vs:@n    if v['name']:@n    \tid = int(v['name'][1:])@n        if id > maxId:@n    \t    maxId = id@nreturn 'P' + str(maxId + 1)@n"
p1
.""").replace("@n", "\n")
        self.vs[4]["GUID__"] = pickle.loads("""ccopy_reg
_reconstructor
p1
(cuuid
UUID
p2
c__builtin__
object
p3
NtRp4
(dp5
S'int'
p6
L99004324448409785593819361867936230344L
sb.""")
        from HNewRuleLHS import HNewRuleLHS
        self.pre = HNewRuleLHS()
    
    def set_name4(self, attr_value, PreNode, graph):
        
        #===============================================================================
        # You can access the value of the current node's attribute value by: attr_value.
        # You can access a matched node labelled n by: PreNode('n').
        # To access attribute x of node n, use: PreNode('n')['x'].
        # Note that the attribute values are those before the match is rewritten.
        # The order in which this code is executed depends on the label value of the encapsulating node.
        # The given action must return the new value of the attribute.
        #===============================================================================
        
        vs = graph.vs.select(mm__ = 'Process')
        maxId = -1
        for v in vs:
            if v['name']:
            	id = int(v['name'][1:])
                if id > maxId:
            	    maxId = id
        return 'P' + str(maxId + 1)


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
        # MT_post__next5
        new_node = graph.add_node()
        labels[5] = new_node
        graph.vs[new_node][Himesis.Constants.META_MODEL] = 'next'
        # MT_post__next6
        new_node = graph.add_node()
        labels[6] = new_node
        graph.vs[new_node][Himesis.Constants.META_MODEL] = 'next'
        # MT_post__Process4
        new_node = graph.add_node()
        labels[4] = new_node
        graph.vs[new_node][Himesis.Constants.META_MODEL] = 'Process'
        try:
            graph.vs[new_node]['name'] = self.set_name4(None, lambda i: graph.vs[match[i]], graph)
        except Exception, e:
            raise Exception('An error has occurred while computing the value of the attribute \'name\'', e)
        
        #===============================================================================
        # Create new edges
        #===============================================================================
        # MT_post__next5 -> MT_post__Process4
        graph.add_edges((labels[5], labels[4]))
        # MT_post__Process4 -> MT_post__next6
        graph.add_edges((labels[4], labels[6]))
        # MT_post__Process1 -> MT_post__next5
        graph.add_edges((labels[1], labels[5]))
        # MT_post__next6 -> MT_post__Process2
        graph.add_edges((labels[6], labels[2]))
        
        #===============================================================================
        # Delete nodes (this will automatically delete the adjacent edges)
        #===============================================================================
        # MT_pre__next3
        graph.delete_nodes([labels[3]])
        
        #===============================================================================
        # Set the output pivots
        #===============================================================================
        
        #===============================================================================
        # Finally, perform the post-action
        #===============================================================================
        try:
            self.action(lambda i: graph.vs[labels[i]], graph)
        except Exception, e:
            raise Exception('An error has occurred while applying the post-action', e)
    
        