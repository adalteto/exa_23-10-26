"""================================================================================================
Institute...: Universidad Técnica Nacional
Campus......: Pacífico
Career......: Tecnologías de Información
Period......: 3-2026
Document....: cls_Stack.py (Pythonic and modern version)
Goals.......: Stack Data Structure implementation using native Python lists and type hinting.
Professor...: Jorge Ruiz (york)
Student.....:
================================================================================================"""
from typing import Any, List


class cls_Stack:
    def __init__(self) -> None:
        # Use a native dynamic list instead of a static array of fixed size
        self._contenedor: List[Any] = []

    # Returns True if the stack is empty, False otherwise.
    def isempty(self) -> bool:
        return len(self._contenedor) == 0

    # In Python, lists are dynamic and have no strict default limit;
    # therefore, a maximum limit of 10 elements is enforced using a conditional statement.
    def isfull(self) -> bool:
        return len(self._contenedor) >= 10

    # Adds an element to the top of the stack.
    def push(self, valor: Any) -> None:
        """Agrega un elemento al tope de la pila."""
        self._contenedor.append(valor)

    # Removes and returns the top element of the stack.
    def pop(self) -> Any:
        if self.isempty():
            raise IndexError("pop from empty stack")
        return self._contenedor.pop()

    # Useful and very Pythonic method: allows viewing the top element without removing it.
    def peek(self) -> Any:
        if self.isempty():
            raise IndexError("peek from empty stack")
        return self._contenedor[-1]

    # Allows using the native len(stack) function directly.
    def __len__(self) -> int:
        return len(self._contenedor)

    # Textual representation of the stack (from bottom to top).
    def __str__(self) -> str:
        return f"Stack(top -> {self._contenedor})"

    # Returns a list of all elements in the stack (from bottom to top).
    def obtener_elementos(self) -> list:
        return self._contenedor

