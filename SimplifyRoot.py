def square(num: int):
    return num*num

def PrimeCheck(num: int):
    for n in range(2, num-1):
        if num % n == 0:
            return False
    return True

def NextPrime(num: int):
    temp = num+1
    while not PrimeCheck(temp):
        temp += 1
    return temp


class SquareRoot:
    def __init__(self, number: int):
        self.number = number
        self.outOfRoot = 1
        self.Imaginary = False

        if int(self.number) < 0:
            self.Imaginary = True
            self.number = -self.number

        prime = 1

        while square(prime) <= self.number:
        
            if self.number % square(prime) == 0:
                self.outOfRoot *= prime
                self.number /= square(prime)
                prime = 1
            prime = NextPrime(prime)
        self.number = int(self.number)


    # def __add__(self, other):
    #     pass

    # def __mul__(self, other):
        
    #     tempSR = SquareRoot(self.number*other.number)
    #     tempSR.outOfRoot = self.outOfRoot*other.outOfRoot
    #     return tempSR


    def __str__(self):
        
        if self.outOfRoot == 1:
            outOfRootShown = ""
        else:
            outOfRootShown = self.outOfRoot
        
        if self.number == 1:
            numberShown = ""
        elif self.Imaginary:
            numberShown = f"i√{self.number}"
        else:
            numberShown = f"√{self.number}"

        return f"{outOfRootShown}{numberShown}"

x = SquareRoot(32)

print(x)
