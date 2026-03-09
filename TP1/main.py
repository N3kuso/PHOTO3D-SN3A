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

    # Display the 3D plotting window
    plt.show()

if __name__ == "__main__":
    main()