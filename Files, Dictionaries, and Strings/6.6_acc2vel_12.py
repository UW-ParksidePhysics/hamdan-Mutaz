from numpy import array, zeros, loadtxt
import matplotlib.pyplot as mp

def velocity(a, dt):
    n = len(a)
    v = zeros(n)
    for k in range(1, n):
        v[k] = v[k-1] + (a[k-1] + a[k]) / 2
    v = v * dt
    return v


a = loadtxt('acc.txt')
dt = 0.1
v = velocity(a, dt)
t = array([i * dt for i in range(0, len(a))])

mp.plot(t, a)
mp.plot(t, v)
mp.show()
© 2020 GitHub, Inc.
