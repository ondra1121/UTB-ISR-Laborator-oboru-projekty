#Magician
def barvicka():
	dType.SetColorSensor(api, 1, 1, version=1)
	dType.SetWAITCmd(api, 500, isQueued=1)
	if(dType.GetColorSensor(api,)[0]==1):
		dType.SetPTPCmd(api, 0, color_pos_red[0], color_pos_red[1], color_pos_red[2], color_pos_red[3], isQueued=1)
		dType.SetEndEffectorSuctionCup(api, 1,  0, isQueued=1)
		print("R")
	if(dType.GetColorSensor(api)[1]==1):
		dType.SetPTPCmd(api, 0, color_pos_green[0], color_pos_green[1], color_pos_green[2], color_pos_green[3], isQueued=1)
		dType.SetEndEffectorSuctionCup(api, 1,  0, isQueued=1)
		print("G")
	if(dType.GetColorSensor(api)[2]==1):
		dType.SetPTPCmd(api, 0, color_pos_blue[0], color_pos_blue[1], color_pos_blue[2], color_pos_blue[3], isQueued=1)
		dType.SetEndEffectorSuctionCup(api, 1,  0, isQueued=1)
		print("B")
	dType.SetWAITCmd(api, 500, isQueued=1)
	dType.SetColorSensor(api, 0, 1, version=1)


import math

#Nastavení HOME (domácí) pozice + HOME robota (je to zakomentované, aby to nedìlal pøi každém spuštìní kódu)
dType.SetHOMEParams(api,  230,  0,  0,  -25,  isQueued=1)
#dType.SetHOMECmd(api, 1, isQueued=0)
#Posunutí robota do HOME pozice, aby se vrátil do ideální polohy + 1,5 sekundy delay, abychom mohli nachystat kostkya zkontrolovat jestli je vše OK
dType.SetPTPCmd(api, 0, 230, 0, 0, -25, isQueued=1)
dType.SetEndEffectorSuctionCup(api, 1,  0, isQueued=1)
print("JEDU!")
dType.SetWAITCmd(api, 1000, isQueued=0)
dType.SetPTPJumpParams(api, 50, 100, isQueued=1)
dType.SetColorSensor(api, 0, 1, version=1)

pocet_kostek_sklad = 3
i = 0
posun_sklad_dalsi_kostka_Y = 32
sklad_pos_x = [282, 246, 211, 179, 143]
sklad_pos_y = [-104, -106, -110, -113, -113]
sklad_pos_z = -55
sklad_pos_r = [-22, -25, -29, -34, -40]

color_pos_red = [290, 3, -49, -1]
color_pos_green = [292, -52, -48, -11]
color_pos_blue = [291, 89, -48, 15]

while i < pocet_kostek_sklad:

	dType.SetPTPCmd(api, 0, sklad_pos_x[i], sklad_pos_y[i], sklad_pos_z, sklad_pos_r[i], isQueued=1)
	dType.SetEndEffectorSuctionCup(api, 1,  1, isQueued=1)
	dType.SetPTPCmd(api, 0, 117, 218, 16, 60, isQueued=1)

	barvicka()

	dType.SetPTPCmd(api, 0, 230, 0, 0, -25, isQueued=1)
	dType.SetEndEffectorSuctionCup(api, 1,  0, isQueued=1)

	i += 1
	list = [0, 0, 0]

dType.SetPTPCmd(api, 0, 230, 0, 0, -25, isQueued=1)

