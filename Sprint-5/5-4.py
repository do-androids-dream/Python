"""
Solve the problem of finding the tangent of the angle alpha given the sine of alpha and 
the cosine of alpha and add event logging to the "app.log" file.

Catching the resulting sine and cosine values should be implemented using the "info" level.
In the case of successful finding of the tangent of the alpha angle, logging should be with the "debug" level.

In the event that cosine alpha = 0, logging should be with the "warning" level and the notification: 
"The cosine of the angle alpha = 0. The tangent is not defined.".

In the event that the tangent is not defined, logging should be with the "critical" level and the notification: 
"The tangent of the angle alpha is not defined.".

tan(α) = sin(α) / cos(α)
Don't use: encoding='utf-8'.

Don't use'print()'.

Don't use'return'.

Please use logging. ....
"""
import math
import logging

logging.basicConfig(filename="app.log", filemode="w", level="DEBUG")

def findingTangent(sin_alpha, cos_alpha):
    logging.info(f"A value has been entered sin(alpha) = {sin_alpha}")
    logging.info(f"A value has been entered cos(alpha) = {cos_alpha}")
    if type(cos_alpha) is str or type(sin_alpha) is str:
        logging.critical("The tangent of the angle alpha is not defined.")
    elif cos_alpha == 0:
        logging.warning("The cosine of the angle alpha = 0. The tangent is not defined.")
    else:
        logging.debug(f"The value of the tangent of the angle alpha is found = {sin_alpha / cos_alpha}")
        

findingTangent(0.5, math.sqrt(3) / 2)
findingTangent(0.5, 'w')
findingTangent(0.5, 0)