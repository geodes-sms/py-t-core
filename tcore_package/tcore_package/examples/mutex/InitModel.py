
from t_core.composer import Composer
from tc_python.srule import SRule
from HHoldRuleLHS import HHoldRuleLHS
from HHoldRuleRHS import HHoldRuleRHS
from HNewRuleLHS import HNewRuleLHS
from HNewRuleRHS import HNewRuleRHS
from HResourceRuleLHS import HResourceRuleLHS
from HResourceRuleRHS import HResourceRuleRHS


class InitModel(Composer):
    def __init__(self, N, R):
        super(InitModel, self).__init__()
        self.N = N
        self.R = R
        self.NewRule = SRule(HNewRuleLHS(), HNewRuleRHS(), max_iterations=N - 2, ignore_resolver=True)
        self.ResourceRule = SRule(HResourceRuleLHS(), HResourceRuleRHS(), max_iterations=R, ignore_resolver=True)
        self.HoldRule = SRule(HHoldRuleLHS(), HHoldRuleRHS(), max_iterations=N, ignore_resolver=True)
    
    def packet_in(self, packet):
        # Processes
        packet = self.NewRule.packet_in(packet)
        packet.clean()
        if not self.NewRule.is_success:
            if self.NewRule.exception is not None:
                self.exception = self.NewRule.exception
                return packet
        
        # Resources
        packet = self.ResourceRule.packet_in(packet)
        packet.clean()
        if not self.ResourceRule.is_success:
            if self.NewRule.exception is not None:
                self.exception = self.ResourceRule.exception
                return packet
        
        # Holding
        packet = self.HoldRule.packet_in(packet)
        packet.clean()
        if not self.HoldRule.is_success:
            if self.HoldRule.exception is not None:
                self.exception = self.HoldRule.exception
                return packet
        self.is_success = True
        return packet


