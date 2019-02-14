import viz
from spaceInvadersModule import *

window = viz.MainWindow
window.ortho(-100,100,-100,100,-1,1)
window.clearcolor(viz.WHITE)
viz.eyeheight(0);


#s = Ship(0,0)
#print(s.getX())
#print(s.getY())

#a = Alien(0,0)
#print(a.getX())
#print(a.getY())

b = Bullet(0,0)
print(b.getX())
print(b.getY())

viz.go()