

from core.himesis import Himesis, HimesisPreConditionPattern
import cPickle as pickle
from uuid import UUID

class HIgnoreRuleNAC0Bridge(HimesisPreConditionPattern):
    def __init__(self):
        """
        Creates the himesis graph representing the AToM3 model HIgnoreRuleNAC0Bridge.
        """
        # Create the himesis graph
        EDGE_LIST = []
        
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HIgnoreRuleNAC0Bridge, self).__init__(name='HIgnoreRuleNAC0Bridge', num_nodes=1, edges=EDGE_LIST)

        # Set the graph attributes
        self["GUID__"] = UUID('cf936002-72b6-4506-a2ac-93c4e15ac8c6')
        
        # Set the node attributes
        self.vs[0]["MT_subtypeMatching__"] = False
        self.vs[0]["MT_label__"] = """1"""
        self.vs[0]["mm__"] = """MT_pre__Process"""
        self.vs[0]["MT_subtypes__"] = pickle.loads("""(lp1
.""")
        self.vs[0]["MT_dirty__"] = False
        self.vs[0]["MT_pre__name"] = """from HIgnoreRuleNAC0 import HIgnoreRuleNAC0
from HIgnoreRuleLHS import HIgnoreRuleLHS
return HIgnoreRuleNAC0().eval_name1(attr_value, PreNode) and HIgnoreRuleLHS().eval_name1(attr_value, PreNode)"""
        self.vs[0]["GUID__"] = UUID('736cb7ae-597e-4f29-8075-133e21668d5a')
    def eval_name1(self, attr_value, PreNode, graph):
        from HIgnoreRuleNAC0 import HIgnoreRuleNAC0
        from HIgnoreRuleLHS import HIgnoreRuleLHS
        return HIgnoreRuleNAC0().eval_name1(attr_value, PreNode) and HIgnoreRuleLHS().eval_name1(attr_value, PreNode)


    def constraint(self, PreNode, graph):
        """
            Executable constraint code. 
            @param PreNode: Function taking an integer as parameter
                            and returns the node corresponding to that label.
        """
        return True

        