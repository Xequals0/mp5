import inspect
import sys
import numpy as np
import pygame as pg
import matplotlib as mp

#
'''
Raise a "not defined" exception as a reminder 
'''
def _raise_not_defined():
    print "Method not implemented: %s" % inspect.stack()[1][3]
    sys.exit(1)

'''
Kalman 2D
'''
def kalman2d(data):
    estimated = []

    # H and H^T are 2x2 identity matrices, not included here because they do not affect the calculations in this case
    pPrev = np.array([[1, 0], [0, 1]])

    I = np.eye(2, dtype=float)
    H = np.eye(2, dtype=float)
    H_T = np.eye(2, dtype=float)
    R = np.array([[10.0**(-2.0), 5.0*(10.0**(-3.0))], [5.0*(10.0**(-3.0)), 2.0*(10.0**(-2.0))]])
    #Check what the values should be. Already confirmed this should be a 2x1 matrix
    xkPrev = np.array([[0.0],[0.0]])

    z1Prev = data[0][2]
    z2Prev = data[0][3]
    zPrev = np.array([[z1Prev], [z2Prev]])

    u1Prev = data[0][0]
    u2Prev = data[0][1]
    uPrev = np.array([[u1Prev], [u2Prev]])

    pList = [pPrev]

    isFirstItem = True
    #partialData = data[0:3]
    
    for item in data:        
        if(isFirstItem):
            isFirstItem = False
            continue
        z = np.array([[item[2]],[item[3]]])
        #Update
        #kGain is a 2x2 matrix
        kGain = np.divide(pPrev.dot(H_T), np.add(H.dot(pPrev.dot(H_T)), R))
        #P is a 2x2 matrix
        P = (I - kGain.dot(H)).dot(pPrev)
        
        #xkU and xkZ are 2x1 matrices
        xk = np.add(xkPrev, kGain.dot(np.subtract(uPrev, xkPrev)))
        
        estimated.append(xk)

        xkPrev = xk
        uPrev = np.array([[item[0]], [item[1]]])
        
    print
    print "ESTIMATED:"
    for pair in estimated:
        print str(pair)
    
    return estimated

'''
Plotting
'''
def plot(data, output):
    # Your code starts here
    # You should remove _raise_not_defined() after you complete your code
    # Your code ends here 
    _raise_not_defined()
    return

'''
Kalman 2D 
'''
def kalman2d_shoot(ux, uy, ox, oy, reset=False):
    decision = (0, 0, False)
    # Your code starts here 
    # Your code ends here 
    _raise_not_defined()
    return decision

'''
Kalman 2D 
'''
def kalman2d_adv_shoot(ux, uy, ox, oy, reset=False):
    decision = (0, 0, False)
    # Your code starts here 
    # Your code ends here 
    _raise_not_defined()
    return decision


