# Carlos Paredes Márquez

class Person:
    def __init__(self,initialAge):
        self.initialAge = initialAge
        
        if initialAge < 0:
            print("Age is not valid, setting age to 0.")
            initialAge = 0
        
    def amIOld(self):
        
        if (self.initialAge < 13):
            print("You are young.")
        
        elif (self.initialAge >= 13 and self.initialAge < 18):
            print("You are a teenager.")
        
        else:
            print("You are old.")
        
    def yearPasses(self):

        self.initialAge += 1

t = int(input())
for i in range(0, t):
    age = int(input())         
    p = Person(age)  
    p.amIOld()
    for j in range(0, 3):
        p.yearPasses()       
    p.amIOld()
    print("")