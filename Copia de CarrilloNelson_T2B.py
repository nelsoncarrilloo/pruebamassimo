print('                          UNIVERSIDAD METROPOLITANA    ')
print('                          ALGORITMOS Y PROGRAMACION    ')                                                #Encabezado institucional.
print('                             PROF. KEYLA RIVAS         ')
print('                              NELSON CARRILLO          \n')                                              #El \n separa con una línea de lo que continúa debajo.

nom = input('Hola, por favor, ingrese su nombre: ')
ap = input('Por favor, ingrese su apellido: ')
ci = input('Por favor, ingrese su numero de cedula (NUMERO, sin puntos): \n')                                   #Datos de entrada.
aux2 = 0                                                                                                        #Variables auxiliares.
aux = 0

if (nom.isalpha()) and (ap.isalpha()) and (ci.isnumeric()):                                                     #Massimo nos enseñó la validación de datos sin castear su ingreso a través de métodos.
    ci = int(ci)                                                                                                
    print('Se le agradece, escribir las cantidades en numeros y separar los decimales con un . (punto).')       #Una vez verificado que sea numérico y entero el número de cédula, se le asigan el tipo de dato integer, era antes str por defecto.
    n1 = float(input('Por favor, ingrese nota obtenida en parcial 1 (Numero entero o decimal del 1-20): '))     #No me quedó de otra que castear todas las variables correspondientes a notas del usuario.
    n2 = float(input('Por favor, ingrese nota obtenida en parcial 2 (Numero entero o decimal del 1-20): '))
    n3 = float(input('Por favor, ingrese nota obtenida de ev. continua (Numero entero o decimal del 1-20): '))  #Validé en dos ifs inadados ya que así no tengo que hacer una condición larguísima de puros and..     
   
    if (ci>0) and (1<=n1<=20) and (1<=n2<=20) and (1<=n3<=20):                                                  #Validación de todos los valores de las notas como datos de entrada.
        
        n1pts = ((n1*4)/20)
        n2pts = ((n2*4)/20)                                                                                     #Ponderación de puntos de acuerdo al porcentaje de cada evaluación.
        n3pts = ((n3*6)/20)
        nteor = n1pts+n2pts+n3pts                                                                               #Suma total de puntos ponderados obtenidos.
        
        if nteor >= 7:                                                                                          #La variable aux es para cuando ya se puede sumar la parte práctica.
            aux=1                                                                                               #En este caso, es cuando ya se sumaron de una los 7 puntos necesarios o más. La variable de los ganadores.
        elif (nteor >= 6) and  (nteor < 7):                                                                     #Excepeción para los que pueden recuperar para alcanzar 7 o más puntos.
            nrec=float(input('Por favor, ingrese nota obtenida en recuperacion (Numero entero o decimal del 1-20): '))
            if (1<= nrec <= 20):                                                                                #Validación del dato de la nota de recuperación.
                nrecpts=(nrec/20)                                                                               #Se divide de una entre 20 directamente ya que vale sólo el 5% de la nota.
                nteor+=nrecpts                                                                                  #Se le suman los puntos ponderados de la recuperación a los teóricos.
                if nteor >= 7:                                                                                  #Sí pasa la teórica con recuperación.
                    aux=1                                                                                       #Es elegible para sumarle su parte práctica, toma valor la variable auxiliar que indica que se le sumará lo práctico.
                else:                                                                                           #Tiene menos de 7 aún sumándole la recuperación, es decir raspó.
                    aux2=1                                                                                      #La variable aux2 es cuando no se le puede sumar lo práctico, cuando está reprobado.
            else: 
                print(nom.capitalize(),', dato invalido, vuelve a ingresar, por favor.')                        #Massimo nos enseñó a printear en mayúscula la primera letra de un string con el método .capitalize().
        else:
            aux2=1                                                                                              #No habría tenido ni más de 7 puntos ni en el rango para recuperar, por lo que de una se sabe que no cumple con lo mínimo teórico.
        if aux2==1:                                                                                             #Todos aquellos que no se le sumará su parte práctica ponderada.
            print('Estudiante: ',nom.capitalize(),ap.capitalize(),'.')
            print('Numero de Cedula de Identidad: ',ci,'.')
            print('Nota definitiva: ',nteor,'puntos.')
            print('No es suficiente para poder sumar las ponderaciones de la parte practica.')                  #Se le indica lo mal que lo hizo.
            print('Lo lamentamos, ha reprobado Algoritmos y Programacion.')  
        if aux == 1:                                                                                            #Los elegibles para sumarle su parte práctica, OJO estos no han aprobado la materia todavía.
            nq1 = float(input('Ingrese nota de quiz 1 (Numero entero o decimal del 1-20): '))                   #Como dije, tuve que castear los inputs de las notas, dependo de la voluntad del usuario a leer mis enunciados de ingreso.
            nq2 = float(input('Ingrese nota de quiz 2 (Numero entero o decimal del 1-20): '))
            npr = float(input('Ingrese nota del proyecto (Numero entero o decimal del 1-20): '))
            if (1<= nq1 <= 20) and (1<= nq2 <= 20) and (1<= npr <= 20):                                         #Validación de datos de parte práctica.
                nq1pts= (nq1/20)
                nq2pts= (nq2/20)                                                                                #Ponderación de puntos de acuerdo al porcentaje de cada práctica.
                nprpts= ((npr*4)/20)
                ndef= (nteor+nq1pts+nq2pts+nprpts)                                                              #Nota definitiva de la materia, con los puntos teóricos y los prácticos obtenidos y ya validados.
                if ndef<10:                                                                                     #Es posible que aún así reprueben, considerando como mínimo 10 puntos, puede ser también 9.5 pts.
                    print('Estudiante: ',nom.capitalize(),ap.capitalize(),'.')
                    print('Numero de Cedula de Identidad: ',ci,'.')
                    print('Nota definitiva: ',ndef,'puntos.')
                    print('Fue sumada la parte practica, aun asi,')
                    print('lo lamentamos, ha reprobado Algoritmos y Programacion.')
                elif ndef >=18:                                                                                 #No solo los de 18 merecen ser felicitados, los que sacaron más también, la excelencia se reconoce.
                    print('Estudiante: ',nom.capitalize(),ap.capitalize(),'.')
                    print('Numero de Cedula de Identidad: ',ci,'.')
                    print('Nota definitiva: ',ndef,'puntos. FELICITACIONES.')                                   #Mensaje de felicitaciones.
                    print('Ha aprobado de manera sobresaliente Algoritmos y Programacion.')
                else:                                                                                           #Queda restante aquellos que tienen 10 o más de 10 pero menos de 18 puntos definitivos, por lo que cumplieron, más no sobresalieron.
                    print('Estudiante: ',nom.capitalize(),ap.capitalize(),'.')
                    print('Numero de Cedula de Identidad: ',ci,'.')
                    print('Nota definitiva: ',ndef,'puntos.')
                    print('Ha aprobado Algoritmos y Programacion.')
            else:
                print(nom.capitalize(),', al menos una nota es invalida, revise y vuelva a entrar, por favor.') #Mensaje validación de datos de evaluación práctica erróneos.
    else:
        print(nom.capitalize(),', al menos uno de tus datos es invalido, revise y vuelva a entrar, por favor.') #Mensaje validación de datos de entrada erróneos.
else:
    print('Datos de identificacion invalidos, coloque un nombre y un apellido correcto y el numero de cedula sin puntos.')
    print('Vuelva a intentar, por favor.')




'''Se combinó el castear y no castear variables. En el caso de las notas, ya se hacía necesario castearlas, al 
admitir valores decimales que hasta donde hemos llegado no sabemos evaluar o verificar. Se trató de trabajar al máximo con condicionales,
a pesar de que Massimo pensaba que estaba loco, pude hacer un eficiente, digamos, sistema de verificación de datos, solo que, en vez de 
pedirle el dato hasta que lo coloque bien (usando while o for) el usuario, lo mando a un else de ser incorrecto, y se imprime el mensaje de validación
y el usuario debe comenzar de 0, sin pasar a los siguientes inputs u operaciones que reflejen datos posteriores de salida.

También, la entrada de datos está organizada de modo que, se ingresen primero las notas de las evaluaciones teóricas y, 
para efectos del usuario, si no se le piden las prácticas, es porque de una vez se imprime que ha reprobado, que no ha podido sumar su parte
práctica. Así, como para los que pueden sumar, sí podrán seguir ingresando sus notas hasta la última del proyecto y observar en un 
mensaje si aprobaron o no la materia (Ya que con 7 ptos no aprueban aún la materia).'''