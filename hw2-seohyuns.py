import numpy as np
import scipy as sp

poll = open ('UN_voting_data.txt')
l = [ map(str,line.split(' ')) for line in poll ]

for i in range(len(l)):
	del l[i][0]


a = np.row_stack(l)
trans = a.transpose()

M= a * trans
#np.dot(a,trans)

print a
print trans
print M

