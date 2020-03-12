# Original
# x=1; print ’sin(%g)=%g’ % (x, sin(x))

# Fixed
from math import sin; x = 1; print('sin(%g)=%g' % (x, sin(x)))

# 1) imported sin from math
# 2) placed parentheses around what was intended to print
# 3) replaced old commas with proper functioning commas
