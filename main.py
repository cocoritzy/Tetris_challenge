# ####################################################
# Title: MAIN
# Authors: Coline Ritz
# Last updated: 12th January 2020
# ####################################################

# ####################################################
# Summary of the development 
#Step 1: Greedy algorithm that finds the best local solution (matching four empty blocks) 
#Step 2: Improved greedy algorithm with a neighbouring system : the chosen best shape is the one with the fewest neighbours, meaning it is the most isolated.
#Step 4: Implementation of an optimisation loop which place an extra three blocks in locations where there are ‘1s’ and one excess block where there is a ‘0’.
#Step 5: optimising time by using the most optimised order of shape_ID.

# ####################################################

import numpy as np
import utils


def Tetris(target):
    
# ------ Variables and Matrix initialisation -------    
    
    
    # creating 3 matrices (i,j) with an extended pad to avoid problems with limits
    
    target1 = np.pad(target, [3,3], mode='constant', constant_values= 0)  # matrix for optimisation algorithm                       
    target2 = np.pad(target, [3,3], mode='constant', constant_values= 0)  # matrix for piece_ID in the final solution                      
    target3 = np.pad(target, [3,3], mode='constant', constant_values= 2)  # matrix for shape_ID in the final solution
    
    rows_target1 = len(target1)                                                                  
    columns_target1 = len(target1[0])
    solution = [[(0,0) for col in range(0, columns_target1)] for row in range(0, rows_target1)]
    
    piece_ID= 1 #initialing the piece_ID 



# ------ Greedy algorithm with an optimisation criteria based on the fewest number of neighbours-------
    
    
    for i in range(3,rows_target1-3): 
        for j in range(3,columns_target1-3):
            if target1[i][j]== 1:       # optimising time  
                neighbours= 100         # initialing the number of neighbours
                best_shape= -1          # initialing the best_shapeID
                for X in range(4,20):   # loop on all the shape_ID
                    
                    shape= utils.generate_shape(X)
                    
                    a=target1[i+shape[0][0]][j+shape[0][1]]     # values of shape_ID coordonates in target1
                    b=target1[i+shape[1][0]][j+shape[1][1]]
                    c=target1[i+shape[2][0]][j+shape[2][1]]
                    d=target1[i+shape[3][0]][j+shape[3][1]]
                    
                   
                    a1=target1[i+shape[0][0]][j+shape[0][1]+1]  # values of shape_ID neighbours coordonates in target1
                    a2=target1[i+shape[0][0]][j+shape[0][1]-1]
                    a3=target1[i+shape[0][0]-1][j+shape[0][1]]
                    a4=target1[i+shape[0][0]+1][j+shape[0][1]]
                     
                    l1= a1+a2+a3+a4
                    
                    b1=target1[i+shape[1][0]][j+shape[1][1]+1]
                    b2=target1[i+shape[1][0]][j+shape[1][1]-1]
                    b3=target1[i+shape[1][0]-1][j+shape[1][1]]
                    b4=target1[i+shape[1][0]+1][j+shape[1][1]]
                    
                    l2= b1+b2+b3+b4
                    
                    c1=target1[i+shape[2][0]][j+shape[2][1]+1]
                    c2=target1[i+shape[2][0]][j+shape[2][1]-1]
                    c3=target1[i+shape[2][0]-1][j+shape[2][1]]
                    c4=target1[i+shape[2][0]+1][j+shape[2][1]]
                    
                    l3= c1+c2+c3+c4
                    
                    d1=target1[i+shape[3][0]][j+shape[3][1]+1]
                    d2=target1[i+shape[3][0]][j+shape[3][1]-1]
                    d3=target1[i+shape[3][0]-1][j+shape[3][1]]
                    d4=target1[i+shape[3][0]+1][j+shape[3][1]]
                    
                    l4= d1+d2+d3+d4

                    L= l4+l3+l2+l1                             # number of shape_ID neighbours

                    if a==1 and b==1 and c==1 and d==1: 
                        if L< neighbours:                      # research of the best shape with the smallest number of neighbours      
                            best_shape= X
                            neighbours= L
                            
                if (best_shape> 0):  
                    shape= utils.generate_shape(best_shape)
                    target1[i+shape[0][0]][j+shape[0][1]]= 0    # best_shape is no longer consider as a neighbours and indicates that the place is locked
                    target1[i+shape[1][0]][j+shape[1][1]]= 0
                    target1[i+shape[2][0]][j+shape[2][1]]= 0
                    target1[i+shape[3][0]][j+shape[3][1]]= 0
                    
                    target2[i+shape[0][0]][j+shape[0][1]]= piece_ID 
                    target2[i+shape[1][0]][j+shape[1][1]]= piece_ID
                    target2[i+shape[2][0]][j+shape[2][1]]= piece_ID
                    target2[i+shape[3][0]][j+shape[3][1]]= piece_ID
            
                    target3[i+shape[0][0]][j+shape[0][1]]= best_shape 
                    target3[i+shape[1][0]][j+shape[1][1]]= best_shape
                    target3[i+shape[2][0]][j+shape[2][1]]= best_shape
                    target3[i+shape[3][0]][j+shape[3][1]]= best_shape
                    piece_ID+=1
                    
                                             
    for i in range (rows_target1):
        for j in range (columns_target1):
            target1[i][j]= target3[i][j]
            
            
          
# ------ Optimisation loop -------    
     
    for i in range(3,rows_target1-3):
        for j in range(3,columns_target1-3):
            if target1[i][j]== 1:
                for X in range(19,3,-1): # better result and faster in this order
                    
                    shape= utils.generate_shape(X)
                    
                    a=target1[i+shape[0][0]][j+shape[0][1]]
                    b=target1[i+shape[1][0]][j+shape[1][1]]
                    c=target1[i+shape[2][0]][j+shape[2][1]]
                    d=target1[i+shape[3][0]][j+shape[3][1]]
         
                    if (a == 0 and  b == 1 and c == 1 and d == 1) or (a == 1 and b == 0 and c == 1 and d == 1) or (a == 1 and b == 1 and c == 0 and d == 1) or (a == 1 and b == 1 and c == 1 and d == 0 ): 
                          target1[i+shape[0][0]][j+shape[0][1]]= X 
                          target1[i+shape[1][0]][j+shape[1][1]]= X
                          target1[i+shape[2][0]][j+shape[2][1]]= X
                          target1[i+shape[3][0]][j+shape[3][1]]= X
                      
                          target2[i+shape[0][0]][j+shape[0][1]]= piece_ID  
                          target2[i+shape[1][0]][j+shape[1][1]]= piece_ID
                          target2[i+shape[2][0]][j+shape[2][1]]= piece_ID
                          target2[i+shape[3][0]][j+shape[3][1]]= piece_ID
                      
                          piece_ID += 1
                      
                          break 
                        
                        
# ------ Formating the solution matrix  -------

    for i in range (3,rows_target1-3): 
        for j in range (3,columns_target1-3):
            solution[i][j]= (target1[i][j],target2[i][j])
            if solution[i][j] == (1,1):
                solution[i][j]= (0,0)

    final_solution = solution[3:-3]    # removing pad
    final_solution = [i[3:-3] for i in final_solution]
       
    return final_solution 
    
               
                


            