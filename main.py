# -*- coding: utf-8 -*-
import random
import copy

n = 6
proposer_preferences = dict()
acceptor_preferences = dict()
propsers = []

for i in range(1, n+1):
    proposer_preferences[i] = random.sample(range(n+1,2*n+1), n)
for i in range(n+1, 2*n+1):
    acceptor_preferences[i] = random.sample(range(1,n+1), n)

propsers = sorted(proposer_preferences.keys())

'''
--Pseudocode--
function stableMatching {
    Initialize all m ∈ M and w ∈ W to free
    while ∃ free man m who still has a woman w to propose to {
       w = highest ranked woman to whom m has not yet proposed
       if w is free
         (m, w) become engaged
       else some pair (m', w) already exists
         if w prefers m to m'
           (m, w) become engaged
           m' becomes free
         else
           (m', w) remain engaged
    }
}
'''
def match():
    free_proposers = propsers[:]
    engaged  = {}
    while free_proposers:
        current_proposer = free_proposers.pop(0)
        current_proposer_preference = proposer_preferences[current_proposer]
        current_acceptor = current_proposer_preference.pop(0)
        fiance = engaged.get(current_acceptor)
        if not fiance: #if acceptor a has not yet been proposed to
            engaged[current_acceptor] = current_proposer
            print("  (%s,%s)" % (current_proposer, current_acceptor))
        else: # some pair(p', a) exists
            current_acceptor_preference = acceptor_preferences[current_acceptor]
            if current_acceptor_preference.index(fiance) > current_acceptor_preference.index(current_proposer): # a prefers p to p'
                engaged[current_acceptor] = current_proposer
                print("  %s prefers %s over %s" % (current_acceptor, current_proposer, fiance))
                if proposer_preferences[fiance]:
                    free_proposers.append(fiance)
            else: # a remains with p'
                if current_proposer_preference:
                    free_proposers.append(current_proposer)
    return engaged

def main():
    print "male preferences female preferences"
    for p_key, a_key in zip(sorted(proposer_preferences), sorted(acceptor_preferences)):
        print "%s: %s   %s: %s" % (p_key, proposer_preferences[p_key], a_key, acceptor_preferences[a_key]) 

    print('\nEngagements:')
    engaged = match()
     
    print('\nCouples:')
    print('  ' + ',\n  '.join('(%s,%s)' % couple
                              for couple in sorted(engaged.items())))
main()