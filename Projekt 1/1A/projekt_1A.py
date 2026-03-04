#Magician
import math

dType.SetHOMEParams(api,  230,  0,  0,  -25,  isQueued=0)
dType.SetHOMECmd(api, 1, isQueued=0)
dType.SetPTPCmd(api, 1, 230, 0, 0, -25, isQueued=0)
dType.SetWAITCmd(api, 1500, isQueued=0)

vyska_papiru_z = -54
i=0
while i < 51:
	dType.SetPTPCmd(api, 1, 300, 0, 0, 0, isQueued=0)
	dType.SetPTPCmd(api, 1, 300, 0, vyska_papiru_z, 0, isQueued=0)
	dType.SetPTPCmd(api, 1, 300, 0, 0, 0, isQueued=0)
	dType.SetPTPCmd(api, 1, 230, 0, 0, -25, isQueued=0)

	dType.SetPTPCmd(api, 1, 113, -286, 55, 0, isQueued=0)
	dType.SetPTPCmd(api, 1, 167, -236, 5, 0, isQueued=0)
	dType.SetPTPCmd(api, 1, 18, -297, 28, 0, isQueued=0)
	i+=1


