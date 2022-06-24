
# Napisz kalkulator obliczający wartość lokaty po pewnym czasie.
#
# Wczytaj od użytkownika informacje o:
#
# Początkowym kapitale (wpłaconej kwocie)
# Oprocentowaniu
# Okresie trwania inwestycji (w latach)
# Umieść funkcję obliczająca wartość lokaty w pakiecie calculations,
# a wczytanie danych i uruchomienie obliczeń w pliku powyżej pakietu.
#
# Skorzystaj ze wzoru: wartość = wartość pocz. * (1 + procent/100) ^ liczba lat

import calculations.investment

initial_value = float(input("Jaka jest wartość wpłaconej kwoty? "))
percentage = float(input("Ile wynosi oprocentowanie? "))
years = float(input("Ile lat będzie trwać inwestycja? "))

final_value = calculations.investment.calculate_investment_value(initial_value, percentage, years)
print(f"Po {years} latach przy oprocentowaniu {percentage} % Twoja lokata będzie warta {final_value:.2f} zł.")
