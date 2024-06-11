class Matrice:
  def __init__(self, righe):
    self.righe = righe
    self.num_righe = len(righe)
    self.num_colonne = len(righe[0]) if righe else 0

  def __matmul__(self, altra): # <1>
    if self.num_colonne != altra.num_righe: # <2>
      raise ValueError("Non è possibile moltiplicare le matrici: "
                       "dimensioni incompatibili.")
    
    risultato = [[0 for _ in range(altra.num_colonne)] # <3>
                 for _ in range(self.num_righe)]
    
    for i in range(self.num_righe): # <4>
      for j in range(altra.num_colonne):
        for k in range(self.num_colonne):
          risultato[i][j] += (self.righe[i][k] *
                              altra.righe[k][j])
    
    return Matrice(risultato)

  def __repr__(self): # <5>
    return '\n'.join([' '.join(map(str, riga)) for riga in self.righe])

A = Matrice([[1, 2],  # <6>
             [3, 4]])
B = Matrice([[5, 6], # <7>
             [7, 8]])

C = A @ B # <8>

print("Matrice A:") 
print(A) # <9>

print("Matrice B:")
print(B)

print("Risultato di A @ B:")
print(C) # <10>