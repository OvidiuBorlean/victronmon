import serial

with  serial.Serial('/dev/ttyUSB0', 19200, timeout=1) as myserial:
    while True:

    	line = myserial.readline()
	#str(line)
	x = line.splitlines()
	for item in x:
		#print (item)
		res = list(filter(lambda x: 'H19' in x, x)) 
		if res:
			newres = str(res[0])
			print newres[4:9]
