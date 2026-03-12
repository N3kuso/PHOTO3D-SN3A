import matplotlib.pyplot as plt
import numpy as np

def toHomogeneous(v: tuple) -> np.array:
    """
    Input:
        v : tuple
    Output
        result = np.array

    Function that that takes in parameter a tuple v representing a vector expressed within Euclidean coordinates 
    and that returns a np.array representing the equivalent vector within homogeneous coordinates
    """
    result = np.array(list(v) + [1.0])
    print(f"""Function toHomogeneous :
Input > v : {v}
Output > {result}
          """)
    return result

def toEuclidean(v: tuple) -> np.array:
    """
    Input:
        v : tuple
    Output
        result = np.array

    Function hat takes in parameter a tuple v representing a vector expressed within homogeneous coordinates 
    and that returns a np.array representing the equivalent vector within Euclidean coordinates
    """
    v=np.array(v)
    result= v[:-1] / v[-1]
    print(f"""Function toEuclidian :
Input > v : {v}
Output > {result}
          """)
    return result

def translate_point_hc(point, alpha, beta, gamma):
    """
    Function that takes in parameter the homogeneous representation of a point 
    and that return the homogeneous vector resulting of the translation (x,y,z) of 
    along vector (alpha, beta, gamma)
    """
    T = np.array([[1,0,0,alpha],
                 [0,1,0,beta],
                 [0,0,1,gamma],
                 [0,0,0,1]])
    
    result=T.dot(point.T)

    print(f""" Function translate_point_hc :
Translatation matrix : {T}
Point : {point}
Result : {result}
            """)
    return result

### MAIN ###
# Exercise 5
v_euclidian = (1.0, 2.0, 3.0)
v_homogeneous = toHomogeneous(v_euclidian)

# Exercise 6
v_homogeneous_bis=(2.0,4.0,6.0,2.0)
v_euclidian_bis= toEuclidean(v_homogeneous_bis)

# Exercise 7
point=(4.0,3.0,2.0)
point=toHomogeneous(point)
translate_vector=(0.0,1.0,1.0)

point_translated=toEuclidean(translate_point_hc(point, *translate_vector))


