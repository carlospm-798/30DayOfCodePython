# Carlos Paredes Márquez
#import sys

phoneNumbers = {}

if __name__ == '__main__':
    N = int(input())        # Number of inputs

    '''         Input and evaluation of stdin           '''

    for i in range(N):                                  # input of name with the phone number
        nameAndNumber = str(input())                    # str input...

        if ' ' in nameAndNumber:                        # if voidSpace, save the values in dictionary
            voidSpace = nameAndNumber.find(' ')         # look for the position of the void space
            name = nameAndNumber[:voidSpace]            # take the name of the str input
            number = nameAndNumber[voidSpace + 1:]      # take the number of the str input, +1 to remove the void space

            phoneNumbers[name] = number                 # Save the data in the dictionary
    
    searchNames = []                                    # void list, for append search names
    
    '''        Querie entry, while there's no more input       '''
 
    #query = sys.stdin.readline().strip()
    query = str(input())
    while query:
        searchNames.append(query)

        #query = sys.stdin.readline().strip()
        query = str(input())
    
    '''         Search and print of values in dictionary                  '''

    for i in range(len(searchNames)):

        if searchNames[i] in phoneNumbers:
            print(str(searchNames[i]) + '=' + str(phoneNumbers.get(searchNames[i])))
        else:
            print("Not found")
            


'''
Sample input:

3
sam 99912222
tom 11122222
harry 12299933
sam
edward
harry

Sample output:

sam=99912222
Not found
harry=12299933
'''