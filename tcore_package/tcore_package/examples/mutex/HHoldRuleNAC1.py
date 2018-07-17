

from core.himesis import Himesis, HimesisPreConditionPatternNAC
import cPickle as pickle

class HHoldRuleNAC1(HimesisPreConditionPatternNAC):
    def __init__(self, LHS):
        """
        Creates the himesis graph representing the AToM3 model HHoldRuleNAC1.
        """
        # Create the himesis graph
        EDGE_LIST = [(1, 0)]
        
        super(HHoldRuleNAC1, self).__init__(name='HHoldRuleNAC1', num_nodes=2, edges=EDGE_LIST, LHS=LHS)
        self.is_compiled = True    # now this instance has been compiled

        # Set the graph attributes
        self["mm__"] = pickle.loads("""(lp1
S'MT_pre__Mutex'
p2
aS'MoTifRule'
p3
a.""")
        self["MT_constraint__"] = pickle.loads("""S"#===============================================================================@n# This code is executed after the nodes in the NAC have been matched.@n# You can access a matched node labelled n by: PreNode('n').@n# To access attribute x of node n, use: PreNode('n')['x'].@n# The given constraint must evaluate to a boolean expression:@n#    returning True forbids the rule from being applied,@n#    returning False enables the rule to be applied.@n#===============================================================================@n@nreturn True@n"
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
L160179377637520873875861494974975545758L
sb.""")
        # Set the node attributes
        self.vs[0]["MT_subtypeMatching__"] = pickle.loads("""I00
.""")
        self.vs[0]["MT_label__"] = pickle.loads("""S'4'
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
L125465582863726898435674588919499575544L
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
L226802655720759481614389774357601028373L
sb.""")
        
        # Load the bridge between this NAC and its LHS
        from HHoldRuleNAC1Bridge import HHoldRuleNAC1Bridge
        self.bridge = HHoldRuleNAC1Bridge()

    def eval_name2(self, attr_value, PreNode, graph):
        
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
        # This code is executed after the nodes in the NAC have been matched.
        # You can access a matched node labelled n by: PreNode('n').
        # To access attribute x of node n, use: PreNode('n')['x'].
        # The given constraint must evaluate to a boolean expression:
        #    returning True forbids the rule from being applied,
        #    returning False enables the rule to be applied.
        #===============================================================================
        
        return True

        