import unittest
from unittest.mock import patch
from io import StringIO
import sys
import workouts

class TestWorkout(unittest.TestCase):
    sys.stdout
    sys.stdin
    
    @patch('sys.stdin', StringIO('7 days\n'))
    def test_main(self):
        time_durations = []
        km_distances = []

        for i in range (1,8):
            day, steps, times = input()

            time_durations.append(times)

            km_distances.append(float(steps)/1000)

            days= {
                1: "Monday",
                2: "Tuesday",
                3: "Wednesday",
                4: "Thursday",
                5: "Friday",
                6: "Saturday",
                7: "Sunday",
            }
            days.get(int(day), "No such Day")



if __name__ == '__main__':
    unittest.main()