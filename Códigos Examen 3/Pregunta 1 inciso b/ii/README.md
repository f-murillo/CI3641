Pregunta 1 - Inciso b - ii - Franco Murillo 1610782

# Implementación de Conjuntos de Personas

# Clases

__Persona__
  - Clase que implementa una persona, con un nombre y una edad
  - __init__: constructor. Inicializa el nombre y la edad
  - __str__: retorna un String con el nombre y la edad de la persona 

__ConjuntoPersonas__
  - Clase que implementa conjuntos de tipo Persona
  - __init__: constructor. Crea una lista vacía
  - __agregar_persona__: agrega una persona a la lista de personas
  - __cantidad_personas__: retorna la longitud de la lista de personas
  - __mayores_de_edad__: retorna una lista (creada por comprensión) de las personas cuyas edades sean mayores o iguales a 18
  - __nombre_mas_comun__: retorna el nombre que más se repite en la lista de personas
    - Crea una lista con los nombres de las personas en la lista
    - Si la lista está vacía, no hay ningún nombre. Retorna None
    - Crea una instancia de Counter con la lista de nombres
    - Obtiene y retorna el nombre más común con most_common(1), el cual retorna una lista de tuplas con los nombres más comunes y sus ocurrencias
    - Con most_common(1)[0] se obtiene el primer elemento de dicha lista de tuplas; y con most_common(1)[0][0] se obtiene el nombre del primer elemento de la lista de tuplas 
