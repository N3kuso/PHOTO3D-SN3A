import matplotlib.pyplot as plt

def main():
    # Initialize a new Plotting window
    plt.figure(figsize=(10, 10))
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


    p=(4.0,3.0,2.0)
    print(f"p : {p}")
    plt.plot(p[0],p[1],p[2], marker='o', color='black')

    translate_vector=(0.0,1.0,1.0)
    p= translate_point(p,translate_vector[0], translate_vector[1], translate_vector[2])
    print(f"p : {p}")

    plt.plot(p[0],p[1],p[2], marker='o', color='red')

    # Display the 3D plotting window
    plt.show()

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


if __name__ == "__main__":
    main()