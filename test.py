l1 = [42., "Hello", 0x42]
print(l1[1])  # <1>

print(len(l1))  # <2>

l2 = [42]

l3 = l1 + l2 
print(l3) # <3>

l2 += l1 
print(l2) # <4>

l4 = []

l4.extend(l1) 
print(l4) # <5>

l5 = []

l5.append(l1) 
print(l5) # <6>

print(l2[1:3])   # <7>

l1[1] = "Ciao"
print(l1)  # <8>

l1.remove("Ciao")
print(l1)  # <9>

l1.pop(0)
print(l1)  # <10>

del l4[1:2] 
print("...")
print(l4) # <11>