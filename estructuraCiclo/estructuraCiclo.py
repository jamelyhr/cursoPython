# from operator import truediv


# menssaje=input('ingrese un mensaje')
##mostrar por consola cuantas vocales 
##tiene el mensaje
# for letra in mensaje:
#     if letra=='a','b','c','d','a':
#         print('la letra a')
#         print(letras)
 ##escribir un programa que muestre el eco de todo lo que el ususrio introduzca hasta que el ususrio escriba
 # "salir" que terminara.

# condicion=True
# while condicion==True:
#     letra=input('ingresa cualquier letra o numero')
#     if letra=='salir':
#         print('salio el programa')
#         condicion=False
#     else:
#        print('sigue intentando')
# palabra=''
# while palabra!='salir';
#    palabra=input('escriba allgo:')
#    print(palabra)
# from asyncio.windows_events import INFINITE


# contador=INFINITE
# for num in range(0,contador):
#     palabra=input('ingrese algo: ')
#     if palabra=='salir':
#       break
#las vocales
# oracion=input('ingrese su oracion')
# vocales=['a','e','i','o','u']
# contadorVocales=0
# for letras in oracion:
#     if letras in vocales:
#         contadorVocales+=1
# print('la cantidad de vocaales es:',
# contadorVocales)
# sentence=input('ingrse una oracion:')
# handlerVocales=0
# for words in sentence:
#     match words:
#         case 'a':
#             handlerVocales+=1
#         case 'e':
#             handlerVocales+=1
#         case 'i':
#             handlerVocales+=1
#         case 'o':
#             handlerVocales+=1
#         case 'u':
#             handlerVocales+=1
# print('laa cantidad de vocales es: ',handlerVocales)

#uso de funcion
#print(suma(4,6))

# from imp import load_source


# numero='10'##'10'
# int es el numero de la funcon () y dentro de parentesis van los
# parametros





##operador matematico(4,5,'ssuma')
##por consola la suma de 4+5
# def mensaje(nombre,apellido,accion):
#     if accion == 'saludo':
#         mensaje='hola',nombre,apellido,'como  estas'
#     elif accion=='despedida':
#         mensaje='adios',nombre,apellido
#     return mensaje
# respuesta=mensaje('jamely','alvares','saludo')
# print(respuesta)
# from contextlib import ContextDecorator
# sentence=input('enter sentence:')
# Vocales=['a','e','i','o','u']
# def coutVocal(oracion,Vocal):
#     contador=0
#     for word in oracion:
#         if word in Vocal:
#             contador+=1
#     return contador
# print(coutVocal(sentence,Vocales))

#Calculadora 
# import time


# time.sleep(1)

# time.sleep(0)

# numero1 = int(input("primer número: "))
# numero2 = int(input(f"segundo número: "))
# print(f"De acuerdo, has escogido el {numero1} y el {numero2}")
# time.sleep(1)

# print(f" (Escribe el numero)\n 1 Sumar\n 2 Restar\n 3 Multiplicar\n 4 Dividir\n 5 salir")
# simbolo = input("digite opcion:"4
# )

# if simbolo == '1' or simbolo == "1":
#     print(f"{numero1} + {numero2} =",(numero1+numero2))
# elif simbolo == '2' or simbolo == "2":
#     print(f"{numero1} - {numero2} =",(numero1-numero2))
# elif simbolo == '3' or simbolo == "3":
#     print(f"{numero1} * {numero2} =",(numero1*numero2))
# elif simbolo == '4' or simbolo == "4":
#     print(f"{numero1} / {numero2} =",(numero1/numero2))
# elif simbolo == '5' or simbolo == "5":
#     print(f"fin")
    
# else:
#     print(f"No has escrito ninguna letra correcta\nS|s para sumar R|r para restar M|m para multiplicar o D|d para dividir")

##operador matematico(4,4,'suma' )
## por consola la suma de 4+5
#1.UTILIZAR LA PALABRA RESERVADA de f
#2.asignamos un nombre a la funcion--descriptivo
#3.simpre tiene que reccibir parametros
    #()--no recibe parametros
    #(nombre)--que la funsion esta recibiendoun parametro
    #(edad,nombre)
#4.simpre la funsion tine que retomar untimmo de dato
# from sqlite3 import DateFromTiks


# def saludo(nombre):
#     respuesta=f'hola como estas{nombre}'
#     return respuesta

#     #como uso
#     arrayamigos=['ronlad','claudio','adriel','diego']
#     for amigo in range(0,len(arrayamigos)):
#         print(saludo(arrayamigos[amigos]))


#FUNSIONES CARPETA
def operaciones(num1,num2,operador):
  if operador=='suma':
     total=num1+num2
  if operador=='resta':
     total=num1-num2
  if operador=='por':
     total=num1*num2
  if operador=='entre':
     total=num1/num2
  return total  

#llamando la funsion
respuesta=operaciones(10,5,'suma')
respuesta2=operaciones(200,44,'resta')
print(f'la suma es {respuesta}')
print(f'la resta es {respuesta}')

  
        