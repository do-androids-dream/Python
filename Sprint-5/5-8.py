"""
You get a list of numbers and you have to write a program that calculates the arithmetic mean of these numbers and 
logs the result in the file 'app.log' with the notification level - "info".

If the input list is empty, the program should return the line "The list is empty" - the notification should be of the "debug" level.

If a ZeroDivisionError error occurs in the process of calculating the arithmetic mean, 
the program should return the line "Division by zero" - the notification should be of the "warning" level.

If the function receives an argument that has the correct type but an inappropriate value, 
then handle a ValueError exception - the notification should be of the "error" level.

If one of the numbers in the list is not a number, the program should return the line "Incorrect data entered" - 
the notification should be of the "critical" level.

Change the basic configuration with filename 'app.log', file read method 'w' and output name, level name and message.

Don't use: encoding='utf-8'.

Don't use'print()'.

Don't use'return'.

Please use logging. ....
"""

import logging

logging.basicConfig(filename="app.log", filemode="w", format="%(name)s - %(levelname)s - %(message)s", level="DEBUG")

def average(numbers):
    try:
        logging.info(f"{sum(numbers) / len(numbers)}")
    except ZeroDivisionError:
        logging.debug("The list is empty")
        logging.warning("Division by zero")
    except ValueError:
        logging.error("ValueError")
    except TypeError:
        logging.critical("Incorrect data entered")

average([1, 2, 3, 4, 5])
average([10, -20, -30])
average([])
average([1, 2, 3, 0, 5])
average([1, 2, "three", 4, 5])