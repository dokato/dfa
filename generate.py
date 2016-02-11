import numpy as np
import matplotlib.pyplot as plt
from dfa import dfa

###
# is alpha really DFA alpha ??
##

def power_law_noise(n, alpha, var):
    '''
    
    Based on:
    N. Jeremy Kasdin, Discrete simulation of power law noise (for oscillator stability evaluation)
    Supporitng with a Matlab code: https://people.sc.fsu.edu/~jburkardt/m_src/cnoise/cnoise.html
    '''
    # computing standard deviation from variance
    stdev = np.sqrt(np.abs(var))
    
    hfa = np.zeros(2*n)
    hfa[0] = 1
    for i in range(1,n):
        hfa[i] = hfa[i-1] * (0.5*alpha + (i-1))/(i)
    
    # sample white noise
    wfa = np.hstack((stdev * np.random.randn(n), np.zeros(n)))
    
    fh = np.fft.fft(hfa)
    fw = np.fft.fft(wfa)
    
    fh = fh[1:n+1]
    fw = fw[1:n+1]
    
    ftot = fh * fw
    
    # matching the conventions of the Numerical Recipes
    
    ftot[1]  /= 2
    ftot[-1] /= 2

    ftot = np.hstack((ftot, np.zeros(n-1)))
    
    x = np.fft.ifft(ftot)
    
    return 2.* np.real(x[:n])

x1 = power_law_noise(2048, 0.5, 3)
x2 = power_law_noise(2048, 0.7, 3)
x3 = power_law_noise(2048, 1.2, 3)

plt.subplot(311)
plt.plot(x1)
plt.subplot(312)
plt.plot(x2)
plt.subplot(313)
plt.plot(x3)

plt.show()

scales, fluct, alpha = dfa(x3, show=1)
print scales
print fluct
print "DFA exponent: {}".format(alpha)
