

from core.himesis import Himesis, HimesisPreConditionPattern
import cPickle as pickle
from uuid import UUID

class HTopClass2TableNAC0Bridge(HimesisPreConditionPattern):
    def __init__(self):
        """
        Creates the himesis graph representing the AToM3 model HTopClass2TableNAC0Bridge.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HTopClass2TableNAC0Bridge, self).__init__(name='HTopClass2TableNAC0Bridge', num_nodes=1, edges=[])
        
        # Add the edges
        self.add_edges([])
        # Set the graph attributes
        self["GUID__"] = UUID('0c4bc850-0acf-4395-80fd-98c56a0fb82c')
        
        # Set the node attributes
        self.vs[0]["MT_subtypeMatching__"] = False
        self.vs[0]["MT_pre__is_persistent"] = """from HTopClass2TableLHS import HTopClass2TableLHS
from HTopClass2TableNAC0 import HTopClass2TableNAC0
lhs = HTopClass2TableLHS()
return HTopClass2TableLHS().eval_is_persistent1(attr_value, this) and HTopClass2TableNAC0(lhs).eval_is_persistent1(attr_value, this)"""
        self.vs[0]["MT_label__"] = """1"""
        self.vs[0]["mm__"] = """MT_pre__Clazz"""
        self.vs[0]["MT_subtypes__"] = pickle.loads("""(lp1
.""")
        self.vs[0]["MT_pre__name"] = """from HTopClass2TableLHS import HTopClass2TableLHS
from HTopClass2TableNAC0 import HTopClass2TableNAC0
lhs = HTopClass2TableLHS()
return HTopClass2TableLHS().eval_name1(attr_value, this) and HTopClass2TableNAC0(lhs).eval_name1(attr_value, this)"""
        self.vs[0]["MT_dirty__"] = False
        self.vs[0]["GUID__"] = UUID('96977051-8531-40e0-952d-fabad1d8489b')

    def eval_is_persistent1(self, attr_value, this):
        from HTopClass2TableLHS import HTopClass2TableLHS
        from HTopClass2TableNAC0 import HTopClass2TableNAC0
        lhs = HTopClass2TableLHS()
        return HTopClass2TableLHS().eval_is_persistent1(attr_value, this) and HTopClass2TableNAC0(lhs).eval_is_persistent1(attr_value, this)


    def eval_name1(self, attr_value, this):
        from HTopClass2TableLHS import HTopClass2TableLHS
        from HTopClass2TableNAC0 import HTopClass2TableNAC0
        lhs = HTopClass2TableLHS()
        return HTopClass2TableLHS().eval_name1(attr_value, this) and HTopClass2TableNAC0(lhs).eval_name1(attr_value, this)


    def constraint(self, PreNode, graph):
        """
            Executable constraint code. 
            @param PreNode: Function taking an integer as parameter
                            and returns the node corresponding to that label.
        """
        return True

