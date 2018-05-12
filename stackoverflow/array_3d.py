
import numpy as np

def set_value():
    a = np.random.rand(3, 3, 3)
    
    print a
    
    for i in range(0, len(a)):
        if len(a[i][a[i] < 0.2]) > 0:
            a[i] = 0.2
    
    print a