from sense_hat import SenseHat
from time import sleep
import datetime

class BinaryClock:

	def __init__(self):
		print("The Program Has Started...")
		self.sense = SenseHat()

	def ModifyPixels(self, data):
		print("Modifying Pixels...")
		self.sense.set_pixels(data)
		sleep(1)


def main():
	program = BinaryClock()
	B = [0,0,255]
	R = [255,0,0]
	G = [0,255,0]
	W = [255,255,255]
	E = [0,0,0]

	while(True):
		curTime =  datetime.datetime.now()
		curSecond = format(curTime.second, '08b')
		curMinute = format(curTime.minute, '08b')
		curHour = format(curTime.hour, '08b') 

		data_bin = [W] * 64
		for counter in range(8,64):
			data_bin[counter] = E

		for counter in range(len(curHour)):
			if(curHour[counter] == '1'):
				data_bin[counter] = R
			else:
				data_bin[counter] = W

		for counter in range(len(curMinute)):
			if(curMinute[counter] == '1'):
				data_bin[counter+16] = G
			else:
				data_bin[counter+16] = W

		for counter in range(len(curSecond)):
			if(curSecond[counter+32] == '1'):
				data_bin[counter+32] = B
			else:
				data_bin[counter+32] = W

		program.ModifyPixels(data_bin)
 

if __name__ == "__main__":
	main()