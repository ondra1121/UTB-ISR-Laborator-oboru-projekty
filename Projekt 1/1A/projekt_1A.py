#Magician
import math

#Nastavení HOME (domácí) pozice + HOME robota (je to zakomentované, aby to nedělal při každém spuštění kódu)
dType.SetHOMEParams(api,  230,  0,  0,  -25,  isQueued=0)
#dType.SetHOMECmd(api, 1, isQueued=0)
#Posunutí robota do HOME pozice, aby se vrátil do ideální polohy + 1,5 sekundy delay, abychom mohli nachystat kostkya zkontrolovat jestli je vše OK
dType.SetPTPCmd(api, 1, 230, 0, 0, -25, isQueued=0)
dType.SetWAITCmd(api, 1500, isQueued=0)

#Určení výšky pro kreslení na papír
vyska_papiru_z = -54

#deklarování proměné pro while loop
i=0
while i < 51:
	#Najetí robota nad bod kontroly
	dType.SetPTPCmd(api, 1, 300, 0, 0, 0, isQueued=0)
	#sjetí robotem dolů na uroveň papíru, aby udělal tečku
	dType.SetPTPCmd(api, 1, 300, 0, vyska_papiru_z, 0, isQueued=0)
	#Najetí robota nad bod kontroly
	dType.SetPTPCmd(api, 1, 300, 0, 0, 0, isQueued=0)
	#posubutí robota do HOME pozice
	dType.SetPTPCmd(api, 1, 230, 0, 0, -25, isQueued=0)

	#Další 3 řádky jsou jen 3 body, aby se robot pohnul a mohli jsme zaznamenat nějakou chybu přesnosti
	dType.SetPTPCmd(api, 1, 113, -286, 55, 0, isQueued=0)
	dType.SetPTPCmd(api, 1, 167, -236, 5, 0, isQueued=0)
	dType.SetPTPCmd(api, 1, 18, -297, 28, 0, isQueued=0)
	i+=1


