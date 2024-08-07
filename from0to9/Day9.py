# Carlos Paredes Márquez
#!/bin/python3
# Complete the 'factorial' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER n as parameter.

def factorial(n):
    # Write your code here
    cont = n - 1
    result = n

    while (cont != 0):
        result *= cont
        cont -= 1
    
    return result

if __name__ == '__main__':
    #fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())
    result = factorial(n)
    print(result)

    #fptr.write(str(result) + '\n')
    #fptr.close()