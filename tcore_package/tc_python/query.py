
from t_core.composer import Composer
from t_core.matcher import Matcher
from t_core.iterator import Iterator


class Query(Composer):
    '''
        Finds a match for the LHS.
    '''
    def __init__(self, LHS):
        '''
            Finds a match for the LHS.
            @param LHS: The pre-condition pattern (LHS + NACs).
        '''
        super(Query, self).__init__()
        self.M = Matcher(condition=LHS, max=1)
        self.I = Iterator(max_iterations=1)
    
    def packet_in(self, packet):
        self.exception = None
        self.is_success = False
        # Match
        packet = self.M.packet_in(packet)
        if not self.M.is_success:
            self.exception = self.M.exception
            return packet
        # Choose the only match
        packet = self.I.packet_in(packet)
        if not self.I.is_success:
            # Clean the packet: required since there is no Rewriter in a Query
            if  len(packet.match_sets[self.I.condition].matches) == 0:
                del packet.match_sets[self.I.condition]
            self.exception = self.I.exception
            return packet
        # Output success packet
        self.is_success = True
        return packet
