#Magician
import math
import numpy as np

dType.SetHOMEParams(api,  230,  0,  0,  -25,  isQueued=0)
#dType.SetHOMECmd(api, 1, isQueued=0)
dType.SetPTPCmd(api, 1, 230, 0, 0, -25, isQueued=0)
dType.SetWAITCmd(api, 1500, isQueued=0)

r = 20
x0 = 230
y0 = 0
z = -54
rot = -25

theta = np.linspace(0, 2*np.pi, 100)

for t in theta:
    x = x0 + r * math.cos(t)
    y = y0 + r * math.sin(t)
    dType.SetPTPCmd(api, 1, x, y, z, rot, isQueued=0)

dType.SetPTPCmd(api, 1, 230, 0, 0, -25, isQueued=0)