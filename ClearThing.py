
from mcpi.minecraft import Minecraft
from mcpi import block
from time import sleep

global depth1
global counter
global blockNumber
global setPosition
global mc
'''
depth1 = 0
counter = 0
blockNumber = 0
setPosition = 1
'''

def init():
	global depth1
	global counter
	global blockNumber
	global setPosition
	
	depth1 = 0
	counter = 0
	blockNumber = 0
	setPosition = 1
	
	#ipString = "192.168.1.73"
	ipString = "127.0.0.1"
	#mc = Minecraft.create("127.0.0.1", 4711)
	mc = Minecraft.create(ipString, 4711)
	mc.setting("world_immutable",False)
	#x, y, z = mc.player.getPos() 
	return mc

def one(mc,x,y,z):
	global depth1
	mc.setBlocks(x-25,y,z,x+10,y+depth1,z+25,0)
	if(counter == 29):
		#print(str(i)+" Go to fun 3 "+str(depth1))
		three(mc,x,y,z)
			
	
	
def two(mc,x,y,z):
	global blockNumber
	if(blockNumber == 1):
		mc.setBlocks(x-0, y+0, z+2, x-0, y+0, z+3, 35,13)#1
	if(blockNumber == 2):
		mc.setBlocks(x-0, y+0, z+4, x-0, y+0, z+4, 35,15)#2
	if(blockNumber == 3):
		mc.setBlocks(x-0, y+0, z+5, x-0, y+0, z+6, 35,13)#3
	if(blockNumber == 4):
		mc.setBlocks(x-0, y+0, z+7, x-0, y+0, z+7, 35,15)#4
	if(blockNumber == 5):
		mc.setBlocks(x-0, y+0, z+8, x-0, y+0, z+9, 35,13)#5
	if(blockNumber == 6):
		mc.setBlocks(x-0, y+1, z+2, x-0, y+1, z+3, 35,13)#6
	if(blockNumber == 7):
		mc.setBlocks(x-0, y+1, z+4, x-0, y+1, z+7, 35,15)#7
	if(blockNumber == 8):
		mc.setBlocks(x-0, y+1, z+8, x-0, y+1, z+9, 35,13)#8
	if(blockNumber == 9):
		mc.setBlocks(x-0, y+2, z+2, x-0, y+2, z+3, 35,13)#9
	if(blockNumber == 10):
		mc.setBlocks(x-0, y+2, z+4, x-0, y+2, z+7, 35,15)#10
	if(blockNumber == 11):
		mc.setBlocks(x-0, y+2, z+8, x-0, y+2, z+9, 35,13)#11
	if(blockNumber == 12):
		mc.setBlocks(x-0, y+3, z+2, x-0, y+3, z+4, 35,13)#12
	if(blockNumber == 13):
		mc.setBlocks(x-0, y+3, z+5, x-0, y+3, z+6, 35,15)#13
	if(blockNumber == 14):
		mc.setBlocks(x-0, y+3, z+7, x-0, y+3, z+9, 35,13)#14
	if(blockNumber == 15):
		mc.setBlocks(x-0, y+4, z+2, x-0, y+4, z+2, 35,13)#15
	if(blockNumber == 16):
		mc.setBlocks(x-0, y+4, z+3, x-0, y+4, z+4, 35,15)#16
	if(blockNumber == 17):
		mc.setBlocks(x-0, y+4, z+5, x-0, y+4, z+6, 35,13)#17
	if(blockNumber == 18):
		mc.setBlocks(x-0, y+4, z+7, x-0, y+4, z+8, 35,15)#18
	if(blockNumber == 19):
		mc.setBlocks(x-0, y+4, z+9, x-0, y+4, z+9, 35,13)#19
	if(blockNumber == 20):
		mc.setBlocks(x-0, y+5, z+2, x-0, y+5, z+2, 35,13)#20
	if(blockNumber == 21):
		mc.setBlocks(x-0, y+5, z+3, x-0, y+5, z+4, 35,15)#21
	if(blockNumber == 22):
		mc.setBlocks(x-0, y+5, z+5, x-0, y+5, z+6, 35,13)#22
	if(blockNumber == 23):
		mc.setBlocks(x-0, y+5, z+7, x-0, y+5, z+8, 35,15)#23
	if(blockNumber == 24):
		mc.setBlocks(x-0, y+5, z+9, x-0, y+5, z+9, 35,13)#24
	if(blockNumber == 25):
		mc.setBlocks(x-0, y+6, z+2, x-0, y+6, z+9, 35,13)#25
	if(blockNumber == 26):
		mc.setBlocks(x-0, y+7, z+2, x-0, y+7, z+9, 35,13)#26
		
def three(mc,x,y,z):
	global depth1
	global counter
	global blockNumber
	global setPosition
	sleep(3)
	for g in range(1,26):
		blockNumber += 1
		if(g < 25):
			mc.postToChat("SSSSsssss........")
			#print(str(blockNumber)+" SSSSssss......")
		elif(g == 25 or g == 26):
			mc.postToChat("Ashi....")
		#print(str(g)+" "+str(blockNumber))
		sleep(0.2)
		two(mc,x,y,z)
		
	
def main():
	global depth1
	global counter
	global blockNumber
	global setPosition
	
	if(setPosition == 1):
		mc = init()
		x,y,z = mc.player.getPos()
		mc.player.setPos(x+4,y,z-4)
		setPosition = 0
		#depth1 = 2
	
	for i in range(1, 30):
		depth1 -= 1
		counter += 1
		#mc = init()
		#x,y,z = mc.player.getPos()
		#mc.player.setPos(x,y,z)
		#print("i " ,i)
		print(str(i)+" "+str(depth1))
		mc.postToChat("Loop: "+ str(i) +" Clearing level: "+ str(depth1))
		sleep(0.1)
		one(mc,x,y,z)
	
		
		
if __name__ == "__main__":
	global depth1
	global counter
	global blockNumber
	global setPosition
	global setPosition2
	depth1 = 0
	counter = 0
	blockNumber = 0
	setPosition = 1
	setPosition2 = 1
	main()
