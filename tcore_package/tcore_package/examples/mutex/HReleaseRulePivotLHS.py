

from core.himesis import Himesis, HimesisPreConditionPatternLHS
import cPickle as pickle

class HReleaseRulePivotLHS(HimesisPreConditionPatternLHS):
    def __init__(self):
        """
        Creates the himesis graph representing the AToM3 model HReleaseRulePivotLHS.
        """
        # Create the himesis graph
        EDGE_LIST = [(1, 0), (0, 2)]
        
        super(HReleaseRulePivotLHS, self).__init__(name='HReleaseRulePivotLHS', num_nodes=3, edges=EDGE_LIST)
        self.is_compiled = True    # now this instance has been compiled

        # Set the graph attributes
        self["mm__"] = pickle.loads("""(lp1
S'MT_pre__Mutex'
p2
aS'MoTifRule'
p3
a.""")
        self["MT_constraint__"] = pickle.loads("""S"#===============================================================================@n# This code is executed after the nodes in the LHS have been matched.@n# You can access a matched node labelled n by: PreNode('n').@n# To access attribute x of node n, use: PreNode('n')['x'].@n# The given constraint must evaluate to a boolean expression:@n#    returning True enables the rule to be applied,@n#    returning False forbids the rule from being applied.@n#===============================================================================@n@nreturn True@n"
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
L110771575284051222755816592876061876048L
sb.""")
        # Set the node attributes
        self.vs[0]["MT_subtypeMatching__"] = pickle.loads("""I00
.""")
        self.vs[0]["MT_label__"] = pickle.loads("""S'3'
.""")
        self.vs[0]["MT_subtypes__"] = pickle.loads("""(lp1
.""")
        self.vs[0]["mm__"] = pickle.loads("""S'MT_pre__held_by'
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
L75521414981770462599036796701584635887L
sb.""")
        self.vs[1]["MT_subtypeMatching__"] = pickle.loads("""I00
.""")
        self.vs[1]["MT_label__"] = pickle.loads("""S'2'
.""")
        self.vs[1]["MT_subtypes__"] = pickle.loads("""(lp1
.""")
        self.vs[1]["mm__"] = pickle.loads("""S'MT_pre__Resource'
p1
.""")
        self.vs[1]["MT_dirty__"] = pickle.loads("""I00
.""")
        self.vs[1]["MT_pre__name"] = pickle.loads("""S"@n#===============================================================================@n# This code is executed when evaluating if a node shall be matched by this rule.@n# You can access the value of the current node's attribute value by: attr_value.@n# You can access a matched node 'n' by: PreNode('n').@n# To access attribute x of node n, use: PreNode('n')['x'].@n# The given constraint must evaluate to a boolean expression.@n#===============================================================================@n@nreturn True@n"
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
L278979674152276671616899428704625047456L
sb.""")
        self.vs[2]["MT_subtypeMatching__"] = pickle.loads("""I00
.""")
        self.vs[2]["MT_pivotIn__"] = pickle.loads("""S'p'
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
L203709663595164370087872903730417269772L
sb.""")
        
        # Load the NACs
        from HReleaseRulePivotNAC0 import HReleaseRulePivotNAC0
        self.NACs = [HReleaseRulePivotNAC0(LHS=self)]

    def eval_name2(self, attr_value, PreNode, graph):
        
        #===============================================================================
        # This code is executed when evaluating if a node shall be matched by this rule.
        # You can access the value of the current node's attribute value by: attr_value.
        # You can access a matched node 'n' by: PreNode('n').
        # To access attribute x of node n, use: PreNode('n')['x'].
        # The given constraint must evaluate to a boolean expression.
        #===============================================================================
        
        return True


    def eval_name1(self, attr_value, PreNode, graph):
        
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

        