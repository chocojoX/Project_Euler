import numpy as np

class LongInt(object):
    def __init__(self, number, basis=10):
        self.basis=basis
        self.number = [0]
        self.add(number)

    def add(self, x):
        assert type(x)==int
        assert x>=0
        self.number[0] = self.number[0] + x

        k = self.basis; i=1
        while int(self.number[0]/k)>0:
            k = k*self.basis
            i+=1
        k = k/self.basis; i-=1
        while i>0:
            to_move = int(self.number[0]/k)
            self.number[0] = self.number[0] - to_move*k
            if i<len(self.number):
                self.number[i] = self.number[i] + to_move
            else:
                self.number.append(to_move)
            k = k/self.basis
            i = i-1

        for i, b in enumerate(self.number):
            if b>self.basis:
                self.number[i] = b-self.basis
                if len(self.number)==i+1:
                    self.number.append(1)
                else:
                    self.number[i+1] = self.number[i+1]+1

    def multiply(self, x):
        assert type(x)==int
        assert x>=0
        self.number = [b*x for b in self.number]

        for j in range(len(self.number)):
            k = self.basis; i=1
            while int(self.number[j]/k)>0:
                k = k*self.basis
                i+=1
            k = k/self.basis; i-=1
            while i>0:
                to_move = int(self.number[j]/k)
                self.number[j] = self.number[j] - to_move*k
                if i+j<len(self.number):
                    self.number[j+i] = self.number[j+i] + to_move
                else:
                    self.number.append(to_move)
                k = k/self.basis
                i = i-1

        for i, b in enumerate(self.number):
            if b>self.basis:
                self.number[i] = b-self.basis
                if len(self.number)==i+1:
                    self.number.append(1)
                else:
                    self.number[i+1] = self.number[i+1]+1




if __name__=="__main__":
    x = LongInt(79)
    print(x.number)
    x.add(62)
    print(x.number)
    x.multiply(20)
    print(x.number)
