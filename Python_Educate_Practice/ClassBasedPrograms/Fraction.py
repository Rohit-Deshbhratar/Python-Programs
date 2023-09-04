import math

class Fraction:
    
    #Create your fraction class here.
    def __init__(self, n, d):
        self.numerator = n
        self.denominator = d
    
    def add(self, fraction1):
        num_1 = self.numerator
        deno_1 = self.denominator
        num_2 = fraction1.numerator
        deno_2 = fraction1.denominator

        if(deno_1 == deno_2):
            self.numerator = num_1 + num_2
            self.denominator = self.denominator
        else:
            self.numerator = (num_1*deno_2) + (num_2*deno_1)
            self.denominator = deno_1 * deno_2
    
    def multiply(self, fraction2):
        num_3 = self.numerator
        deno_3 = self.denominator
        num_4 = fraction2.numerator
        deno_4 = fraction2.denominator

        self.numerator = num_3 * num_4
        self.denominator = deno_3 * deno_4
    
    def printFraction(self):
        num_1 = math.gcd(self.numerator, self.denominator)
        self.numerator = self.numerator // num_1
        self.denominator = self.denominator // num_1

        print(self.numerator, self.denominator, sep="/")

def main():
    n1, d1 = map(int, input().split())
    query = int(input())
    fraction1 = Fraction(n1,d1)

    for i in range(query):
        choice, n2, d2 = map(int, input().split())
        fraction2 = Fraction(n2, d2)

        if(choice == 1):
            fraction1.add(fraction2)
            fraction1.printFraction()
        elif(choice == 2):
            fraction1.multiply(fraction2)
            fraction1.printFraction()

main()
