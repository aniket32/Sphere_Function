import numpy as np
import math as m
from random import random

# FITNESS FUNCTION
def fitness_function( func_no, x ):
    global FEs

    # SPHERE FUNCTION
    if func_no == 1:
        sum = 0.0
        for i in range( len(x) ):
            sum = sum + m.pow(x[i],2)

    # WRITE A NEW FUNCTION HERE
    # elif func_no == 2:
    #     sum = 0.0
    #     for k in y:
    #         sum = sum + m.pow(y[k], 2)

    FEs = FEs + 1
    return sum


FEs = 0		# COUNTING THE NUMBER OF TIMES FITNESS FUNCTION IS CALLED
D   = 30	# ASSUME THE DIMENSIONALITY OF THE PROBLEM TO BE 30


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
# --->
x = np.random.uniform( low= lower_bound, high=upper_bound, size=(D))

# DISPLAY THE SAMPLE SOLUTION
print ( 'x: \n', x, '\n')


###########################################
# EVALUATE AND DISPLAY THE SAMPLE SOLUTON #
###########################################
# --->
print (fitness_function(1,x))


###########################################
# GENERATE 50 SOLUTIONS AND FIND THE BEST #
###########################################
N = 50				# NUMBER OF SOLUTIONS
# --->  X = ?		# 2D LIST HOLDING ALL N SOLUTIONS
# X SHOULD BE (N x D)
print("\n")


###############################
# EVALUATE THE SAMPLE SOLUTON #
###############################
fitness = [None]*N	# FITNESS VALUES

print ("Solution for the second problem")
y = np.random.uniform(low=lower_bound, high=upper_bound, size=(N,D))
fitness_variable = []
for k in y:
    fitness_variable.append(fitness_function(1,k))
    print(k)

print("Total number of fitness variables")
print (len(fitness_variable))

minimum = min(fitness_variable)
# --->

# ---> 

###################################
# FIND THE INDEX OF BEST SOLUTION #
###################################
best_index = fitness_variable.index(minimum)


#######################################################################
# DISPLAY ALL FITNESS VALUES, THE BEST SOLUTION, AND THE BEST FITNESS #
#######################################################################
print('Fitness values for all solutions: \n', fitness_variable, '\n')
print('Best solution: \n', y[best_index], '\n')
print('Best fitness value: ', minimum)
