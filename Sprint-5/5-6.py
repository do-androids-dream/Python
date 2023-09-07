"""
We have a function calc(a, b, op) as shown on screenshot.

Write your code insode run_calc with calling of function calc. Script must work with any arguments. 
Catch ValueError and print it, catch TypeError and print "TypeError", Catch error of division by zero and print "Division by zero".
After call calc print "End of calculation" in all cases.

"""
def run_calc(a, b, op):
    try:
        print(calc(a, b, op))
    except ValueError as e:
        print(e)
    except TypeError:
        print("TypeError")
    except ZeroDivisionError:
        print("Division by zero")
    print("End of calculation")