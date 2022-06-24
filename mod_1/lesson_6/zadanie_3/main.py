
import calculations.investment

initial_value_input = float(input("Jaka jest wartość początkowa? "))
percentage_input = float(input("Ile wynosi oprocentowanie? "))
years_input = int(input("Ile lat trwa inwestycja? "))

final_value = calculations.investment.investment_calculator(initial_value_input, percentage_input, years_input)
print(f"Po {years_input} latach przy wpłacie {initial_value_input} i oprocentowaniu {percentage_input}% wartość inwestycji wyniesie {final_value:.2f} zł.")