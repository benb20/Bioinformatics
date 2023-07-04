#!/usr/bin/python
import time
import sys
import numpy as np

# YOUR FUNCTIONS GO HERE -------------------------------------
# 1. Populate the scoring matrix and the backtracking matrix
def sMatrix(s1,s2):
    n = len(s1)
    m = len(s2)
    
    array1 = [0,-1]
    array2 = [0,-1]
    array3 = [-1]
    array4 = [-1]
    for i in s1:
        array1.append(ord(i))
        
    for j in s2:
        array2.append(ord(j))
        
    for k in range(len(array1)-1):
        array3.append(-2*k)

    for l in range(len(array2)-1):
        array4.append(-2*l)
    S = np.zeros((m+2, n+2)) # initialise empty matrix
    #fill in sequence rows
    S[0] = array1
    S[:,0] = array2

    B = S.copy()
    
    S[1] = array3
    S[:,1] = array4 

    
    return [S, B]
# ------------------------------------------------------------

def s(i,j):
    if i == 1 or j == 1:
        return scoreMatrix[i][j]

    if scoreMatrix[0][j] == scoreMatrix[i][0] == 65:
        v = 4
    elif scoreMatrix[0][j] == scoreMatrix[i][0] == 67:
        v = 3
    elif scoreMatrix[0][j] == scoreMatrix[i][0] == 71:
        v = 2
    elif scoreMatrix[0][j] == scoreMatrix[i][0] == 84:
        v = 1
    else:
        v = -1

    value = max(v + s(i-1, j-1), s(i-1, j) - 2, s(i, j-1) - 2)
    scoreMatrix[i][j] = value

    #finds where value came from:
    #index_min = np.argmin(values)
    #if index_min == 0:
    #elif index_min == 1:
    #elif index_min == 2:
    
    return int(value)

# DO NOT EDIT ------------------------------------------------
# Given an alignment, which is two strings, display it

def displayAlignment(alignment):
    string1 = alignment[0]
    string2 = alignment[1]
    string3 = ''
    for i in range(min(len(string1),len(string2))):
        if string1[i]==string2[i]:
            string3=string3+"|"
        else:
            string3=string3+" "
    print('Alignment ')
    print('String1: '+string1)
    print('         '+string3)
    print('String2: '+string2+'\n\n')

# ------------------------------------------------------------


# DO NOT EDIT ------------------------------------------------
# This opens the files, loads the sequences and starts the timer
file1 = open(sys.argv[1], 'r')
seq1=file1.read()
file1.close()
file2 = open(sys.argv[2], 'r')
seq2=file2.read()
file2.close()
start = time.time()

#-------------------------------------------------------------


# YOUR CODE GOES HERE ----------------------------------------
# The sequences are contained in the variables seq1 and seq2 from the code above.
# Intialise the scoring matrix and backtracking matrix and call the function to populate them
# Use the backtracking matrix to find the optimal alignment 
# To work with the printing functions below the best alignment should be called best_alignment and its score should be called best_score. 
m = len(seq1)
n = len(seq2)
global scoreMatrix
matrices = sMatrix(seq1,seq2)
scoreMatrix = matrices[0]
bMatrix = matrices[1]

#print(scoreMatrix)
#print(bMatrix)
out = s(m+1,n+1)
print(out)
print(scoreMatrix)

#-------------------------------------------------------------


# DO NOT EDIT (unless you want to turn off displaying alignments for large sequences)------------------
# This calculates the time taken and will print out useful information 
stop = time.time()
time_taken=stop-start

# Print out the best
print('Time taken: '+str(time_taken))
print('Best (score '+str(best_score)+'):')
displayAlignment(best_alignment)

#-------------------------------------------------------------

