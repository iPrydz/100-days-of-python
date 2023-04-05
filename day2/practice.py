# Data types

# String examples

# Esto hace que haga un print de la posición 1 de la palabra, es decir letra 'e'
print("Hello"[1])
# Última letra 
print("Hello"[-1]) 

# Integer largo, podemos usar _ para separar el número y que visualmente sea más fácil de leer
123_456_789

# Así se sabe el tipo de una variable
num = 6
type(num)

# Conversión de tipos de variable
str(num) # num era int y pasa a ser string
float()
int()

# Mathematical operations
1 + 2
4 - 3
3 * 2
6 / 3 # Dividir siempre devuelve float
2 ** 2 # Exponente

# Orden de ejecución

# PEMDAS (LR) multiplicación, división, suma y resta son igual de importantes pero se calculan de izquierda a derecha.
# Parentesis
# Exponentes
# Multiplicación y División
# Suma (Addition en inglés) y Resta (Subtraction en inglés)

# Redondear
round(8 / 3) # Redondea a 3
round(8 / 3, 2) # Redondea con 2 decimales, es decir 2.67 en vez de 3

8 // 3 # División que directamente te devuelve un int en vez de float

num = 4 / 2
num /= 2 # += -= /= *=
print(num)

# f-String
score = 0
height = 1.8
isWinning = True

print(f"You score is {score}, your height is {height} and your winning is {isWinning}.")