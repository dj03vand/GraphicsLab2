import viz
from spaceInvadersModule import *

window = viz.MainWindow
window.ortho(-100,100,-100,100,-1,1)
window.clearcolor(viz.WHITE)
viz.eyeheight(0);

s = Ship(0,0)

viz.go()