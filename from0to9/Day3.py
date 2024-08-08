# Carlos Paredes Márquez

def case(n):

    if (n%2 != 0):
        # Odd case
        print("Weird")
    elif (n%2 == 0 and n in range(2,5)):
        # Even case in range 2,5
        print("Not Weird")
    elif (n%2 == 0 and n in range(6,21)):
        # Even case in range 6,20
        print("Weird")
    elif (n%2 == 0 and n > 20):
        # Even case bigger than 20
        print("Not Weird")

if __name__ == '__main__':
    N = int(input().strip())
    case(N)
