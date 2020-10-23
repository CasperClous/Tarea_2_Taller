def desviar_confirmacion(packet):
	try:
		if packet['FTP']['response.arg'] == "File successfully transferred":
			print("La direccion actual es: ")
			print(packet['IP']['addr'])
			packet['IP']['addr'] = "172.17.0.6"
			print("Nueva direccion en el segmento IP")
			print(packet['IP']['addr'])
			return packet
	except:
		return None
