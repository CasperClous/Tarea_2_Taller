def logout(packet):
	try:
		if packet['FTP']['response.code'] == "0x323537":
			print ("Paquete de directorio")
			print ("Se cambio por:")
			packet['FTP']['response.code'] = "0x323236"
			packet['FTP']['response.arg'] = "Logout"
			print (packet['FTP']['response.arg'])

			return packet
	except:
		return None
