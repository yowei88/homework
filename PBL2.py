from mcpi.minecraft import Minecraft
mc=Minecraft.create()
x,y,z=mc.player.getTilePos()
while True:
    mc.setBlocks(x+3,y+3,z+3,38)
    