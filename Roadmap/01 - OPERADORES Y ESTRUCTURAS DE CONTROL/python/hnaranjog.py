"""
01 - OPERADORES Y ESTRUCTURAS DE CONTROL
EJERCICIO:
  - Crea ejemplos utilizando todos los tipos de operadores de tu lenguaje:
    Aritméticos, lógicos, de comparación, asignación, identidad, pertenencia, bits...
  - Utilizando las operaciones con operadores que tú quieras, crea ejemplos
    que representen todos los tipos de estructuras de control que existan
    en tu lenguaje:
    Condicionales, iterativas, excepciones...
  - Debes hacer print por consola del resultado de todos los ejemplos.
 
 DIFICULTAD EXTRA (opcional):
  Crea un programa que imprima por consola todos los números comprendidos
  entre 10 y 55 (incluidos), pares, y que no son ni el 16 ni múltiplos de 3.
"""

"""
# OPERADORES ARITMÉTICOS
+ Suma
- Resta
* Multiplicación
/ División
% Módulo
** Exponente
// Cociente
"""
x=5
y=3


print(f'Operadores aritméticos:\n')
print(f'Suma: {x} + {y} = {x + y}')
print(f'Resta: {x} + {y}  = {5 - 3}')
print(f'Multiplicación: {x} * {y} = {x * y}')
print(f'División: {x} / {y} = {x / y}')
print(f'Módulo: {x} % {y} = {x % y}')
print(f'Exponente: {x} ** {y} = {x ** y}')
print(f'Cociente: {x} // {y} = {x // y}')
print("\n")

"""
# OPERADORES DE ASIGNACIÓN
= Asignación
+= Suma y asignación
-= Resta y asignación
*= Multiplicación y asignación
/= División y asignación
%= Módulo y asignación
//= Cociente y asignación
**= Exponente y asignación
&= AND y asignación
|= OR y asignación
^= XOR y asignación
>>= Desplazamiento a la derecha y asignación
<<= Desplazamiento a la izquierda y asignación
"""

print("Operadores de asignación\n")

x = 5
print(f'valor de x = {x}')
print(f'Asignación x = {x}')

x+=3
print(f'Suma y asignación x += 3 = {x}')

print(f'valor de x = {x}')

x-=3
print(f'Resta y asignación x -= 3 = {x}')

print(f'valor de x = {x}')

x*=3
print(f'Multiplicación y asignación x *= 3 = {x}')

print(f'valor de x = {x}')

x/=3
print(f'División y asignación x /= 3 = {x}')

print(f'valor de x = {x}')

x%=3
print(f'Módulo y asignación x %= 3 = {x}')

print(f'valor de x = {x}')

x//=3
print(f'Cociente y asignación x //= 3 = {x}')

x=5
print(f'valor de x = {x}')

x**=3
print(f'Exponente y asignación x **= 3 = {x}')

x=1
print(f'valor de x = {x}')

x&=1
print(f'AND y asignación x&=1 = {bin(x)}')


x|=2 
print(f'valor de x = {x}')

print(f'OR y asignación x &= 3 = {bin(x)}')

print(f'valor de x = {x}')

x^=2
print(f'XOR y asignación x ^= 3 = {bin(x)}')

x = 10
x>>=1
print(f'Desplazamiento a la derecha y asignación x >>= 1 = {x}')


x = 10
x<<=1
print(f'Desplazamiento a la izquierda y asignación x <<= 1 = {x}')

"""
# OPERADORES RELACIONALES
== Igual
!= Distinto
> Mayor
< Menor
>= Mayor o igual
<= Menor o igual
"""

x=5
y=10
print("Operadores relacionales\n")
print(f'x = {x} y = {y}')

print(f'Igual: {x} == {y} = {x == y}')
print(f'Distinto: {x} != {y} = {x != y}')
print(f'Mayor: {x} > {y} = {x > y}')
print(f'Menor: {x} < {y} = {x < y}')
print(f'Mayor o igual: {x} >= {y} = {x >= y}')
print(f'Menor o igual: {x} <= {y} = {x <= y}')
print("\n")

"""
# OPERADORES LOGICOS
and Y. Devuelve True si ambos son True
or O. Devuelve True si uno de los dos es True    
not NO. Devuelve True si es False y False si es True
"""

print("Operadores lógicos\n")
print(f'Operardor and')
print(f'True and True = ', True and True)
print(f'True and False = ', True and False)
print(f'False and True = ', False and True)
print(f'False and False = ', False and False)
print("\n")
print(f'Operardor or')
print(f'True or True = ', True or True)
print(f'True or False = ', True or False)
print(f'False or True = ', False or True)
print(f'False or False = ', False or False)
print("\n")
print(f'Operardor not')
print(f'not True = ', not True)
print(f'not False = ', not False)
print("\n")

"""
# OPERADORES BITWISE
& AND a nivel de bits
| OR a nivel de bits
~ NOT a nivel de bits
^ XOR a nivel de bits  
>> Desplazamiento a la derecha
<< Desplazamiento a la izquierda
"""
a = 0b1100
b = 0b1011

print("Operadores bitwise\n")
print(f'AND a nivel de bits: {bin(a)} & {bin(b)} = {bin(a & b)}')
print(f'OR a nivel de bits: {bin(a)} | {bin(b)} = {bin(a | b)}')
print(f'NOT a nivel de bits: ~ {bin(a)} = {bin(~a)}')
print(f'XOR a nivel de bits: {bin(a)} ^ {bin(b)} = {bin(a ^ b)}')
print(f'Desplazamiento a la derecha: {bin(a)} >> 1 = {bin(a >> 1)}')
print(f'Desplazamiento a la izquierda: {bin(a)} << 1 = {bin(a << 1)}')
print("\n")

"""
# OPERADORES DE IDENTIDAD
is Devuelve True si ambas variables son el mismo objeto
is not Devuelve True si ambas variables no son el mismo objeto

"""
print("Operadores de identidad\n")
x = 5
y = 5
print(f'x = {x} y = {y}')
print(f'is: x is y = {x is y}') 

"""
# OPERADORES DE PERTENENCIA
in Devuelve True si un valor está presente en una secuencia
not in Devuelve True si un valor no está presente en una secuencia
"""
print("Operadores de pertenencia\n")
x = 5
y = [1,2,3,4,5]
print(f'x = {x} y = {y}') 
print(f'in: x in y = {x in y}')
print(f'not in: x not in y = {x not in y}')




