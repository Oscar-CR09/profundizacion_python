# Profundisando en el tipo str
# concatenacion automatica en python 
#from mi_clase import Miclase
#help(Miclase)

#print(Miclase.__doc__)
#print(Miclase.__init__.__doc__)
#print(Miclase.mi_metodo.__doc__)
#print(Miclase.mi_metodo)
''' 
variable='adios'
mensaje = 'Hola' + ' ' + 'Mundo' + ' '+ variable
mensaje += 'Universidad' 'Python'
print(mensaje)

'''
#help(str)

#mensaje1 = 'hola mundo '
#mensaje2 = mensaje1.capitalize()
#print(f'mensaje1: {mensaje1}, id  {id(mensaje1)}')
#print(f'mensaje1: {mensaje2}, id {id(mensaje2)}')

#help(str.join)
tupla_str = ('hola', 'mundo', 'Universidad','curso python')
mensaje = ' '.join(tupla_str)
print(f'mensaje: {mensaje}')

lista_cursos = ['java','python','angular','sprint']
mensaje = ', '.join(lista_cursos)
print(f'mensaje: {mensaje}')

cadena = 'Holamundo'
mensaje = '.'.join(cadena)
print(f'mensaje: {mensaje}')

diccionario = {'nombre':'juan','apellido':'Perez', 'edad':'18'}
llaves = '-'.join(diccionario.keys())
valores = '-'.join(diccionario.values())
print(f'llaves: {llaves}, type: {type(llaves)}')
print(f'valores: {valores}, valores: {type(valores)}')

#help(str.split)
cusrsos = 'java python javascript Angular sprint Excel'
lista_cursos = cusrsos.split()
print(f'listas de cursos: {lista_cursos}')
print(type(lista_cursos))

cusrsos_separados_coma = 'java, python, javascript, excel'
lista_cursos = cusrsos_separados_coma.split()
print(f'listas de cursos: {lista_cursos}')
print(len(lista_cursos))

lista_cursos = cusrsos_separados_coma.split(', ',2)
print(f'listas de cursos: {lista_cursos}')
print(len(lista_cursos))
