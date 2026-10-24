"""=================================================================================================
Institute....: Universidad Técnica Nacional
Campus.......: Pacífico
Career.......: Tecnologías de Información
Course.......: ITI-321 - Programación III
Period.......: 3-2026
Documents....: Exam_01 - 01_Stack
Goals........: Using stack class
Professor....: Jorge Ruiz (york)
Student......:
================================================================================================="""
from cls_Stack import cls_Stack

print()
print("Stack implementation")
print("=================================")

# Create stack instance
pilita = cls_Stack()

# Load data chunk into stack while this not full
for letra in "Cuquita":
    if not pilita.isfull():
        pilita.push(letra)
    else:
        break

while not pilita.isempty():
    print(pilita.pop())

