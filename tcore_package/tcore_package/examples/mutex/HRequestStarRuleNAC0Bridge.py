

from core.himesis import Himesis, HimesisPreConditionPattern
import cPickle as pickle

class HRequestStarRuleNAC0Bridge(HimesisPreConditionPattern):
    def __init__(self):
        """
        Creates the himesis graph representing the AToM3 model HRequestStarRuleNAC0Bridge.
        """
        # Create the himesis graph
        EDGE_LIST = []
        
        super(HRequestStarRuleNAC0Bridge, self).__init__(name='HRequestStarRuleNAC0Bridge', num_nodes=2, edges=EDGE_LIST)
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
L271594817068501154406645432777552248950L
sb.""")
        # Set the node attributes
        self.vs[0]["MT_subtypeMatching__"] = pickle.loads("""I00
.""")
        self.vs[0]["MT_label__"] = pickle.loads("""S'5'
.""")
        self.vs[0]["mm__"] = pickle.loads("""S'MT_pre__Resource'
p1
.""")
        self.vs[0]["MT_subtypes__"] = pickle.loads("""(lp1
.""")
        self.vs[0]["MT_pre__name"] = pickle.loads("""S'from HRequestStarRuleNAC0 import HRequestStarRuleNAC0@nfrom HRequestStarRuleLHS import HRequestStarRuleLHS@nreturn HRequestStarRuleNAC0().eval_name5(attr_value, PreNode) and HRequestStarRuleLHS().eval_name5(attr_value, PreNode)'
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
L274966528288541626611720680788409477996L
sb.""")
        self.vs[1]["MT_subtypeMatching__"] = pickle.loads("""I00
.""")
        self.vs[1]["MT_label__"] = pickle.loads("""S'1'
.""")
        self.vs[1]["mm__"] = pickle.loads("""S'MT_pre__Process'
p1
.""")
        self.vs[1]["MT_subtypes__"] = pickle.loads("""(lp1
.""")
        self.vs[1]["MT_pre__name"] = pickle.loads("""S'from HRequestStarRuleNAC0 import HRequestStarRuleNAC0@nfrom HRequestStarRuleLHS import HRequestStarRuleLHS@nreturn HRequestStarRuleNAC0().eval_name1(attr_value, PreNode) and HRequestStarRuleLHS().eval_name1(attr_value, PreNode)'
p1
.""").replace("@n", "\n")
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
L144395182965853596662250778849471302941L
sb.""")
    def eval_name5(self, attr_value, PreNode, graph):
        from HRequestStarRuleNAC0 import HRequestStarRuleNAC0
        from HRequestStarRuleLHS import HRequestStarRuleLHS
        return HRequestStarRuleNAC0().eval_name5(attr_value, PreNode) and HRequestStarRuleLHS().eval_name5(attr_value, PreNode)


    def eval_name1(self, attr_value, PreNode, graph):
        from HRequestStarRuleNAC0 import HRequestStarRuleNAC0
        from HRequestStarRuleLHS import HRequestStarRuleLHS
        return HRequestStarRuleNAC0().eval_name1(attr_value, PreNode) and HRequestStarRuleLHS().eval_name1(attr_value, PreNode)


    def constraint(self, PreNode, graph):
        """
            Executable constraint code. 
            @param PreNode: Function taking an integer as parameter
                            and returns the node corresponding to that label.
        """
        return True

        