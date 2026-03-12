import matplotlib.pyplot as plt
import numpy as np

def toHomogeneous(v: tuple) -> np.array:
    """
    Input:
        v : tuple
    Output
        result = np.array

    Function that that takes in parameter a tuple v representing a vector expressed within homogeneous coordinates 
    and that returns a np.array representing the equivalent vector within Euclidean coordinates
    """
    result = np.array(list(v) + [1])
    print(f"""Function toHomogeneous :
        Input > v : {v}
        Output > {result}
          """)
    return result

### MAIN ###
# Exercise 5
v_euclidian = (1.0, 2.0, 3.0)
v_homogeneous = toHomogeneous(v_euclidian)


