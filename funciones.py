from colorama import Fore, Style
import os
import msvcrt
import random
import numpy

#Crear Arreglo
libros = numpy.empty([10,4],object)

#Funciones de Diseño
def printv(texto : str):
    print(f"{Fore.GREEN}{Style.BRIGHT}{texto}{Fore.RESET}{Style.RESET_ALL}")

def printr(texto : str):
    print(f"{Fore.RED}{Style.BRIGHT}{texto}{Fore.RESET}{Style.RESET_ALL}")

def limpiarpantalla():
    printv("<<Presione Una Tecla Para Continuar>>")
    msvcrt.getch()
    os.system('cls')

#Funciones de Arreglo

#Validar Código

#Guardar

#Búsqueda

#Certificado Criticas
#Certificado Detalle
