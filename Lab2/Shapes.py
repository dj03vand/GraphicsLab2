import math
class Circle:
	def __init__(self, radius):
		self.radius = radius

	def toString(self):
		return "Circle with radius " + str(self.radius)

	def area(self):
		result = math.pi * (self.radius**2)
		return result
	
	def perimeter(self):
		result = 2 * math.pi * self.radius
		return result
		
class Rectangle:
	def __init__(self, width, height):
		self.width = width
		self.height = height
		
	def toString(self):
		return "Rectangle with width " + str(self.width) + " and height " + str(self.height)
		
		
	def area(self):
		result = self.width * self.height
		return result
		
	def perimeter(self):
		result = 2*(self.width + self.height)
		return result

		