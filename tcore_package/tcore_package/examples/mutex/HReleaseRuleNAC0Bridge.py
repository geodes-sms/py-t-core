

from core.himesis import Himesis, HimesisPreConditionPattern
import cPickle as pickle

class HReleaseRuleNAC0Bridge(HimesisPreConditionPattern):
    def __init__(self):
        """
        Creates the himesis graph representing the AToM3 model HReleaseRuleNAC0Bridge.
        """
        # Create the himesis graph
        EDGE_LIST = []
        
        super(HReleaseRuleNAC0Bridge, self).__init__(name='HReleaseRuleNAC0Bridge', num_nodes=1, edges=EDGE_LIST)
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
L190412927260092338697445483992440745833L
sb.""")
        # Set the node attributes
        self.vs[0]["MT_subtypeMatching__"] = pickle.loads("""I00
.""")
        self.vs[0]["MT_label__"] = pickle.loads("""S'1'
.""")
        self.vs[0]["mm__"] = pickle.loads("""S'MT_pre__Process'
p1
.""")
        self.vs[0]["MT_subtypes__"] = pickle.loads("""(lp1
.""")
        self.vs[0]["MT_pre__name"] = pickle.loads("""S'from HReleaseRuleNAC0 import HReleaseRuleNAC0@nfrom HReleaseRuleLHS import HReleaseRuleLHS@nreturn HReleaseRuleNAC0().eval_name1(attr_value, PreNode) and HReleaseRuleLHS().eval_name1(attr_value, PreNode)'
p1
.""").replace("@n", "\n")
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
L83615215737654088064135540601591418602L
sb.""")
    def eval_name1(self, attr_value, PreNode, graph):
        from HReleaseRuleNAC0 import HReleaseRuleNAC0
        from HReleaseRuleLHS import HReleaseRuleLHS
        return HReleaseRuleNAC0().eval_name1(attr_value, PreNode) and HReleaseRuleLHS().eval_name1(attr_value, PreNode)


    def constraint(self, PreNode, graph):
        """
            Executable constraint code. 
            @param PreNode: Function taking an integer as parameter
                            and returns the node corresponding to that label.
        """
        return True

        