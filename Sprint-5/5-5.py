"""
Write  the function day_of_week(day) whose input parameter is a number or string representation of number. 
The function returns the corresponding day of the week if the input parameter is in the range of 1 to 7, namely

in the case when the input parameter is 5 the function should be displayed the message – "Friday"

in the case when the input parameter is not in the range of 1 to 7 the function should be displayed the message – 
"There is no such day of the week! Please try again."

in the case of incorrect data the function should be displayed the message - "You did not enter a number! Please try again."

Note: in the function you must use the "try except" construct.
"""

def day_of_week(day):
    week = {1: "Monday", 2: "Tuesday", 3: "Wednesday", 4: "Thursday", 5: "Friday", 6: "Saturday", 7: "Sunday"}
    try:
        return week[int(day)]
    except KeyError:
        return "There is no such day of the week! Please try again."
    except ValueError:
        return "You did not enter a number! Please try again."
        


print(day_of_week(2))                     # output:   "Tuesday"

print(day_of_week(11))                     # output:  "There is no such day of the week! Please try again."

print(day_of_week("Monday"))       # output:   "You did not enter a number! Please try again."