from __future__ import division
def get_at_content2(dna):
	length= len(dna)
    a_count= dna.count('A')
    t_count= dna.count('T')
    at_content= (a_count +t_count) / length
    return at_content
