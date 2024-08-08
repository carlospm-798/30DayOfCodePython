def wordByOrder(word):
    ''' This funciton separates the even and odd index
    values of the words that we reads at the STDIN  '''
    even = []   #even numbers of index list
    odd = []    #odd numbers of index list

    for i in range(0,len(word), 2):     #goes from 0 to the last element
        even.append(word[i])            #appends the <i> element of the string
    
    for i in range(1, len(word), 2):    #goes from 1 to the last element
        odd.append(word[i])             #appends the <i> element of the string
        
    outOfWords(even, odd)


def outOfWords(even, odd):
    ''' This function helps to unify the elements of 
    the list in the same string output to STDIN     '''
    evenString = "".join(even)          #join the list into a string
    oddString = "".join(odd)            #join the list into a string

    both = evenString + " " + oddString     #joint both strings into a same with a space in the middle
    print(both)     #prints the result


if __name__ == '__main__':

    n = int(input())    #Number of inputs
    words = []      #Null list of words
    
    for i in range(n):
        words.append(str(input()))      #Introduce of the words
    
    for word in words:
        wordByOrder(word)   #goes to the function