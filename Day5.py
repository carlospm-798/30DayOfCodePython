# Carlos Paredes Márquez
def multiplication(n):
    for i in range(1, 11):
        print(n, 'x', i, '=', i*n)


if __name__ == '__main__':
    n = int(input().strip())
    
    multiplication(n)