

from core.himesis import Himesis

import cPickle as pickle
from uuid import UUID

class HSource(Himesis):
    def __init__(self):
        """
        Creates the himesis graph representing the AToM3 model HSource.
        """
        # Flag this instance as compiled now
        self.is_compiled = True
        
        super(HSource, self).__init__(name='HSource', num_nodes=2, edges=[])
        
        # Add the edges
        self.add_edges([])
        # Set the graph attributes
        self["mm__"] = pickle.loads("""(lp1
S'SimpleDSLTransMM'
p2
a.""")
        self["name"] = """source"""
        self["GUID__"] = UUID('fe8250c4-134c-49b4-961e-2695baa47547')
        
        # Set the node attributes
        self.vs[0]["mm__"] = """Station_S"""
        self.vs[0]["name"] = """s1"""
        self.vs[0]["GUID__"] = UUID('6f05ef17-a1be-4b68-b028-28c8ddaa5d98')
        self.vs[1]["mm__"] = """Station_S"""
        self.vs[1]["name"] = """s2"""
        self.vs[1]["GUID__"] = UUID('247bd54b-129e-4b2b-88cd-b1a8a1cfd73d')

