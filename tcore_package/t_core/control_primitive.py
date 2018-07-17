
from primitive import Primitive

# Abstract class
class ControlPrimitive(Primitive):
    def __init__(self):
        super(ControlPrimitive, self).__init__()
        self.success = []   # [Packet]
        self.fail = []      # [Packet]
    
    def success_in(self, packet):
        raise AttributeError('Method not implemented')
    
    def fail_in(self, packet):
        raise AttributeError('Method not implemented')
    
    def reset(self):
        self.success = []
        self.fail = []