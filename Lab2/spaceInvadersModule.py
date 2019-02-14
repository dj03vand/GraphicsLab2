import viz
class Ship:
	def __init__(self, x, y):
		height = 10
		width = 10
		self.x = 0
		self.y = 0
		viz.startLayer(viz.QUADS)
		viz.vertexColor(1,0,0)
		viz.pointSize(1)
		viz.vertex(-25,25)
		viz.vertex(25,25)
		viz.vertex(25,-25)
		viz.vertex(-25,-25)
		viz.endLayer()
		
		
	def getX(self):
		return self.x
		
	def getY(self):
		return self.y
		
class Alien:
	def __init__(self, x, y):
		height = 10
		width = 10
		self.x = 0
		self.y = 0
		viz.startLayer(viz.QUADS)
		viz.vertexColor(1,0,0)
		viz.pointSize(1)
		viz.vertex(-20,20)
		viz.vertex(20,20)
		viz.vertex(20,-20)
		viz.vertex(-20,-20)
		viz.endLayer()
		
	def getX(self):
		return self.x
		
	def getY(self):
		return self.y
	
class Bullet:
	def __init__(self, x, y):
		height = 10
		width = 10
		self.x = 0
		self.y = 0
		viz.startLayer(viz.QUADS)
		viz.vertexColor(1,1,0)
		viz.pointSize(1)
		viz.vertex(-5,10)
		viz.vertex(5,10)
		viz.vertex(5,-10)
		viz.vertex(-5,-10)
		viz.endLayer()
		
	def getX(self):
		return self.x
		
	def getY(self):
		return self.y
		
	
		