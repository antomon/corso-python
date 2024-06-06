import sys

float_info = sys.float_info  # <1>

print(f"Massimo valore rappresentabile (max): {float_info.max}")  # <2>
print(f"Minimo valore rappresentabile positivo (min): {float_info.min}")  # <3>
print(f"Massimo esponente base 10 (max_exp): {float_info.max_exp}")  # <4>
print(f"Minimo esponente base 10 (min_exp): {float_info.min_exp}")  # <5>
print(f"Massimo esponente base 2 (max_10_exp): {float_info.max_10_exp}")  # <6>
print(f"Minimo esponente base 2 (min_10_exp): {float_info.min_10_exp}")  # <7>
print(f"Precisione in bit (dig): {float_info.dig}")  # <8>
print(f"Numero di bit di mantissa (mant_dig): {float_info.mant_dig}")  # <9>
print(f"Epsilon macchina (epsilon): {float_info.epsilon}")  # <10>