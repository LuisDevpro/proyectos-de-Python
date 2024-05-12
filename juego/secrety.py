import platform
import os
import time


jugador = 0
def limpiar_pantalla(): 
   
    if platform.system () == 'windows':
      os.system('cls')
    else:
      os.system('cls')
limpiar_pantalla()



def inicio ():
    print ("________________VAMOR A JUAGAR UN JUEGO ___________________")
    print ("DEBES DE ELEJIR UN NUMERO PARA QUE EL OTRO JUGADOR LO ADIVINE")
    secrety = int(input("INGRESE UN NUMERO DEL 1 AL 20...:"))
    limpiar_pantalla()
 




    if secrety <= 20 :
      print("_________________DEBES DE ADIVINAR UN NUERO DEL 1 AL 20_____________________________")
      print("------------------------------------------------------------------------------------")

      while secrety != jugador : 
       jugador =  int(input (".....ESCOGE UN NUMERO____:"))

      if jugador > secrety:
        print("....EL NUMERO ES MAYOR.....:")
        time.sleep(1)
        limpiar_pantalla()
      elif jugador < secrety :
        print("....EL NUMERO ES MENOR.....:")
        time.sleep(1)
        limpiar_pantalla()
      else :
        limpiar_pantalla()
        print("__________________FELICIDADES GANASTE EL JUEGO______________________ ")
        time.sleep(3)
        limpiar_pantalla()

    elif secrety > 20:
         print("ERROR EL NUMERO NO ES VALIDO ")
         time.sleep(2)
         limpiar_pantalla()
         print("______________________GAMER OVER__________________")
         time.sleep(3)
         limpiar_pantalla()
         return inicio()
  
  