
from primitive import Primitive

# Abstract class
class CompositePrimitive(Primitive):
    def __init__(self):
        super(CompositePrimitive, self).__init__()
    
    def packet_in(self, packet):
        raise AttributeError('Method not implemented')
    
    def next_in(self, packet):
        raise AttributeError('Method not implemented')