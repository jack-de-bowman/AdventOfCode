import csv 
import os
import re
def calculator():
	abs_path = os.path.dirname(os.path.abspath(__file__))
	input = os.path.join(abs_path, "input.csv")
	
	with open(input, newline = '') as file :
		input = csv.reader(file)
		total_surface = 0
		ribbon_lenght = 0
		
		for row in input:
	
			dimensions = row[0].split('x')
			lenght, width, height = map(int, dimensions)
			
			present_volume = lenght * height * width
			a_dimension =  2 * lenght * width 
			b_dimension = 2* width * height
			c_dimension = 2* lenght * height
			present_surface = a_dimension + b_dimension + c_dimension
			
			smallest_side = min(a_dimension, b_dimension, c_dimension)
			sides = [lenght, width, height]
			sides.sort()
			ribbon_lenght += (sides[0] * 2) + (sides[1] * 2)
			smallest_side /= 2
			total_surface += present_surface + smallest_side
			
			ribbon_lenght += present_volume
		
		print(f"The presents need {total_surface}square feet of paper and {ribbon_lenght}ft of ribbon")

calculator()
	#lenght  	widht  height

