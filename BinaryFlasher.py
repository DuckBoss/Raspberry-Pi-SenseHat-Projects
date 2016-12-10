#Import the necessary packages for the SenseHat and the Time/Sleep controls.
from sense_hat import SenseHat
import time


#declare and initialize the SenseHat module.
sense = SenseHat()

#declare text to translate to Binary.
normalText = "Hello World!"
#declare variable to hold binary translation.
binaryText = ' '.join(format(ord(x), 'b') for x in normalText)

#declare variable to hold flashing speed of the 8x8 matrix lED.
flashSpeed = 0.4

#Prints the binary translation for debugging purposes.
print(' '.join(format(ord(x), 'b') for x in normalText))

#Turn off low light mode so the LED shines bright.
sense.low_light = False


#Loop through individual binary digits from translated text and display
#it to the user through the 8x8 matrix LED.
#
#The loop works on a timer so that it flashes the individual digits.
i = 0
while i < len(binaryText):

    #Pause for 0.6 seconds if the word is complete.
    if(binaryText[i] == ' '):
        time.sleep(0.6)
    else:
        #Shows the individual binary digit on the 8x8 matrix LED.
        sense.show_letter(binaryText[i], text_colour=[255,255,255])


        #Blue colored decorative frame along the edges of the 8x8 matrix LED.
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

        #Waits x-seconds before clearing the screen and flashing the new digit.
        time.sleep(flashSpeed)
        sense.clear()
        time.sleep(flashSpeed)

    #Loop iteration.
    i+=1
    
