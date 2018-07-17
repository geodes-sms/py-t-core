
from t_core.composer import Composer


class Sequence(Composer):
    '''
        Applies each rule in the order provided.
    '''
    def __init__(self, rules):
        '''
            Applies each rule in the order provided.
            @param rules: The rules to apply.
        '''
        super(Sequence, self).__init__()
        self.rules = rules
    
    def packet_in(self, packet):
        self.exception = None
        self.is_success = False
        for rule in self.rules:
            packet = rule.packet_in(packet)
            packet.clean()
            if not rule.is_success:
                if rule.exception is not None:
                    self.exception = rule.exception
                return packet
        self.is_success = True
        return packet
