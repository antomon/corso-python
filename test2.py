from typing import TypeAlias

type Point = tuple[float, float] # <1>

def distanza(p1: Point, p2: Point) -> float: # <2>
  return ((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2) ** 0.5

punto1: Point = (1.0, 2.0) # <3>
punto2: Point = (4.0, 6.0)

print(distanza(punto1, punto2)) # <4>

print(type(punto1)) # <5>

punto2: Point = "Coppia di coordinate"
