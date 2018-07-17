

from core.himesis import Himesis
import cPickle as pickle
from uuid import UUID

class HA(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the AToM3 model HA.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HA, self).__init__(name='HA', num_nodes=1, edges=[])
        
        # Add the edges
        self.add_edges([])
        # Set the graph attributes
        self["mm__"] = pickle.loads("""(lp1
S'CDMetaModel'
p2
a.""")
        self["name"] = """a"""
        self["GUID__"] = UUID('f86d10ce-c06f-4e24-a86c-9790e120704e')
        
        # Set the node attributes
        self.vs[0]["mm__"] = """Clazz"""
        self.vs[0]["is_persistent"] = True
        self.vs[0]["name"] = """a"""
        self.vs[0]["GUID__"] = UUID('2131d6d9-b9cf-48b7-8dbe-7161f4fba3ac')

