

from core.himesis import Himesis, HimesisPreConditionPattern
import cPickle as pickle

class HRequestSimpleRuleNAC0Bridge(HimesisPreConditionPattern):
    def __init__(self):
        """
        Creates the himesis graph representing the AToM3 model HRequestSimpleRuleNAC0Bridge.
        """
        # Create the himesis graph
        EDGE_LIST = []
        
        super(HRequestSimpleRuleNAC0Bridge, self).__init__(name='HRequestSimpleRuleNAC0Bridge', num_nodes=2, edges=EDGE_LIST)
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
L146637052767111949362208920316723548035L
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
        self.vs[0]["MT_pre__name"] = pickle.loads("""S'from HRequestSimpleRuleNAC0 import HRequestSimpleRuleNAC0@nfrom HRequestSimpleRuleLHS import HRequestSimpleRuleLHS@nreturn HRequestSimpleRuleNAC0().eval_name2(attr_value, PreNode) and HRequestSimpleRuleLHS().eval_name2(attr_value, PreNode)'
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
L339665020396135801221171508913979770898L
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
        self.vs[1]["MT_pre__name"] = pickle.loads("""S'from HRequestSimpleRuleNAC0 import HRequestSimpleRuleNAC0@nfrom HRequestSimpleRuleLHS import HRequestSimpleRuleLHS@nreturn HRequestSimpleRuleNAC0().eval_name1(attr_value, PreNode) and HRequestSimpleRuleLHS().eval_name1(attr_value, PreNode)'
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
L119841419163540126656299293599774230373L
sb.""")
    def eval_name2(self, attr_value, PreNode, graph):
        from HRequestSimpleRuleNAC0 import HRequestSimpleRuleNAC0
        from HRequestSimpleRuleLHS import HRequestSimpleRuleLHS
        return HRequestSimpleRuleNAC0().eval_name2(attr_value, PreNode) and HRequestSimpleRuleLHS().eval_name2(attr_value, PreNode)


    def eval_name1(self, attr_value, PreNode, graph):
        from HRequestSimpleRuleNAC0 import HRequestSimpleRuleNAC0
        from HRequestSimpleRuleLHS import HRequestSimpleRuleLHS
        return HRequestSimpleRuleNAC0().eval_name1(attr_value, PreNode) and HRequestSimpleRuleLHS().eval_name1(attr_value, PreNode)


    def constraint(self, PreNode, graph):
        """
            Executable constraint code. 
            @param PreNode: Function taking an integer as parameter
                            and returns the node corresponding to that label.
        """
        return True

        