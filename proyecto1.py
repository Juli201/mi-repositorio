print("bienvenid@ a jplay la mejor casa de apuestas mundialista")
nombre=str(input("por favor digite su nombre: "))
edad1=int(input("digite su edad: "))
if(edad1>=18):
    print("crea tu contraseña ")
    contra=str(input(""))
    while True:
        contraseña=str(input("digite su contraseña creada: "))
        if(contraseña==contra):
            print("Felicidades ahora sigue con el siguiente paso ")
            break
        else:
            print("contraseña incorrecta intente nuevamente")
else:
    print("no puede jugar")
print("para empezar a apostar  debes hacer un deposito de minimo 10000")
while True:
    deposito=int(input("digite el valor que desea depositar"))
    if(deposito>=10000):
        print(" Muy bien ya puedes empezar a apostar")
        break
    else:
      print("deposito invalido, deposite un valor valido")
croacia=2.10
marruecos=6.65
España= 1.54
costarica=3.67
Alemania=1.76
Japon=3.8
Belgica=1.43
Canada= 2.45
while True:
 print("los partidos de hoy son los siguientes elije a cual quieres apostar")
 print("1. croacia vs marruecos")
 print("2. españa  vs costa rica")
 print("3.  alemania vs japon")
 print("4. belgica vs canada ")
 opc=input("ingrese una opcion: ")
 if opc=="1":
  print("1. croacia 2.10 ")
  print("2. marruecos. 6.65 ")
  opc=input("digite el equipo al que qquiere apostar: ")
 elif opc=="2":
  print("1. España. 1.54")
  print("2. costa rica. 3.67")
  opc=input("digite el equipo al que qquiere apostar: ")
 elif opc=="3":
  print("1. Alemania. 1.76")
  print("2. japon. 3.8")
  opc=input("digite el equipo al que qquiere apostar: ")
 elif opc== "4":
  print("1. Belgica 1.43")
  print("2. canada 2.45")
  opc=input("digite el equipo al que qquiere apostar: ")
 break
