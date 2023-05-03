numero=12#Numero que se desea adivinar
control=0#variable de control de ciclo
intentos=1#Controlar de intentos
print("Bienvenido al juego adivina un numero")
while(control==0):
    print("Intento numero: ",intentos)
    print("Ingrese un numero")
    num = int(input())#Solicitamos numero para comparar
    if(num==numero):
        print("Numero Correcto")
        print("Utilizaste",intentos,"intentos")
        print("Juego finalizado")
        control=1
    elif(num > numero):
        print("El numero ingresado es Mayor, intente de nuevo")
        intentos+=1
    elif(num < numero):
        print("El numero ingresado es Menor, intente de nuevo")
        intentos+=1