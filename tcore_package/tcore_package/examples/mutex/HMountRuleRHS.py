

from core.himesis import Himesis, HimesisPostConditionPattern
import cPickle as pickle

class HMountRuleRHS(HimesisPostConditionPattern):
    def __init__(self):
        """
        Creates the himesis graph representing the AToM3 model HMountRuleRHS.
        """
        # Create the himesis graph
        EDGE_LIST = [(2, 0), (0, 1)]
        
        super(HMountRuleRHS, self).__init__(name='HMountRuleRHS', num_nodes=3, edges=EDGE_LIST)
        self.is_compiled = True    # now this instance has been compiled

        # Set the graph attributes
        self["MT_action__"] = pickle.loads("""S"#===============================================================================@n# This code is executed after the rule has been applied.@n# You can access a node labelled n matched by this rule by: PostNode('n').@n# To access attribute x of node n, use: PostNode('n')['x'].@n#===============================================================================@n@npass@n"
p1
.""").replace("@n", "\n")
        self["name"] = pickle.loads("""S'HMountRuleRHS'
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
L204181169989380058006610160678131469781L
sb.""")
        # Set the node attributes
        self.vs[0]["mm__"] = pickle.loads("""S'MT_post__toke'
p1
.""")
        self.vs[0]["MT_label__"] = pickle.loads("""S'3'
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
L194618085095321478715411846101328385378L
sb.""")
        self.vs[1]["mm__"] = pickle.loads("""S'MT_post__Process'
p1
.""")
        self.vs[1]["MT_label__"] = pickle.loads("""S'1'
.""")
        self.vs[1]["MT_post__name"] = pickle.loads("""S"@n#===============================================================================@n# You can access the value of the current node's attribute value by: attr_value.@n# You can access a matched node labelled n by: PreNode('n').@n# To access attribute x of node n, use: PreNode('n')['x'].@n# Note that the attribute values are those before the match is rewritten.@n# The order in which this code is executed depends on the label value of the encapsulating node.@n# The given action must return the new value of the attribute.@n#===============================================================================@n@nreturn attr_value@n"
p1
.""").replace("@n", "\n")
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
L146735793891330158366608615282295876673L
sb.""")
        self.vs[2]["mm__"] = pickle.loads("""S'MT_post__Resource'
p1
.""")
        self.vs[2]["MT_label__"] = pickle.loads("""S'2'
.""")
        self.vs[2]["MT_post__name"] = pickle.loads("""V\u000a#===============================================================================\u000a# You can access the value of the current node's attribute value by: attr_value.\u000a# You can access a matched node labelled n by: PreNode('n').\u000a# To access attribute x of node n, use: PreNode('n')['x'].\u000a# Note that the attribute values are those before the match is rewritten.\u000a# The order in which this code is executed depends on the label value of the encapsulating node.\u000a# The given action must return the new value of the attribute.\u000a#===============================================================================\u000a\u000avs = graph.vs.select(mm__ = 'Resource')\u000amaxId = -1\u000afor v in vs:\u000a    if v['name']:\u000a    	id = int(v['name'][1:])\u000a        if id > maxId:\u000a    	    maxId = id\u000areturn 'R' + str(maxId + 1)\u000a
p1
.""")
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
L179332148605988684518009168156561057543L
sb.""")
        from HMountRuleLHS import HMountRuleLHS
        self.pre = HMountRuleLHS()
    
    def set_name2(self, attr_value, PreNode, graph):
        
        #===============================================================================
        # You can access the value of the current node's attribute value by: attr_value.
        # You can access a matched node labelled n by: PreNode('n').
        # To access attribute x of node n, use: PreNode('n')['x'].
        # Note that the attribute values are those before the match is rewritten.
        # The order in which this code is executed depends on the label value of the encapsulating node.
        # The given action must return the new value of the attribute.
        #===============================================================================
        
        vs = graph.vs.select(mm__ = 'Resource')
        maxId = -1
        for v in vs:
            if v['name']:
            	id = int(v['name'][1:])
                if id > maxId:
            	    maxId = id
        return 'R' + str(maxId + 1)


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
        # MT_post__toke3
        new_node = graph.add_node()
        labels[3] = new_node
        graph.vs[new_node][Himesis.Constants.META_MODEL] = 'toke'
        # MT_post__Resource2
        new_node = graph.add_node()
        labels[2] = new_node
        graph.vs[new_node][Himesis.Constants.META_MODEL] = 'Resource'
        try:
            graph.vs[new_node]['name'] = self.set_name2(None, lambda i: graph.vs[match[i]], graph)
        except Exception, e:
            raise Exception('An error has occurred while computing the value of the attribute \'name\'', e)
        
        #===============================================================================
        # Create new edges
        #===============================================================================
        # MT_post__Resource2 -> MT_post__toke3
        graph.add_edges((labels[2], labels[3]))
        # MT_post__toke3 -> MT_post__Process1
        graph.add_edges((labels[3], labels[1]))
        
        #===============================================================================
        # Delete nodes (this will automatically delete the adjacent edges)
        #===============================================================================
        
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
    
        