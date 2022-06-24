
import speed_calculator

running_distance = float(input("Ile km przebiegłeś? "))
running_time = float(input("Ile godzin Ci to zajęło? "))

speed = speed_calculator.speed(running_distance, running_time)

print(f"Średnia prędkość biegu wynosi {speed} km/h.")