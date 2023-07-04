import numpy as np

s1 = "ACG"
s2 = "AGT"
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
B = np.zeros((m+2, n+2))
C = np.empty((m,n))
print(C)
print(B)
B[0] = array1
B[1] = array3
B[:,0] = array2
B[:,1] = array4

print(B)


#can ignore 0th column and 0th row for indexing purposes
#we can instead use them for c(i,j) comparisons
#i-1th row and i-1th element is bottom right, which is the best alignment score

#the function s(i,j) computes the score at the current index in the matrix, so all  we want
#is to return s(i-1,j-1)th element to get score.

#i and j are simply the position you are at.
def s(i,j):
    if i == 1 or j == 1:
        return B[i][j]

    if B[0][j] == B[i][0]:
        v = 2 
    else:
        v = -1

    value = max(v + s(i-1, j-1), s(i-1, j) - 2, s(i, j-1) - 2)
    B[i][j] = value
    
    #index_min = np.argmin(values)
    #if index_min == 0:
    
    return int(value)
