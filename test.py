def somma_numeri(numeri: list[int]) -> int:  # <1>
    """Restituisce la somma di una lista di numeri interi."""  # <2>
    return sum(numeri)  # <3>

print(somma_numeri([1, 2, 3, 4]))  # <4>
print(somma_numeri.__annotations__)  # <5>