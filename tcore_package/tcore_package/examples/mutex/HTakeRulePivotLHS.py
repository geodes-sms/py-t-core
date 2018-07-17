

from core.himesis import Himesis, HimesisPreConditionPatternLHS
import cPickle as pickle

class HTakeRulePivotLHS(HimesisPreConditionPatternLHS):
    def __init__(self):
        """
        Creates the himesis graph representing the AToM3 model HTakeRulePivotLHS.
        """
        # Create the himesis graph
        EDGE_LIST = [(1, 0), (0, 2), (3, 1), (2, 3)]
        
        super(HTakeRulePivotLHS, self).__init__(name='HTakeRulePivotLHS', num_nodes=4, edges=EDGE_LIST)
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
L66613134182183156760649441909829310981L
sb.""")
        # Set the node attributes
        self.vs[0]["MT_subtypeMatching__"] = pickle.loads("""I00
.""")
        self.vs[0]["MT_label__"] = pickle.loads("""S'3'
.""")
        self.vs[0]["MT_subtypes__"] = pickle.loads("""(lp1
.""")
        self.vs[0]["mm__"] = pickle.loads("""S'MT_pre__toke'
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
L101478540246274308243670670373967117124L
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
L234957555377491434960538458538073441619L
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
L44671250922236119758829670160080311637L
sb.""")
        self.vs[3]["MT_subtypeMatching__"] = pickle.loads("""I00
.""")
        self.vs[3]["MT_label__"] = pickle.loads("""S'4'
.""")
        self.vs[3]["MT_subtypes__"] = pickle.loads("""(lp1
.""")
        self.vs[3]["mm__"] = pickle.loads("""S'MT_pre__request'
p1
.""")
        self.vs[3]["MT_dirty__"] = pickle.loads("""I00
.""")
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
L275539598258230508610242844206271449731L
sb.""")
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

        