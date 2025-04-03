# Tetris_challenge
<img width="749" alt="Image" src="https://github.com/user-attachments/assets/fe66de40-30b2-4321-b588-81fb1594e9e6" />

This project is an algorithm to solve the tetriling with missing pieces problem using python. This problem consists of finding a tiling of an arbitrary finite polyomino region by using Tetris pieces.

this is an improved greedy algorithm in Python with low running time and hight accuracy.

# Summary of the development 
- Step 1: Greedy algorithm that finds the best local solution (matching four empty blocks) 
- Step 2: Improved greedy algorithm with a neighbouring system : the chosen best shape is the one with the fewest neighbours, meaning it is the most isolated.
- Step 4: Implementation of an optimisation loop which place an extra three blocks in locations where there are ‘1s’ and one excess block where there is a ‘0’.
- Step 5: optimising time by using the most optimised order of shape_ID.

<img width="582" alt="Image" src="https://github.com/user-attachments/assets/c9127af6-50ee-4b6f-b8fb-0c2bcad5d82f" />

<img width="493" alt="Image" src="https://github.com/user-attachments/assets/eb818b70-d511-4922-b5af-83708815ddec" />
