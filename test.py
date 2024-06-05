



s = "Hello" + ' ' + 'World!'
print(s)

ss = s

ss *= 2
print(ss)
print(s)

b = 'el' in s
print(b)

b = 'oo' not in s
print(b)

b = "Ciao Mondo!" < s
print(b)

s_ = ss[:len(s)]
print(s)

l = len(ss)
print(l)

s_ = ss[:int(len(ss) / 2)]
print(s_)