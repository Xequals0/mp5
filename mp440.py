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

    # H and H^T are 2x2 identity matrices, not included here because they do not affect the calculations in this case
    pPrev = np.array([[1, 0], [0, 1]])

    I = np.eye(2, dtype=float)
    H = np.eye(2, dtype=float)
    H_T = np.eye(2, dtype=float)
    Q = np.array([[10.0**(-4.0), 2.0*(10.0**(-5.0))], [2.0*(10.0**(-5.0)), 10.0**(-4.0)]])
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
        #TODO: Modify to include z?
        xk = np.add(xkPrev, kGain.dot(np.subtract(uPrev, xkPrev)))
        
        estimated.append(xk.tolist())

        xkPrev = xk
        uPrev = np.array([[item[0]], [item[1]]])
        pPrev = P + Q
        
       
    #print
    #print "ESTIMATED:"
    #for pair in estimated:
    #    print str(pair)
    #print str(estimated)

    return estimated

'''
Plotting
'''
def plot(data, output):
    # Your code starts here
    # You should remove _raise_not_defined() after you complete your code
    k = []
    z1 = []
    z2 = []
    x1 = []
    x2 = []

    for i in range(1, len(data)):
        k.append(i)
        z1.append(data[i][2])
        z2.append(data[i][3])
        #x1.append(output[i])

    for row in output:
        x1.append(row[0][0])
        x2.append(row[1][0])

    '''
    print "x1:"
    for line in x1:
        print str(line)
    '''
    
    pyp.plot(k, z1, 'b')
    pyp.plot(k, z2, 'b--')
    pyp.plot(k, x1, 'r')
    pyp.plot(k, x2, 'r--')
    
    '''
    pyp.plot(x1, x2, 'r')
    pyp.plot(z1, z2, 'b')
    '''
    
    pyp.show()
    # Your code ends here 
    #_raise_not_defined()
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


