from datetime import *
import calendar


def get_workout_input():
    print("\nworkout input -------------------------------")
    while True:
        sample = input("\nDo you wish input a 7-days sample or 1-month sample? ")
        if sample == "7-days" or sample == "7 days" or sample == "7" or sample == "7-days sample":
            print("Please enter your sample of days worked out")
            
            time_durations = []
            km_distances = []

            for i in range (1,8):
                try:
                    day, steps, times = input().split(",")
                except:
                    print("wrong input. Please try again")
                    day, steps, times = input().split(",")

                # LIST OF TIME TAKEN (HOURS:MINUTES:SECONDS)  
                time_durations.append(times)

                #STEPS (CM -> KM)
                km_distances.append(float(steps)/1000)

                # DAY
                days= {
                    1: "Monday",
                    2: "Tuesday",
                    3: "Wednesday",
                    4: "Thursday",
                    5: "Friday",
                    6: "Saturday",
                    7: "Sunday",
                }

            day_data = days.get(int(day), "No such Day")

            conversion_factor = 0.621371

            get_hours = [float(timeduration.split(":")[0]) + float(timeduration.split(":")[1])/60 + float(timeduration.split(":")[2])/3600 for timeduration in time_durations]
            mi_distances = [x*conversion_factor for x in km_distances]

            speed = [x/y for x,y in zip(km_distances, get_hours)]
            mi_per_hour = [round(x/y, 2) for x,y in zip(mi_distances, get_hours)]
            km_per_hour = [round(x/y, 2) for x,y in zip(km_distances, get_hours)]

            weekly_average_km = sum(km_per_hour)/len(km_per_hour)
            weekly_average_mi = sum(mi_per_hour)/len(mi_per_hour)
            weekly_average_distance = sum(km_distances)/len(km_distances)

            return km_distances, speed, weekly_average_km, weekly_average_mi, weekly_average_distance

        elif sample == "1-month" or sample == "1 month" or sample == "1" or sample == "1-month sample":
            current_day = datetime.now()
            days_in_month = calendar.monthrange(current_day.year, current_day.month)
            res = days_in_month[1]

            print("Please enter your sample of days worked out")

            time_durations = []
            km_distances = []

            for i in range(1, res+1):
                try:
                    day, steps, time = input().split(",")
                except:
                    print("wrong input. Please try again")
                    day, steps, time = input().split(",")

                 #STEPS (CM -> KM)
                km_distances.append(float(steps)/1000)

                # LIST OF TIME TAKEN (HOURS:MINUTES:SECONDS)  
                time_durations.append(times)

                # DAY
                days= {
                    1: "Monday",
                    2: "Tuesday",
                    3: "Wednesday",
                    4: "Thursday",
                    5: "Friday",
                    6: "Saturday",
                    7: "Sunday",
                }

            day_data = days.get(int(day), "No such Day")

            conversion_factor = 1.609344
            get_hours = [float(timeduration.split(":")[0]) + float(timeduration.split(":")[1])/60 + float(timeduration.split(":")[2])/3600 for timeduration in time_durations]
            mi_distances = [x*conversion_factor for x in km_distances]

            speed = [x/y for x,y in zip(km_distances, get_hours)]
            mi_per_hour = [round(x/y, 2) for x,y in zip(mi_distances, get_hours)]
            km_per_hour = [round(x/y, 2) for x,y in zip(km_distances, get_hours)]

            weekly_average_km = sum(km_per_hour)/len(km_per_hour)
            weekly_average_mi = sum(mi_per_hour)/len(mi_per_hour)
            weekly_average_distance = sum(km_distances)/len(km_distances)

            return km_distances, speed, weekly_average_km, weekly_average_mi, weekly_average_distance
 
        else:
            print("Invalid Sample")
            continue

