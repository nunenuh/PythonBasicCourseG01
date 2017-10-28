

rahasia = 75
a = True
while a==True:
    b = input("Tebak Angka Saya: ")
    if b==rahasia:
        print("Anda Berhasil, angka saya "+str(rahasia))
        a = False
    else:
        print("Ma'af Anda belum Beruntung!")
        c = str(input("Mau Coba Lagi (Y/N): "))
        if c=='Y':
            a = True
        elif c=='N':
            a = False
        else:
            print('ERROR: Anda Salah Memasukan Pilihan!')
            print('ERROR: Masukan huruf Y atau N')