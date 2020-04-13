import numpy as np


def conv(A, B):
    FA = np.fft.rfft(A, 2*(N+1))
