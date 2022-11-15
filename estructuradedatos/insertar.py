##estructura de datos
##listas
##metodos para estructura de dato tipo lista en python
# list=['deyanira']#lista vacia
# list.append('diego')
# list.insert(0,'daniel')
# list.insert(2,'hola')
# list.insert(len(list),'jose')
# print(list)
##ejercio uno
# list=[]
# for i in range(21):
#   if i%2==0:
#     list.append(i)
# print(list)

# unir listas
vocalesuno=['a','e']
vocalesdos=['i','o','u']

vocalesuno.extend(vocalesdos)

vocalesuno[3]='OO'
vocalesuno.remove('u')
print(vocalesuno)