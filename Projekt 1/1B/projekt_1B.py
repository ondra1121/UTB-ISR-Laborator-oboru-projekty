#Magician
import math
import numpy as np

#Nastavení HOME (domácí) pozice + HOME robota (je to zakomentované, aby to nedělal při každém spuštění kódu)
dType.SetHOMEParams(api,  230,  0,  0,  -25,  isQueued=0)
#dType.SetHOMECmd(api, 1, isQueued=0)
#Posunutí robota do HOME pozice, aby se vrátil do ideální polohy + 1,5 sekundy delay, abychom mohli nachystat kostkya zkontrolovat jestli je vše OK
dType.SetPTPCmd(api, 1, 230, 0, 0, -25, isQueued=0)
dType.SetWAITCmd(api, 1500, isQueued=0)

#Nastavení hodnot pro rovnici kružnice
r = 20
x0 = 230
y0 = 0
z = -54
rot = -25

#nastavení thety pro 360°
theta = np.linspace(0, 2*np.pi, 100)

#Vykreslení pro každé theta v rovnici
for t in theta:
    #výpočet hodnoty x
    x = x0 + r * math.cos(t)
    #výpočet hodnoty y
    y = y0 + r * math.sin(t)
    #Vykreslení hodnot X a Y
    dType.SetPTPCmd(api, 1, x, y, z, rot, isQueued=0)

#Posunutí robota do HOME pozice
dType.SetPTPCmd(api, 1, 230, 0, 0, -25, isQueued=0)