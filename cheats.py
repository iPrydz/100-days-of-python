# Comments using # at the start

### Console log ###
print("Hello")


### Salto de página ###
print("Hello \n World")


### Función para hacer preguntas por consola ###
name = input("What is your name? ")


### Length ###
len(name)


### Esto hace que haga un print de la posición 1 de la palabra, es decir letra 'e' ###
print("Hello"[1])
# Última letra 
print("Hello"[-1]) 


### Integer largo, podemos usar _ para separar el número y que visualmente sea más fácil de leer ###
123_456_789


### Así se sabe el tipo de una variable ###
num = 6
type(num)


### Conversión de tipos de variable ###
str(num) # num era int y pasa a ser string
float()
int()


### Mathematical operations ###
1 + 2
4 - 3
3 * 2
6 / 3 # Dividir siempre devuelve float
2 ** 2 # Exponente


### Redondear ###
round(8 / 3) # Redondea a 3
round(8 / 3, 2) # Redondea con 2 decimales, es decir 2.67 en vez de 3

8 // 3 # División que directamente te devuelve un int en vez de float

num = 4 / 2
num /= 2 # += -= /= *=
print(num)


### f-String ###
score = 0
height = 1.8
isWinning = True

print(f"You score is {score}, your height is {height} and your winning is {isWinning}.")


### IF / ELSE ###
height = 120

if height > 100:
    print("¡Qué alto!")
else:
    print("Qué bajito haha")


### Reverse ###
not height > 10


### Hay una forma de que ignore los apóstrofes en los strings usando \ e ignorará la siguiente letra ###
print('You\'re... Type "left" or "right"')


### Random ###
import random

random_int = random.randint(100, 250)
print(random_int)

# random de 0.0 a 5.0
random_float = random.random() * 5 
print(random_float) 

fruits = ["Apple", "Pear"]
vegetables = ["Spinach", "Kale"]
fruits.append("Banana") # Añadir un ítem al final de la lista
fruits.extend(["Banana", "Orange"]) # Añadir varios ítems al final de la lista
print(fruits)

all_together = [fruits, vegetables]
print(all_together[1][1])


### Loops ###
fruits = ["Apple", "Peach", "Pear"]
years = [1, 200, 2020]

for fruit in fruits:
    print(fruit)
    
print(max(years)) # MAX() Averigua el máximo de una lista
print(sum(years)) # SUM() Suma todos los valores de una lista

for number in range(1, 10, 2): # range(principio, final, saltos)
    print(number)