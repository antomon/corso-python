def pari_o_dispari(n):
    assert isinstance(n, int), \
      "Errore: l'input deve essere un numero intero"
    
    if n % 2 == 0:
        return "Pari"
    else:
        return "Dispari"
      
print(pari_o_dispari(3))