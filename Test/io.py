import RPi.GPIO as GPIO



GPIO.setmode(GPIO.BCM)
GPIO.setup(4, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(25, GPIO.OUT, initial=GPIO.LOW)
print(GPIO.input(4))


def btn_callback(channel):
	print(GPIO.input(4))
	GPIO.output(25, GPIO.input(4))


GPIO.add_event_detect(4, GPIO.BOTH, callback=btn_callback)

try:
	while True:
		pass
except KeyboardInterrupt:
	GPIO.cleanup()
	print('Interupted: Exiting')
	