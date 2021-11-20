ruta_archivo = ""
data_users=[]

def showRuta():
	global ruta_archivo
	print(ruta_archivo)

    
def setRuta(nueva_ruta):
	global ruta_archivo
	ruta_archivo = nueva_ruta


def appendUser(user):
	global data_users
	data_users.append(user)

	
def getUsers():
	global data_users
	return data_users
