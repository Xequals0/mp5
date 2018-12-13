import inspect
import sys
import numpy as np
import pygame as pg
import matplotlib as mpl
import matplotlib.pyplot as pyp

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
    holder = []
    myLambda = 1.0

    # H and H^T are 2x2 identity matrices, not included here because they do not affect the calculations in this case
    pEstimate = np.eye(2, dtype=float)
    pEstimate = pEstimate.dot(myLambda)

    I = np.eye(2, dtype=float)
    H = np.array([1.0, 1.0])
    H_T = np.array([[1.0],[1.0]])
    Q = np.array([[10.0**(-4.0), 2.0*(10.0**(-5.0))], [2.0*(10.0**(-5.0)), 10.0**(-4.0)]])
    R = np.array([[10.0**(-2.0), 5.0*(10.0**(-3.0))], [5.0*(10.0**(-3.0)), 2.0*(10.0**(-2.0))]])
    #Check what the values should be. Already confirmed this should be a 2x1 matrix
    initialGuess = np.array([[1.0],[1.0]])
    xkPrev = initialGuess.dot(myLambda)

    u1Prev = data[0][0]
    u2Prev = data[0][1]
    uPrev = np.array([[u1Prev], [u2Prev]])

    isFirstItem = True
    partialData = data[0:5]

    for item in data:
        u = np.array([[data[0][0]], [data[0][1]]])
        z = np.array([[data[0][2]], [data[0][3]]])

        #Prediction step
        xk = np.add(xkPrev, u)
        pk = np.add((H.dot(pEstimate)).dot(H_T), Q)

        #Update step
        kGainNumerator = pk.dot(H_T)
        kGainDenominator = np.add((H.dot(pk)).dot(H_T), R)
        kGain = np.divide(kGainNumerator, kGainDenominator)

        xkPrev = np.add(xk, kGain.dot(np.subtract(z, H.dot(xk))))
        pEstimate = np.subtract(pk, (kGain.dot(H)).dot(pk))

        Q = np.subtract(Q, kGain.dot(Q))
        R = np.subtract(R, kGain.dot(R))

        holder.append(xk)


        
    for npArray in holder:
        listForm = npArray.tolist()
        estimated.append(listForm)

    return estimated

'''
Plotting
'''
def plot(data, output):
    # Your code starts here
    # You should remove _raise_not_defined() after you complete your code

    k = []
    x1 = []
    x2 = []
    z1 = []
    z2 = []

    print str(len(output))
    for i in range(0, len(output)):
        k.append(i)
        x1.append(output[i][0][0])
        x2.append(output[i][1][0])
        z1.append(data[i][2])
        z2.append(data[i][3])
    
    lx1 = pyp.plot(k, x1, 'b')
    lx2 = pyp.plot(k, x2, 'r')
    lz1 = pyp.plot(k, z1, 'g')
    lz2 = pyp.plot(k, z2, 'm')
    pyp.xlabel("k")
    pyp.ylabel("x, z")
    pyp.legend(["x1", "x2", "z1", "z2"])
    
    pyp.show()
    # Your code ends here 
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


