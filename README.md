# Forest Fire Simulation (Drossel-Schwabl)
A Forest Fire Model based on the Drossel and Schwabl (1992) paper.
Here we consider a 2-D grid based approch to represent the forest and parallely update the state of the system by the following rules : 
1. A burning tree becomes an empty site.
2. A green tree becomes a burning tree if at least one of its neighbour is burning.
3. At an empty site a tree grows with probability($growthProb$).
4. A tree without a burning nearest neighbour becomes a burning tree during one time step with probability ($lightProb$) [Like a forest fire initiated by a lightning strike]

Here is an example scenario based on the above rules:

<img width="356" height="358" alt="Simulation_Explain_forestFire" src="https://github.com/user-attachments/assets/422c4c4e-2234-40f8-bf68-3bde361fce98" />


Based on these rule we iterate over the system and observe the different type of evolution of the system based on different ratio of : $growthProb/lightProb$


The Results are visualized using matplotlib by plotting the state of the forest in real-time after each iteration with color coding the state of each sites.
