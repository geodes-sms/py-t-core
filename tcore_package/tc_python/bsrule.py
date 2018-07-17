
from util.infinity import INFINITY
from t_core.composer import Composer
from tc_python.brule import BRule


class BSRule(Composer):
    '''
        Selects a branch in which the matcher succeeds, as long as matches can be found.
    '''
    def __init__(self, branches, max_iterations=INFINITY):
        '''
            Selects a branch in which the matcher succeeds, as long as matches can be found.
            @param branches: A list of ARules.
            @param max_iterations: The maximum number of times to apply the transformation.
        '''
        super(BSRule, self).__init__()
        self.brule = BRule(branches)
        self.max_iterations = max_iterations
        self.iterations = 1
    
    def packet_in(self, packet):
        self.exception = None
        self.is_success = False
        # Apply the BRule
        packet = self.brule.packet_in(packet)
        if not self.brule.is_success:
            self.exception = self.brule.exception
            return packet
        else:
            # Rule has been applied once, so it's a success anyway
            self.is_success = True
            while self.iterations < self.max_iterations:
                # Re-apply the BRule
                packet = self.brule.packet_in(packet)
                if not self.brule.is_success:
                    self.exception = self.brule.exception
                    return packet
                self.iterations += 1
            return packet
