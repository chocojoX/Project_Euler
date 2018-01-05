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

        for j in range(len(self.number)):
            to_move = int(self.number[j]/self.basis)
            self.number[j] = self.number[j] - to_move*self.basis
            if 1+j<len(self.number):
                self.number[j+1] = self.number[j+1] + to_move
            else:
                self.number.append(to_move)

        for i, b in enumerate(self.number):
            if b>self.basis:
                self.number[i] = b-self.basis
                if len(self.number)==i+1:
                    self.number.append(1)
                else:
                    self.number[i+1] = self.number[i+1]+1

        while self.number[-1]>=self.basis:
            b = self.number[-1]
            to_move = int(b/self.basis)
            self.number[-1] = b-to_move*self.basis
            self.number.append(to_move)


    def multiply(self, x):
        assert type(x)==int
        assert x>=0
        self.number = [b*x for b in self.number]

        for j in range(len(self.number)):
            to_move = int(self.number[j]/self.basis)
            self.number[j] = self.number[j] - to_move*self.basis
            if 1+j<len(self.number):
                self.number[j+1] = self.number[j+1] + to_move
            else:
                self.number.append(to_move)

        for i, b in enumerate(self.number):
            if b>self.basis:
                to_move = int(b/self.basis)
                self.number[i] = b-to_move*self.basis
                if len(self.number)==i+1:
                    self.number.append(to_move)
                else:
                    self.number[i+1] = self.number[i+1]+to_move

        while self.number[-1]>=self.basis:
            b = self.number[-1]
            to_move = int(b/self.basis)
            self.number[-1] = b-to_move*self.basis
            self.number.append(to_move)




if __name__=="__main__":
    x = LongInt(79)
    print(x.number)
    x.add(62)
    print(x.number)
    x.multiply(20)
    print(x.number)
