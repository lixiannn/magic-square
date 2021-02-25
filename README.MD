# Project Description & Background

This project calculates the minimum cost of transforming a 3x3 matrix into a magic square.

A magic square is an nxn matrix of distinct positive integers from 1 to n^2 where the sum of any row, column,
or diagonal of length n is always equal to the same number: the magic constant.

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

---

8 1 6 | 6 1 8

3 5 7 | 7 5 3

4 9 2 | 2 9 4

Rotations:

8 3 4 | 4 3 8

1 5 9 | 9 5 1

6 7 2 | 2 7 6

---

6 7 2 | 2 7 6

1 5 9 | 9 5 1

8 3 4 | 4 3 8

# Demo

Initial matrix:

5 3 4

1 5 8

6 4 2

We can convert it to the following magic square:

8 3 4

1 5 9

6 7 2

This took 3 replacements at a cost of |5-8| + |8-9| + |4-7| = 7

# Installation & Resources

This project uses python 3.7.4. No further installation of modules required.
