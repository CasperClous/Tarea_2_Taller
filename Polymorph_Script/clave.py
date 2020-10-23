def clave(packet):
	try:
		if packet['FTP']['request.command'] == 'PASS':
			print (packet['FTP']['request.arg'])
			packet['FTP']['request.arg'] = 'NotThisPassword'
			print('Se cambio la pass')
			return packet
	except:
		return None
