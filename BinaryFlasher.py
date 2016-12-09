from sense_hat import SenseHat
import time

sense = SenseHat()

normalText = "Hello World!"
binaryText = ' '.join(format(ord(x), 'b') for x in normalText)
flashSpeed = 0.4

print(' '.join(format(ord(x), 'b') for x in normalText))

sense.low_light = False

    

i = 0
while i < len(binaryText):
    
    if(binaryText[i] == ' '):
        time.sleep(0.6)
    else:
        sense.show_letter(binaryText[i], text_colour=[255,255,255])


        
        sense.set_pixel(0, 0, [0,0,255])
        sense.set_pixel(1, 0, [0,0,255])
        sense.set_pixel(2, 0, [0,0,255])
        sense.set_pixel(3, 0, [0,0,255])
        sense.set_pixel(4, 0, [0,0,255])
        sense.set_pixel(5, 0, [0,0,255])
        sense.set_pixel(6, 0, [0,0,255])
        sense.set_pixel(7, 0, [0,0,255])

        sense.set_pixel(0, 1, [0,0,255])
        sense.set_pixel(0, 2, [0,0,255])
        sense.set_pixel(0, 3, [0,0,255])
        sense.set_pixel(0, 4, [0,0,255])
        sense.set_pixel(0, 5, [0,0,255])
        sense.set_pixel(0, 6, [0,0,255])
        sense.set_pixel(0, 7, [0,0,255])

        sense.set_pixel(7, 1, [0,0,255])
        sense.set_pixel(7, 2, [0,0,255])
        sense.set_pixel(7, 3, [0,0,255])
        sense.set_pixel(7, 4, [0,0,255])
        sense.set_pixel(7, 5, [0,0,255])
        sense.set_pixel(7, 6, [0,0,255])
        sense.set_pixel(7, 7, [0,0,255])
        
        time.sleep(flashSpeed)
        sense.clear()
        time.sleep(flashSpeed)
    i+=1
    
