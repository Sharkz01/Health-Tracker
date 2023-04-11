import bmi_calculator as bmi
import workouts as workout

def main():

    name = bmi.get_name()
    gender = bmi.get_gender()
    bmi.get_age()
    your_bmi = bmi.calculate_bmi()

    km_distances, speed, weekly_average_km, weekly_average_mi, weekly_average_distance = workout.get_workout_input()

    print("\nOutput -------------------------------------------------\n")

    print(f"Hi {gender}. {name}")

    if your_bmi <= 18.5:
        print(f"Your BMI is: {your_bmi}. You have some work ahead of you, but it's great that you are taking this first step. Try to put on some weight. You are considered UNDERWEIGHT.")
    elif your_bmi <= 24.9:
        print(f"Your BMI is: {your_bmi}. That is a good weight, you are starting from a great place!. You are AVERAGE, which is considered NORMAL.")
    elif your_bmi <= 29.9:
        print(f"Your BMI is: {your_bmi}. You have some work ahead of you, but it's great that you are taking this first step. Try to loose some weight. You are considered OVERWEIGHT.")
    else:
        print(f"Your BMI is: {your_bmi}. There's a lot you could gain by losing a little weight. You are considered OBESE.")

    print(f"Your Weekly achievement is as follows:")
    for step in km_distances:
        if step == 0:
            print("No Awards this week, as there are breaks in the schedule")
        else:
            print("No breakout in Sessions: You get a 7/7 award")
            break
    print(f"Your Fastest Speed is: {round(max(speed), 2)} Km/hr")
    print(f"Your Longest Distance is: {max(km_distances)} Km")
    print(f"Your Slowest Speed is: {round(min(speed), 2)} Km/hr")
    print(f"Your Shortest Distance is: {min(km_distances)} Km")
    print(f"Your Weekly Average Speed is: {round(weekly_average_km,2)} Km//hr (or {round(weekly_average_mi,2)} mi/hr)")
    print(f"Your Weekly Average Distance is: {round(weekly_average_distance, 2)} Km")

if __name__ =="__main__":
   main()
