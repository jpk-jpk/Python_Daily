import sys
import numpy as np

def mysum():
    """To give a brief the default command line arguments are stored in to sys.argv variable, it holds all the values.
    Command line arguments are differed by spaces with each space give one variable
    If you want to use single argument command don't use spaces in single argument use comma and
    use string.split(',') method to separate values"""
    inpv = float(sys.argv[1])
    print(f'The sum of all the integers, {inpv}')
    sumx = 0.0
    for number in range(int(inpv)):
        sumx += number
    print(sumx)
    sumx = 0.0
    nop = int(inpv)
    for number in np.linspace(0.0,inpv,nop,endpoint=False, dtype=float):
        sumx += number
    print(sumx)

mysum()

