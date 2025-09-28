# Practicando lógica booleana en Python aprendiendo a usar "and", "or" y "not"

# Declaracion de valores o inicialización de Valores para probar diferentes combinaciones
edad = 16
tiene_permiso = True
es_finde = False

# TODO 1: Usa una expresión booleana con "and"
# Por ejemplo: ¿Puede salir hoy solo si tiene 18 años o más Y si tiene permiso?
puede_salir=(edad>=18 and tiene_permiso)


print("¿Puede salir solo?:", puede_salir)

# TODO 2: Usa una expresión booleana con "or" para permitir salir si es fin de semana o tiene permiso

puede_salir_2=es_finde or tiene_permiso

print("¿Puede salir por alguna razón?:", puede_salir_2)

# TODO 3: Usa una expresión booleana con "not" para negar una condición
# Por ejemplo: De ninguna manera tiene permiso
no_tiene_permiso=not tiene_permiso

print("¿No tiene permiso?:", no_tiene_permiso)

# TODO 5: Escribe tu propia condición con and, or o not e imprimelo a la pantalla.
# Ejemplo: ¿Puede conducir si tiene 18 o más y tiene permiso? u cualquier otra idea. 
# Puede ir a un concierto con sus amigos?
# Puede ir si: Tiene 15 anos y No es fin de semana.
puede_ir_a_concierto=(edad>=15 and not es_finde)

print("Puede ir a un concierto con sus amigos?:", puede_ir_a_concierto)



