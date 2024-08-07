# Carlos Paredes Márquez

def result(arr):
    arr = arr[::-1]     # flip the array
    
    text = '-'.join(str(element) for element in arr)
    print(text)

if __name__ == '__main__':
    n = int(input().strip())
    arr = list(map(int, input().rstrip().split()))

    result(arr)