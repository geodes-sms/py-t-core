
from primitive import Primitive

# Abstract class
class RulePrimitive(Primitive):
    def __init__(self):
        super(RulePrimitive, self).__init__()
    
    def packet_in(self, packet):
        raise AttributeError('Method not implemented')