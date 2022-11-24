nombre = 'Oscar'
edad = 33
sueldo = 3000
mensaje_con_formato = 'Mi nombre es %s y tengo %d años '%(nombre,edad)
print(mensaje_con_formato)

persona = ('karla','Gomez',5000.00)
mensaje_con_formato = 'Hola %s %s. Tu sueldo es %.5f'%persona
print(mensaje_con_formato)

mensaje_con_formato = 'Nombre {} edad {} sueldo {:.2f}'.format(nombre, edad, sueldo)
print(mensaje_con_formato)

mensaje= 'Nombre {0} edad {1} sueldo {2:.2f}'.format(nombre, edad, sueldo)
print(mensaje)

mensaje = 'sueldo {2:.2f} edad {1} Nombre {0}  '.format(nombre, edad, sueldo)
print(mensaje)

mensaje = 'Nombre {n} edad {e} Sueldo {s:.2f} '.format(n=nombre,e=edad,s=sueldo)
print(mensaje)

diccionario = {'nombre':'ivan','edad':35,'sueldo':800.00}
mensaje = 'Nombre {dic[nombre]} Edad {dic[edad]} Sueldo {dic[sueldo]:.2f}'.format(dic=diccionario)
print(mensaje)