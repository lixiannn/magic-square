# import all functions
import magicSquare

# driver function for finding minimum cost of transforming into magic square
if __name__ == "__main__":
    # initialisation of matrix size and array
    MATRIX_SIZE = 3
    array = [[0, 0, 0],
             [0, 0, 0],
             [0, 0, 0]]

    # get user input
    for i in range(0, MATRIX_SIZE):
        for j in range(0, MATRIX_SIZE):
            try:
                number = input("Please enter a number: ")
                array[i][j] = int(number)
            except:
                print("Invalid input.")
                exit()

    # get minimum cost and display it
    cost = magicSquare.checkMagicSquare(array, MATRIX_SIZE)
    print("The minimum cost is: {}".format(cost))
