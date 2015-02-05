#! /usr/bin/python
from __future__ import division

length= len(dna)
def get_at_content2(dna):
    a_count= dna.count('A,a')
    t_count= dna.count('T,t')
    at_content= (a_count +t_count) / length
    return at_content
    m=re.finditer(r"T",dna)
    for T in m:
    	T_startpos=T.start()
    	T_endpos=T.end()
    	print("T positions" + str(T_startpos) + "to" +str(T_endpos))
    n=re.finditer(r"A",dna)
    for A in n:
        A_startpos=A.start()
    	A_endpos=A.end()
    	print("A positions" + str(A_startpos) + "to" +str(A_endpos))


