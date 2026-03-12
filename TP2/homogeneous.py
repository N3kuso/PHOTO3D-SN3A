import matplotlib.pyplot as plt
import numpy as np

def init_3d_axes(title="3D Scene"):
    """Initialise une fenêtre matplotlib 3D avec les paramètres standards."""
    fig = plt.figure(figsize=(10, 10))
    fig.suptitle(title, fontsize=14)
    axes = plt.axes(projection="3d", proj_type='ortho')
 
    axes.set_xlim(-10, 10)
    axes.set_ylim(-10, 10)
    axes.set_zlim(-10, 10)
 
    axes.set_xlabel('X')
    axes.set_ylabel('Y')
    axes.set_zlabel('Z')
 
    axes.xaxis.label.set_color('red')
    axes.yaxis.label.set_color('green')
    axes.zaxis.label.set_color('blue')
 
    axes.tick_params(axis='x', colors='red')
    axes.tick_params(axis='y', colors='green')
    axes.tick_params(axis='z', colors='blue')
 
    return axes

def draw_referential(axes):
    """
    Dessine le repère 3D avec :
    - X en rouge, Y en vert, Z en bleu
    - Partie positive en trait plein, partie négative en tirets
    """
    length = 8
 
    # Axe X (rouge)
    axes.plot([0, length], [0, 0], [0, 0], color='red',   linestyle='solid')
    axes.plot([0, -length], [0, 0], [0, 0], color='red',  linestyle='dashed')
 
    # Axe Y (vert)
    axes.plot([0, 0], [0, length], [0, 0], color='green',  linestyle='solid')
    axes.plot([0, 0], [0, -length], [0, 0], color='green', linestyle='dashed')
 
    # Axe Z (bleu)
    axes.plot([0, 0], [0, 0], [0, length], color='blue',   linestyle='solid')
    axes.plot([0, 0], [0, 0], [0, -length], color='blue',  linestyle='dashed')

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

def rot_x_point(point, omega):
    """
Function that takes in parameter an homegeneous vector that represents a point (x,y,z)
and returns the homogeneous vector that represents the rotated point around X axis by an angle omega (expressed in radians).
    """
    c, s = np.cos(omega), np.sin(omega)
    Rx = np.array([
        [1,  0,  0,  0],
        [0,  c, -s,  0],
        [0,  s,  c,  0],
        [0,  0,  0,  1]
    ])
    
    result = Rx.dot(point.T)

    print(f""" Function rot_x_point :
Rotation matrix : {Rx}
Point : {point}
Result : {result}
            """)
    
    return result

def rot_y_point(point, phi):
    """
Function that takes in parameter an homegeneous vector that represents a point (x,y,z)
and returns the homogeneous vector that represents the rotated point around Y axis by an angle phi (expressed in radians).
    """
    c, s = np.cos(phi), np.sin(phi)
    Ry = np.array([
        [c, 0,  s,  0],
        [0, 1, 0,  0],
        [-s, 0, c,  0],
        [0, 0,  0,  1]
    ])
    
    result = Ry.dot(point.T)

    print(f""" Function rot_y_point :
Rotation matrix : {Ry}
Point : {point}
Result : {result}
            """)
    return result

def rot_z_point(point, kappa):
    """
Function that takes in parameter an homegeneous vector that represents a point (x,y,z)
and returns the homogeneous vector that represents the rotated point around Z axis by an angle kappa (expressed in radians).
    """
    c, s = np.cos(kappa), np.sin(kappa)
    Rz = np.array([
        [c, -s, 0, 0],
        [s, c, 0,  0],
        [0, 0, 1,  0],
        [0, 0,  0, 1]
    ])
    
    result = Rz.dot(point.T)

    print(f""" Function rot_z_point :
Rotation matrix : {Rz}
Point : {point}
Result : {result}
            """)
    return result

def rot_point(point, omega, phi, kappa):
    """
Function that takes in parameter an homegeneous vector that represents a point (x,y,z) 
and returns the homogeneous vector that represents the rotated point around the three axis X, Y and Z axis by angles omega, phi and kappa respectively (expressed in radians).
    """
    cx, sx = np.cos(omega), np.sin(omega)
    cy, sy = np.cos(phi),   np.sin(phi)
    cz, sz = np.cos(kappa), np.sin(kappa)

    R = np.array([
        [cz*cy, (cz*sy*sx)-(sz*cx), (cz*sy*cx)+(sz*sx), 0],
        [sz*cy, (sz*sy*sx)+(cz*cx), (sz*sy*cx)-(cz*sx),  0],
        [-sy, cy*sx, cy*cx,  0],
        [0, 0,  0, 1]
    ])

    result = R.dot(point.T)

    print(f""" Function rot_point :
Rotation matrix : {R}
Point : {point}
Result : {result}
            """)
    return result

def rot_point_comp(point, omega, phi, kappa):
    """
Function that takes in parameter an homegeneous vector that represents a point (x,y,z) 
and returns the homogeneous vector that represents the rotated point around the three axis X, Y and Z axis by angles omega, phi and kappa respectively (expressed in radians).
Using the comp version    
    """

    result = rot_x_point(point, omega)
    result = rot_y_point(result, phi)
    result = rot_z_point(result, kappa)

    print(f""" Function rot_point_comp :
Point : {point}
Result : {result}
            """)
    
    return result

def scale_point(point, sx, sy, sz):
    """
Function that takes in parameter an homegeneous vector that represents a point (x,y,z)
and returns the homogeneous vector that represents the scaled point along the three axis X, Y 
and Z axis by factors sx, sy and sz respectively.
    """
    S = np.array([
        [sx, 0, 0, 0],
        [0, sy, 0, 0],
        [0, 0, sz, 0],
        [0, 0,  0, 1]
    ])

    result = S.dot(point.T)

    print(f""" Function scale_point :
Scale matrix : {S}
Point : {point}
Result : {result}
            """)
    return result

def create_transform(tx, ty, tz, sx, sy, sz, omega, phi, kappa) -> np.array:
    """
    Function that takes in parameter translation parameters tx, ty and tz, scale parameters sx, sy and sz and rotation angles omega, phi and kappa 
    and that return a 4 x 4 np.array that represent the combined homogeneous transform matrix
    F = T(tx,ty,tz) @ S(sx,sy,sz) @ Rz(kappa) @ Ry(phi) @ Rx(omega)
  
    Input:
        tx, ty, tz (float): Translation along X, Y, Z.
        sx, sy, sz (float): Scale factors along X, Y, Z.
        omega (float)      : Rotation around X axis in radians.
        phi   (float)      : Rotation around Y axis in radians.
        kappa (float)      : Rotation around Z axis in radians.
 
    Output:
        np.array: 4x4 transformation matrix.
    """
    co, so = np.cos(omega), np.sin(omega)
    cp, sp = np.cos(phi),   np.sin(phi)
    ck, sk = np.cos(kappa), np.sin(kappa)
 
    F = np.array([
        [sx*ck*cp,  sx*(ck*sp*so - sk*co),  sx*(ck*sp*co + sk*so),  tx],
        [sy*sk*cp,  sy*(sk*sp*so + ck*co),  sy*(sk*sp*co - ck*so),  ty],
        [-sz*sp,    sz*cp*so,               sz*cp*co,               tz],
        [0,         0,                       0,                      1 ]
    ])
 
    return F

### MAIN ###
# Exercise 5
print("""
######################
#     EXERCISE 5     #
######################
            """)
v_euclidian = (1.0, 2.0, 3.0)
v_homogeneous = toHomogeneous(v_euclidian)

# Exercise 6
print("""
######################
#     EXERCISE 6     #
######################
            """)
v_homogeneous_bis=(2.0,4.0,6.0,2.0)
v_euclidian_bis= toEuclidean(v_homogeneous_bis)

# Exercise 7
print("""
######################
#     EXERCISE 7     #
######################
            """)
point=(4.0,3.0,2.0)
point=toHomogeneous(point)
translate_vector=(0.0,1.0,1.0)

point_translated=toEuclidean(translate_point_hc(point, *translate_vector))

px, py, pz = toEuclidean(point)
tx, ty, tz = point_translated

axes = init_3d_axes(title="Exercice 7")
draw_referential(axes)

axes.plot(px, py, pz,  marker='o', color='black', markersize=8, label="Original")
axes.plot(tx, ty, tz, marker='o', color='red',   markersize=8, label="Translated")
axes.legend()
#plt.show()

# Exercise 8
print("""
######################
#     EXERCISE 8     #
######################
            """)
point=(4.0, 3.0, 2.0)
point=toHomogeneous(point)
rotation_angle=np.pi/6

point_rotated=toEuclidean(rot_x_point(point, rotation_angle))

px, py, pz = toEuclidean(point)
rx, ry, rz = point_rotated

axes = init_3d_axes(title="Exercice 8")
draw_referential(axes)

axes.plot(px, py, pz,  marker='o', color='black', markersize=8, label="Original")
axes.plot(*point_rotated, marker='o', color='red',   markersize=8, label="Rx(π/6)")
axes.legend()
#plt.show()

# Exercise 9
print("""
######################
#     EXERCISE 9     #
######################
            """)
point=(4.0, 3.0, 2.0)
point=toHomogeneous(point)
rotation_angle=np.pi/7

point_rotated=toEuclidean(rot_y_point(point, rotation_angle))

px, py, pz = toEuclidean(point)
rx, ry, rz = point_rotated

axes = init_3d_axes(title="Exercice 9")
draw_referential(axes)

axes.plot(px, py, pz,  marker='o', color='black', markersize=8, label="Original")
axes.plot(*point_rotated, marker='o', color='green',   markersize=8, label="Ry(π/7)")
axes.legend()
#plt.show()

# Exercise 10
print("""
######################
#     EXERCISE 10    #
######################
            """)
point=(4.0, 3.0, 2.0)
point=toHomogeneous(point)
rotation_angle=np.pi/8

point_rotated=toEuclidean(rot_z_point(point, rotation_angle))

px, py, pz = toEuclidean(point)
rx, ry, rz = point_rotated

axes = init_3d_axes(title="Exercice 10")
draw_referential(axes)

axes.plot(px, py, pz,  marker='o', color='black', markersize=8, label="Original")
axes.plot(*point_rotated, marker='o', color='blue',   markersize=8, label="Ry(π/8)")
axes.legend()
#plt.show()

# Exercise 11
print("""
######################
#     EXERCISE 11    #
######################
            """)
point=(4.0, 3.0, 2.0)
point=toHomogeneous(point)
rotation_angle_vector=(np.pi/6, np.pi/7,np.pi/8) #alpha, beta, gamma

point_rotated=toEuclidean(rot_point(point, *rotation_angle_vector))
point_rotated_comp=toEuclidean(rot_point_comp(point, *rotation_angle_vector))

px, py, pz = toEuclidean(point)
rx, ry, rz = point_rotated
r2x, r2y, r2z = point_rotated_comp

axes = init_3d_axes(title="Exercice 11")
draw_referential(axes)

axes.plot(px, py, pz,  marker='o', color='black', markersize=8, label="Original")
axes.plot(*point_rotated, marker='o', color='red',   markersize=8, label="R(π/6, π/7, π/8)")
axes.plot(*point_rotated_comp, marker='+', color='orange',   markersize=8, label="Rcomp(π/6, π/7, π/8)")
axes.legend()
#plt.show()

# Exercise 12
print("""
######################
#     EXERCISE 12    #
######################
            """)
point=(4.0, 3.0, 2.0)
point=toHomogeneous(point)
scale_vector=(0.5,1.5,1.0)

point_scaled=toEuclidean(scale_point(point, *scale_vector))

px, py, pz = toEuclidean(point)
sx, sy, sz = point_scaled

axes = init_3d_axes(title="Exercice 12")
draw_referential(axes)

axes.plot(px, py, pz,  marker='o', color='black', markersize=8, label="Original")
axes.plot(*point_scaled, marker='+', color='purple',   markersize=8, label="S(0.5,1.5,1.0)")
axes.legend()
plt.show()

# Exercise 13
print("\n" + "#" * 60)
print("Exercise 13 — create_transform")
print("#" * 60)

# Pure rotation (tx=ty=tz=0, sx=sy=sz=1)
F_rot = create_transform(0, 0, 0, 1, 1, 1, np.pi/6, np.pi/7, np.pi/8)
print("Pure rotation (tx=ty=tz=0, sx=sy=sz=1):")
print(np.round(F_rot, 4))

# Pure translation (omega=phi=kappa=0, sx=sy=sz=1)
F_trans = create_transform(1, 2, 3, 1, 1, 1, 0, 0, 0)
print("\nPure translation (angles=0, sx=sy=sz=1):")
print(np.round(F_trans, 4))

# Pure scale (omega=phi=kappa=0, tx=ty=tz=0)
F_scale = create_transform(0, 0, 0, 2, 3, 4, 0, 0, 0)
print("\nPure scale (angles=0, tx=ty=tz=0):")
print(np.round(F_scale, 4))

# Rigid body (sx=sy=sz=1)
F_rigid = create_transform(1, 2, 3, 1, 1, 1, np.pi/6, np.pi/7, np.pi/8)
print("\nRigid body (sx=sy=sz=1):")
print(np.round(F_rigid, 4))