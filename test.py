nome = "Python"
definizione = "Linguaggio"

f_stringa_multi_linea = f'''Questo è un esempio
di f-stringa multi-linea
in {definizione.lower() + ' ' + nome}''' # <2>

print(f_stringa_multi_linea)