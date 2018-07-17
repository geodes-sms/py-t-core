
from copy import deepcopy
from util.infinity import INFINITY
from core.match_algo import HimesisMatcher
from core.himesis import HConstants as HC
from rule_primitive import RulePrimitive
from messages import MatchSet, Match, TransformationException


class Matcher(RulePrimitive):
    '''
        Binds the source graph according to the pre-condition pattern.
    '''
    def __init__(self, condition, max=INFINITY):
        '''
            Binds the source graph according to the pre-condition pattern.
            @param condition: The pre-condition pattern.
            @param max: The maximum number of matches.
        '''
        super(Matcher, self).__init__()
        self.max = max
        self.condition = condition
    
    def __str__(self):
        s = super(Matcher, self).__str__()
        s = s.split(' ')
        s.insert(1, '[%s]' % self.condition.name)
        return reduce(lambda x, y: '%s %s' % (x,y), s)
    
    def packet_in(self, packet):
        self.exception = None
        self.is_success = False
        if self.condition[HC.GUID] in packet.match_sets:
            matchSet = packet.match_sets[self.condition[HC.GUID]]
        else:
            matchSet = MatchSet()
        
        # Find the matches
        try:
            i = 1
            if i <= self.max:
                for mapping in self._match(packet.graph, packet.global_pivots):
                    # Convert the mapping to a Match object
                    match = Match()
                    match.from_mapping(mapping, packet.graph, self.condition)
                    matchSet.matches.append(match)
                    i += 1
                    if i > self.max:
                        # We don't need any more matches
                        break
        except Exception, e:
            self.is_success = False
            self.exception = TransformationException(e)
            self.exception.packet = packet
            self.exception.transformation_unit = self
            return packet
        
        # Don't forget to add the match set to the packet, even if no matches were found
        if len(matchSet.matches) > 0:
            packet.match_sets[self.condition[HC.GUID]] = matchSet
        
        # Identify that this is the condition we are currently processing
        packet.current = self.condition[HC.GUID]
        
        # Success only if matches were found
        self.is_success = len(matchSet.matches) > 0
        return packet
    
    def _match(self, graph, pivots) :
        def getSourceNodeFromLabel(label, mapping, pattern_graph):
            vs = pattern_graph.vs(MT_label__ = label)
            if len(vs) == 0:
                #TODO: This should be a TransformationLanguageSpecificException
                raise Exception('Label %d does not exist in the pattern' % label)
            elif len(vs) > 1:
                #TODO: This should be a TransformationLanguageSpecificException
                raise Exception('Duplicate label %d in the pattern' % label)
            elif not vs[0].index in mapping:
                #TODO: This should be a TransformationLanguageSpecificException
                raise Exception('Node with label %d was not matched' % label)
            else:
                return graph.vs[mapping[vs[0].index]]
        '''
            Matcher with pivots and (possibly) multiple NACs
            1. Verify that no unbound NAC has a match
            2. Let the "bridge" denote the biggest graph that is the intersection of the LHS and a NAC, among all NACs
            3. Match the common part between the LHS & the NAC, i.e., the "bridge"
            3.1 Continue the matching ensuring no occurrence of the NAC
            3.2. If a NAC is found, ignore the current bridge mapping
            3.3. Continue to find complete matches of the LHS,
                 given each partial match found in 3.1.
            3.4. For each valid match, verify that no occurrence of any remaining bound NAC is found,
                 given the mapping found in 3.3.
        '''
        bound_NACs = []          # Keep track of which NACs to look for after the LHS matching
        pred1 = {}              # To optimize the matcher, since otherwise matcher will compute the predecessors of the source graph many times
        succ1 = {}              # To optimize the matcher, since otherwise matcher will compute the successors of the source graph many times
        
        # Cache the pivot nodes of the source graph
        pivots = deepcopy(pivots)
        pivots.to_source_node_indices(graph)
        
        for NAC in self.condition.NACs:
            # Delay the case where the NAC has some nodes bound to the LHS
            if NAC.bridge.vcount() > 0:
                bound_NACs.append(NAC)
            
            #===================================================================
            # First process the NACs that are not bound to the LHS
            #===================================================================
            else:
                # Look for a NAC match
                nacMatcher = HimesisMatcher(source_graph=graph, pattern_graph=NAC)
                # Convert the pivots
                nac_pivots = pivots.to_mapping(graph, NAC)
                try:
                    for mapping in nacMatcher.match_iter(context=nac_pivots):
                        if NAC.constraint(lambda i: getSourceNodeFromLabel(i, mapping, self.condition), graph):
                            # An unbound NAC has been found: this pattern can never match
                            return
                except: raise
                finally: nacMatcher.reset_recursion_limit()
                # For further matching optimizations
                pred1 = nacMatcher.pred1
                succ1 = nacMatcher.succ1
        
        # Either there are no NACs, or there were only unbound NACs that do not match, so match the LHS now
        bound_NACs.sort(key=lambda nac: nac.bridge.vcount(), reverse=True)
        if not bound_NACs:
            lhsMatcher = HimesisMatcher(source_graph=graph, pattern_graph=self.condition, pred1=pred1, succ1=succ1)
            # Convert the pivots
            lhs_pivots = pivots.to_mapping(graph, self.condition)
            try:
                for mapping in lhsMatcher.match_iter(context=lhs_pivots):
                    if self.condition.constraint(lambda i: getSourceNodeFromLabel(i, mapping, self.condition), graph):
                        yield mapping
            except: raise
            finally: lhsMatcher.reset_recursion_limit()
            
            # The matching is complete
            return
        
        #===================================================================
        # Now process the NACs that have some nodes bound to the LHS
        #===================================================================
        
        # Continue the matching looking for the LHS now
        lhsMatcher = HimesisMatcher(source_graph=graph, pattern_graph=self.condition, pred1=pred1, succ1=succ1)
        # Augment the bridge mapping with the pivot mappings
        lhs_pivots = pivots.to_mapping(graph, self.condition)
        
        try:
            for mapping in lhsMatcher.match_iter(context=lhs_pivots):
                if self.condition.constraint(lambda i: getSourceNodeFromLabel(i, mapping, self.condition), graph):
                    # A match of the LHS is found: ensure that no remaining NAC do match
                    invalid = False
                    for NAC in bound_NACs:
                        # This mapping represents the mapping of the bridge of this NAC with the LHS
                        match = Match()
                        match.from_mapping(mapping, graph, self.condition)
                        bridgeMapping = match.to_mapping(graph, NAC)
                        
                        # Now continue the matching looking for a match of the corresponding NAC
                        nacMatcher = HimesisMatcher(source_graph=graph, pattern_graph=NAC, pred1=pred1, succ1=succ1)
                        for nac_mapping in nacMatcher.match_iter(context=bridgeMapping):
                            if NAC.constraint(lambda i: getSourceNodeFromLabel(i, nac_mapping, NAC), graph):
                                # An occurrence of the NAC is found: current mapping is not valid
                                invalid = True
                                break
                        if invalid:
                            # An occurrence of the NAC was found: current mapping is not valid
                            break
                    else:
                        # Either there are no bound NACs or no occurrence of any bound NAC was found: current mapping is valid
                        yield mapping
        except: raise
        finally: lhsMatcher.reset_recursion_limit()
