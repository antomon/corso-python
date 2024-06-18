_count = 0  # <1>

def contatore():  # <2>


  _count += 1  # <4>

  return _count  # <5>

print(contatore())  # <6>
print(contatore())  # <7>