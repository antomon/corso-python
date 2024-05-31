print(type(...))  # <class 'ellipsis'> # <1>

def funzione_da_completare():
  ... # <2>

class ClasseEsempio:
  def metodo_da_completare(self):
    ...

from typing import Callable

def funzione_variadica(func: Callable[..., int]): # <3>
  pass

import numpy as np

array = np.array([[[1, 2, 3],    [4, 5, 6]], 
                  [[7, 8, 9], [10, 11, 12]]]) 

print(array[..., 1]) # <4>