n = int(input("Masukan Jumlah Perulangan: "))
n = n + 1

a = 0
for var in range(1,n): 

    if var==5:
        print(str(var)+" adalah angka favorit saya")
    else:
        print('ini angka yang lain')
        
    print('var: '+str(var))
    print('a: '+str(a))
    a = a + 2
    print('-------')