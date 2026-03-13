import matplotlib.pyplot as plt
import math

def main():
    # Initialize a new Plotting window
    plt.figure(1, figsize=(10, 10))
    # Initializing 3D capabilities
    axes = plt.axes(projection="3d", proj_type='ortho')
    # Setting axis properties
    axes.set_xlim(-10, 10) # X Axis graduation
    axes.set_ylim(-10, 10) # Y Axis graduation
    axes.set_zlim(-10, 10) # Z Axis graduation
    axes.set_xlabel('X') # X Axis label
    axes.set_ylabel('Y') # Y Axis label
    axes.set_zlabel('Z') # Z Axis label
    axes.xaxis.label.set_color('red') # X Axis color
    axes.yaxis.label.set_color('green') # Y Axis color
    axes.zaxis.label.set_color('blue') # Z Axis color
    axes.tick_params(axis='x', colors='red') # X Axis graduation color
    axes.tick_params(axis='y', colors='green') # Y Axis graduation color
    axes.tick_params(axis='z', colors='blue') # Z Axis graduation color
    
    ## Exercise 2
    origin_point=(0,0,0)

    # X points
    x_pos=(10,0,0)
    x_neg=(-10,0,0)

    # Y points
    y_pos=(0,10,0)
    y_neg=(0,-10,0)

    # Z points
    z_pos=(0,0,10)
    z_neg=(0,0,-10)

    # Draw X referential axis
    plt.plot([origin_point[0] , x_pos[0]],[origin_point[1] , x_pos[1]],[origin_point[2] , x_pos[2]], color='red', linestyle='solid')
    plt.plot([origin_point[0] , x_neg[0]],[origin_point[1] , x_neg[1]],[origin_point[2] , x_neg[2]], color='red', linestyle='dashed')

    # Draw Y referential axis
    plt.plot([origin_point[0] , y_pos[0]],[origin_point[1] , y_pos[1]],[origin_point[2] , y_pos[2]], color='green', linestyle='solid')
    plt.plot([origin_point[0] , y_neg[0]],[origin_point[1] , y_neg[1]],[origin_point[2] , y_neg[2]], color='green', linestyle='dashed')

    # Draw X referential axis
    plt.plot([origin_point[0] , z_pos[0]],[origin_point[1] , z_pos[1]],[origin_point[2] , z_pos[2]], color='blue', linestyle='solid')
    plt.plot([origin_point[0] , z_neg[0]],[origin_point[1] , z_neg[1]],[origin_point[2] , z_neg[2]], color='blue', linestyle='dashed')

    ## Exercise 3
    p=(4.0,3.0,2.0)
    print(f"p : {p}")
    plt.plot(p[0],p[1],p[2], marker='o', color='cyan')

    translate_vector=(0.0,1.0,1.0)
    p_translate= translate_point(p,translate_vector[0], translate_vector[1], translate_vector[2])
    print(f"p_translate : {p_translate}")
    plt.plot(p_translate[0],p_translate[1],p_translate[2], marker='o', color='yellow')

    ## Exercise 4
    p=(4.0, 4.0, 4.0)
    print(f"p : {p}")
    plt.plot(p[0],p[1],p[2], marker='o', color='black')

    # Rotation X
    p_rotx=rot_x_point(p, math.pi/4)
    print(f"p_rotx : {p_rotx}")
    plt.plot(p_rotx[0],p_rotx[1],p_rotx[2], marker='o', color='red')

    # Rotation Y
    p_roty=rot_y_point(p, math.pi/4)
    print(f"p_roty : {p_roty}")
    plt.plot(p_roty[0],p_roty[1],p_roty[2], marker='o', color='green')

    # Rotation Z
    p_rotz=rot_z_point(p, math.pi/4)
    print(f"p_rotz : {p_rotz}")
    plt.plot(p_rotz[0],p_rotz[1],p_rotz[2], marker='o', color='blue')

    ## Exercice 7
    # Rotation by all angles
    p_rot= rot_point(p, math.pi/4, math.pi/4, math.pi/4)
    print(f"p_rot : {p_rot}")
    plt.plot(p_rot[0],p_rot[1],p_rot[2], marker='+', color='orange')

    ## Exercice 8
    # Rotation by all angles
    p_rot_comp= rot_point_comp(p, math.pi/4, math.pi/4, math.pi/4)
    print(f"p_rot_comp : {p_rot_comp}")
    plt.plot(p_rot_comp[0],p_rot_comp[1],p_rot_comp[2], marker='x', color='purple')

    ## Exercice 9
    # Initialize a new Plotting window
    plt.figure(2, figsize=(10, 10))
    # Initializing 3D capabilities
    axes = plt.axes(projection="3d", proj_type='ortho')
    # Setting axis properties
    axes.set_xlim(-10, 10) # X Axis graduation
    axes.set_ylim(-10, 10) # Y Axis graduation
    axes.set_zlim(-10, 10) # Z Axis graduation
    axes.set_xlabel('X') # X Axis label
    axes.set_ylabel('Y') # Y Axis label
    axes.set_zlabel('Z') # Z Axis label
    axes.xaxis.label.set_color('red') # X Axis color
    axes.yaxis.label.set_color('green') # Y Axis color
    axes.zaxis.label.set_color('blue') # Z Axis color
    axes.tick_params(axis='x', colors='red') # X Axis graduation color
    axes.tick_params(axis='y', colors='green') # Y Axis graduation color
    axes.tick_params(axis='z', colors='blue') # Z Axis graduation color

    # Display the 3D plotting window
    plt.show()

    # ------------------------------------------------------------------
    # Exercise 10
    # ------------------------------------------------------------------
    print("\n" + "#" * 60)
    print("Exercise 10 ")
    print("#" * 60)

    vertices = cube(3.0)
    print(f"  Cube vertices (size 3) :")
    for i, v in enumerate(vertices):
        print(f"    Vertices {i+1} : {v}")
 
    axes = init_3d_axes(title="Exercises 9 & 10 - Cube size 3")
    draw_referential(axes)
    display_cube(axes, vertices)
    plt.show()

def init_3d_axes(title="3D Scene"):
    """Initialize a matplotlib3d windows with the standard parameter"""
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
    Draw the 3D referential :
    - X in red, Y in green, Z in blue
    - Positive part -> solid, negative part -> dashed
    """
    length = 10
 
    # X axis (red)
    axes.plot([0, length], [0, 0], [0, 0], color='red',   linestyle='solid')
    axes.plot([0, -length], [0, 0], [0, 0], color='red',  linestyle='dashed')
 
    # Y axis (green)
    axes.plot([0, 0], [0, length], [0, 0], color='green',  linestyle='solid')
    axes.plot([0, 0], [0, -length], [0, 0], color='green', linestyle='dashed')
 
    # Z axis (blue)
    axes.plot([0, 0], [0, 0], [0, length], color='blue',   linestyle='solid')
    axes.plot([0, 0], [0, 0], [0, -length], color='blue',  linestyle='dashed')

def translate_point(point, alpha, beta, gamma):
    """
    Input:
        point (tuple)
        alpha (int)
        beta (int)
        gamma (int)
    Output:
        (tuple)

   Function that takes in parameter a point represented by a tuple (x, y, z) and that return a tuple that represents the translated point along vector (alpha,beta,gamma).  
    """
    return (point[0]+alpha, point[1]+beta, point[2]+gamma)

def  rot_x_point(point, omega):
    """
    takes in parameter a point represented by a 
tuple (x, y, z) and returns the tuple (xr, yr, zr) that represents the rotated point around X 
axis by an angle omega. 
    """
    x, y, z = point

    xr = x
    yr = (y*math.cos(omega))-(z*math.sin(omega))
    zr = (y*math.sin(omega))+(z*math.cos(omega))

    return (xr,yr,zr) 

def rot_y_point(point, phi):
    """
    that takes in parameter a point represented by a 
tuple (x, y, z) and returns the tuple (xr, yr, zr) that represents the rotated point around Y 
axis by an angle phi. 
    """
    x, y, z = point

    xr = (x*math.cos(phi))+(z*math.sin(phi))
    yr = y
    zr = (z*math.cos(phi))-(x*math.sin(phi))

    return (xr,yr,zr)

def rot_z_point(point, kappa):
    """
    that takes in parameter a point represented by a 
tuple (x, y, z) and returns the tuple (xr, yr, zr) that represents the rotated point around Z 
axis by an angle kappa. 
    """
    x, y, z = point

    xr = (x*math.cos(kappa))-(y*math.sin(kappa))
    yr = (x*math.sin(kappa))+(y*math.cos(kappa))
    zr = z

    return (xr,yr,zr)

def rot_point(point, omega, phi, kappa):
    """
    that takes in parameter a point 
represented by a tuple (x, y, z) and returns the tuple (xr, yr, zr) that represents the 
rotated point around X, Y and Z axis by the angles omega, phi, kappa respectively.
    """
    x, y, z = point

    xr = x*math.cos(phi)*math.cos(kappa) + y*(math.sin(omega)*math.sin(phi)*math.sin(kappa)-math.cos(omega)*math.sin(kappa)) + z*(math.cos(omega)*math.sin(phi)*math.cos(kappa)+math.sin(omega)*math.sin(kappa))
    yr = x*math.cos(phi)*math.sin(kappa)+ y*(math.sin(omega)*math.sin(phi)*math.sin(kappa)+math.cos(omega)*math.cos(kappa)) + z*(math.cos(omega)*math.sin(phi)*math.sin(kappa)-math.sin(omega)*math.cos(kappa))    
    zr = -x*math.sin(phi)+y*math.sin(omega)*math.cos(phi)+z*math.cos(omega)*math.cos(phi)

    return xr, yr, zr

def rot_point_comp(point, omega, phi, kappa):
    """
    takes in parameter a point represented by a tuple (x, y, z) and returns the tuple (xr, yr, zr) that represents the rotated point around X, Y and Z axis by the angles omega, phi, kappa respectively. 
    """
    p = rot_x_point(point, omega)
    p = rot_y_point(p, phi)
    p = rot_z_point(p, kappa)

    return p

def cube(size):
    """
    Function that takes in parameter a size and create a cube represented by an
    array of 8 tuples corresponding to its vertices
    1:(-s,-s,-s)  2:(s,-s,-s)  3:(-s,s,-s)  4:(s,s,-s)
    5:(-s,-s,s)   6:(s,-s,s)   7:(-s,s,s)   8:(s,s,s)
    """
    s = size
    return [
        (-s, -s, -s),  # 1
        ( s, -s, -s),  # 2
        (-s,  s, -s),  # 3
        ( s,  s, -s),  # 4
        (-s, -s,  s),  # 5
        ( s, -s,  s),  # 6
        (-s,  s,  s),  # 7
        ( s,  s,  s),  # 8
    ]

def display_cube(axes, vertices):
    """
    Function that take in parameter an array of tuples that
    represent the vertices of a cube and that display the cube within the 3D environment. 
    Each edge of the cube is colorized with the same color as its parallel axis :
    - Red    : parallel to X
    - Green  : parallel to Y
    - Blue   : parallel to Z
 
    
    0:(-s,-s,-s)  1:(s,-s,-s)  2:(-s,s,-s)  3:(s,s,-s)
    4:(-s,-s,s)   5:(s,-s,s)   6:(-s,s,s)   7:(s,s,s)
    """
    def edge(i, j, color):
        p1, p2 = vertices[i], vertices[j]
        axes.plot([p1[0], p2[0]], [p1[1], p2[1]], [p1[2], p2[2]],
                  color=color, linestyle='solid', linewidth=1.5)
 
    # Edges parallels to X (red)
    edge(0, 1, 'red')   
    edge(2, 3, 'red')   
    edge(4, 5, 'red')   
    edge(6, 7, 'red')   
 
    # Edges parallels to Y (green)
    edge(0, 2, 'green')  
    edge(1, 3, 'green')  
    edge(4, 6, 'green')  
    edge(5, 7, 'green')  
 
    # Edges parallels to Z (blue)
    edge(0, 4, 'blue')   
    edge(1, 5, 'blue')   
    edge(2, 6, 'blue')   
    edge(3, 7, 'blue')   

if __name__ == "__main__":
    main()