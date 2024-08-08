# Carlos Paredes Márquez
# Task: given a base 10 integer n, convert it to binary
# then find the denotation of maximun number of 
# consecutive 1's in binary reprersentation.
# example, n = 215, bin = 1111101, print the maximum: 5
import re

def maxOne (n):
    bin_n = str(bin(n))
    bin_n = bin_n[2:]

    sequence = re.findall(r'1+', bin_n)
    longestSequence = max(sequence, key=len)

    print(len(longestSequence))

if __name__ == '__main__':
    n = int(input().strip())
    maxOne(n)
