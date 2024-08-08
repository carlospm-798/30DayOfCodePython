# Carlos Paredes Márquez
# 2D Arrays
# Task: Given a 6x6 2D Array, A, we define a hourglass 
# in A to be a subset of values with indices failling in 
# this pattern:
#
#       a b c       2 4 4
#         d           2         sum = 19
#       e f g       1 2 4  
#
# And we need to return the value of the maximum sum
# with a hourglass form, inside of their values.

def sumHourglass(arr):
    allSums = []

    for i in range(4):
        for j in range(4):
            actualSum = int(arr[i][j]) + int(arr[i][j+1]) + int(arr[i][j+2]) 
            actualSum += int(arr[i+1][j+1]) 
            actualSum += int(arr[i+2][j]) + int(arr[i+2][j+1]) + int(arr[i+2][j+2])
            allSums.append(actualSum)
    
    return max(allSums)



if __name__ == '__main__':

    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))
    
    print(sumHourglass(arr))
