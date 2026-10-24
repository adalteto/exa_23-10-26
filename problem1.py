# Problema 1 - Evaluacion de expresiones - adalteto - commit 2from cls_Stack import cls_Stack

def es_formula(expresion):
    texto = expresion.strip()
    if len(texto) == 0:
        return False
    # Si es solo letras como "hola", no es formula
    if texto.isalpha():
        return False
    # Debe tener al menos un simbolo matematico
    simbolos = "+-*/^()[]{}"
    for c in texto:
        if c in simbolos:
            return True
    return False

def verificar_expresion(expresion):
    pila = cls_Stack()
    if not pila.isempty():
        return False
    parejas = {')': '(', ']': '[', '}': '{'}
    for char in expresion:
        if char in "([{":
            if pila.isfull():
                return False
            pila.push(char)
        elif char in ")]}":
            if pila.isempty():
                return False
            ultimo = pila.pop()
            if ultimo != parejas[char]:
                return False
    return pila.isempty()

while True:
    print()
    fx = input("Ingrese la expresion fx = (o 'salir'): ")
    if fx.lower() == 'salir':
        break
    if not es_formula(fx):
        print(f"fx = {fx} -> NO es una formula valida")
        continue
    if verificar_expresion(fx):
        print(f"fx = {fx} correctamente escrita")
    else:
        print(f"fx = {fx} incorrectamente escrita")