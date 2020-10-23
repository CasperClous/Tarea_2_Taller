def cambiar_dir(packet):
	try:
		if packet['FTP']['response.arg'] == '\"/home/casper\" is your current location':
			print ("Anterior")
			print (packet['FTP']['response.arg'])
			packet['FTP']['response.arg'] = '\"/root\" is your current location'
			print ("Nuevo")
			print (packet['FTP']['response.arg'])
	except:
    		return packet

