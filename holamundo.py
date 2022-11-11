print("hola mundo")
numero1=int(input("digite numero 1:"))
numero2=int(input("digite numero 2:"))
suma=numero1+numero2
print("suma:",suma)
print("suma:" +str(suma))
print(f"suma:{suma}")
a=2
b=8
print(a<b)
a=True 
b=False
print(not(a))
print(a and b)
print(a or b)
edad1=int(input("digite la edad1"))
edad2=int(input("digite la edad2"))
edad3=int(input("digite la edad3"))
promedio=(edad1+edad2[edad3])/3
print("el promedio es: "+(str (promedio)))
temperatura=float(input("digite temperatura"))
deporte=""
if(temperatura>85) :
    deporte="natacion"
elif(temperatura>=60 and temperatura<=85):
    deporte="tenis"
elif(temperatura>=33 and temperatura<=70):
    deporte="golf"
elif(temperatura>10 and temperatura<=32):
    deporte="esqui"
elif(temperatura<10):
    deporte="marcha"
    print(deporte)
    for i  in range(1,101,1):
        print(i)
        while True:
            contraseña= int(input("pedimos la contraseña"))
            if(contraseña==123):
                break 
            palabra="viva colombia"
            print(palabra[-4])
            print(palabra+"Bogota")
            for i in range(97,1004):
                if (1%2==0):
                    suma=suma+1
                    print(suma)
                    mylista=[1, 3, "soy un texto", 3.1416, 5,1]
                    mylista2=[10,50]
                    mylista.append(1000)
print(mylista)
mylista.extend(mylista2)
print(mylista)
mylista.remove(1000)
print(mylista)
numero=mylista.index("soy un texto")
print(numero)
tam=len(mylista)
print(tam)
cantidad=mylista.count(1)
print(cantidad)
mylista.reverse()
print(mylista)
mylista2.sort()
print(mylista2)
mylista.pop(1)
print(mylista)
lista=[1,2,3,45,]
tupla=[1,2,3]
c=tupla.count 
print(c)
coleccion=[1,2,3,4]
print(coleccion)
colec=set(lista)
lista2=list(colec)
print(lista2)
lista3=[]
for i in range(1,1001):
    lista3.append(1)
    print(lista3)
    print(max(lista3))
    edad=int(input("digite su edad"))
    while True:
        try:
          edad=int(input("digite su edad"))  
          if (edad >0):
              break 
          else:
            print("solo se pueden numeros positivos")
        except ValueError:
            print("solo se puede ingresar umeros enteros")
casos=int(input())
c=0
suma=0
while True:
    if (casos==c):
        break
    c=c+1
    led=input()
    for numero  in led:
        if(numero==1):
            suma=+2
            print(str(suma+"leds"))
            suma=0
            estudiante={
                "nombre":"julian orjuela",
                "edad":30,
                "nota media":7.25,
                "repetidor": False
            }
            estudiante.update({"genero":"F"})
            estudiante[edad]=25
            edad= estudiante["edad"]
            print(estudiante)
            Ejemplo=[12, 23, 5, 12, 92, 5,12, 5, 29, 92, 64,23]
            diccionario={}
            for i in Ejemplo:
                a=Ejemplo.count(i)
                diccionario.update({i:a}) 
                print(diccionario)
                def mayor(a:int,b:int)-> int:
                    return max(a,b)
                    a=int(input("digite a"))
                    a=int(input("digite b"))
            resultado=mayor(a,b)
            print(resultado)
            



            









"""







"""