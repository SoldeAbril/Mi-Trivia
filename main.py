# Lo primero es mostrar en pantalla el texto de bienvenida para quien juegue tu trivia
print ("Bienvenido a mi trivia sobre computación")
print ("Pondremos a prueba tus conocimientos")

# Es importante dar instrucciones sobre cómo jugar:
print ("Responder las siguientes preguntas escribiendo la letra de la alternativa y presionando 'Entrer' para enviar tu respuesta:\n")

# OJO, el \n al final de la línea 6 es para dar un "salto de línea"

# Pregunta 1
print ("1) ¿Quién fue el creador de windows?")
print ("a) Linus Torvalds")
print ("b) Bill Gates")
print ("c) Mark Zuckerberg")
print ("d) Dennis Ritchie")

# Almacenamos la respuesta del usuario en la variable "respuesta_1"
respuesta_1 = input("\nTu respuesta: ")


# Selección de respuesta

if respuesta_1 == "b":
  print ("¡Correcto!")

else:
  print ("Intenta de nuevo")

