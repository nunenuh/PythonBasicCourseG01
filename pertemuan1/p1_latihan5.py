a = input("Masukan Nilai a: ")
a = float(a)

b = input("Masukan Nilai b: ")
b = float(b)

c = a*b
d = a+b

print("Nilai C = "+str(c))
print("Nilai D = "+str(d))

if c>=100:
    print("Nilai C lebih besar dari dan sama dengan 100")
    print("ini tambahan broh!")
else:
    print("Nilai C lebih kecil dan tidak sama dengan 100")
    print("Simple kan broh!")

if c==d:
    print("Nilai C adalah sama dengan D")
else:
    print("Nilai C tidak sama dengan D")
