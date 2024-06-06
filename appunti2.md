# NOTA 1

-3 in python è una espressione che viene valutata in un oggetto che ha valore -3




### Insiemi

Python ha due tipi di insiemi di elemeni unici non ordinati: `set` e `frozenset`. 


### Set e Frozenset

Python ha due tipi di set incorporati: , per rappresentare collezioni di elementi unici con ordine arbitrario. Gli elementi in un set possono essere di tipi diversi, ma devono essere tutti hashable. Le istanze del tipo `set` sono mutabili e quindi non hashable, mentre le istanze del tipo `frozenset` sono immutabili e hashable. Non è possibile avere un set i cui elementi siano altri set, ma è possibile avere un set (o un frozenset) i cui elementi siano frozenset. I set e i frozenset non sono ordinati.

### Creazione di Set e Frozenset

#### Utilizzo di Letterali

Per denotare un set, si utilizza una serie di espressioni (gli elementi del set) separate da virgole (,) all'interno di parentesi graffe ({}). Se ogni elemento è un letterale, l'intera costruzione è un letterale di set. Si può opzionalmente mettere una virgola ridondante dopo l'ultimo elemento. 

Esempi di letterali di set:

- **Set con tre elementi**:

  ```python
  s = {42, 3.14, 'hello'}
  ```

- **Set con un elemento (opzionalmente con una virgola finale)**:

  ```python
  s = {100}
  ```

- **Set vuoto**:

  Non esiste un letterale per un set vuoto; si deve usare il costruttore `set()`:

  ```python
  s = set()
  ```

```python
# Set con tre elementi
s1 = {42, 3.14, 'hello'}

# Set con un elemento
s2 = {100}

# Set vuoto
s3 = set()
```

#### Utilizzo della Classe `set`

Si può creare un set chiamando il tipo built-in `set` senza argomenti (per un set vuoto) o con un argomento che è un oggetto iterabile (per un set i cui elementi sono quelli dell'iterabile).

```python
# Creazione di un set da una lista
s = set([1, 2, 3, 4])
print(s)  # Output: {1, 2, 3, 4}

# Creazione di un set vuoto
s_empty = set()
print(s_empty)  # Output: set()
```

#### Utilizzo della Classe `frozenset`

Allo stesso modo, si può creare un frozenset chiamando il tipo built-in `frozenset` senza argomenti (per un frozenset vuoto) o con un argomento che è un oggetto iterabile (per un frozenset i cui elementi sono quelli dell'iterabile).

```python
# Creazione di un frozenset da una lista
fs = frozenset([1, 2, 3, 4])
print(fs)  # Output: frozenset({1, 2, 3, 4})

# Creazione di un frozenset vuoto
fs_empty = frozenset()
print(fs_empty)  # Output: frozenset()
```

### Derivazione della Classe `set` e `frozenset`

Entrambi i tipi `set` e `frozenset` derivano direttamente dalla classe base `object` e non hanno superclassi intermedie.

### Caratteristiche dei Set e dei Frozenset

#### Set

I set sono mutabili, il che significa che una volta creati, possono essere modificati. Supportano operazioni come aggiunta, rimozione e controllo dell'esistenza di elementi.

- **Aggiunta di Elementi**:

  ```python
  s = {1, 2, 3}
  s.add(4)
  print(s)  # Output: {1, 2, 3, 4}
  ```

- **Rimozione di Elementi**:

  ```python
  s = {1, 2, 3, 4}
  s.remove(3)
  print(s)  # Output: {1, 2, 4}
  ```

- **Controllo dell'Esistenza di un Elemento**:

  ```python
  s = {1, 2, 3}
  print(2 in s)  # Output: True
  print(5 in s)  # Output: False
  ```

#### Frozenset

I frozenset sono immutabili, il che significa che una volta creati, non possono essere modificati. Supportano operazioni di lettura come controllo dell'esistenza di elementi e operazioni di set (unione, intersezione, differenza), ma non supportano operazioni di modifica.

- **Controllo dell'Esistenza di un Elemento**:

  ```python
  fs = frozenset([1, 2, 3])
  print(2 in fs)  # Output: True
  print(5 in fs)  # Output: False
  ```

- **Operazioni di Set**:

  ```python
  fs1 = frozenset([1, 2, 3])
  fs2 = frozenset([3, 4, 5])
  
  # Unione
  print(fs1 | fs2)  # Output: frozenset({1, 2, 3, 4, 5})
  
  # Intersezione
  print(fs1 & fs2)  # Output: frozenset({3})
  
  # Differenza
  print(fs1 - fs2)  # Output: frozenset({1, 2})
  ```


































### Altri

#### None
Il tipo `None` ha un solo valore, `None`, che rappresenta l'assenza di un valore. È spesso utilizzato come valore predefinito per variabili o come valore di ritorno per funzioni che non restituiscono nulla.

Esempio:
```python
a = None
print(type(a))  # <class 'NoneType'>
```

#### NotImplemented
`NotImplemented` è un valore speciale che può essere restituito dai metodi aritmetici e di confronto quando l'operazione non è supportata per gli operandi forniti. Non dovrebbe essere valutato in un contesto booleano.

Esempio:
```python
class MyNumber:
    def __eq__(self, other):
        if isinstance(other, MyNumber):
            return True
        return NotImplemented

a = MyNumber()
b = MyNumber()
print(a == b)  # True
print(a == 42)  # NotImplemented
```

#### Ellipsis
`Ellipsis` ha un solo valore, rappresentato dal letterale `...` o dal nome predefinito `Ellipsis`. È utilizzato principalmente in contesti di slicing avanzati.

Esempio:
```python
a = ...
print(type(a))  # <class 'ellipsis'>
```
