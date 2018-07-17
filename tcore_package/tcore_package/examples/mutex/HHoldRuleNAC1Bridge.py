

from core.himesis import Himesis, HimesisPreConditionPattern
import cPickle as pickle

class HHoldRuleNAC1Bridge(HimesisPreConditionPattern):
    def __init__(self):
        """
        Creates the himesis graph representing the AToM3 model HHoldRuleNAC1Bridge.
        """
        # Create the himesis graph
        EDGE_LIST = []
        
        super(HHoldRuleNAC1Bridge, self).__init__(name='HHoldRuleNAC1Bridge', num_nodes=1, edges=EDGE_LIST)
        self.is_compiled = True    # now this instance has been compiled

        # Set the graph attributes
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
L91887268072828218732508076701595401833L
sb.""")
        # Set the node attributes
        self.vs[0]["MT_subtypeMatching__"] = pickle.loads("""I00
.""")
        self.vs[0]["MT_label__"] = pickle.loads("""S'2'
.""")
        self.vs[0]["mm__"] = pickle.loads("""S'MT_pre__Resource'
p1
.""")
        self.vs[0]["MT_subtypes__"] = pickle.loads("""(lp1
.""")
        self.vs[0]["MT_dirty__"] = pickle.loads("""I00
.""")
        self.vs[0]["MT_pre__name"] = pickle.loads("""S'from HHoldRuleNAC1 import HHoldRuleNAC1@nfrom HHoldRuleLHS import HHoldRuleLHS@nreturn HHoldRuleNAC1().eval_name2(attr_value, PreNode) and HHoldRuleLHS().eval_name2(attr_value, PreNode)'
p1
.""").replace("@n", "\n")
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
L226802655720759481614389774357601028373L
sb.""")
    def eval_name2(self, attr_value, PreNode, graph):
        from HHoldRuleNAC1 import HHoldRuleNAC1
        from HHoldRuleLHS import HHoldRuleLHS
        return HHoldRuleNAC1().eval_name2(attr_value, PreNode) and HHoldRuleLHS().eval_name2(attr_value, PreNode)


    def constraint(self, PreNode, graph):
        """
            Executable constraint code. 
            @param PreNode: Function taking an integer as parameter
                            and returns the node corresponding to that label.
        """
        return True

        