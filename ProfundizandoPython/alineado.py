titulo = 'sitio web'

print(titulo.center(len(titulo)+10,'+'))#centra texto
print(titulo.ljust(50,'*'))
print(titulo.ljust(len(titulo)+50,'*'))#alinea a la izquierda
print(titulo.rjust(len(titulo)+10,'/'))#alinea a la derecha

#remplazar un contenido en un string
print(titulo.replace(' ','-'))

#eliminiar caracteres al inicio y al final de un str strip

titulo= '*** cadena original  ***'
print('cadena original: ',titulo,len(titulo))
titulo =titulo.strip()
print('cadena modificada: ',titulo,len(titulo))

titulo= ' ***cadena original*** '.strip('*')
print('cadena modificada: ',titulo)

titulo = '***cadena original***'.lstrip('*')
print('cadena modificada: ', titulo)

titulo = '***cadena original***'.rstrip('*')
print('cadena modificada: ', titulo)

titulo= ' ***cadena original*** '.strip().strip('*').strip()
print('cadena modificada: ',titulo)