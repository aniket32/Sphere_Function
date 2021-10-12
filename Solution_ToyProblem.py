import numpy as np
import math as m
from random import random

# FITNESS FUNCTION 
def fitness_function( func_no, x ):
    global FEs
    
    # SPHERE FUNCTION
    if func_no == 1: 
        result = 0.0
        for i in range( len(x) ):
            result = result + m.pow(x[i],2)

    # WRITE A NEW FUNCTION HERE
	# elif func_no == 2: 
	# 

    FEs = FEs + 1
    return result


FEs = 0 			# Function Evaluation Counter: COUNTING THE NUMBER OF TIMES FITNESS FUNCTION IS CALLED
D   = 30 			# ASSUME THE DIMENSIONALITY OF THE PROBLEM TO BE 30


###############
# CONSTRAINTS #
###############
lower_bound = -5.12
upper_bound =  5.12


############################
# GENERATE RANDOM SOLUTION #
############################
x = [None] * D 		# A SOLUTION

# INITIALISE THE VALUES FOR x
for i in range(D):
	x[i] = lower_bound + random()*(upper_bound - lower_bound)

# DISPLAY THE SAMPLE SOLUTION
print ( 'x: \n', x, '\n') 


###########################################
# EVALUATE AND DISPLAY THE SAMPLE SOLUTON #
###########################################
print ( 'Fitness: ', fitness_function(1, x), '\n' ) 


###########################################
# GENERATE 50 SOLUTIONS AND FIND THE BEST #
###########################################
N = 50				# NUMBER OF SOLUTIONS
X = np.random.uniform(low=lower_bound, high=upper_bound, size=(N,D)) 	# 2D LIST HOLDING ALL N SOLUTIONS
# X SHOULD BE (N x D)


###############################
# EVALUATE THE SAMPLE SOLUTON #
###############################
fitness = [None]*N	# FITNESS VALUES

for i in range(N):
	fitness[i] = fitness_function( 1, X[i] )


###################################
# FIND THE INDEX OF BEST SOLUTION #
###################################
best_index = np.argmin(fitness)


#######################################################################
# DISPLAY ALL FITNESS VALUES, THE BEST SOLUTION, AND THE BEST FITNESS #
#######################################################################
print('Fitness values for all solutions: \n', fitness, '\n')
print('Best solution: \n', X[best_index], '\n')
print('Best fitness value: ', fitness[best_index])
