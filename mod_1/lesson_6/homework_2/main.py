
# Zaimplementuj funkcję obliczającą długość przeciwprostokątnej trójkąta
# na podstawie otrzymanych długości przyprostokątnych.
#
# Wzór to: c = pierwiastek_z(a ^ 2 + b ^ 2), gdzie c to przeciwprostokątna.
#
# Wykorzystaj w tym celu moduł math z biblioteki standardowej oraz funkcje:
#
# sqrt(x) - liczy pierwiastek drugiego stopnia z podanej wartości x
# pow(x, y) - podnosi x do potęgi y

import math

def side_c(side_a, side_b):
    return math.sqrt(math.pow(side_a, 2) + math.pow(side_b, 2))

a = float(input("Ile wynosi długość boku a? "))
b = float(input("Ile wynosi długość boku b? "))

print(f"Długość przeciwprostokątnej trójkąta o przyprostokątnych {a} i {b} wynosi {side_c(a, b)}")
