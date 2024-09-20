import sys
sys.path.append("../")

from topologies.topo import *
from simulator import simulator

sim = simulator()
sim.set_params(ResNet18_8)
sim.run()
sim.show()
