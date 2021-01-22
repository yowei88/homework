from mcpi.minecraft import Minecraft
import time
mc=Minecraft.create()
x,y,z=mc.player.getTilePos()
while True:
    mc.spawnEntity(x,y+6,z,93)
    time.sleep(5)