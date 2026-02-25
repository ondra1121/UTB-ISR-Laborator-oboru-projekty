#Magician
import math
dType.SetHOMEParams(api,  230,  0,  0,  -25,  isQueued=0)
dType.SetPTPJumpParams(api, 40, 200, isQueued=0)
#dType.SetHOMECmd(api, 1, isQueued=0)
dType.SetPTPCmd(api, 1, 230, 0, 0, -25, isQueued=0)
dType.SetWAITCmd(api, 1500, isQueued=0)

vyska_kostky = 25

pos_z_vez_kostaka = -35
pos_x_vez = 240
pos_y_vez = -160
pos_r_vez = -20

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

dType.SetPTPCmd(api, 0, pos_x_kostaka1, pos_y_kostaka1, pos_z_kostaka1, pos_r_kostaka1, isQueued=0)
dType.SetEndEffectorSuctionCup(api, 1,  1, isQueued=1)
#dType.SetPTPCmd(api, 1, 230, 0, 0, -25, isQueued=0)
dType.SetPTPCmd(api, 0, pos_x_vez, pos_y_vez, pos_z_vez_kostaka, pos_r_vez, isQueued=0)
dType.SetEndEffectorSuctionCup(api, 1,  0, isQueued=1)
#dType.SetPTPCmd(api, 0, 230, 0, 0, -25, isQueued=0)

dType.SetPTPCmd(api, 0, pos_x_kostaka2, pos_y_kostaka2, pos_z_kostaka2, pos_r_kostaka2, isQueued=0)
dType.SetEndEffectorSuctionCup(api, 1,  1, isQueued=1)
#dType.SetPTPCmd(api, 1, 230, 0, 0, -25, isQueued=0)
dType.SetPTPCmd(api, 0, pos_x_vez, pos_y_vez, pos_z_vez_kostaka + vyska_kostky, pos_r_vez, isQueued=0)
dType.SetEndEffectorSuctionCup(api, 1,  0, isQueued=1)
#dType.SetPTPCmd(api, 0, 230, 0, 0, -25, isQueued=0)

dType.SetPTPCmd(api, 0, pos_x_kostaka3, pos_y_kostaka3, pos_z_kostaka3, pos_r_kostaka3, isQueued=0)
dType.SetEndEffectorSuctionCup(api, 1,  1, isQueued=1)
#dType.SetPTPCmd(api, 1, 230, 0, 0, -25, isQueued=0)
dType.SetPTPCmd(api, 0, pos_x_vez, pos_y_vez, pos_z_vez_kostaka + vyska_kostky * 2, pos_r_vez, isQueued=0)
dType.SetEndEffectorSuctionCup(api, 1,  0, isQueued=1)
#dType.SetPTPCmd(api, 0, 230, 0, 0, -25, isQueued=0)

dType.SetPTPCmd(api, 0, pos_x_kostaka4, pos_y_kostaka4, pos_z_kostaka4, pos_r_kostaka4, isQueued=0)
dType.SetEndEffectorSuctionCup(api, 1,  1, isQueued=1)
#dType.SetPTPCmd(api, 1, 230, 0, 0, -25, isQueued=0)
dType.SetPTPCmd(api, 0, pos_x_vez, pos_y_vez, pos_z_vez_kostaka + vyska_kostky * 3, pos_r_vez, isQueued=0)
dType.SetEndEffectorSuctionCup(api, 1,  0, isQueued=1)
dType.SetPTPCmd(api, 0, 230, 0, 0, -25, isQueued=0)
####rozloz blbe

dType.SetPTPCmd(api, 0, pos_x_kostaka1, pos_y_kostaka1, pos_z_kostaka1, pos_r_kostaka1, isQueued=0)
dType.SetEndEffectorSuctionCup(api, 1,  1, isQueued=1)
#dType.SetPTPCmd(api, 1, 230, 0, 0, -25, isQueued=0)
dType.SetPTPCmd(api, 0, pos_x_vez, pos_y_vez, pos_z_vez_kostaka, pos_r_vez, isQueued=0)
dType.SetEndEffectorSuctionCup(api, 1,  0, isQueued=1)
#dType.SetPTPCmd(api, 0, 230, 0, 0, -25, isQueued=0)

dType.SetPTPCmd(api, 0, pos_x_kostaka2, pos_y_kostaka2, pos_z_kostaka2, pos_r_kostaka2, isQueued=0)
dType.SetEndEffectorSuctionCup(api, 1,  1, isQueued=1)
#dType.SetPTPCmd(api, 1, 230, 0, 0, -25, isQueued=0)
dType.SetPTPCmd(api, 0, pos_x_vez, pos_y_vez, pos_z_vez_kostaka + vyska_kostky, pos_r_vez, isQueued=0)
dType.SetEndEffectorSuctionCup(api, 1,  0, isQueued=1)
#dType.SetPTPCmd(api, 0, 230, 0, 0, -25, isQueued=0)

dType.SetPTPCmd(api, 0, pos_x_kostaka3, pos_y_kostaka3, pos_z_kostaka3, pos_r_kostaka3, isQueued=0)
dType.SetEndEffectorSuctionCup(api, 1,  1, isQueued=1)
#dType.SetPTPCmd(api, 1, 230, 0, 0, -25, isQueued=0)
dType.SetPTPCmd(api, 0, pos_x_vez, pos_y_vez, pos_z_vez_kostaka + vyska_kostky * 2, pos_r_vez, isQueued=0)
dType.SetEndEffectorSuctionCup(api, 1,  0, isQueued=1)
#dType.SetPTPCmd(api, 0, 230, 0, 0, -25, isQueued=0)

dType.SetPTPCmd(api, 0, pos_x_kostaka4, pos_y_kostaka4, pos_z_kostaka4, pos_r_kostaka4, isQueued=0)
dType.SetEndEffectorSuctionCup(api, 1,  1, isQueued=1)
#dType.SetPTPCmd(api, 1, 230, 0, 0, -25, isQueued=0)
dType.SetPTPCmd(api, 0, pos_x_vez, pos_y_vez, pos_z_vez_kostaka + vyska_kostky * 3, pos_r_vez, isQueued=0)
dType.SetEndEffectorSuctionCup(api, 1,  0, isQueued=1)
dType.SetPTPCmd(api, 0, 230, 0, 0, -25, isQueued=0)