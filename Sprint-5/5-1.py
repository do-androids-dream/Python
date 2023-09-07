"""
Write  the function solve_quadric_equation(a, b, c) the three input parameters of which are numbers. The function should return 
the solution of quadratic equation ax**2+bx+c=0, where coefficients a, b, c are input parameters of  the function solve_quadric_equation:

 in case of correct data the function should displayed the corresponding message – "The solution are x1=… and x2=…"

in the case of division by zero the function should displayed the corresponding message – "Zero Division Error" 

in the case of incorrect data the function should displayed the message – "Could not convert string to float"
Note: in the function you must use the "try except" construct.  

 Function example:

solve_quadric_equation(1, 5, 6)            #output:   " The solution are x1=(-2-0j) and x2=(-3+0j)"

solve_quadric_equation(0, 8, 1)            #output:   "Zero Division Error"

solve_quadric_equation(1,”abc”, 5)       #output:   "Could not convert string to float"

"""
import cmath

def solve_quadric_equation(a, b, c):
    try:
        a, b, c = complex(a), complex(b), complex(c)
        d = b ** 2 - 4 * a * c
        # if d > 0:
        x1 = (-b + d) / (2 * a)
        x2 = (-b - d) / (2 * a)
        return f"The solution are x1={x1} and x2={x2}"
    except ZeroDivisionError:
        return "Zero Division Error"
    except ValueError:
        return "Could not convert string to float"


print(solve_quadric_equation(1, 5, 6))
print(solve_quadric_equation(0, 8, 1))
print(solve_quadric_equation(1, "abc", 5))
print(solve_quadric_equation(1, 4, 5))