---
reference-location: margin
citation-location: margin
---

# La struttura lessicale di Python

Per iniziare ad imparare Python come linguaggio, partiamo dalla stuttura lessicale, cioè l'insieme delle regole sintattiche, sia per comprendere le regole di composizione di programmi comprensibili all'interprete, sia per sfrutturne appieno tutte le potenzialità. 

## Dal programma ai token

### Codifica del testo

Tecnicamente, quando eseguiamo l'interprete sia con input dato da un file di codice sorgente, che in modalità interattiva, viene invocato automaticamente un analizzatore lessicale che suddivide tale input in token. Per poterlo fare, deve conoscere, aprioristicamente, che tipo di codifica hanno i caratteri e il default per Python è l'UTF-8.[^1] Si può modificare inserendo un commento, all'inizio del file, con un testo che rispetta l'espressione regolare `coding[=:]\s*([-\w.]+)` per definire una codifica diversa:
```python
# coding: latin-1
```

oppure

```python
# coding: iso-8859-15
```

[^1]: UTF-8 (Unicode Transformation Format, 8 bit) è una codifica di caratteri Unicode in sequenze di lunghezza variabile di byte. Unicode [sito ufficiale](https://home.unicode.org/) è un sistema di codifica che assegna un numero univoco ad ogni carattere usato per la scrittura di testi, in maniera indipendente dalla lingua, dalla piattaforma informatica e dal programma utilizzato. Unicode comprende quasi tutti i sistemi di scrittura attualmente utilizzati, glifi appartenenti a sistemi di scritture particolari, anche di lingue estinte e, infine, anche molti simboli, come quelli valutari, matematici,  musicali e gli emoticon (a cui corrispondono gli emoji di cui rappresentano le immagini).

### Righe logiche

L'analizzatore lessicale individua tutti i token contenuti nel testo e definisce le righe logiche, per mezzo di un token specifico, NEWLINE, non da confondere con caratteri di a capo o di altro genere. 

Una riga logica è costituita da una o più righe fisiche, seguendo le regole di giunzione esplicita o implicita delle righe, che vedremo nel seguito e, quando ha identificato tutte le righe fisiche appartenenti ad una logica, genera un NEWLINE per separare due righe logiche consecutive.

### Righe fisiche

Una riga fisica di un file sorgente o di una stringa nel REPL, è una sequenza di caratteri terminata da uno o più di fine riga (sequenza di a capo), la cui esatta definizione dipende dal sistema operativo.[^2]

[^2]: A seconda del sistema operativo, si utilizzano diversi caratteri di a capo: Unix (Linux e macOS) utilizza LF (linefeed), Windows utilizza CR LF (ritorno seguito da linefeed) e il vecchio Macintosh utilizza CR (return).

### Commenti

Un commento inizia con un carattere cancelletto (`#`) che non fa parte di un letterale stringa (cioè una stringa con all'interno il `#` come `'# è detto cancelletto'`{.python} oppure `"Il carattere #"`{.python}) e termina alla fine della riga fisica. Un commento indica la fine della riga logica, a meno che non vengano invocate le regole di giunzione implicita delle righe. I commenti sono ignorati dall'analizzatore, quindi hanno una funzione di annotazione e documentazione.

### Giunzione esplicita delle righe

Due o più righe fisiche possono essere unite in righe logiche utilizzando il carattere backslash (`\`, poco usata la traduzione barra rovesciata o simili), come segue:

- Quando una riga fisica termina con un backslash che non fa parte di un letterale stringa o commento, essa è unita alla riga successiva formando una singola riga logica, eliminando il backslash e il carattere di fine riga seguente. Ad esempio:
  ```python
  if 1900 < anno < 2100 and 1 <= mese <= 12 \ # <1> 
  and 1 <= giorno <= 31 and 0 <= ora < 24 \ # <2> 
  and 0 <= minuto < 60 and 0 <= secondo < 60: # La data è valida? # <3> 
      print("Data corretta") # Sì! # <4> 
  ```
  1. Prima riga fisica che continua nella successiva per via del backslash.
  2. Seconda riga fisica che continua nella successiva per via del backslash.
  3. Terza riga fisica che termina la riga logica.
  4. Altra riga fisica e logica.
- Una riga che termina con un backslash non può contenere un commento e un commento non può essere spezzato su più righe fisiche da un backslash:
  ```python
  if 1900 < anno < 2100 and 1 <= mese <= 12 \ # Commento # <1>
    and 1 <= giorno <= 31 and 0 <= ora < 24 \     
    and 0 <= minuto < 60 and 0 <= secondo < 60:
      return True

  # Questo è un esempio di commento \ # <2>
  che non può essere spezzato su più righe
  ```
  1. Posizione commento non valida. Si può mettere nella riga fisica successiva.
  2. Non si può spezzare il commento ma va messo il `#` all'inizio della seconda riga fisica.
- Un backslash non continua un token tranne che per quelli letterali: 
  ```python
  text = "Questa è una \ # <1> 
  stringa che continua \ 
  su più righe ed è valida"

  text = "Questa è una \\ # <2> 
  stringa non è valida"
  
  x = 1\ # <3>
  2
  ```
  1. Il letterale stringa è spezzata su più righe fisiche.
  2. La stringa non ha il backslash perché quando si usa un backslash prima di un altro carattere (ad esempio, un altro backslash) all'interno di una stringa, esso indica che il carattere successivo deve essere interpretato letteralmente e non come parte della sintassi.
  3. Il letterale intero non si può spezzare su più righe fisiche.
- Un backslash è illegale altrove in una riga al di fuori di una stringa letterale:
  ```python
  variable = 42 \  # <1>

  string_with_backslash = "Qui è ok: \\" # <2>
  ```
  1. Non valido.
  2. Valido perché il doppio backslash indica il carattere.

### Giunzione implicita delle righe

Le espressioni tra parentesi tonde, quadre o graffe possono essere suddivise su più righe fisiche (di cui le seguenti alla priam dette di continuazione) senza utilizzare backslash. Le righe continuate implicitamente possono contenere commenti e la loro indentazione non è importante. Inoltre, le righe di continuazione vuote sono consentite. Ad esempio il seguente è codice valido:

```python
x = (1 + 2 + # Commento valido
     3 + 4)

y = [1, 2, # Commento valido
# <1>
# Commento valido # <2>
           3, 4] # <3>

z = [1, 2 + # Commento valido
     3, 4]

j = {1, 2 + # Commento valido
     3, 4}

k = {1, 2 + # <4>
     3, 4]     
```
1. Si possono inserire righe fisiche vuote all'interno delle parentesi.
2. Anche con commenti.
3. Non importa quanto sono indentate le righe fisiche di continuazione e ciò incrementa la leggibilità ad esempio allineando i token in colonna.
4. Non si possono mischiare le parentesi.

Non c'è un token NEWLINE tra le righe di continuazione implicite. Le righe di continuazione implicite possono anche verificarsi all'interno di stringhe con triple virgolette, presentate nel seguito, e, in tal caso, non possono contenere commenti.

### Righe vuote

Una riga logica che contiene solo spazi, tabulazioni, form feed e possibilmente un commento viene ignorata (cioè, non viene generato alcun token NEWLINE). 

Nell'interprete interattivo standard, una riga logica completamente vuota (cioè, che non contiene nemmeno spazi o un commento) termina un'istruzione su più righe.

### Indentazione

Gli spazi e le tabulazioni all'inizio di una riga logica sono utilizzati per calcolare il livello di indentazione della riga, che a sua volta è usato per determinare il raggruppamento delle istruzioni. 

Tutte le tabulazioni, cioè non solo quelle all'inizio di una riga fisica, sono trasformate in spazi con un certo algoritmo e l'indentazione viene rifiutata come incoerente, generando un errore [TabError](https://docs.python.org/3/library/exceptions.html#TabError) se un file sorgente mescola tabulazioni e spazi in modo tale che il significato del codice dipenda da come vengono sostituite le tabulazioni.

---
Le tabulazioni vengono sostituite (da sinistra a destra) con uno a otto spazi in modo tale che il numero totale di caratteri fino alla sostituzione, inclusa la sostituzione stessa, sia un multiplo di otto (questa è la stessa regola usata da Unix). Il numero totale di spazi che precede il primo carattere non bianco determina quindi l'indentazione della riga. L'indentazione non può essere suddivisa su più righe fisiche utilizzando i backslash; lo spazio bianco fino al primo backslash determina l'indentazione.

Python tratta ogni tabulazione come se fosse fino a 8 spazi, in modo tale che il carattere successivo dopo la tabulazione si trovi nelle colonne logiche 9, 17, 25, e così via.



I livelli di indentazione delle righe consecutive vengono utilizzati per generare i token `INDENT` e `DEDENT`, utilizzando uno stack, come segue:

1. Prima di leggere la prima riga del file, uno zero viene inserito nello stack; questo zero non verrà mai rimosso.

2. I numeri inseriti nello stack aumentano sempre in modo strettamente crescente dal basso verso l'alto.

3. All'inizio di ciascuna riga logica, il livello di indentazione della riga viene confrontato con il valore in cima allo stack.
   - Se è uguale, non accade nulla.
   - Se è maggiore, il nuovo livello di indentazione viene inserito nello stack e viene generato un token `INDENT`.
   - Se è minore, deve corrispondere a uno dei numeri presenti nello stack. Tutti i numeri nello stack che sono maggiori vengono rimossi e per ciascuno di essi viene generato un token `DEDENT`.

4. Alla fine del file, viene generato un token `DEDENT` per ogni numero rimanente nello stack che è maggiore di zero.

Consideriamo un esempio per illustrare meglio il funzionamento. Sia la funzione seguente salvata in un file:

```python
# <1>
def esempio(): # <2>
  if True: # <3>
      print("Indentato") # <4>
  print("Fine") # <5>
# <6>
```
1. Prima di iniziare, lo stack contiene: `[0]`.
2. Leggiamo la prima riga `def esempio():`{.python}. Il livello di indentazione è 0, uguale al valore in cima allo stack, quindi non accade nulla.
3. Leggiamo la riga successiva `if True:`{.python}.
   - Il livello di indentazione è 4 (cioè il numero di spazi dopo la trasformazione delle tabulazioni se presenti, prima della `i`), maggiore del valore in cima allo stack.
   - Inseriamo 4 nello stack e generiamo un token `INDENT`.
   - Stack ora: `[0, 4]`.
4. Leggiamo la riga `print("Indentato")`{.python}.
   - Il livello di indentazione è 12 (per esempio), maggiore del valore in cima allo stack.
   - Inseriamo 12 nello stack e generiamo un token `INDENT`. Notiamo che non è 8 cioè il doppio di 4, ma un altro valore arbitrario maggiore di 4.
   - Stack ora: `[0, 4, 12]`.
5. Leggiamo la riga `print("Fine")`{.python}.
   - Il livello di indentazione è 4, minore del valore in cima allo stack.
   - Rimuoviamo 8 dallo stack e generiamo un token `DEDENT`.
   - Stack ora: `[0, 4]`.
6. Fine del file.
   - Generiamo un token `DEDENT` per ogni livello rimanente maggiore di zero.
   - Rimuoviamo 4 dallo stack e generiamo un token `DEDENT`.
   - Stack finale: `[0]`.

E vediamo un esempio di codice non valido che genera un errore [IndentationError](https://docs.python.org/3/library/exceptions.html#IndentationError):

```python
def esempio(): 
  if True: # <1>
      print("Indentato")
    print("Fine") # <2>
# <6>
```
1. Il livello di indentazione è 4.
2. Il livello di indentazione è 8 che non esiste nello stack, quindi viene generato l'errore.

Ecco un esempio di codice Python correttamente indentato (anche se in modo poco leggibile):

```python
def perm(l):
        # Calcola la lista di tutte le permutazioni di l
    if len(l) <= 1:
                  return [l]
    r = []
    for i in range(len(l)):
             s = l[:i] + l[i+1:]
             p = perm(s)
             for x in p:
              r.append(l[i:i+1] + x)
    return r
```

Il seguente esempio mostra vari errori di indentazione:

```python
 def perm(l):  # <1>
for i in range(len(l)): # <2>
    s = l[:i] + l[i+1:]
        p = perm(l[:i] + l[i+1:]) # <3>  
        for x in p:
                r.append(l[i:i+1] + x)
            return r  # <4>          
```
1. Errore: prima riga indentata.
2. Errore: non indentata.
3. Errore: indentazione inaspettata perché non può aumentare.
4. Errore: indentazione incoerente perché dovrebbe corrispondere a `s = l[:i] + l[i+1:]`{.python}. Questo è l'unico errore rilevato dall'analizzatore lessicale, mentre i rimanenti dal parser.

### Spazi bianchi tra i token

Tranne che all'inizio di una riga logica o nei letterali stringa, i caratteri di spaziatura (spazio, tabulazione e interruzione di pagina o formfeed) possono essere utilizzati in modo intercambiabile per separare i token. Gli spazi bianchi sono necessari tra due token solo se la loro concatenazione potrebbe altrimenti essere interpretata come un token diverso (ad esempio, `ab` è un token, ma `a b` sono due token).

### Altri token

Oltre a `NEWLINE`, `INDENT` e `DEDENT`, esistono le seguenti categorie di token: identificatori, parole chiave, letterali, operatori e delimitatori. I caratteri di spaziatura (diversi dai terminatori di riga, discussi in precedenza) non sono token, ma servono a delimitare i token. Dove esiste ambiguità, un token comprende la stringa più lunga possibile che forma un token legale, quando letta da sinistra a destra.

### 2.3. Identificatori e parole chiave

Gli identificatori (noti anche come nomi) sono descritti dalle seguenti definizioni lessicali.

La sintassi degli identificatori in Python si basa sull'allegato standard Unicode UAX-31, con elaborazioni e modifiche come definito di seguito; vedere anche PEP 3131 per ulteriori dettagli.

All'interno dell'intervallo ASCII (U+0001..U+007F), i caratteri validi per gli identificatori sono gli stessi di Python 2.x: le lettere maiuscole e minuscole da A a Z, il carattere di sottolineatura `_` e, tranne per il primo carattere, le cifre da 0 a 9.

Python 3.0 introduce caratteri aggiuntivi al di fuori dell'intervallo ASCII (vedere PEP 3131). Per questi caratteri, la classificazione utilizza la versione del Database dei Caratteri Unicode inclusa nel modulo `unicodedata`.

Gli identificatori non hanno limiti di lunghezza. Il maiuscolo e il minuscolo sono distinti.

### 2.3.1. Parole chiave

I seguenti identificatori sono usati come parole riservate o parole chiave del linguaggio e non possono essere usati come identificatori ordinari. Devono essere scritti esattamente come riportato qui:

```plaintext
False      await      else       import     pass
None       break      except     in         raise
True       class      finally    is         return
and        continue   for        lambda     try
as         def        from       nonlocal   while
assert     del        global     not        with
async      elif       if         or         yield
```

### 2.3.2. Soft Keywords

Aggiunto nella versione 3.10.

Alcuni identificatori sono riservati solo in contesti specifici. Questi sono noti come soft keywords. Gli identificatori `match`, `case`, `type` e `_` possono agire sintatticamente come parole chiave in alcuni contesti, ma questa distinzione viene fatta a livello di parser, non durante la tokenizzazione.

Come soft keywords, il loro uso nella grammatica è possibile pur preservando la compatibilità con il codice esistente che utilizza questi nomi come identificatori.

`match`, `case` e `_` sono usati nell'istruzione `match`. `type` è usato nell'istruzione `type`.

Modificato nella versione 3.12: `type` è ora una soft keyword.

### 2.3.3. Classi riservate di identificatori

Alcune classi di identificatori (oltre alle parole chiave) hanno significati speciali. Queste classi sono identificate dai modelli di caratteri di sottolineatura iniziale e finale:

- `_`*: Non importato da `from module import *`.
- `_`: In un pattern di case all'interno di un'istruzione `match`, `_` è una soft keyword che denota un carattere jolly.
  Separatamente, l'interprete interattivo rende disponibile il risultato dell'ultima valutazione nella variabile `_`. (È memorizzato nel modulo `builtins`, insieme alle funzioni incorporate come `print`).
  Altrove, `_` è un identificatore normale. Spesso è usato per nominare elementi “speciali”, ma non è speciale per Python stesso.
  Nota: il nome `_` è spesso usato in congiunzione con l'internazionalizzazione; consultare la documentazione per il modulo `gettext` per ulteriori informazioni su questa convenzione. È anche comunemente usato per variabili non utilizzate.
- `__*__`: Nomi definiti dal sistema, conosciuti informalmente come nomi “dunder”. Questi nomi sono definiti dall'interprete e dalla sua implementazione (inclusa la libreria standard). I nomi di sistema attuali sono discussi nella sezione Nomi dei metodi speciali e altrove. È probabile che ne vengano definiti altri nelle versioni future di Python. Qualsiasi uso di nomi `__*__`, in qualsiasi contesto, che non segua l'uso esplicitamente documentato, è soggetto a rotture senza preavviso.
- `__*`: Nomi privati di classe. I nomi in questa categoria, quando utilizzati nel contesto di una definizione di classe, sono riscritti in una forma offuscata per evitare conflitti di nomi tra attributi “privati” delle classi base e derivate. Vedere la sezione Identificatori (Nomi).

### 2.4. Letterali

I letterali sono notazioni per valori costanti di alcuni tipi integrati.

#### 2.4.1. Letterali di stringa e byte

I letterali di stringa sono descritti dalle seguenti definizioni lessicali:

```plaintext
stringliteral   ::=  [stringprefix](shortstring | longstring)
stringprefix    ::=  "r" | "u" | "R" | "U" | "f" | "F"
                     | "fr" | "Fr" | "fR" | "FR" | "rf" | "rF" | "Rf" | "RF"
shortstring     ::=  "'" shortstringitem* "'" | '"' shortstringitem* '"'
longstring      ::=  "'''" longstringitem* "'''" | '"""' longstringitem* '"""'
shortstringitem ::=  shortstringchar | stringescapeseq
longstringitem  ::=  longstringchar | stringescapeseq
shortstringchar ::=  <any source character except "\" or newline or the quote>
longstringchar  ::=  <any source character except "\">
stringescapeseq ::=  "\" <any source character>
```

I letterali di byte sono descritti dalle seguenti definizioni lessicali:

```plaintext
bytesliteral   ::=  bytesprefix(shortbytes | longbytes)
bytesprefix    ::=  "b" | "B" | "br" | "Br" | "bR" | "BR" | "rb" | "rB" | "Rb" | "RB"
shortbytes     ::=  "'" shortbytesitem* "'" | '"' shortbytesitem* '"'
longbytes      ::=  "'''" longbytesitem* "'''" | '"""' longbytesitem* '"""'
shortbytesitem ::=  shortbyteschar | bytesescapeseq
longbytesitem  ::=  longbyteschar | bytesescapeseq
shortbyteschar ::=  <any ASCII character except "\" or newline or the quote>
longbyteschar  ::=  <any ASCII character except "\">
bytesescapeseq ::=  "\" <any ASCII character>
```

Una restrizione sintattica non indicata da queste produzioni è che non è consentito inserire spazi bianchi tra il prefisso della stringa o dei byte e il resto del letterale. L'insieme dei caratteri sorgente è definito dalla dichiarazione di codifica; è UTF-8 se non viene fornita alcuna dichiarazione di codifica nel file sorgente; vedere la sezione Dichiarazioni di codifica.

In parole semplici: entrambi i tipi di letterali possono essere racchiusi tra apici singoli (') o doppi ("). Possono anche essere racchiusi in gruppi corrispondenti di tre apici singoli o doppi (questi sono generalmente indicati come stringhe con tripli apici). Il carattere barra rovesciata (\) viene utilizzato per dare un significato speciale a caratteri altrimenti ordinari come `n`, che significa 'a capo' quando è preceduto da una barra rovesciata (`\n`). Può anche essere utilizzato per escludere caratteri che altrimenti avrebbero un significato speciale, come il carattere di nuova riga, la barra rovesciata stessa o il carattere di apice. Vedere le sequenze di escape di seguito per esempi.

I letterali di byte sono sempre preceduti da 'b' o 'B'; producono un'istanza del tipo `bytes` anziché del tipo `str`. Possono contenere solo caratteri ASCII; i byte con un valore numerico di 128 o superiore devono essere espressi con sequenze di escape.

Sia i letterali di stringa che quelli di byte possono essere facoltativamente preceduti da una lettera 'r' o 'R'; tali stringhe sono chiamate stringhe raw e trattano le barre rovesciate come caratteri letterali. Di conseguenza, nei letterali di stringa, le sequenze di escape '\U' e '\u' nelle stringhe raw non vengono trattate in modo speciale. Poiché i letterali unicode raw di Python 2.x si comportano in modo diverso rispetto a quelli di Python 3.x, la sintassi 'ur' non è supportata.

Aggiunto nella versione 3.3: il prefisso 'rb' dei letterali di byte raw è stato aggiunto come sinonimo di 'br'.

Il supporto per il letterale unicode legacy (u'value') è stato reintrodotto per semplificare la manutenzione di codebase compatibili con Python 2.x e 3.x. Vedere PEP 414 per ulteriori informazioni.

Un letterale di stringa con il prefisso 'f' o 'F' è un letterale di stringa formattato; vedere le f-string. Il 'f' può essere combinato con 'r', ma non con 'b' o 'u', quindi le stringhe formattate raw sono possibili, ma i letterali di byte formattati non lo sono.

Nelle stringhe con tripli apici, le nuove righe e gli apici non preceduti da una barra rovesciata sono consentiti (e vengono mantenuti), ad eccezione di tre apici non preceduti da una barra rovesciata consecutivi che terminano il letterale. (Un “apice” è il carattere usato per aprire il letterale, cioè o ' o ".)

### 2.4.1.1. Sequenze di escape

A meno che non sia presente un prefisso 'r' o 'R', le sequenze di escape nei letterali di stringa e di byte sono interpretate secondo regole simili a quelle utilizzate dal C standard. Le sequenze di escape riconosciute sono:

| Sequenza di escape | Significato                     | Note  |
|--------------------|---------------------------------|-------|
| \<newline>         | Barra rovesciata e nuova riga ignorati | (1)   |
| \\                 | Barra rovesciata (\)            |       |
| \'                 | Apice singolo (')               |       |
| \"                 | Doppio apice (")                |       |
| \a                 | Campanello ASCII (BEL)          |       |
| \b                 | Backspace ASCII (BS)            |       |
| \f                 | Formfeed ASCII (FF)             |       |
| \n                 | Linefeed ASCII (LF)             |       |
| \r                 | Carriage Return ASCII (CR)      |       |
| \t                 | Tabulazione orizzontale ASCII (TAB) |    |
| \v                 | Tabulazione verticale ASCII (VT) |      |
| \ooo               | Carattere con valore ottale ooo | (2,4) |
| \xhh               | Carattere con valore esadecimale hh | (3,4) |

Le sequenze di escape riconosciute solo nei letterali di stringa sono:

| Sequenza di escape | Significato                               | Note  |
|--------------------|-------------------------------------------|-------|
| \N{name}           | Carattere denominato name nel database Unicode | (5)   |
| \uxxxx             | Carattere con valore esadecimale a 16 bit xxxx | (6)   |
| \Uxxxxxxxx         | Carattere con valore esadecimale a 32 bit xxxxxxxx | (7)   |

Note:

1. Una barra rovesciata può essere aggiunta alla fine di una riga per ignorare la nuova riga:
    ```python
    'Questa stringa non includerà \
    barre rovesciate o caratteri di nuova riga.'
    ```
    Lo stesso risultato può essere ottenuto usando stringhe con tripli apici, o parentesi e concatenazione di letterali di stringa.

2. Come in C standard, sono accettate fino a tre cifre ottali.

   Modificato nella versione 3.11: le sequenze di escape ottali con valore superiore a 0o377 producono un DeprecationWarning.

   Modificato nella versione 3.12: le sequenze di escape ottali con valore superiore a 0o377 producono un SyntaxWarning. In una futura versione di Python saranno eventualmente un SyntaxError.

3. A differenza del C standard, sono richieste esattamente due cifre esadecimali.

4. In un letterale di byte, le sequenze di escape esadecimali e ottali denotano il byte con il valore dato. In un letterale di stringa, queste sequenze denotano un carattere Unicode con il valore dato.

   Modificato nella versione 3.3: è stato aggiunto il supporto per gli alias di nome [1].

5. Sono richieste esattamente quattro cifre esadecimali.

6. Qualsiasi carattere Unicode può essere codificato in questo modo. Sono richieste esattamente otto cifre esadecimali.

A differenza del C standard, tutte le sequenze di escape non riconosciute vengono lasciate nella stringa inalterate, cioè la barra rovesciata rimane nel risultato. (Questo comportamento è utile durante il debug: se una sequenza di escape viene digitata male, l'output risultante è più facilmente riconoscibile come errato). È anche importante notare che le sequenze di escape riconosciute solo nei letterali di stringa rientrano nella categoria delle sequenze di escape non riconosciute per i letterali di byte.

Modificato nella versione 3.6: le sequenze di escape non riconosciute producono un DeprecationWarning.

Modificato nella versione 3.12: le sequenze di escape non riconosciute producono un SyntaxWarning. In una futura versione di Python saranno eventualmente un SyntaxError.

Anche in un letterale raw, gli apici possono essere escludi con una barra rovesciata, ma la barra rovesciata rimane nel risultato; per esempio, `r"\""` è un letterale di stringa valido composto da due caratteri: una barra rovesciata e un doppio apice; `r"\"` non è un letterale di stringa valido (nemmeno una stringa raw può terminare con un numero dispari di barre rovesciate). Si noti inoltre che una singola barra rovesciata seguita da una nuova riga è interpretata come quei due caratteri come parte del letterale, non come una continuazione di linea.

### 2.4.2. Concatenazione di letterali di stringa

È consentito concatenare più letterali di stringa o di byte adiacenti (delimitati da spazi bianchi), eventualmente utilizzando convenzioni di citazione diverse, e il loro significato è lo stesso della loro concatenazione. Quindi, `"hello" 'world'` è equivalente a `"helloworld"`. Questa funzionalità può essere utilizzata per ridurre il numero di barre rovesciate necessarie, per dividere comodamente le stringhe lunghe su più righe lunghe, o anche per aggiungere commenti a parti di stringhe, per esempio:

```python
re.compile("[A-Za-z_]"       # lettera o trattino basso
           "[A-Za-z0-9_]*")  # lettera, cifra o trattino basso
```

Si noti che questa funzionalità è definita a livello sintattico, ma implementata a tempo di compilazione. L'operatore '+' deve essere utilizzato per concatenare espressioni di stringa a tempo di esecuzione. Inoltre, la concatenazione di letterali può utilizzare stili di citazione diversi per ciascun componente (anche mescolando stringhe raw e stringhe con tripli apici), e i letterali di stringa formattati possono essere concatenati con letterali di stringa semplici.

### 2.4.3. f-strings

Aggiunto nella versione 3.6.

Un letterale di stringa formattato o f-string è un letterale di stringa che è prefissato con 'f' o 'F'. Queste stringhe possono contenere campi di sostituzione, che sono espressioni delimitate da parentesi graffe `{}`. Mentre altri letterali di stringa hanno sempre un valore costante, le stringhe formattate sono in realtà espressioni valutate a tempo di esecuzione.

Le sequenze di escape sono decodificate come nei letterali di stringa ordinari (eccetto quando un letterale è anche contrassegnato come stringa raw). Dopo la decodifica, la grammatica per il contenuto della stringa è:

```plaintext
f_string          ::=  (literal_char | "{{" | "}}" | replacement_field)*
replacement_field ::=  "{" f_expression ["="] ["!" conversion] [":" format_spec] "}"
f_expression      ::=  (conditional_expression | "*" or_expr)
                         ("," conditional_expression | "," "*" or_expr)* [","]
                       | yield_expression
conversion        ::=  "s" | "r" | "a"
format_spec       ::=  (literal_char | replacement_field)*
literal_char      ::=  <any code point except "{", "}" or NULL>
```

Le parti della stringa al di fuori delle parentesi graffe sono trattate letteralmente, eccetto che eventuali doppie parentesi graffe '{{' o '}}' sono sostituite con la corrispondente parentesi graffa singola. Una singola parentesi graffa aperta '{' segna un campo di sostituzione, che inizia con un'espressione Python. Per visualizzare sia il testo dell'espressione che il suo valore dopo la valutazione (utile nel debug), può essere aggiunto un segno di uguale '=' dopo l'espressione. Può seguire un campo di conversione, introdotto da un punto esclamativo '!'. Può essere aggiunto anche uno specificatore di formato, introdotto da due punti ':'. Un campo di sostituzione termina con una parentesi graffa chiusa '}'.

Le espressioni nei letterali di stringa formattati sono trattate come normali espressioni Python racchiuse tra parentesi, con alcune eccezioni. Non è consentita un'espressione vuota e le espressioni lambda e di assegnazione := devono essere racchiuse tra parentesi esplicite. Ogni espressione è valutata nel contesto in cui appare il letterale di stringa formattato, in ordine da sinistra a destra. Le espressioni di sostituzione possono contenere nuove righe sia nelle f-string con apici singoli che in quelle con tripli apici e possono contenere commenti. Tutto ciò che segue un # all'interno di un campo di sostituzione è un commento (anche le parentesi graffe e gli apici di chiusura).

### Traduzione Richiesta

```plaintext
>>> f"abc{a # This is a comment }"
... + 3}"
'abc5'
```
Modificato nella versione 3.7: Prima della versione 3.7, un'espressione `await` e comprensioni contenenti una clausola `async for` erano illegali nelle espressioni nei letterali di stringa formattati a causa di un problema con l'implementazione.

Modificato nella versione 3.12: Prima della versione 3.12, i commenti non erano consentiti all'interno dei campi di sostituzione delle f-string.

Quando è fornito il segno di uguale '=', l'output includerà il testo dell'espressione, l'uguale '=' e il valore valutato. Gli spazi dopo la parentesi graffa di apertura '{', all'interno dell'espressione e dopo l'uguale '=' sono tutti mantenuti nell'output. Per impostazione predefinita, l'uguale '=' fa sì che venga fornito il `repr()` dell'espressione, a meno che non sia specificato un formato. Quando viene specificato un formato, si predefinisce lo `str()` dell'espressione a meno che non sia dichiarata una conversione '!r'.

Aggiunto nella versione 3.8: Il segno di uguale '='.

Se è specificata una conversione, il risultato della valutazione dell'espressione viene convertito prima della formattazione. La conversione '!s' chiama `str()` sul risultato, '!r' chiama `repr()`, e '!a' chiama `ascii()`.

Il risultato viene quindi formattato utilizzando il protocollo `format()`. Lo specificatore di formato viene passato al metodo `__format__()` dell'espressione o del risultato della conversione. Una stringa vuota viene passata quando lo specificatore di formato è omesso. Il risultato formattato viene quindi incluso nel valore finale dell'intera stringa.

Gli specificatori di formato di livello superiore possono includere campi di sostituzione annidati. Questi campi annidati possono includere i propri campi di conversione e specificatori di formato, ma non possono includere campi di sostituzione più profondamente annidati. Il mini-linguaggio degli specificatori di formato è lo stesso utilizzato dal metodo `str.format()`.

I letterali di stringa formattati possono essere concatenati, ma i campi di sostituzione non possono essere suddivisi tra letterali.

Alcuni esempi di letterali di stringa formattati:

```python
>>> name = "Fred"
>>> f"He said his name is {name!r}."
"He said his name is 'Fred'."
>>> f"He said his name is {repr(name)}."  # repr() is equivalent to !r
"He said his name is 'Fred'."
>>> width = 10
>>> precision = 4
>>> value = decimal.Decimal("12.34567")
>>> f"result: {value:{width}.{precision}}"  # nested fields
'result:      12.35'
>>> today = datetime(year=2017, month=1, day=27)
>>> f"{today:%B %d, %Y}"  # using date format specifier
'January 27, 2017'
>>> f"{today=:%B %d, %Y}" # using date format specifier and debugging
'today=January 27, 2017'
>>> number = 1024
>>> f"{number:#0x}"  # using integer format specifier
'0x400'
>>> foo = "bar"
>>> f"{ foo = }" # preserves whitespace
" foo = 'bar'"
>>> line = "The mill's closed"
>>> f"{line = }"
'line = "The mill\'s closed"'
>>> f"{line = :20}"
"line = The mill's closed   "
>>> f"{line = !r:20}"
'line = "The mill\'s closed" '
```

Riutilizzare il tipo di citazione esterno della f-string all'interno di un campo di sostituzione è consentito:

```python
>>> a = dict(x=2)
>>> f"abc {a['x']} def"
'abc 2 def'
```
Modificato nella versione 3.12: Prima della versione 3.12, il riutilizzo dello stesso tipo di citazione della f-string esterna all'interno di un campo di sostituzione non era possibile.

Le barre rovesciate sono anche consentite nei campi di sostituzione e vengono valutate allo stesso modo di qualsiasi altro contesto:

```python
>>> a = ["a", "b", "c"]
>>> print(f"List a contains:\n{'\n'.join(a)}")
List a contains:
a
b
c
```
Modificato nella versione 3.12: Prima della versione 3.12, le barre rovesciate non erano consentite all'interno di un campo di sostituzione di una f-string.

I letterali di stringa formattati non possono essere usati come docstring, anche se non includono espressioni.

```python
>>> def foo():
...     f"Not a docstring"
...
>>> foo.__doc__ is None
True
```
Consultare anche PEP 498 per la proposta che ha aggiunto i letterali di stringa formattati, e `str.format()`, che utilizza un meccanismo di stringa di formato correlato.

### 2.4.4. Letterali numerici

Esistono tre tipi di letterali numerici: interi, numeri in virgola mobile e numeri immaginari. Non esistono letterali complessi (i numeri complessi possono essere formati aggiungendo un numero reale e un numero immaginario).

Si noti che i letterali numerici non includono un segno; una frase come `-1` è in realtà un'espressione composta dall'operatore unario ‘-’ e dal letterale `1`.

### 2.4.5. Letterali interi

I letterali interi sono descritti dalle seguenti definizioni lessicali:

```plaintext
integer      ::=  decinteger | bininteger | octinteger | hexinteger
decinteger   ::=  nonzerodigit (["_"] digit)* | "0"+ (["_"] "0")*
bininteger   ::=  "0" ("b" | "B") (["_"] bindigit)+
octinteger   ::=  "0" ("o" | "O") (["_"] octdigit)+
hexinteger   ::=  "0" ("x" | "X") (["_"] hexdigit)+
nonzerodigit ::=  "1"..."9"
digit        ::=  "0"..."9"
bindigit     ::=  "0" | "1"
octdigit     ::=  "0"..."7"
hexdigit     ::=  digit | "a"..."f" | "A"..."F"
```

Non esiste un limite per la lunghezza dei letterali interi a parte ciò che può essere memorizzato nella memoria disponibile.

Gli underscore sono ignorati per determinare il valore numerico del letterale. Possono essere usati per raggruppare le cifre per una maggiore leggibilità. Un underscore può verificarsi tra le cifre e dopo i prefissi di base come `0x`.

Si noti che gli zeri iniziali in un numero decimale diverso da zero non sono consentiti. Questo serve per evitare ambiguità con i letterali ottali in stile C, che Python usava prima della versione 3.0.

Alcuni esempi di letterali interi:

```plaintext
7     2147483647                        0o177    0b100110111
3     79228162514264337593543950336     0o377    0xdeadbeef
      100_000_000_000                   0b_1110_0101
```
Modificato nella versione 3.6: gli underscore sono ora consentiti per scopi di raggruppamento nei letterali.

### 2.4.6. Letterali in virgola mobile

I letterali in virgola mobile sono descritti dalle seguenti definizioni lessicali:

```plaintext
floatnumber   ::=  pointfloat | exponentfloat
pointfloat    ::=  [digitpart] fraction | digitpart "."
exponentfloat ::=  (digitpart | pointfloat) exponent
digitpart     ::=  digit (["_"] digit)*
fraction      ::=  "." digitpart
exponent      ::=  ("e" | "E") ["+" | "-"] digitpart
```

Si noti che le parti intere e degli esponenti sono sempre interpretate utilizzando la base 10. Ad esempio, `077e010` è legale e denota lo stesso numero di `77e10`. L'intervallo consentito di letterali in virgola mobile dipende dall'implementazione. Come nei letterali interi, sono supportati gli underscore per il raggruppamento delle cifre.

Alcuni esempi di letterali in virgola mobile:

```plaintext
3.14    10.    .001    1e100    3.14e-10    0e0    3.14_15_93
```
Modificato nella versione 3.6: gli underscore sono ora consentiti per scopi di raggruppamento nei letterali.

### 2.4.7. Letterali immaginari

I letterali immaginari sono descritti dalle seguenti definizioni lessicali:

```plaintext
imagnumber ::=  (floatnumber | digitpart) ("j" | "J")
```

Un letterale immaginario produce un numero complesso con una parte reale di 0.0. I numeri complessi sono rappresentati come una coppia di numeri in virgola mobile e hanno le stesse restrizioni sul loro intervallo. Per creare un numero complesso con una parte reale diversa da zero, aggiungere un numero in virgola mobile, ad esempio, `(3+4j)`. Alcuni esempi di letterali immaginari:

```plaintext
3.14j   10.j    10j     .001j   1e100j   3.14e-10j   3.14_15_93j
```

### 2.5. Operatori

I seguenti token sono operatori:

```plaintext
+       -       *       **      /       //      %      @
<<      >>      &       |       ^       ~       :=
<       >       <=      >=      ==      !=
```

### 2.6. Delimitatori

I seguenti token fungono da delimitatori nella grammatica:

```plaintext
(       )       [       ]       {       }
,       :       .       ;       @       =       ->
+=      -=      *=      /=      //=     %=      @=
&=      |=      ^=      >>=     <<=     **=
```

Il punto può anche comparire nei letterali in virgola mobile e immaginari. Una sequenza di tre punti ha un significato speciale come letterale di ellissi. La seconda metà dell'elenco, gli operatori di assegnazione aumentata, fungono lessicalmente da delimitatori, ma eseguono anche un'operazione.

I seguenti caratteri ASCII stampabili hanno un significato speciale come parte di altri token o sono altrimenti significativi per l'analizzatore lessicale:

```plaintext
'       "       #       \
```

I seguenti caratteri ASCII stampabili non sono usati in Python. La loro presenza al di fuori dei letterali di stringa e dei commenti è un errore incondizionato:

```plaintext
$       ?       `
```


```{=html}
<script type="py" terminal worker>
import code
code.interact()
</script>
<div id="editor"></div>
```






----




### Ambito e Visibilità degli Identificatori delle Funzioni

L'ambito (scope) e la visibilità degli identificatori delle funzioni determinano dove nel codice una funzione può essere chiamata e utilizzata. Questi concetti sono simili a quelli delle variabili, ma presentano alcune differenze chiave che è importante comprendere.

#### Ambito delle Funzioni

L'ambito di una funzione si riferisce alla regione del codice in cui l'identificatore della funzione è valido e può essere utilizzato.

- **Ambito Globale**: Una funzione dichiarata a livello globale, cioè al di fuori di qualsiasi altra funzione o blocco di codice, ha un ambito globale. Questo significa che la funzione è visibile e può essere chiamata da qualsiasi punto del programma dopo la sua dichiarazione.

  Esempio in C++:

  ```cpp
  #include <iostream>

  void globalFunction() {  // <1>
      std::cout << "Funzione globale" << std::endl;
  }

  int main() {
      globalFunction();  // <2>
      return 0;
  }
  ```

  1. Dichiarazione della funzione `globalFunction` a livello globale.
  2. Chiamata della funzione `globalFunction` all'interno di `main`.

  Il comportamento è identico in Java e C. In Python, le funzioni definite a livello globale hanno ambito globale, come mostrato nei precedenti esempi.

- **Ambito Locale**: Una funzione dichiarata all'interno di un blocco di codice (come all'interno di una funzione o di una classe) ha un ambito locale. La funzione è visibile e può essere chiamata solo all'interno di quel blocco.

  Esempio in Python:

  ```python
  def outerFunction():
      def localFunction():  // <1>
          print("Funzione locale")
      localFunction()  # <2>

  outerFunction()
  # localFunction()  # <3> Errore: localFunction non è visibile qui
  ```

  1. Dichiarazione della funzione `localFunction` all'interno di `outerFunction`.
  2. Chiamata della funzione `localFunction` all'interno di `outerFunction`.
  3. Chiamata a `localFunction` al di fuori di `outerFunction`, che genera un errore poiché `localFunction` non è visibile

 a questo livello.

  In Java e C++, le funzioni dichiarate all'interno di un blocco (come metodi all'interno di una classe) sono accessibili solo all'interno di quel blocco, simile a Python. 

  In C, le funzioni locali non sono standard, ma è possibile ottenere un comportamento simile usando funzioni statiche o funzioni inline definite all'interno di un file sorgente specifico.

#### Visibilità delle Funzioni

La visibilità si riferisce a dove nel codice l'identificatore di una funzione può essere utilizzato. La visibilità è strettamente legata all'ambito, ma può essere influenzata anche da altre considerazioni come la modularità e le regole di accesso.

- **Visibilità Globale**: Le funzioni con ambito globale sono visibili ovunque nel programma. Tuttavia, la loro visibilità può essere limitata dall'uso di namespace (C++) o moduli (Python).

  Esempio in C++ con namespace:

  ```cpp
  #include <iostream>

  namespace MyNamespace {
      void myFunction() {  // <1>
          std::cout << "Funzione nel namespace" << std::endl;
      }
  }

  int main() {
      MyNamespace::myFunction();  // <2>
      return 0;
  }
  ```

  1. Dichiarazione della funzione `myFunction` all'interno di `MyNamespace`.
  2. Chiamata della funzione `myFunction` utilizzando il qualificatore di namespace `MyNamespace::`.

  Il comportamento è identico in C. In Python, i moduli e gli spazi dei nomi (`namespace`) possono essere utilizzati per limitare la visibilità delle funzioni.

- **Visibilità Locale**: Le funzioni con ambito locale sono visibili solo all'interno del blocco in cui sono dichiarate. Questo è utile per creare funzioni helper o interne che non devono essere accessibili dall'esterno.

  Esempio in Python:

  ```python
  def outerFunction():
      def helperFunction():  # <1>
          print("Funzione helper")
      helperFunction()  # <2>
      print("Funzione esterna")

  outerFunction()
  ```

  1. Dichiarazione della funzione `helperFunction` all'interno di `outerFunction`.
  2. Chiamata della funzione `helperFunction` all'interno di `outerFunction`.

  Il comportamento è identico in C++ e Java, dove le funzioni dichiarate all'interno di un metodo o di una classe sono visibili solo all'interno di quel blocco.

### Differenze tra Funzioni e Variabili/oggetti

Sebbene l'ambito e la visibilità delle funzioni condividano concetti simili con le variabili e gli oggetti, ci sono alcune differenze chiave:

- **Durata di vita**: Le variabili locali (automatiche) hanno una durata di vita limitata al blocco di codice in cui sono dichiarate. Quando il controllo esce dal blocco, la memoria allocata per la variabile viene liberata. Le funzioni, tuttavia, non vengono "distrutte" quando il controllo esce dal loro ambito; semplicemente non sono più visibili e chiamabili. In Python, le variabili definite all'interno di un blocco di un'istruzione composta rimangono accessibili finché sono nello stesso ambito di funzione o modulo, mentre le funzioni definite all'interno di un'altra funzione (nested functions) sono visibili solo all'interno di quella funzione.
  
- **Allocazione dinamica**: In C++, le variabili e gli oggetti possono essere allocati dinamicamente usando `new` e deallocati usando `delete`. Le funzioni non richiedono un'allocazione esplicita di memoria; la loro dichiarazione è sufficiente per renderle utilizzabili nell'ambito definito.

---


---

Questa sezione riorganizzata presenta prima le funzioni, seguite dal capitolo su namespace, moduli e file, fornendo una spiegazione dettagliata di come ciascun concetto si applica ai diversi linguaggi di programmazione.