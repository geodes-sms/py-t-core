
from t_core.composer import Composer
from tc_python.arule import ARule
from tc_python.srule import SRule
from tc_python.frule import FRule
from HBlockedRuleLHS import HBlockedRuleLHS
from HBlockedRuleRHS import HBlockedRuleRHS
from HGiveRuleLHS import HGiveRuleLHS
from HGiveRuleRHS import HGiveRuleRHS
from HIgnoreRuleLHS import HIgnoreRuleLHS
from HIgnoreRuleRHS import HIgnoreRuleRHS
from HReleaseStarRuleLHS import HReleaseStarRuleLHS
from HReleaseStarRuleRHS import HReleaseStarRuleRHS
from HRequestStarRuleLHS import HRequestStarRuleLHS
from HRequestStarRuleRHS import HRequestStarRuleRHS
from HTakeRuleLHS import HTakeRuleLHS
from HTakeRuleRHS import HTakeRuleRHS
from HUnlockRuleLHS import HUnlockRuleLHS
from HUnlockRuleRHS import HUnlockRuleRHS
from HWaitingRuleLHS import HWaitingRuleLHS
from HWaitingRuleRHS import HWaitingRuleRHS


class LongTransformationSequence(Composer):
    def __init__(self, N, debug_folder=''):
        super(LongTransformationSequence, self).__init__()
        self.length = 0
        self.debug_suffix = 'lts'
        self.debug_folder = debug_folder
        self.N = N
        self.RequestStarRule = FRule(HRequestStarRuleLHS(), HRequestStarRuleRHS(), max_iterations=N, ignore_resolver=True)
        self.BlockedRule = ARule(HBlockedRuleLHS(), HBlockedRuleRHS(), ignore_resolver=True)
        self.WaitingRule = SRule(HWaitingRuleLHS(), HWaitingRuleRHS(), max_iterations=N - 1, ignore_resolver=True)
        self.UnlockRule = ARule(HUnlockRuleLHS(), HUnlockRuleRHS(), ignore_resolver=True)
        self.IgnoreRule = ARule(HIgnoreRuleLHS(), HIgnoreRuleRHS(), ignore_resolver=True)
        self.GiveRule = ARule(HGiveRuleLHS(), HGiveRuleRHS(), ignore_resolver=True)
        self.TakeRule = ARule(HTakeRuleLHS(), HTakeRuleRHS(), ignore_resolver=True)
        self.ReleaseStarRule = ARule(HReleaseStarRuleLHS(), HReleaseStarRuleRHS(), ignore_resolver=True)
    
    def packet_in(self, packet):
        if self.debug_folder: packet.graph.draw(label='name', debug=True).save(self.debug_folder + '/%s%d.png' % (self.debug_suffix, self.length))
        
        # Request
        packet = self.RequestStarRule.packet_in(packet)
        packet.clean()
        if not self.RequestStarRule.is_success:
            if self.RequestStarRule.exception is not None:
                self.exception = self.HRequestStarRule.exception
                return packet
        self.length += self.RequestStarRule.I.iterations
        if self.debug_folder: packet.graph.draw(label='name', debug=True).save(self.debug_folder + '/%s%d.png' % (self.debug_suffix, self.length))
        
        # Block
        packet = self.BlockedRule.packet_in(packet)
        packet.clean()
        if not self.BlockedRule.is_success:
            if self.BlockedRule.exception is not None:
                self.exception = self.HBlockedRule.exception
                return packet
        self.length += self.BlockedRule.I.iterations
        if self.debug_folder: packet.graph.draw(label='name', debug=True).save(self.debug_folder + '/%s%d.png' % (self.debug_suffix, self.length))
        
        # Wait
        packet = self.WaitingRule.packet_in(packet)
        packet.clean()
        if not self.WaitingRule.is_success:
            if self.WaitingRule.exception is not None:
                self.exception = self.WaitingRule.exception
                return packet
        self.length += self.WaitingRule.I.iterations
        if self.debug_folder: packet.graph.draw(label='name', debug=True).save(self.debug_folder + '/%s%d.png' % (self.debug_suffix, self.length))
        
        # Unlock
        packet = self.UnlockRule.packet_in(packet)
        packet.clean()
        if not self.UnlockRule.is_success:
            if self.UnlockRule.exception is not None:
                self.exception = self.UnlockRule.exception
                return packet
        self.length += self.UnlockRule.I.iterations
        if self.debug_folder: packet.graph.draw(label='name', debug=True).save(self.debug_folder + '/%s%d.png' % (self.debug_suffix, self.length))
        
        # Block
        packet = self.BlockedRule.packet_in(packet)
        packet.clean()
        if not self.BlockedRule.is_success:
            if self.BlockedRule.exception is not None:
                self.exception = self.HBlockedRule.exception
                return packet
        self.length += self.BlockedRule.I.iterations
        if self.debug_folder: packet.graph.draw(label='name', debug=True).save(self.debug_folder + '/%s%d.png' % (self.debug_suffix, self.length))
        
        # Wait
        packet = self.WaitingRule.packet_in(packet)
        packet.clean()
        if not self.WaitingRule.is_success:
            if self.WaitingRule.exception is not None:
                self.exception = self.WaitingRule.exception
                return packet
        self.length += self.WaitingRule.I.iterations
        if self.debug_folder: packet.graph.draw(label='name', debug=True).save(self.debug_folder + '/%s%d.png' % (self.debug_suffix, self.length))
        
        # Ignore
        packet = self.IgnoreRule.packet_in(packet)
        packet.clean()
        if not self.IgnoreRule.is_success:
            if self.IgnoreRule.exception is not None:
                self.exception = self.IgnoreRule.exception
                return packet
        self.length += self.IgnoreRule.I.iterations
        if self.debug_folder: packet.graph.draw(label='name', debug=True).save(self.debug_folder + '/%s%d.png' % (self.debug_suffix, self.length))
        
        # Circle around
        for _ in range(self.N - 1):
            # Give
            packet = self.GiveRule.packet_in(packet)
            packet.clean()
            if not self.GiveRule.is_success:
                if self.GiveRule.exception is not None:
                    self.exception = self.GiveRule.exception
                    return packet
            self.length += self.GiveRule.I.iterations
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
            
            # Release
            packet = self.ReleaseStarRule.packet_in(packet)
            packet.clean()
            if not self.ReleaseStarRule.is_success:
                if self.ReleaseStarRule.exception is not None:
                    self.exception = self.ReleaseStarRule.exception
                    return packet
            self.length += self.ReleaseStarRule.I.iterations
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


