import accesoOracle
miLista=[ ]

query="select * from personaje p inner join descripcion_personaje dp on dp.ID_PERSONAJE = p.ID_PERSONAJE"

ao=accesoOracle.connectToOracle(query)


try:
	cursorData=ao.connect()

	for personaje in cursorData:

		miLista.append(personaje)

	print(miLista[6])
	#print(usuario)
except TypeError:
	print("No se pueden sacar resultados")