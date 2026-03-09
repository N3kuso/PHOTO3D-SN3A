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
    # Display the 3D plotting window
    plt.show()

if __name__ == "__main__":
    main()