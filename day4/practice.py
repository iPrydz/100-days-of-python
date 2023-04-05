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