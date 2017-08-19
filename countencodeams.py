import gpiozero
import time
import urllib2

delay = 0.01
fire1 = gpiozero.LED(2)
fire2 = gpiozero.LED(3)
up = gpiozero.LED(4)
down = gpiozero.LED(17)
fire1.on()
fire2.on()
up.on()

while True:
    message = urllib2.urlopen("google.com")
    file = message.read()
    for d in file:
        for x in range(1, ord(d) + 1):
            fire1.off()
            time.sleep(delay)
            fire1.on()
            time.sleep(delay)
            fire2.off()
            time.sleep(delay)
            fire2.on()
        time.sleep(delay)
        up.off()
        time.sleep(delay)
        up.on()
        time.sleep(delay)
    time.sleep(3)
    down.off()
    time.sleep(delay)
    down.on()
    time.sleep(delay)
