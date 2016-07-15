import numpy as np
import scipy as sp

poll = open ('UN_voting_data.txt')
l = [ map(str,line.split(' ')) for line in poll ]

a = np.row_stack(l)
trans = a.transpose()



print a
print trans

