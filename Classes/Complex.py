import math

class Complex(object):
    def __init__(self, real, imaginary):
        self.real, self.imaginary = real, imaginary
        
    def __add__(self, no):
        return Complex(self.real + no.real, self.imaginary + no.imaginary)
        
    def __sub__(self, no):
        return Complex(self.real - no.real, self.imaginary - no.imaginary)
        
    def __mul__(self, no):
        return Complex(self.real * no.real - self.imaginary * no.imaginary, 
            self.real * no.imaginary + self.imaginary * no.real)

    def __truediv__(self, no):
        cd_square = no.real ** 2 + no.imaginary ** 2
        A = self.real * no.real + self.imaginary * no.imaginary
        B = self.imaginary * no.real - self.real * no.imaginary
        return Complex(A / cd_square, B / cd_square)
            
    def mod(self):
        return Complex(pow(self.real ** 2 + self.imaginary ** 2, 0.5), 0)
        
    def __str__(self):
        if self.imaginary == 0:
            result = "%.2f+0.00i" % (self.real)
        elif self.real == 0:
            if self.imaginary >= 0:
                result = "0.00+%.2fi" % (self.imaginary)
            else:
                result = "0.00-%.2fi" % (abs(self.imaginary))
        elif self.imaginary > 0:
            result = "%.2f+%.2fi" % (self.real, self.imaginary)
        else:
            result = "%.2f-%.2fi" % (self.real, abs(self.imaginary))
        return result

if __name__ == '__main__':
    c = map(float, input().split())
    d = map(float, input().split())
    x = Complex(*c)
    y = Complex(*d)
    print(*map(str, [x+y, x-y, x*y, x/y, x.mod(), y.mod()]), sep='\n')