"""
Module for computing with temperatures.
Symbols: C is Celsius, F is Fahrenheit, K is Kelvin.
Given one parameter, the other can be computed as follows:
    F = C2F(C)
    C = F2C(F)
    K = C2K(C)
    C = K2C(K)
    K = F2K(F)
    F = K2F(K)
"""


def C2F(C):
    F = (C * (9 / 5)) + 32
    return F


def F2C(F):
    C = (5 / 9) * (F - 32)
    return C


def C2K(C):
    K = C + 273.15
    return K


def K2C(K):
    C = K - 273.15
    return C


def F2K(F):
    K = (F - 32) * (5 / 9) + 273.15
    return K


def K2F(K):
    F = (K - 273.15) * (9 / 5) + 32
    return F
