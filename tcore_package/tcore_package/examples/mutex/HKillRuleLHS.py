

from core.himesis import Himesis, HimesisPreConditionPatternLHS
import cPickle as pickle

class HKillRuleLHS(HimesisPreConditionPatternLHS):
    def __init__(self):
        """
        Creates the himesis graph representing the AToM3 model HKillRuleLHS.
        """
        # Create the himesis graph
        EDGE_LIST = [(2, 0), (0, 3), (3, 1), (1, 4)]
        
        super(HKillRuleLHS, self).__init__(name='HKillRuleLHS', num_nodes=5, edges=EDGE_LIST)
        self.is_compiled = True    # now this instance has been compiled

        # Set the graph attributes
        self["MT_constraint__"] = pickle.loads("""S"#===============================================================================@n# This code is executed after the nodes in the LHS have been matched.@n# You can access a matched node labelled n by: PreNode('n').@n# To access attribute x of node n, use: PreNode('n')['x'].@n# The given constraint must evaluate to a boolean expression:@n#    returning True enables the rule to be applied,@n#    returning False forbids the rule from being applied.@n#===============================================================================@n@nreturn True@n"
p1
.""").replace("@n", "\n")
        self["name"] = pickle.loads("""S'HKillRuleLHS'
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
L18442321865415244356622957945051150877L
sb.""")
        # Set the node attributes
        self.vs[0]["MT_subtypeMatching__"] = pickle.loads("""I00
.""")
        self.vs[0]["MT_label__"] = pickle.loads("""S'4'
.""")
        self.vs[0]["MT_subtypes__"] = pickle.loads("""(lp1
.""")
        self.vs[0]["mm__"] = pickle.loads("""S'MT_pre__next'
p1
.""")
        self.vs[0]["MT_dirty__"] = pickle.loads("""I00
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
L30273376065343805843958472981264470130L
sb.""")
        self.vs[1]["MT_subtypeMatching__"] = pickle.loads("""I00
.""")
        self.vs[1]["MT_label__"] = pickle.loads("""S'5'
.""")
        self.vs[1]["MT_subtypes__"] = pickle.loads("""(lp1
.""")
        self.vs[1]["mm__"] = pickle.loads("""S'MT_pre__next'
p1
.""")
        self.vs[1]["MT_dirty__"] = pickle.loads("""I00
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
L328554853358455331346205911493797456672L
sb.""")
        self.vs[2]["MT_subtypeMatching__"] = pickle.loads("""I00
.""")
        self.vs[2]["MT_label__"] = pickle.loads("""S'1'
.""")
        self.vs[2]["MT_subtypes__"] = pickle.loads("""(lp1
.""")
        self.vs[2]["mm__"] = pickle.loads("""S'MT_pre__Process'
p1
.""")
        self.vs[2]["MT_dirty__"] = pickle.loads("""I00
.""")
        self.vs[2]["MT_pre__name"] = pickle.loads("""S"@n#===============================================================================@n# This code is executed when evaluating if a node shall be matched by this rule.@n# You can access the value of the current node's attribute value by: attr_value.@n# You can access a matched node 'n' by: PreNode('n').@n# To access attribute x of node n, use: PreNode('n')['x'].@n# The given constraint must evaluate to a boolean expression.@n#===============================================================================@n@nreturn True@n"
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
L165009034650108222987415177235648016564L
sb.""")
        self.vs[3]["MT_subtypeMatching__"] = pickle.loads("""I00
.""")
        self.vs[3]["MT_label__"] = pickle.loads("""S'2'
.""")
        self.vs[3]["MT_subtypes__"] = pickle.loads("""(lp1
.""")
        self.vs[3]["mm__"] = pickle.loads("""S'MT_pre__Process'
p1
.""")
        self.vs[3]["MT_dirty__"] = pickle.loads("""I00
.""")
        self.vs[3]["MT_pre__name"] = pickle.loads("""S"@n#===============================================================================@n# This code is executed when evaluating if a node shall be matched by this rule.@n# You can access the value of the current node's attribute value by: attr_value.@n# You can access a matched node 'n' by: PreNode('n').@n# To access attribute x of node n, use: PreNode('n')['x'].@n# The given constraint must evaluate to a boolean expression.@n#===============================================================================@n@nreturn True@n"
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
L73980624501117965779453092797674415786L
sb.""")
        self.vs[4]["MT_subtypeMatching__"] = pickle.loads("""I00
.""")
        self.vs[4]["MT_label__"] = pickle.loads("""S'3'
.""")
        self.vs[4]["MT_subtypes__"] = pickle.loads("""(lp1
.""")
        self.vs[4]["mm__"] = pickle.loads("""S'MT_pre__Process'
p1
.""")
        self.vs[4]["MT_dirty__"] = pickle.loads("""I00
.""")
        self.vs[4]["MT_pre__name"] = pickle.loads("""S"@n#===============================================================================@n# This code is executed when evaluating if a node shall be matched by this rule.@n# You can access the value of the current node's attribute value by: attr_value.@n# You can access a matched node 'n' by: PreNode('n').@n# To access attribute x of node n, use: PreNode('n')['x'].@n# The given constraint must evaluate to a boolean expression.@n#===============================================================================@n@nreturn True@n"
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
L292064108001480532935557560315945411793L
sb.""")
    def eval_name1(self, attr_value, PreNode, graph):
        
        #===============================================================================
        # This code is executed when evaluating if a node shall be matched by this rule.
        # You can access the value of the current node's attribute value by: attr_value.
        # You can access a matched node 'n' by: PreNode('n').
        # To access attribute x of node n, use: PreNode('n')['x'].
        # The given constraint must evaluate to a boolean expression.
        #===============================================================================
        
        return True


    def eval_name2(self, attr_value, PreNode, graph):
        
        #===============================================================================
        # This code is executed when evaluating if a node shall be matched by this rule.
        # You can access the value of the current node's attribute value by: attr_value.
        # You can access a matched node 'n' by: PreNode('n').
        # To access attribute x of node n, use: PreNode('n')['x'].
        # The given constraint must evaluate to a boolean expression.
        #===============================================================================
        
        return True


    def eval_name3(self, attr_value, PreNode, graph):
        
        #===============================================================================
        # This code is executed when evaluating if a node shall be matched by this rule.
        # You can access the value of the current node's attribute value by: attr_value.
        # You can access a matched node 'n' by: PreNode('n').
        # To access attribute x of node n, use: PreNode('n')['x'].
        # The given constraint must evaluate to a boolean expression.
        #===============================================================================
        
        return True


    def constraint(self, PreNode, graph):
        """
            Executable constraint code. 
            @param PreNode: Function taking an integer as parameter
                            and returns the node corresponding to that label.
        """
        #===============================================================================
        # This code is executed after the nodes in the LHS have been matched.
        # You can access a matched node labelled n by: PreNode('n').
        # To access attribute x of node n, use: PreNode('n')['x'].
        # The given constraint must evaluate to a boolean expression:
        #    returning True enables the rule to be applied,
        #    returning False forbids the rule from being applied.
        #===============================================================================
        
        return True

        