from mcpi.minecraft import Minecraft
mc = Minecraft.create()
while True:
    t=mc.events.pollBlockHits()
    if len(t)>0:
        hit=t[0]
        x,y,z=hit.pos.x,hit.pos.y,hit.pos.z
        b=mc.getBlock(x,y,z)
        if b==2:
            mc.setBlock(x,y,z,46)