
from util.infinity import INFINITY
from tc_python.lrule import LRule


class LQSRule(LRule):
    '''
        Applies an inner rule for each match of the LHS as long as matches can be found.
    '''
    def __init__(self, LHS, inner_rule, max_iterations=INFINITY):
        '''
            Applies an inner rule for each match of the LHS as long as matches can be found.
            @param LHS: The pre-condition pattern (LHS + NACs).
            @param inner_rule: The rule to apply in the loop.
            @param max_iterations: The maximum number of matches of the LHS.
        '''
        super(LQSRule, self).__init__(LHS, inner_rule, max_iterations)
    
    def packet_in(self, packet):
        self.exception = None
        self.is_success = False
        # Match
        packet = self.M.packet_in(packet)
        if not self.M.is_success:
            self.exception = self.M.exception
            return packet
        # Choose the first match
        packet = self.I.packet_in(packet)
        if not self.I.is_success:
            self.exception = self.I.exception
            return packet
        while True:
            # Apply the inner rule
            packet = self.inner_rule.packet_in(packet)
            if not self.inner_rule.is_success:
                self.exception = self.inner_rule.exception
                self.is_success = True
                return packet
            # Rule has been applied once, so it's a success anyway
            
            if self.I.iterations == self.I.max_iterations:
                return packet
            # Re-Match
            packet = self.M.packet_in(packet)
            if not self.M.is_success:
                self.exception = self.M.exception
                return packet
            # Choose another match
            packet = self.I.next_in(packet)
            # No more iterations are left
            if not self.I.is_success:
                if self.I.exception:
                    self.exception = self.I.exception
                return packet
