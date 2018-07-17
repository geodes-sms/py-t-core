
from t_core.composer import Composer
from util.seeded_random import Random


class BRule(Composer):
    '''
        Selects a branch in which the matcher succeeds.
    '''
    def __init__(self, branches):
        '''
            Selects a branch in which the matcher succeeds.
            @param branches: A list of ARules.
        '''
        super(BRule, self).__init__()
        self.branches = branches
    
    def packet_in(self, packet):
        self.exception = None
        self.is_success = False
        remaining_branches = range(len(self.branches))
        original = packet.clone()
        # Success on the first branch that is in success
        while True:
            if len(remaining_branches) == 0:
                # They all failed
                return packet
            branch_no = Random.choice(remaining_branches)
            branch = self.branches[branch_no]
            packet = branch.packet_in(packet)
            if not branch.is_success:
                if branch.exception is not None:
                    self.exception = branch.exception
                    return packet
                else:
                    # Ignore this branch for next try
                    remaining_branches.remove(branch_no)
                    packet = original
            else:
                self.is_success = True
                return packet
        
