from math import sin, cos, pi

x = pi / 4
VAL = (sin(x)) ** 2 + (cos(x)) ** 2
print(VAL)

# imported pi from math
# switched " ^ " to " ** "
# placed the exponent on (sin(x)), rather than sin
# placed parentheses around what was intended to be printed
# Changed 1_val and 1_VAL to val and VAL respectively
# synchronized val and VAL under the same case

v0 = 3
t = 1
a = 2
s = v0 * t + 0.5 * a * t ** 2
print(s, "m")

# removed units and returned them when printed
# placed parentheses around what was intended to be printed
# switched " . " with " * "

a = 3.3
b = 5.3

a2 = a ** 2
b2 = b ** 2

eq1_sum = a2 + (2 * a * b) + b2
eq2_sum = a2 - (2 * a * b) + b2

eq1_pow = (a + b) ** 2
eq2_pow = (a - b) ** 2

print('First equation: %f = %f' % (eq1_sum, eq1_pow))
print('Second equation: %g = %g' % (eq2_pow, eq2_pow))

# switched " , " with " . " when used in place of decimals
# placed parentheses around what was intended to be printed
# switched "g" with "f" and "h" with "g"
# removed "," before the "%"
# moved a and b to their own respective lines
