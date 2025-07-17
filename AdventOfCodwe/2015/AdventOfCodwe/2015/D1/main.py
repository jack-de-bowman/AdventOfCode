import os
import json
def read():
	abs_path= os.path.dirname(os.path.abspath(__file__))
	input = os.path.join(abs_path, "input.json")
	with open(input,"r") as file:
		input = json.load(file)
	print(input)
	x = 0
	y = 0
	lenght = len(input)
	for p in input:
		if x == -1:
			break
		else :
			y += 1
		if p  == "(" :
			x += 1
	
		elif p ==")":
			x -= 1
		
			
			
	print(x, y)
			
read()
 