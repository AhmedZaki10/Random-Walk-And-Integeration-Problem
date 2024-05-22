#!/usr/bin/env python
# coding: utf-8

# In[4]:


#Random Walk
import pandas as pd
import matplotlib.pyplot as plt

# Define probabilities and corresponding directions
probabilities = {
    'F': 0.5,  # Forward
    'L': 0.3,  # Left
    'R': 0.2   # Right
}

# Given random numbers
random_numbers = [6, 2, 0, 6, 8, 5, 7, 7, 9, 8, 4, 8, 2, 6, 2, 1, 3, 9, 8, 4]

# Initial position
position = [0, 0]

# Lists to store step, random number, direction, x-coordinate, and y-coordinate
steps = []
directions = []
x_coords = []
y_coords = []

# Simulate motion for each random number
for step, num in enumerate(random_numbers, start=1):
    steps.append(step)
    cumulative_prob = 0
    rand_prob = num / 10.0  # Convert single-digit random numbers to probabilities
    
    # Determine direction based on random number
    for d, prob in probabilities.items():
        cumulative_prob += prob
        if rand_prob < cumulative_prob:
            direction = d
            directions.append(direction)
            break

    # Update position based on direction
    if direction == 'F':
        position[1] += 1  # Move forward in Y-direction
    elif direction == 'L':
        position[0] -= 1  # Move left in X-direction
    elif direction == 'R':
        position[0] += 1  # Move right in X-direction
    
    # Append current position to coordinate lists
    x_coords.append(position[0])
    y_coords.append(position[1])

# Create a DataFrame to display the information
df = pd.DataFrame({
    'Step': steps,
    'Random Number': random_numbers,
    'Direction': directions,
    'X-coordinate': x_coords,
    'Y-coordinate': y_coords
})

# Display the DataFrame
print(df)
# Plot the motion
plt.figure(figsize=(8, 6))
plt.plot(x_coords, y_coords, marker='o', linestyle='-', color='b')
plt.scatter(x_coords[-1], y_coords[-1], color='r', label='Final Position')
plt.title('Drunkard\'s Walk Simulation')
plt.xlabel('X-coordinate')
plt.ylabel('Y-coordinate')
plt.legend()
plt.grid(True)
plt.show()

print("Final Position:", tuple(position))


# In[5]:


#Numerical Integration 

import pandas as pd

# Define the known area of the rectangle
A = 3 * 140

# Given random numbers for x and y coordinates
random_numbers_x = [22, 25, 18, 45, 25, 27, 48, 43, 40, 47]
random_numbers_y = [0.57, 0.18, 0.00, 0.90, 0.05, 0.77, 0.66, 0.10, 0.76, 0.42]

# Initialize counters for points inside the curve (M) and total points (N)
M = 0
N = len(random_numbers_x)

# Lists to store the results for the simulation table
x_coordinates = []
y_coordinates = []
x_cubed = []
M_counters = []
N_counters = []

# Iterate through the random numbers to generate coordinates and perform the check
for random_x, random_y in zip(random_numbers_x, random_numbers_y):
    # Calculate x-coordinate
    x_coord = 0.1 * random_x
    
    # Calculate y-coordinate
    y_coord = random_y * 140
    
    # Calculate x^3
    x_cube = x_coord ** 3
    
    # Check if the point is under the curve and update M counter
    if y_coord <= x_cube:
        M += 1
    
    # Append results to lists
    x_coordinates.append(x_coord)
    y_coordinates.append(y_coord)
    x_cubed.append(x_cube)
    M_counters.append(M)
    N_counters.append(len(M_counters))

# Create a DataFrame to display the simulation table
simulation_table = pd.DataFrame({
    'Random number of x coordinates': random_numbers_x,
    'X-coordinate': x_coordinates,
    'Random number of y coordinate': random_numbers_y,
    'Y-coordinate': y_coordinates,
    'x^3': x_cubed,
    'M': M_counters,
    'N': N_counters
})

# Display the simulation table and the estimated value of the integral
print("\nEstimated Value of the Integral:", (M / N) * A)
Simu_Table = simulation_table.style.set_properties(**{'text-align': 'center'})                                          
Simu_Table


# In[ ]:




