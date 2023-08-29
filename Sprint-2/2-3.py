"""
The string defining the points of the quadrilateral has the next form: "#LB1:1#RB4:1#LT1:3#RT4:3"

 LB - Left Bottom point
 LT - Left Top point
 RT - Right Top point
 RB - Right Bottom point
numbers after letters are the coordinates of a point.
Write a function figure_perimetr() that calculates the perimeter of a quadrilateral

The formula for calculating the distance between points:
((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5
"""
import re

def figure_perimetr(str):
    pattern = r"(\d+):(\d+)"
    coord = re.findall(pattern, str)
    lb = coord[0]
    rb = coord[1]
    lt = coord[2]
    rt = coord[3]
    bottom_side = ((int(rb[0]) - int(lb[0])) ** 2 + (int(rb[1]) - int(lb[1])) ** 2) ** 0.5
    right_side = ((int(rt[0]) - int(rb[0])) ** 2 + (int(rt[1]) - int(rb[1])) ** 2) ** 0.5
    top_side = ((int(rt[0]) - int(lt[0])) ** 2 + (int(rt[1]) - int(lt[1])) ** 2) ** 0.5
    left_side = ((int(lt[0]) - int(lb[0])) ** 2 + (int(lt[1]) - int(lb[1])) ** 2) ** 0.5
    return bottom_side + right_side + top_side + left_side


test1 = "#LB1:1#RB4:1#LT1:3#RT4:3"
print(figure_perimetr(test1))
# 10.0
test2 = "#LB0:1#RB5:1#LT4:5#RT8:3"
print(figure_perimetr(test2))
# 18.73454147995595
