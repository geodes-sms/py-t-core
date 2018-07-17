
from composite_primitive import CompositePrimitive


class Composer(CompositePrimitive):
    '''
        Encapsulates T-Core primitives.
        Both packet_in & next_in methods must be overridden to provide meaningful behaviour. 
    '''
    def __init__(self):
        '''
            Encapsulates T-Core primitives.
            Both packet_in & next_in methods must be overridden to provide meaningful behaviour. 
        '''
        super(Composer, self).__init__()
    
    def packet_in(self, packet):
        return packet
    
    def next_in(self, packet):
        return packet
