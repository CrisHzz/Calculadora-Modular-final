import sys
import pyfiglet
from pyfiglet import figlet_format
import math
from sympy.ntheory import primefactors
from sympy.ntheory.modular import crt


def menu(usuario):
    print(figlet_format("Calculadora Modular", font="slant"))
    print("Bienvenido a esta calculadora modular, aqui podrea realizar las operaciones basicas ")
    print("")
    print(1, "Suma modular")
    print("")
    print(2, "Multiplicacion modular")
    print("")
    print(3, "Inverso modular")
    print("")
    print(4, "Division modular")
    print("")
    print(5, "Potencia modular")
    print("")
    print(6, "Raiz cuadrada modular")
    print("")
    print(7, "Cuadrados perfectos")
    print("")
    print(8, "Salir")

    print("")
    print("RECUERDE EL 0 NUNCA PUEDE SER USADO COMO MODULO")
    print("")
    print("")



    opcion = int(input("Por favor ingrese la opcion deseada siga las condiciones indicadas para dicha operacion: "))

    if opcion == 1:
        usuario.numeros_del_Usuario()
        
        resultado_suma = suma_modular(usuario.A, usuario.B, usuario.C)
        print(f"El resultado de la suma modular es: {resultado_suma}")
    elif opcion == 2:
        usuario.numeros_del_Usuario()
        resultado_producto = multiplicacion_modular(usuario.A, usuario.B, usuario.C)
        print(f"El resultado de la multiplicacion modular es: {resultado_producto}")
    elif opcion == 3:
        usuario.numeros_del_Usuario()
        resultado_producto=inverso_modular(usuario.A,usuario.C)
        print(f"El resultado del inverso modular es: {resultado_producto}")
    elif opcion == 4:
        usuario.numeros_del_Usuario()
        resultado_division = division_modular(usuario.A, usuario.B, usuario.C)
        print(f"El resultado de la division modular es: {resultado_division}")

    elif opcion == 5:
        print("Recuerde que en este caso A sera la base, B sera el exponente y C sera el modulo")
        usuario.numeros_del_Usuario()
        resultado_potenciacion=potenciacion_modular(usuario.A,usuario.B,usuario.C)
        print(f"El resultado de la potenciacion modular es: {resultado_potenciacion}")
        

    elif opcion == 6:
        print("Caso 1")
        print("")
        print("Recuerde que en este caso A sera el radicando y C sera el modulo")
        usuario.numeros_del_Usuario()
        resultado_raiz=raices_cuadradas_modulares(usuario.A,usuario.C)
        print("")
        print("Caso 2")
        print("")
        print("Recuerde que en este caso B sera el radicando y C sera el modulo")
        resultado_raiz2=raices_cuadradas_modulares2(usuario.B,usuario.C)

    elif opcion == 8:
        print("Gracias por usar esta calculadora modular")
        sys.exit()

    else:
        print("Por favor ingrese una opcion valida")
        menu(usuario)

    while True:
        reiniciar = input("¿Desea seguir operando ? (S/N): ")
        if reiniciar.lower() == "s":
            menu(usuario)
        elif reiniciar.lower() == "n":
            print("Gracias por usar esta calculadora modular")
            sys.exit()
        else:
            print("Por favor ingrese una opcion valida")
            continue


    

        
class Usuario:
    def __init__(self):
        self.A = None
        self.B = None
        self.C = None
        self.intentos = 0

    def numeros_del_Usuario(self):
        while True:
            try:
                self.A=int(input("Ingrese el numero A entero positivo "))
                self.B=int(input("Ingrese el numero B entero positivo "))
                self.C=int(input("Ingrese el numero C entero positivo Este sera su modulo "))

                if self.C == 0:
                    print("El valor de C no puede ser cero. Por favor ingrese un número entero distinto de cero.")
                    continue

                if self.A < 0 or self.B < 0 or self.C < 0:
                    print("Por favor ingrese un numero entero positivo")
                    continue

                break
            except ValueError:
                print("Por favor ingrese un número entero para A, B y C.")

def suma_modular(A,B,C):
    return (A + B) % C


def multiplicacion_modular(A, B, C):
    resultado = (A * B) % C
    return resultado


def inverso_modular(A, C):
    def egcd(a, b):
        if a == 0:
            return (b, 0, 1)
        else:
            g, y, x = egcd(b % a, a)
            return (g, x - (b // a) * y, y)

    g, x, y = egcd(A, C)
    if g != 1:
        return "No hay inverso modular en la operacion"
    else:
        return x % C

def division_modular(A, B, C):
    if A < C:
        A = A % C
    if B < C:
        B = B % C
    inverso = inverso_modular(B, C)
    if isinstance(inverso, int):
        division = (A * inverso) % C
        return division
    
def potenciacion_modular(A, B, C):
    resultado = 1
    A = A % C
    while B > 0:
        if B % 2 == 1:
            resultado = (resultado * A) % C
        B = B // 2
        A = (A * A) % C
    return resultado

def raices_cuadradas_modulares(A, C):
    raices = []
    numero = A % C
    for r in range(C):
        if (r * r) % C == numero:
            raices.append(r)
    if raices:
        print(f"Las raíces cuadradas modulares de {A} módulo {C} son: {', '.join(map(str, raices))}")
    else:
        print(f"No hay raíces cuadradas modulares de {A} módulo {C}")
    return raices



def raices_cuadradas_modulares2(B, C):
    numero = B % C
    raices = []
    for r in range(C):
        if (r * r) % C == numero:
            raices.append(r)
    if raices:
        print(f"Las raíces cuadradas modulares de {B} módulo {C} son: {', '.join(map(str, raices))}")
    else:
        print(f"No hay raíces cuadradas modulares de {B} módulo {C}")
    return raices






usuario = Usuario()
menu(usuario)