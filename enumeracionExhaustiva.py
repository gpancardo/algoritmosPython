#ENUMERACIÓN EXHAUSTIVA
#Es un algoritmo básico y uno de los primeros a considerar cuando se resuelve un problema

#Vamos a determinar si un número tiene una raís cuadrada exacta a partir de enumeración exhaustiva

#El usuario establece el número al que vamos a calcular la raíz
objetivo=int(input("Escoge un entero: "))
#Va a iniciar un conteo desde 0
respuesta=0

#Le decimos a la computadora que agregue uno a la variable del conteo mientras el cuadrado de esta
#no llegue al objetivo
while respuesta**2 < objetivo:
    respuesta += 1
#Si respuesta al cuadrado es igual a objetivo, esa es la raíz
if respuesta**2==objetivo:
    print("La raíz cuadrada de ",objetivo," es ",respuesta)
#En caso contrario, no tiene raíz cuadrada
else:
    print(objetivo, " no tiene raíz cuadrada")