# Crear un set de colores: Rojo, Blanco, Azul
# Agregar: Violeta, Dorado
# Eliminar: Celeste, Blanco, Dorado
# ¿Qué pasa si usamos discard para eliminar Celeste?

colores = {'Rojo', 'Blanco', 'Azul'}
print(colores)
print(type(colores))

colores.add('Violeta')
colores.add('Dorado')
print(colores)

colores.discard('Celeste')
colores.discard('Blanco')
colores.discard('Dorado')
print(colores)

colores.discard('Celeste') # No pasa nada si no está en el set
print(colores)
