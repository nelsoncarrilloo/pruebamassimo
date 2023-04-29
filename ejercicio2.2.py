lista=[]
listaaux=[]
aux=0
miem=input('Por favor, ingrese numero o palabra: ')
for i in miem:
    lista.append(i)
    listaaux.append(i)
listaaux.reverse()
if listaaux==lista:
    print(miem.upper(),'es palindromo.')
else:
    print(miem.upper(),'no es palindromo.')