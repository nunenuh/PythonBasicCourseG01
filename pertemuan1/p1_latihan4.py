a = input("Masukan Nilai (True/False) a: ")
c = bool(a)

b = input("Masukan Nilai (True/False) b: ")
d = bool(b)

f = input("Masukan Nilai f: ")
g = float(f)

h = input("Masukan Nilai h: ")
k = float(h)



ab1 = (c == d)
cd1 = (g >= k)
cd2 = (g <= k)
cd3 = (g != k)
cd4 = (g == k)



out1 = "c == d adalah "+str(ab1)
print(out1)

out2 = "g >= k adalah "+str(cd1)
print(out2)

out3 = "g <= k adalah "+str(cd2)
print(out3)

out4 = "g != k adalah "+str(cd3)
print(out4)

out5 = "g == k adalah "+str(cd4)
print(out5)