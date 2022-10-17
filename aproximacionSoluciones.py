#Vamos a resolver el mismo problema que en el ejercicio anterior, pero
#en lugar de decir que no tiene raíz si no encontramos el número entero
#vamos a proponer una aproximación con decimales, aunque sea menos precisa


#Pedimos al usuario el número objetivo
objetivo=int(input("Escoge un número: "))

#Establecemos las variables epsilon y paso para que nos ayuden en el
#calculo
epsilon=0.01
paso=epsilon**2

#Iniciamos el contador en ceros
respuesta=0.0

#Mientras el valor absoluto de la respuesta menos la variable paso y el contador siga siendo menor a
#la variable objetivo aumente el contador 
while abs(respuesta**2-objetivo)>=epsilon and respuesta <=objetivo:
    respuesta+=paso
#Si la resta (aproximación) es igual o menor a epsilon, no se pudo encontrar una raíz
if abs(respuesta**2-objetivo)>=epsilon:
    print("No se encontró la raíz cuadrada de "+objetivo)
#Si es mayor a epsilon, tenemos una raíz
else:
    print("La raíz cuadrada de "+str(objetivo)+" es "+str(respuesta))