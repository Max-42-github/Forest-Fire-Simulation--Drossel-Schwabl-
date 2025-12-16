import numpy as np 
import random
import matplotlib.pyplot as plt
from matplotlib.colors import ListedColormap

# Version 4 : 
# Visualizing with an animation
# Change is here we are considering all the eight neighbour instead of only four

# Grid Size of the forest and the growth and lightning strick Probabilities
Nsize = 300
growthProb = 0.005
lightProb = 1e-5

# Number of ticks of the simulation (End time)
totalTime = 500

# Forest Ground
forestArr = np.zeros(shape = (Nsize,Nsize), dtype = int)

# Checking for nearest neighbour to find location of propagation of fire
def neighbourCheck(forestArr,i,j):
    
    pos_lst = []
    count = 0

    # Nearest neighbour selection
    
    if forestArr[i-1][j] == 1:
        count += 1
        pos_lst.append([i-1,j])
        
    if forestArr[i+1][j] == 1:
        count += 1
        pos_lst.append([i+1,j])
    
    if forestArr[i][j+1] == 1:
        count += 1
        pos_lst.append([i,j+1])
        
    if forestArr[i][j-1] == 1:
        count += 1
        pos_lst.append([i,j-1])
    
    if forestArr[i-1][j-1] == 1:
        count += 1
        pos_lst.append([i-1,j-1])
        
    if forestArr[i+1][j+1] == 1:
        count += 1
        pos_lst.append([i+1,j+1])
    
    if forestArr[i-1][j+1] == 1:
        count += 1
        pos_lst.append([i-1,j+1])
        
    if forestArr[i+1][j-1] == 1:
        count += 1
        pos_lst.append([i+1,j-1])
    
    # Returing the input tree pos to indicate no near neighbour found
    if count == 0:
        pos_lst.append([i,j])
        
    return pos_lst
        

plt.figure(figsize = (7,7))

# Color map for each state 

color_map = ListedColormap([
    (0.1,0.1,0.1),
    (0.1,0.4,0.0),
    (1.0,0.5,0.0)
])

# Three states are refered as : 
#0 -> Empty
#1 -> Tree
#2 -> Burning


for k in range(totalTime):

    forestCopy = forestArr.copy()
    
    for i in range(1,Nsize-1):
        for j in range(1,Nsize-1):
            
            # Burning --> Empty site
            if forestArr[i][j] == 2:
                forestCopy[i][j] = 0
                
            # Tree --> Burning(either lightning or near propagation)
            if forestArr[i][j] == 1:
                
                if random.random() < lightProb:
                    forestCopy[i][j] = 2

                    neighbour_pos = neighbourCheck(forestCopy,i,j)
                    # if a burning tree is its own neighbour it has no neighbour to spread and the fire dies down
                    if neighbour_pos[-1] != [[i,j]]:
                        # Checking for all possible spread to update parallelly
                        for pos in neighbour_pos:
                            forestCopy[pos[0]][pos[1]] = 2
                            neighbour_pos.pop(0)
                            neighbour_pos.extend(neighbourCheck(forestCopy,pos[0],pos[1]))
                    else:
                        continue        

            # Empty site --> tree (with a prob.)   
            if forestArr[i][j] == 0:
                if random.random() < growthProb:
                    forestCopy[i][j] = 1
                
    forestArr = forestCopy    
    

    # Updating the frame in real time with a delay of 0.1 sec between each frame
    plt.cla()
    plt.imshow(forestArr, cmap = color_map, vmin = 0, vmax = 2)
    plt.title(f'Drossel-Schwabl Forest Fire Sim (Time = {k}/{totalTime})')
    plt.axis('off')
    plt.pause(0.1)

