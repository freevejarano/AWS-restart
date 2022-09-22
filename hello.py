"""Problema 1
Se necesita un programa que le permita a un usuario dada su edad actual conocer su edad en el
año 2070. Diseñe un algoritmo que satisfaga este requerimiento e impleméntelo en Python.
Input: Edad (entero >0), Año actual (entero >0).
Output: Edad en el 2070 (entero >0), Salida en pantalla con mensaje informativo."""



age = int(input("Ingrese su edad: "))

year = int(input("Ingrese el año actual: "))

futureYear = (2070-year) + age

print(f"\nEl año actual es {year} y su edad es {age} años")

print(f"\nSu edad en el 2070 será {futureYear} años")