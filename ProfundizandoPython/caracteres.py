print('hola\u0020Mundo')
print('Notacion simple: ', '\u0041')
print('Notacion extendida ', '\U00000041')
print('notacion hexadecimal', '\x41')
print('corazon ', '\u2665')
print('cara sonriza: ', '\U0001f600')
print('serpiente ', '\U0001f40D')

#caracteres ascii

caracter = chr(65)
print(' A mayuscula:', caracter)
caracter = chr(64)
print(' Simbolo @ :', caracter)
caracter = chr(97)
print('a minuscula:', caracter)

#caracteres en bytes
caracter_en_byte = b'holamundo'
print(caracter_en_byte)
mensaje = b'Universidad'
print(mensaje[0])
print(chr(mensaje[0]))

string = 'programacion con Python'
print('string original:' ,string)
bytes = string.encode('UTF-8')
print('byte codificado: ',bytes)

string2 = bytes.decode('UTF-8')
print('string decoficado: ',string2)