

from core.himesis import Himesis, HimesisPostConditionPattern
import cPickle as pickle

class HReleaseStarRuleRHS(HimesisPostConditionPattern):
    def __init__(self):
        """
        Creates the himesis graph representing the AToM3 model HReleaseStarRuleRHS.
        """
        # Create the himesis graph
        EDGE_LIST = [(3, 0), (0, 6), (4, 1), (1, 6), (2, 3), (5, 2)]
        
        super(HReleaseStarRuleRHS, self).__init__(name='HReleaseStarRuleRHS', num_nodes=7, edges=EDGE_LIST)
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
L275342879871712987182831716975335400395L
sb.""")
        # Set the node attributes
        self.vs[0]["mm__"] = pickle.loads("""S'MT_post__release'
p1
.""")
        self.vs[0]["MT_label__"] = pickle.loads("""S'8'
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
L127660524158242123192194902481588065043L
sb.""")
        self.vs[1]["mm__"] = pickle.loads("""S'MT_post__held_by'
p1
.""")
        self.vs[1]["MT_label__"] = pickle.loads("""S'7'
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
L172463930727310080946475282605668615304L
sb.""")
        self.vs[2]["mm__"] = pickle.loads("""S'MT_post__request'
p1
.""")
        self.vs[2]["MT_label__"] = pickle.loads("""S'5'
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
L271861368933388930861877912992458843782L
sb.""")
        self.vs[3]["mm__"] = pickle.loads("""S'MT_post__Resource'
p1
.""")
        self.vs[3]["MT_label__"] = pickle.loads("""S'3'
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
L37667417383731107038707424221284694450L
sb.""")
        self.vs[4]["mm__"] = pickle.loads("""S'MT_post__Resource'
p1
.""")
        self.vs[4]["MT_label__"] = pickle.loads("""S'4'
.""")
        self.vs[4]["MT_post__name"] = pickle.loads("""S"@n#===============================================================================@n# You can access the value of the current node's attribute value by: attr_value.@n# You can access a matched node labelled n by: PreNode('n').@n# To access attribute x of node n, use: PreNode('n')['x'].@n# Note that the attribute values are those before the match is rewritten.@n# The order in which this code is executed depends on the label value of the encapsulating node.@n# The given action must return the new value of the attribute.@n#===============================================================================@n@nreturn attr_value@n"
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
L14058129745318233217905725061677395409L
sb.""")
        self.vs[5]["mm__"] = pickle.loads("""S'MT_post__Process'
p1
.""")
        self.vs[5]["MT_label__"] = pickle.loads("""S'1'
.""")
        self.vs[5]["MT_post__name"] = pickle.loads("""S"@n#===============================================================================@n# You can access the value of the current node's attribute value by: attr_value.@n# You can access a matched node labelled n by: PreNode('n').@n# To access attribute x of node n, use: PreNode('n')['x'].@n# Note that the attribute values are those before the match is rewritten.@n# The order in which this code is executed depends on the label value of the encapsulating node.@n# The given action must return the new value of the attribute.@n#===============================================================================@n@nreturn attr_value@n"
p1
.""").replace("@n", "\n")
        self.vs[5]["GUID__"] = pickle.loads("""ccopy_reg
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
L45412691984527298822013851144206475597L
sb.""")
        self.vs[6]["mm__"] = pickle.loads("""S'MT_post__Process'
p1
.""")
        self.vs[6]["MT_label__"] = pickle.loads("""S'2'
.""")
        self.vs[6]["MT_post__name"] = pickle.loads("""S"@n#===============================================================================@n# You can access the value of the current node's attribute value by: attr_value.@n# You can access a matched node labelled n by: PreNode('n').@n# To access attribute x of node n, use: PreNode('n')['x'].@n# Note that the attribute values are those before the match is rewritten.@n# The order in which this code is executed depends on the label value of the encapsulating node.@n# The given action must return the new value of the attribute.@n#===============================================================================@n@nreturn attr_value@n"
p1
.""").replace("@n", "\n")
        self.vs[6]["GUID__"] = pickle.loads("""ccopy_reg
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
L59675172891408720859339814351054246416L
sb.""")
        from HReleaseStarRuleLHS import HReleaseStarRuleLHS
        self.pre = HReleaseStarRuleLHS()
    
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
        # MT_post__release8
        new_node = graph.add_node()
        labels[8] = new_node
        graph.vs[new_node][Himesis.Constants.META_MODEL] = 'release'
        
        #===============================================================================
        # Create new edges
        #===============================================================================
        # MT_post__Resource3 -> MT_post__release8
        graph.add_edges((labels[3], labels[8]))
        # MT_post__release8 -> MT_post__Process2
        graph.add_edges((labels[8], labels[2]))
        
        #===============================================================================
        # Delete nodes (this will automatically delete the adjacent edges)
        #===============================================================================
        # MT_pre__held_by6
        graph.delete_nodes([labels[6]])
        
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
    
        