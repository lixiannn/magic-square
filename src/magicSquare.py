''' This file contains 2 functions that will help us check for the minimum cost of forming magic square.

A magic square is an nxn matrix of distinct positive integers from 1to n^2 where the sum of any row, column, 
or diagonal of length n is always equal to the same number: the magic constant.

The following 2 functions will help us to generate all possible combinations of a 3x3 magic square and to find the
minimum cost of swapping into one. '''


# import math module for abs() to calculate cost difference
import math

''' generateMagicSquare() is a function that generates all possible combinations of a 3x3 magic square. 
This function does not take in any argument and it returns a list of possible combinations of b 3x3m matrices.

Each matrix is predefined by following these rules:

The magic constant can be obtained by this formula: (n/2)((n^2+1)). In this case, n = 3 will give us 
magic constant = 15.

The 8 valid combinations of 3 numbers that add to 15 are:
- 9, 5, 1
- 7, 5, 3
- 2, 5, 8
- 4, 5, 6
- 2, 9, 4
- 6, 1, 8
- 6, 7, 2
- 8, 3, 4

These 8 combinations will form our rows,columns and diagonals. The only number that appears 4 times will be the 
number that is in the middle of the matrix, and the only number here is 5. Each of the corner tile will appear 3 
in a row, column and diagonal. Hence, numbers that form the corner tiles must appear at least 3 times, which are 2,
4, 6, 8. Hence, diagonals must be 2, 5, 8 and 4, 5, 6.

After we put 5 in the center, we can form pairs that sum up to 10. This gives us the following pairs:
- 2, 8
- 4, 6
- 3, 7
- 1, 9

Since we already found the diagonals, we just need to insert the remaining 2 odd pairs into the matrix. Hence, the
middle column/row will be 7, 5, 3 and 9, 5, 1.

This will give us:
[[2, 9, 4],
 [7, 5, 3],
 [6, 1, 8]]

 By taking the mirror images and rotation, we will derive all 8 possible combinations. Putting these 8 matrices into
 a list, we can return the list. 
 
 Mirror images:

4 9 2 | 2 9 4
3 5 7 | 7 5 3
8 1 6 | 6 1 8
-------------
8 1 6 | 6 1 8
3 5 7 | 7 5 3
4 9 2 | 2 9 4

Rotations:

8 3 4 | 4 3 8
1 5 9 | 9 5 1
6 7 2 | 2 7 6
-------------
6 7 2 | 2 7 6
1 5 9 | 9 5 1
8 3 4 | 4 3 8          '''


def generateMagicSquare():
    m1 = [[2, 9, 4],
          [7, 5, 3],
          [6, 1, 8]]

    m2 = [[4, 9, 2],
          [3, 5, 7],
          [8, 1, 6]]

    m3 = [[8, 1, 6],
          [3, 5, 7],
          [4, 9, 2]]

    m4 = [[6, 1, 8],
          [7, 5, 3],
          [2, 9, 4]]

    m5 = [[8, 3, 4],
          [1, 5, 9],
          [6, 7, 2]]

    m6 = [[4, 3, 8],
          [9, 5, 1],
          [2, 7, 6]]

    m7 = [[6, 7, 2],
          [1, 5, 9],
          [8, 3, 4]]

    m8 = [[2, 7, 6],
          [9, 5, 1],
          [4, 3, 8]]

    allMagicSquares = [m1, m2, m3, m4, m5, m6, m7, m8]
    return allMagicSquares


''' checkMagicSquare(matrix, MATRIX_SIZE) is a function that will calculate the minimum cost of swapping a user 
input matrix into a magic square.

The function takes in 2 arguments: matrix and MATRIX_SIZE
1. matrix is the matrix inputted by the user.It is a 3x3 matrix consisting of values ranging from [1:9] inclusive.
2. MATRIX_SIZE is the size of the matrix

The function will first get the list of all possible combinations of magic square from the generateMagicSquare() function.
SUbsequently, it will initialise minCost to an arbitraily large value. Subsequently, the function will loop through
every matrix in the list of possible matrices. For each matrix, we will compare each element against the user input matrix
and calculate the cost required. If the cost required is smaller than minCost, then we will update minCost accordingly.

We will return minCost at the end of the function.

'''


def checkMagicSquare(matrix, MATRIX_SIZE):
    magicSquareList = generateMagicSquare()
    minCost = 10000000
    for i in magicSquareList:
        cost = 0
        for m in range(MATRIX_SIZE):
            for n in range(MATRIX_SIZE):
                diff = abs(i[m][n] - matrix[m][n])
                cost += diff
        if cost < minCost:
            minCost = cost

    return minCost
