

from core.himesis import Himesis
import cPickle as pickle
from uuid import UUID

class HInit2Processes(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the AToM3 model HInit2Processes.
        """
        # Create the himesis graph
        EDGE_LIST = [(3, 0), (0, 2), (2, 1), (1, 3)]
        
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HInit2Processes, self).__init__(name='HInit2Processes', num_nodes=4, edges=EDGE_LIST)

        # Set the graph attributes
        self["mm__"] = pickle.loads("""(lp1
S'Mutex'
p2
a.""")
        self["name"] = """Init2Processes"""
        self["GUID__"] = UUID('54f6831c-7013-4f5b-aae6-2d0668512e2c')
        
        # Set the node attributes
        self.vs[0]["mm__"] = """Process"""
        self.vs[0]["name"] = """P0"""
        self.vs[0]["GUID__"] = UUID('80c78d1d-fd5d-4bd8-a224-d8a73651525a')
        self.vs[1]["mm__"] = """Process"""
        self.vs[1]["name"] = """P1"""
        self.vs[1]["GUID__"] = UUID('2a116b48-c6bb-41af-a208-ce7693285082')
        self.vs[2]["mm__"] = """next"""
        self.vs[2]["GUID__"] = UUID('6873525d-fba9-453b-8193-634befefe5a0')
        self.vs[3]["mm__"] = """next"""
        self.vs[3]["GUID__"] = UUID('498a7840-d6b5-49fb-b2a3-548ff5809cbf')
        