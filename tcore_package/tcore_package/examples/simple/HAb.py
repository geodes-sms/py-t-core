

from core.himesis import Himesis
import cPickle as pickle
from uuid import UUID

class HAb(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the AToM3 model HAb.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HAb, self).__init__(name='HAb', num_nodes=4, edges=[])
        
        # Add the edges
        self.add_edges([(1, 0), (0, 2), (2, 3), (3, 1)])
        # Set the graph attributes
        self["mm__"] = pickle.loads("""(lp1
S'CDMetaModel'
p2
a.""")
        self["name"] = """ab"""
        self["GUID__"] = UUID('c0345fb9-28f5-43fb-8a71-d0efd555dd41')
        
        # Set the node attributes
        self.vs[0]["mm__"] = """Parent"""
        self.vs[0]["GUID__"] = UUID('8d6c3270-1b59-46cc-91b2-51c861cca7b9')
        self.vs[1]["mm__"] = """Clazz"""
        self.vs[1]["is_persistent"] = True
        self.vs[1]["name"] = """a"""
        self.vs[1]["GUID__"] = UUID('928d0fc0-adb3-43c7-b6d2-97e300448d79')
        self.vs[2]["mm__"] = """Clazz"""
        self.vs[2]["is_persistent"] = True
        self.vs[2]["name"] = """b"""
        self.vs[2]["GUID__"] = UUID('0feab044-6354-4e64-8bd4-2aa31f2dfc43')
        self.vs[3]["mm__"] = """Parent"""
        self.vs[3]["GUID__"] = UUID('b6bd3d53-cad8-4e0b-9967-e5b7a5e31b98')

