# wartość = wartość pocz. * (1 + procent/100) ^ liczba lat

def calculate_investment_value(initial_value, percentage, years):
    return initial_value * (1 + percentage / 100) ** years