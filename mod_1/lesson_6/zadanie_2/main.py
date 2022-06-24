
import math

def hypotenuse_lenght(a, b):
    return math.sqrt(math.pow(a, 2) + math.pow(b, 2))

a_length = float(input("Jaka jest długość przyprostokątnej a? "))
b_lenght = float(input("Jaka jest długość przyprostokątnej b? "))

print(f"Długość przeciwprostokątnej wynosi {hypotenuse_lenght(a_length, b_lenght):.2f}.")