

class operators:
    def biggest(self,li): #MY FORM OF MAX FUNCTION
        big = 0 
        for i in li:
            if big == 0 or i > big:
                big = i
        return big
    def smallest(self,li): #MY FORM OF MIN FUNCTION 
        smal = 0 
        for i in li:
            if smal == 0 or i < smal:
                smal = i
        return smal
    def totalSum(self,li):#MY FORM OF SUM FUNCTION 
        j = 0
        for i in li:
            j += i
        return j 
    def newlen(self, y):#MY FORM OF LEN FUNCTION 
        x = 0
        for _ in y:
            x = x + 1
        return x

    




class listfunctions:
    def __init__(self):
        self.listt = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100] #random.sample(range(0, 100), 10)
    def __str__(self) -> str:
        return "\n list: " + str(self.listt)
    

    def bigAndSmall(self, x): 
        total = ['sum of a list is: ' , operators().totalSum(self.listt)]
        if x == "big":
            biggest = ['biggest variable in the list is: ', operators().biggest(self.listt)]
            return biggest, total
        elif x == "smal":
            smal = ['smallest variable in the list is: ', operators().smallest(self.listt)]
            
        return smal.__str__()
            

    def reversing(self):
        return [self.listt.pop() for _ in range(len(self.listt))]
    
    def average(self):
        return operators().totalSum(self.listt) / operators().newlen(self.listt)

    def rotate(self, n):
        return [self.listt[(i + int(n)) % operators().newlen(self.listt)] for i, x in enumerate(self.listt)]
            
    def search(self, y):
        return int(y) in self.listt

            


if __name__ == '__main__':
    print(listfunctions().__str__())
    x = input("big ar smal?\n")
    print(listfunctions().bigAndSmall(x))
    print("reversed list:")
    print(listfunctions().reversing())
    print("average:")
    print(listfunctions().average())
    y = input("number of rotates")
    print(listfunctions().rotate(y))
    z = input("number you want to search for; ")
    print(listfunctions().search(z))





