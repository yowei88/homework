from mcpi.minecraft import Minecraft
mc = Minecraft.create()
x,y,z=mc.player.getTilePos()
for i in range(1,1001):
    mc.setBlock(x+i,y-1,z+i,46)