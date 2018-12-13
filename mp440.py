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
    #holder.append(xkPrev)

    u1Prev = data[0][0]
    u2Prev = data[0][1]
    uPrev = np.array([[u1Prev], [u2Prev]])

    #holder.append(initialGuess)

    isFirstItem = True
    partialData = data[0:5]


    
    for item in data:
        '''
        if(isFirstItem):
            isFirstItem = False
            continue
        '''
        u = np.array([[data[0][0]], [data[0][1]]])
        z = np.array([[data[0][2]], [data[0][3]]])

        #Prediction step
        xk = np.add(xkPrev, u)
        pk = np.add((H.dot(pEstimate)).dot(H_T), Q)

        #Update step
        kGainNumerator = pk.dot(H_T)
        kGainDenominator = np.add((H.dot(pk)).dot(H_T), R)
        kGain = np.divide(kGainNumerator, kGainDenominator)

        print
        print "kGain: " + str(kGain)
        print "z: " + str(z)
        print "xk: " + str(xk)
        print "H: " + str(H)
        print "H.xk: " + str(H.dot(xk))
        print "Q: " + str(Q)
        print "R: " + str(R)
        print

        xkPrev = np.add(xk, kGain.dot(np.subtract(z, H.dot(xk))))
        pEstimate = np.subtract(pk, (kGain.dot(H)).dot(pk))

        Q = np.subtract(Q, kGain.dot(Q))
        R = np.subtract(R, kGain.dot(R))

        holder.append(xk)


        
    for npArray in holder:
        listForm = npArray.tolist()
        print "listForm: " + str(listForm)
        estimated.append(listForm)

    print "ESTIMATED: " + str(estimated)
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
    x1 = []
    x2 = []
    z1 = []
    z2 = []

    print str(len(output))
    for i in range(0, len(output)):
        #print str(i)
        k.append(i)
        x1.append(output[i][0][0])
        x2.append(output[i][1][0])
        z1.append(data[i][2])
        z2.append(data[i][3])

    '''
    pyp.plot(x1, x2, 'b')
    pyp.plot(z1, z2, 'r')
    '''

    
    pyp.plot(k, x1, 'b')
    pyp.plot(k, x2, 'r')
    pyp.plot(k, z1, 'g')
    pyp.plot(k, z2, 'm')
    



    '''
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

    '''
    print "x1:"
    for line in x1:
        print str(line)
    '''
    
    '''
    pyp.plot(k, z1, 'b')
    pyp.plot(k, z2, 'b--')
    pyp.plot(k, x1, 'r')
    pyp.plot(k, x2, 'r--')

    pyp.plot(k, output[row][0][0], 'g')
    '''
    
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


