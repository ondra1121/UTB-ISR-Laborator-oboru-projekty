#Magician
import math


dType.SetPTPJointParams(api,200,200,200,200,200,200,200,200,0)
dType.SetPTPCoordinateParams(api,200,200,200,200,0)
dType.SetPTPJumpParams(api, 10, 200,0)
dType.SetPTPCommonParams(api, 100, 100,0)

#dType.SetHOMECmd(api, 0, isQueued=1)

#Start pozice
#z = -55
z = -52
rHead = 35
dType.SetPTPCmd(api, 0, 310, -5, z, rHead, isQueued=0) #x50 y-5

#Bludiste
dType.SetPTPCmd(api, 2, 302, -5, z, rHead, isQueued=0)
dType.SetPTPCmd(api, 2, 302, 4, z, rHead, isQueued=0)
dType.SetPTPCmd(api, 2, 295, 4, z, rHead, isQueued=0)
dType.SetPTPCmd(api, 2, 295, 27, z, rHead, isQueued=0)
dType.SetPTPCmd(api, 2, 286, 27, z, rHead, isQueued=0)
dType.SetPTPCmd(api, 2, 286, 20, z, rHead, isQueued=0)
dType.SetPTPCmd(api, 2, 277, 20, z, rHead, isQueued=0)
dType.SetPTPCmd(api, 2, 277, 35, z, rHead, isQueued=0)
dType.SetPTPCmd(api, 2, 286, 35, z, rHead, isQueued=0)
dType.SetPTPCmd(api, 2, 286, 42, z, rHead, isQueued=0)
dType.SetPTPCmd(api, 2, 270, 42, z, rHead, isQueued=0)
dType.SetPTPCmd(api, 2, 270, 20, z, rHead, isQueued=0)
dType.SetPTPCmd(api, 2, 261, 20, z, rHead, isQueued=0)
dType.SetPTPCmd(api, 2, 261, 13, z, rHead, isQueued=0)
dType.SetPTPCmd(api, 2, 268, 13, z, rHead, isQueued=0)
dType.SetPTPCmd(api, 2, 268, 3, z, rHead, isQueued=0)
dType.SetPTPCmd(api, 2, 277, 3, z, rHead, isQueued=0)
dType.SetPTPCmd(api, 2, 277, 10, z, rHead, isQueued=0)
dType.SetPTPCmd(api, 2, 285, 10, z, rHead, isQueued=0)
dType.SetPTPCmd(api, 2, 285, -4, z, rHead, isQueued=0)
dType.SetPTPCmd(api, 2, 294, -4, z, rHead, isQueued=0)
dType.SetPTPCmd(api, 2, 294, -29, z, rHead, isQueued=0)
dType.SetPTPCmd(api, 2, 285, -29, z, rHead, isQueued=0)
dType.SetPTPCmd(api, 2, 286, -43, z, rHead, isQueued=0)
dType.SetPTPCmd(api, 2, 274, -43, z, rHead, isQueued=0)
dType.SetPTPCmd(api, 2, 274, -29, z, rHead, isQueued=0)
dType.SetPTPCmd(api, 2, 267, -29, z, rHead, isQueued=0)
dType.SetPTPCmd(api, 2, 267, -44, z, rHead, isQueued=0)
dType.SetPTPCmd(api, 2, 252, -44, z, rHead, isQueued=0)
dType.SetPTPCmd(api, 2, 252, -52, z, rHead, isQueued=0)
dType.SetPTPCmd(api, 2, 243, -52, z, rHead, isQueued=0)
dType.SetPTPCmd(api, 2, 243, -43, z, rHead, isQueued=0)
dType.SetPTPCmd(api, 2, 201, -43, z, rHead, isQueued=0)
dType.SetPTPCmd(api, 2, 201, -36, z, rHead, isQueued=0)
dType.SetPTPCmd(api, 2, 209, -36, z, rHead, isQueued=0)
dType.SetPTPCmd(api, 2, 209, -29, z, rHead, isQueued=0)
dType.SetPTPCmd(api, 2, 202, -29, z, rHead, isQueued=0)
dType.SetPTPCmd(api, 2, 202, -23, z, rHead, isQueued=0)
dType.SetPTPCmd(api, 2, 189, -23, z, rHead, isQueued=0)
dType.SetPTPCmd(api, 2, 184, -19, z, rHead, isQueued=0)
dType.SetPTPCmd(api, 2, 184, -7, z, rHead, isQueued=0)
dType.SetPTPCmd(api, 2, 178, -7, z, rHead, isQueued=0)
dType.SetPTPCmd(api, 2, 178, -13, z, rHead, isQueued=0)
dType.SetPTPCmd(api, 2, 174, -13, z, rHead, isQueued=0)



