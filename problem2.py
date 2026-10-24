# Problema 2 - Reina de Corazones - adalteto - commit 3
from cls_Stack import cls_Stack
import random
import time

# Baraja del profesor - 52 cartas
# C=Corazon, D=Diamante, T=Trebol, B=Bastos/Picas
VALORES = ['A', '2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K']
PALOS = ['C', 'D', 'T', 'B']
BARAJA = [v + p for p in PALOS for v in VALORES]


class Jugador:
    def __init__(self, nombre):
        self.nombre = nombre
        # Composicion: cada jugador tiene su propia pila
        self.pila = cls_Stack()
        # Validacion que pide el examen: vacia antes de usar
        if not self.pila.isempty():
            print(f"Error pila de {nombre} no vacia al iniciar")

        self.naipes_obtenidos = []  # Lo que va ganando en el juego

    def cargar_naipe(self, naipe):
        if self.pila.isfull():
            return False
        self.pila.push(naipe)
        return True

    def jugar_carta(self):
        if self.pila.isempty():
            return None
        carta = self.pila.pop()
        self.naipes_obtenidos.append(carta)
        return carta


# --- SUBRUTINAS QUE VAN EN Subrutinas.py SEGUN EL PDF ---

def repartir_naipes(jugadores):
    """Reparte 1 a la vez por jugador, 10 naipes cada uno, sin repetir"""
    mazo = BARAJA.copy()
    random.shuffle(mazo)

    # Reparte hasta 10 por jugador
    for _ in range(10):
        for jugador in jugadores:
            if mazo and not jugador.pila.isfull():
                carta = mazo.pop()
                jugador.cargar_naipe(carta)


def jugar_partida(jugadores):
    ganador = None

    # Encabezado
    print(f"\n{'Merlina':<12} {'Tio Lucas':<12} {'Pericles':<12} {'Homero':<12}")
    print("-" * 55)

    # El juego sigue mientras tengan naipes
    hay_cartas = True
    while hay_cartas and ganador is None:
        fila = []
        hay_cartas = False

        for jugador in jugadores:
            carta = jugador.jugar_carta()
            if carta is not None:
                hay_cartas = True
                fila.append(carta)
                # Verifica si es la Reina de Corazones
                if carta == "QC":
                    ganador = jugador
            else:
                fila.append("")

            time.sleep(2)  # Espera de 2 seg entre jugador y jugador

        # Imprime la fila en 4 columnas
        if any(fila):
            print(f"{fila[0]:<12} {fila[1]:<12} {fila[2]:<12} {fila[3]:<12}")

        if ganador:
            break

    return ganador


# --- PROGRAMA PRINCIPAL ---

jugadores = [
    Jugador("Merlina"),
    Jugador("Tio Lucas"),
    Jugador("Pericles"),
    Jugador("Homero")
]

repartir_naipes(jugadores)
ganador = jugar_partida(jugadores)

if ganador:
    print(f"\n¡Ganador: {ganador.nombre} con QC!")
    # Requisito del examen: List Comprehension o lambda con filter
    corazones = list(filter(lambda c: c.endswith('C'), ganador.naipes_obtenidos))
    # Otra forma valida: corazones = [c for c in ganador.naipes_obtenidos if c.endswith('C')]
    print(f"Cartas de Corazon del ganador: {corazones}")
    print(f"Lista completa del ganador: {ganador.naipes_obtenidos}")
else:
    print("\nJuego terminado, nadie saco la QC")

# Validacion final que pide el examen: pilas vacias al terminar
for j in jugadores:
    print(f"Pila de {j.nombre} vacia al final: {j.pila.isempty()}")