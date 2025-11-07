
"""""
---Semana 11: Diseño del Programa Final
Actividad 1: Crear un diagrama de flujo que muestre el flujo de datos y decisiones (condicionales y bucles).
Actividad 2: Escribir el pseudocódigo, detallando la lógica paso a paso.

Entregables:
Diagrama de flujo (formato visual claro).
Pseudocódigo entendible (con la lógica del programa).

---Semana 12: Codigo
Actividad: Comenzar a escribir el código Python basado en el pseudocódigo.

Aplicar:
Funciones (mínimo 2 con retorno de valor).
Condicionales (if, else), bucles (for, while).
Listas, diccionarios o conjuntos (mínimo 1 estructura de datos).
Clases y objetos.
Expresiones regulares.
Manejo de errores con try-except.

Pruebas Iniciales:
Al menos 3 casos de prueba (válidos e inválidos).
Documentar entradas, salidas esperadas y resultados reales.

Entregables:
Código parcial funcional.
Lista con pruebas realizadas.

---Semana 13: Finalización y Documentación
Actividad: Completar el programa y asegurar que todo funcione correctamente.

Comentar el código adecuadamente.
Hacer pruebas finales con valores extremos y casos límite.
Escribir el archivo README.md con:
Descripción del programa.
Instrucciones de uso.
Documentación técnica básica.

Entregables:
Código final completo y funcional.
Archivo README.md.
Lista final de pruebas con entradas/salidas esperadas.

-- Semana 14: Presentacion de su programa (continuacion)
La presentacion debe ser dentro de 5-10 minutos
Asegurate de mostrar capturas de pantalla del código o diagramas.
Y de responder las siguientes preguntas:

1. Concepción e Inspiración: Establecer el contexto y la justificación del proyecto.
- ¿Cuál fue la chispa inicial o el problema central que te llevó a crear este juego, programa o solución?
- ¿Cómo se originó la idea? 

2. Público Objetivo y Diseño: Demostrar un entendimiento del usuario y del mercado/necesidad.
- ¿A quién está dirigido este proyecto? Definición del público/usuario objetivo.
- ¿Cómo influyó el público objetivo en las decisiones de diseño y funcionalidad?
        
3. Proceso y Desarrollo: Informar sobre la robustez del proyecto y la capacidad de resolución de problemas.
- ¿Dónde y cómo se integraron los requisitos o pasos obligatorios del curso/proyecto
(por ejemplo, el uso de Git, ciertas estructuras de datos, etc.)?
- Muestra la estructura del proyecto y las decisiones técnicas clave.
- Probar el cumplimiento de las especificaciones y la aplicación de los conocimientos.

4. Calidad y Lecciones Aprendidas
- ¿Qué pruebas se ejecutaron (unitarias, integración, aceptación, etc.) y
cuáles fueron los resultados iniciales?
- Presenta una lista de los errores (bugs) críticos que encontraste y explica brevemente
la solución implementada para cada uno.
   
5. Feedback y Proyección a Futuro
- ¿Qué sugerencias, dudas o retroalimentación recibiste de las personas que probaron tu código o producto por primera vez?
- Si tuvieras más tiempo, ¿cuáles serían las mejoras o nuevas funcionalidades prioritarias que implementarías?

"""
"""
Seudocodigo

  // 1. Inicializar estructuras
  estilos <- diccionario con claves:
      "contemporaneo" -> 0
      "moderno"       -> 0
      "industrial"    -> 0
      "shabby"        -> 0

  preguntas <- lista vacía
  // Cada elemento de 'preguntas' será un registro con:
  //   texto, opciones (lista de 4 strings), respuesta (lista de 4 estilos)

  Agregar a preguntas el registro para la Pregunta 1:
    texto = "¿Qué tipo de colores prefieres...?"
    opciones = ["a) ...", "b) ...", "c) ...", "d) ..."]
    respuesta = ["contemporaneo", "moderno", "industrial", "shabby"]

  Repetir para todas las preguntas (2, 3, 4, ...)

  // 2. Recorrer preguntas (bucle)
  PARA cada pregunta p EN preguntas HACER
    Mostrar p.texto
    PARA cada opcion EN p.opciones HACER
      Mostrar opcion
    FIN PARA

    leer respuesta_usuario (convertir a minúsculas)

    SI respuesta_usuario está en ["a","b","c","d"] ENTONCES
      indice <- posición de respuesta_usuario en ["a","b","c","d"]
      estilo_elegido <- p.respuesta[indice]
      estilos[estilo_elegido] <- estilos[estilo_elegido] + 1
    SINO
      Mostrar "Respuesta inválida, se omitirá esta pregunta."
    FIN SI
  FIN PARA

  // 3. Calcular resultado
  mayor <- valor máximo en estilos (max(estilos.values()))
  lista_ganadores <- lista vacía

  PARA cada (estilo, puntos) EN estilos HACER
    SI puntos == mayor ENTONCES
      añadir estilo a lista_ganadores
    FIN SI
  FIN PARA

  // 4. Mostrar resultado (manejo de empates)
  SI longitud(lista_ganadores) == 1 ENTONCES
    estilo_final <- lista_ganadores[0]
    Mostrar "Tu estilo es: " + estilo_final
    Mostrar descripción correspondiente a estilo_final
  SINO
    // Hay empate entre dos o más estilos
    Mostrar "Hay un empate entre: " + lista_ganadores
    Mostrar "Puedes repetir el test o ver una descripción de cada estilo."
    (Opcional) pedir pregunta de desempate o mostrar los estilos empatados
  FIN SI

FIN


## De la charla recibida se pudo evidenciar que aun falta mucho por hacer en cuanto a reciclaje, hay que trabajar no solamente en el proceso, sino en como las personas puedan desde sus hogares aportar con soluciones. Me parecio muy valido lo que menciono que ya existen leyes que protegen a paises pobres de recibir basura
"""