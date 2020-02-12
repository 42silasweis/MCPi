from mcpi.minecraft import Minecraft
from mcpi import block
from time import sleep
chatMSG = ""

def init():
 #ipString = "192.168.7.2" + lastIP
 #ipString = "127.0.0.1"
 #mc = Minecraft.create("127.0.0.1", 4711)
 sendToOther = input("Would you like to send to other IP? y or n : ")
 if(sendToOther == "y"):
	 lastIP = input("Last 3 digits of IP: ")
	 mc = Minecraft.create("192.168.7." + lastIP, 4711)
 elif(sendToOther == "n"):
	 ipString = "127.0.0.1"
	 mc = Minecraft.create(ipString, 4711)
 
 return mc

def main(mc):
	global chatMSG

	while(chatMSG != "exit"):
		if(chatMSG != "exit"):
			chatMSG = input("Say Something: ")
			mc.postToChat(chatMSG)
		else:
			mc.postToChat("192.168.7.217 Disconnected.")
			exit()




if __name__ == "__main__":
	mc = init()
	main(mc)
