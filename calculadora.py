"""
Este archivo contiene una calculadora simple en Python.
Permite sumar, restar, multiplicar y dividir dos números.
"""

def sumar(a, b):
    return a + b

def restar(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "Error: División por cero"
    return a / b

print("Calculadora Simple")
print("1. Sumar")
print("2. Restar")
print("3. Multiplicar")
print("4. Dividir")

try:
    opcion = int(input("Elige una opción (1-4): "))

    num1 = float(input("Introduce el primer número: "))
    num2 = float(input("Introduce el segundo número: "))

    if opcion == 1:
        print("1. Resultado de la suma:", sumar(num1, num2))
    elif opcion == 2:
        print("2. Resultado de la resta:", restar(num1, num2))
    elif opcion == 3:
        print("3. Resultado de la multiplicación:", multiplicar(num1, num2))
    elif opcion == 4:
        print("4. Resultado de la división:", dividir(num1, num2))
    else:
        print("Opción no válida")
except ValueError:
    print("Por favor, ingresa valores numéricos válidos.")