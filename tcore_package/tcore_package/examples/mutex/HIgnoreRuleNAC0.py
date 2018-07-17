

from core.himesis import Himesis, HimesisPreConditionPatternNAC
import cPickle as pickle
from uuid import UUID

class HIgnoreRuleNAC0(HimesisPreConditionPatternNAC):
    def __init__(self, LHS):
        """
        Creates the himesis graph representing the AToM3 model HIgnoreRuleNAC0.
        """
        # Create the himesis graph
        EDGE_LIST = [(1, 0), (0, 2)]
        
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HIgnoreRuleNAC0, self).__init__(name='HIgnoreRuleNAC0', num_nodes=3, edges=EDGE_LIST, LHS=LHS)

        # Set the graph attributes
        self["mm__"] = pickle.loads("""(lp1
S'MT_pre__Mutex'
p2
aS'MoTifRule'
p3
a.""")
        self["MT_constraint__"] = """#===============================================================================
# This code is executed after the nodes in the NAC have been matched.
# You can access a matched node labelled n by: PreNode('n').
# To access attribute x of node n, use: PreNode('n')['x'].
# The given constraint must evaluate to a boolean expression:
#    returning True forbids the rule from being applied,
#    returning False enables the rule to be applied.
#===============================================================================

return True
"""
        self["name"] = """"""
        self["GUID__"] = UUID('e7b125bc-601d-45cd-bd93-94bf2458403b')
        
        # Set the node attributes
        self.vs[0]["MT_subtypeMatching__"] = False
        self.vs[0]["MT_label__"] = """5"""
        self.vs[0]["MT_subtypes__"] = pickle.loads("""(lp1
.""")
        self.vs[0]["mm__"] = """MT_pre__held_by"""
        self.vs[0]["MT_dirty__"] = False
        self.vs[0]["GUID__"] = UUID('b5c13282-57af-43e8-9c0d-b2ba70fa3e80')
        self.vs[1]["MT_subtypeMatching__"] = False
        self.vs[1]["MT_label__"] = """4"""
        self.vs[1]["MT_subtypes__"] = pickle.loads("""(lp1
.""")
        self.vs[1]["mm__"] = """MT_pre__Resource"""
        self.vs[1]["MT_dirty__"] = False
        self.vs[1]["MT_pre__name"] = """
#===============================================================================
# This code is executed when evaluating if a node shall be matched by this rule.
# You can access the value of the current node's attribute value by: attr_value.
# You can access a matched node 'n' by: PreNode('n').
# To access attribute x of node n, use: PreNode('n')['x'].
# The given constraint must evaluate to a boolean expression.
#===============================================================================

return True
"""
        self.vs[1]["GUID__"] = UUID('a2180a79-1b82-4100-ae03-de9961620a9e')
        self.vs[2]["MT_subtypeMatching__"] = False
        self.vs[2]["MT_label__"] = """1"""
        self.vs[2]["MT_subtypes__"] = pickle.loads("""(lp1
.""")
        self.vs[2]["mm__"] = """MT_pre__Process"""
        self.vs[2]["MT_dirty__"] = False
        self.vs[2]["MT_pre__name"] = """
#===============================================================================
# This code is executed when evaluating if a node shall be matched by this rule.
# You can access the value of the current node's attribute value by: attr_value.
# You can access a matched node 'n' by: PreNode('n').
# To access attribute x of node n, use: PreNode('n')['x'].
# The given constraint must evaluate to a boolean expression.
#===============================================================================

return True
"""
        self.vs[2]["GUID__"] = UUID('736cb7ae-597e-4f29-8075-133e21668d5a')
        
        # Load the bridge between this NAC and its LHS
        from HIgnoreRuleNAC0Bridge import HIgnoreRuleNAC0Bridge
        self.bridge = HIgnoreRuleNAC0Bridge()

    def eval_name4(self, attr_value, PreNode, graph):
        
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
        # This code is executed after the nodes in the NAC have been matched.
        # You can access a matched node labelled n by: PreNode('n').
        # To access attribute x of node n, use: PreNode('n')['x'].
        # The given constraint must evaluate to a boolean expression:
        #    returning True forbids the rule from being applied,
        #    returning False enables the rule to be applied.
        #===============================================================================
        
        return True

        