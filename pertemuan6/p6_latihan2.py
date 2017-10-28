# luas persegi
# luas = s*s
def luas_persegi(sisi):
    luas = sisi*sisi
    return luas

s = 20
lp = luas_persegi(s)
print(lp)


# luas persegi panjang
# luas = p x l
def luas_persegi_panjang(a, b):
    luas = a*b
    return luas

lebar = 15
panjang = 20
lpp = luas_persegi_panjang(panjang, lebar)
print(lpp)