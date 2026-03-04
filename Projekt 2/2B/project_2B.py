#Magician
import math
#Nastavení HOME (domácí) pozice + HOME robota (je to zakomentované, aby to nedělal při každém spuštění kódu)
dType.SetHOMEParams(api,  230,  0,  0,  -25,  isQueued=0)
#dType.SetHOMECmd(api, 1, isQueued=0)
#Nastavení JUMP parametrů, aby rameno nenaráželo do ostatních kostek a nemuselo se procházet přes další bod
dType.SetPTPJumpParams(api, 80, 200, isQueued=0)
#Posunutí robota do HOME pozice, aby se vrátil do ideální polohy + 1,5 sekundy delay, abychom mohli nachystat kostkya zkontrolovat jestli je vše OK
dType.SetPTPCmd(api, 1, 230, 0, 0, -25, isQueued=0)
dType.SetWAITCmd(api, 1500, isQueued=0)

#Určení výšky kostky pro následné přičtení při stavbě věže
vyska_kostky = 23

#Nastavení pozice kde se bude stavět věž
pos_z_vez_kostaka = -35
pos_x_vez = 240
pos_y_vez = -160
pos_r_vez = -20

#Nastavení pozic pro sklad kostek 1-4
pos_z_kostaka1 = -40
pos_x_kostaka1 = 254
pos_y_kostaka1 = 29
pos_r_kostaka1 = -20

pos_z_kostaka2 = -40
pos_x_kostaka2 = 250
pos_y_kostaka2 = -38
pos_r_kostaka2 = -20

pos_z_kostaka3 = -40
pos_x_kostaka3 = 195
pos_y_kostaka3 = 25
pos_r_kostaka3 = -20

pos_z_kostaka4 = -40
pos_x_kostaka4 = 195
pos_y_kostaka4 = -41
pos_r_kostaka4 = -20

#Nekonečná smyčka
While (true):
  #Posunutí robota na pozici úchopu první kostky
  dType.SetPTPCmd(api, 0, pos_x_kostaka1, pos_y_kostaka1, pos_z_kostaka1, pos_r_kostaka1, isQueued=0)
  #Zapnutí vývěvy k chycení kostky
  dType.SetEndEffectorSuctionCup(api, 1,  1, isQueued=1)
  #Posunutí robota na pozici první kostky věže
  dType.SetPTPCmd(api, 0, pos_x_vez, pos_y_vez, pos_z_vez_kostaka, pos_r_vez, isQueued=0)
  #Vypnutí vývěvy k puštění kostky
  dType.SetEndEffectorSuctionCup(api, 1,  0, isQueued=1)

  #V dalších 3 blocích kódu je to obdobně jen s rozdílem pozice kostky ve skladu a přičtení hodnoty vyska_kostky do Z pozice pro uložení do věže, aby se kostky pokládaly stále o jednu nahoru (to se zvětšuje o 1 v každém patře)
  dType.SetPTPCmd(api, 0, pos_x_kostaka2, pos_y_kostaka2, pos_z_kostaka2, pos_r_kostaka2, isQueued=0)
  dType.SetEndEffectorSuctionCup(api, 1,  1, isQueued=1)
  dType.SetPTPCmd(api, 0, pos_x_vez, pos_y_vez, pos_z_vez_kostaka + vyska_kostky, pos_r_vez, isQueued=0)
  dType.SetEndEffectorSuctionCup(api, 1,  0, isQueued=1)

  dType.SetPTPCmd(api, 0, pos_x_kostaka3, pos_y_kostaka3, pos_z_kostaka3, pos_r_kostaka3, isQueued=0)
  dType.SetEndEffectorSuctionCup(api, 1,  1, isQueued=1)
  dType.SetPTPCmd(api, 0, pos_x_vez, pos_y_vez, pos_z_vez_kostaka + vyska_kostky * 2, pos_r_vez, isQueued=0)
  dType.SetEndEffectorSuctionCup(api, 1,  0, isQueued=1)

  dType.SetPTPCmd(api, 0, pos_x_kostaka4, pos_y_kostaka4, pos_z_kostaka4, pos_r_kostaka4, isQueued=0)
  dType.SetEndEffectorSuctionCup(api, 1,  1, isQueued=1)
  dType.SetPTPCmd(api, 0, pos_x_vez, pos_y_vez, pos_z_vez_kostaka + vyska_kostky * 3, pos_r_vez, isQueued=0)
  dType.SetEndEffectorSuctionCup(api, 1,  0, isQueued=1)

  dType.SetPTPCmd(api, 0, 230, 0, 0, -25, isQueued=0)

  #Rozklad věže je velmi podobný jako stavba věže, jen se kroky vyvolávají v opačném pořadí
  dType.SetPTPCmd(api, 0, pos_x_vez, pos_y_vez, pos_z_vez_kostaka + vyska_kostky * 3, pos_r_vez, isQueued=0)
  dType.SetEndEffectorSuctionCup(api, 1,  1, isQueued=1)
  dType.SetPTPCmd(api, 0, pos_x_kostaka4, pos_y_kostaka4, pos_z_kostaka4, pos_r_kostaka4, isQueued=0)
  dType.SetEndEffectorSuctionCup(api, 1,  0, isQueued=1)

  dType.SetPTPCmd(api, 0, pos_x_vez, pos_y_vez, pos_z_vez_kostaka + vyska_kostky * 2, pos_r_vez, isQueued=0)
  dType.SetEndEffectorSuctionCup(api, 1,  1, isQueued=1)
  dType.SetPTPCmd(api, 0, pos_x_kostaka3, pos_y_kostaka3, pos_z_kostaka3, pos_r_kostaka3, isQueued=0)
  dType.SetEndEffectorSuctionCup(api, 1,  0, isQueued=1)

  dType.SetPTPCmd(api, 0, pos_x_vez, pos_y_vez, pos_z_vez_kostaka + vyska_kostky, pos_r_vez, isQueued=0)
  dType.SetEndEffectorSuctionCup(api, 1,  1, isQueued=1)
  dType.SetPTPCmd(api, 0, pos_x_kostaka2, pos_y_kostaka2, pos_z_kostaka2, pos_r_kostaka2, isQueued=0)
  dType.SetEndEffectorSuctionCup(api, 1,  0, isQueued=1)

  dType.SetPTPCmd(api, 0, pos_x_vez, pos_y_vez, pos_z_vez_kostaka, pos_r_vez, isQueued=0)
  dType.SetEndEffectorSuctionCup(api, 1,  1, isQueued=1)
  dType.SetPTPCmd(api, 0, pos_x_kostaka1, pos_y_kostaka1, pos_z_kostaka1, pos_r_kostaka1, isQueued=0)
  dType.SetEndEffectorSuctionCup(api, 1,  0, isQueued=1)

  dType.SetPTPCmd(api, 0, 230, 0, 0, -25, isQueued=0)



