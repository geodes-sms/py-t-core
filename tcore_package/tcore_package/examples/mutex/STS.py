
from t_core.composer import Composer
from tc_python.arule import ARule
from tc_python.srule import SRule
from tc_python.frule import FRule
from HGiveRuleLHS import HGiveRuleLHS
from HGiveRuleRHS import HGiveRuleRHS
from HMountRuleLHS import HMountRuleLHS
from HMountRuleRHS import HMountRuleRHS
from HNewRuleLHS import HNewRuleLHS
from HNewRuleRHS import HNewRuleRHS
from HReleaseRuleLHS import HReleaseRuleLHS
from HReleaseRuleRHS import HReleaseRuleRHS
from HRequestRuleLHS import HRequestRuleLHS
from HRequestRuleRHS import HRequestRuleRHS
from HTakeRuleLHS import HTakeRuleLHS
from HTakeRuleRHS import HTakeRuleRHS

from HGiveRulePivotLHS import HGiveRulePivotLHS
from HGiveRulePivotRHS import HGiveRulePivotRHS
from HReleaseRulePivotLHS import HReleaseRulePivotLHS
from HReleaseRulePivotRHS import HReleaseRulePivotRHS
from HTakeRulePivotLHS import HTakeRulePivotLHS
from HTakeRulePivotRHS import HTakeRulePivotRHS


class ShortTransformationSequence(Composer):
    def __init__(self, N, debug_folder=''):
        super(ShortTransformationSequence, self).__init__()
        self.length = 0
        self.debug_suffix = 'sts'
        self.debug_folder = debug_folder
        self.N = N
        self.NewRule = SRule(HNewRuleLHS(), HNewRuleRHS(), max_iterations=N - 2, ignore_resolver=True)
        self.MountRule = ARule(HMountRuleLHS(), HMountRuleRHS(), ignore_resolver=True)
        self.RequestRule = FRule(HRequestRuleLHS(), HRequestRuleRHS(), max_iterations=N, ignore_resolver=True)
        self.TakeRule = ARule(HTakeRuleLHS(), HTakeRuleRHS(), ignore_resolver=True)
        self.ReleaseRule = ARule(HReleaseRuleLHS(), HReleaseRuleRHS(), ignore_resolver=True)
        self.GiveRule = ARule(HGiveRuleLHS(), HGiveRuleRHS(), ignore_resolver=True)
    
    def packet_in(self, packet):
        if self.debug_folder: packet.graph.draw(label='name', debug=True).save(self.debug_folder + '/%s%d.png' % (self.debug_suffix, self.length))
        
        # New Processes
        packet = self.NewRule.packet_in(packet)
        packet.clean()
        if not self.NewRule.is_success:
            if self.NewRule.exception is not None:
                self.exception = self.NewRule.exception
                return packet
        self.length += self.NewRule.I.iterations
        if self.debug_folder: packet.graph.draw(label='name', debug=True).save(self.debug_folder + '/%s%d.png' % (self.debug_suffix, self.length))
        
        # Mount
        packet = self.MountRule.packet_in(packet)
        packet.clean()
        if not self.MountRule.is_success:
            if self.MountRule.exception is not None:
                self.exception = self.MountRule.exception
                return packet
        self.length += self.MountRule.I.iterations
        if self.debug_folder: packet.graph.draw(label='name', debug=True).save(self.debug_folder + '/%s%d.png' % (self.debug_suffix, self.length))
        
        # Request
        packet = self.RequestRule.packet_in(packet)
        packet.clean()
        if not self.RequestRule.is_success:
            if self.RequestRule.exception is not None:
                self.exception = self.RequestRule.exception
                return packet
        self.length += self.RequestRule.I.iterations
        if self.debug_folder: packet.graph.draw(label='name', debug=True).save(self.debug_folder + '/%s%d.png' % (self.debug_suffix, self.length))
        
        # Pass it around
        for _ in range(self.N):
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
        
        self.is_success = True
        return packet


class ShortTransformationSequencePivot(ShortTransformationSequence):
    def __init__(self, N, debug_folder=''):
        super(ShortTransformationSequencePivot, self).__init__(N, debug_folder)
        self.debug_suffix = 'sts_pivot'
        self.TakeRule = ARule(HTakeRulePivotLHS(), HTakeRulePivotRHS(), ignore_resolver=True)
        self.ReleaseRule = ARule(HReleaseRulePivotLHS(), HReleaseRulePivotRHS(), ignore_resolver=True)
        self.GiveRule = ARule(HGiveRulePivotLHS(), HGiveRulePivotRHS(), ignore_resolver=True)


