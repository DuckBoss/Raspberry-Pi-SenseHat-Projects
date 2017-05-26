from sense_hat import SenseHat
from time import sleep
import datetime

sense = SenseHat()
B = [0,0,255]
R = [255,0,0]
G = [0,255,0]
W = [255,255,255]
E = [0,0,0]


while(True):
        curTime = datetime.datetime.now()
        curSecond = curTime.second
        curMinute = curTime.minute
        curHour = curTime.hour
        curSecondBin = format(curSecond, '08b')
        curMinuteBin = format(curMinute, '08b')
        curHourBin = format(curHour, '08b')
        
        data_bin = [W] * 64
        for counter in range(8,16):
                data_bin[counter] = E
        for counter in range(16,32):
                data_bin[counter] = E
        for counter in range(32,64):
                data_bin[counter] = E

        for counter in range(len(curHourBin)):
                if(curHourBin[counter] == '1'):
                        data_bin[counter] = R
                else:
                        data_bin[counter] = W

        for counter in range(len(curMinuteBin)):
                if(curMinuteBin[counter] == '1'):
                        data_bin[counter+16] = G
                else:
                        data_bin[counter+16] = W

        for counter in range(len(curSecondBin)):
                if(curSecondBin[counter] == '1'):
                        data_bin[counter+32] = B
                else:
                        data_bin[counter+32] = W



        
        sense.set_pixels(data_bin)
        
        sleep(1)
	



