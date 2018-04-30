from robots.robot import Robot as rien
from robots.rconverter import RConverter as Robot

#from strategie.strat70 import Strat70 as Strat
#from strategie.stratCarre70 import StratCarre70 as Strat
from strategie.stratRotD90 import StratRotD90 as Strat

POS=(0,0,0)
DIR=90
V=360

r=Robot(POS,DIR,V)
print(r.toString())

s=Strat(r)
r.setStrat(s)

while not r.strat.stop():
    r.runStrat()
    print(r.toString())
r.setStrat(None)
print("Strat stopped")

"""
print("Move:")
r.move()
print(r.toString())
print("---Test Rotate 1 -> 180°---")
r.rotate(180)
print(r.toString())

print("Move:")
r.move()
print(r.toString())

print("---Test Rotate 2 -> -90° ---")
r.rotate(-90)
print(r.toString())

print("---Test Speed -> 720 dps ---")
r.setVitesse(720)
print(r.toString())

print("Move:")
r.move()
print(r.toString())

print("---Test Rotate 3 -> -180° ---")
r.rotate(-180)
print(r.toString())

print("Move:")
r.move()
print(r.toString())"""
