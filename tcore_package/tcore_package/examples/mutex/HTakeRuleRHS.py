

from core.himesis import Himesis, HimesisPostConditionPattern
import cPickle as pickle

class HTakeRuleRHS(HimesisPostConditionPattern):
    def __init__(self):
        """
        Creates the himesis graph representing the AToM3 model HTakeRuleRHS.
        """
        # Create the himesis graph
        EDGE_LIST = [(2, 0), (0, 1)]
        
        super(HTakeRuleRHS, self).__init__(name='HTakeRuleRHS', num_nodes=3, edges=EDGE_LIST)
        self.is_compiled = True    # now this instance has been compiled

        # Set the graph attributes
        self["mm__"] = pickle.loads("""(lp1
S'MT_post__Mutex'
p2
aS'MoTifRule'
p3
a.""")
        self["MT_action__"] = pickle.loads("""S"#===============================================================================@n# This code is executed after the rule has been applied.@n# You can access a node labelled n matched by this rule by: PostNode('n').@n# To access attribute x of node n, use: PostNode('n')['x'].@n#===============================================================================@n@npass@n"
p1
.""").replace("@n", "\n")
        self["name"] = pickle.loads("""S''
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
L279045862316403260946314971313193102995L
sb.""")
        # Set the node attributes
        self.vs[0]["mm__"] = pickle.loads("""S'MT_post__held_by'
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
L158350772038903817286361436259146439733L
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
L324506222296820921592298491159903208905L
sb.""")
        self.vs[2]["mm__"] = pickle.loads("""S'MT_post__Resource'
p1
.""")
        self.vs[2]["MT_label__"] = pickle.loads("""S'2'
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
L230036789737900129212649521188190682802L
sb.""")
        from HTakeRuleLHS import HTakeRuleLHS
        self.pre = HTakeRuleLHS()
    
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
        # MT_post__held_by5
        new_node = graph.add_node()
        labels[5] = new_node
        graph.vs[new_node][Himesis.Constants.META_MODEL] = 'held_by'
        
        #===============================================================================
        # Create new edges
        #===============================================================================
        # MT_post__Resource2 -> MT_post__held_by5
        graph.add_edges((labels[2], labels[5]))
        # MT_post__held_by5 -> MT_post__Process1
        graph.add_edges((labels[5], labels[1]))
        
        #===============================================================================
        # Delete nodes (this will automatically delete the adjacent edges)
        #===============================================================================
        # MT_pre__toke3, MT_pre__request4
        graph.delete_nodes([labels[3], labels[4]])
        
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
    
        