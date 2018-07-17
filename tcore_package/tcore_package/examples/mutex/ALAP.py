
from t_core.composer import Composer
from tc_python.frule import FRule
from HGiveRuleLHS import HGiveRuleLHS
from HGiveRuleRHS import HGiveRuleRHS
from HReleaseRuleLHS import HReleaseRuleLHS
from HReleaseRuleRHS import HReleaseRuleRHS
from HRequestSimpleRuleLHS import HRequestSimpleRuleLHS
from HRequestSimpleRuleRHS import HRequestSimpleRuleRHS
from HTakeRuleLHS import HTakeRuleLHS
from HTakeRuleRHS import HTakeRuleRHS


class AsLongAsPossible(Composer):
    def __init__(self, N, debug_folder=''):
        super(AsLongAsPossible, self).__init__()
        self.length = 0
        self.debug_suffix = 'alap'
        self.debug_folder = debug_folder
        self.N = N
        self.ReleaseRule = FRule(HReleaseRuleLHS(), HReleaseRuleRHS(), max_iterations=N, ignore_resolver=True)
        self.GiveRule = FRule(HGiveRuleLHS(), HGiveRuleRHS(), max_iterations=N, ignore_resolver=True)
        self.RequestSimpleRule = FRule(HRequestSimpleRuleLHS(), HRequestSimpleRuleRHS(), max_iterations=N, ignore_resolver=True)
        self.TakeRule = FRule(HTakeRuleLHS(), HTakeRuleRHS(), max_iterations=N, ignore_resolver=True)
        
    def packet_in(self, packet):
        if self.debug_folder: packet.graph.draw(label='name', debug=True).save(self.debug_folder + '/%s%d.png' % (self.debug_suffix, self.length))
        
        # Release
        packet = self.ReleaseRule.packet_in(packet)
        packet.clean()
        if not self.ReleaseRule.is_success:
            if self.ReleaseRule.exception is not None:
                self.exception = self.ReleaseRule.exception
                return packet
        self.length += self.ReleaseRule.I.iterations
        if self.debug_folder: packet.graph.draw(label='name', debug=True).save(self.debug_folder + '/%s%d.png' % (self.debug_suffix, self.length))
        
        # Give
        packet = self.GiveRule.packet_in(packet)
        packet.clean()
        if not self.GiveRule.is_success:
            if self.GiveRule.exception is not None:
                self.exception = self.GiveRule.exception
                return packet
        self.length += self.GiveRule.I.iterations
        if self.debug_folder: packet.graph.draw(label='name', debug=True).save(self.debug_folder + '/%s%d.png' % (self.debug_suffix, self.length))
        
        # Request
        packet = self.RequestSimpleRule.packet_in(packet)
        packet.clean()
        if not self.RequestSimpleRule.is_success:
            if self.RequestSimpleRule.exception is not None:
                self.exception = self.RequestSimpleRule.exception
                return packet
        self.length += self.RequestSimpleRule.I.iterations
        if self.debug_folder: packet.graph.draw(label='name', debug=True).save(self.debug_folder + '/%s%d.png' % (self.debug_suffix, self.length))
        
        # Take
        packet = self.TakeRule.packet_in(packet)
        packet.clean()
        if not self.TakeRule.is_success:
            if self.TakeRule.exception is not None:
                self.exception = self.TakeRule.exception
                return packet
        self.length += self.TakeRule.I.iterations
        if self.debug_folder: packet.graph.draw(label='name', debug=True).save(self.debug_folder + '/%s%d.png' % (self.debug_suffix, self.length))
        
        self.is_success = True
        return packet


