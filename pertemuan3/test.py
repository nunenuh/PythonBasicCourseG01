a = input ("Pilih Gender (Pria/Wanita) a:")
b = input ("Masukan Umur Anda : ")
b = int(b)

# a.upper() akan membuat semua string
# menjadi huruf besar
a = a.upper()

x = 25
y = 20


#jika pria
    # ber umur 25 keatas maka dia boleh menikah
     
    # ber umur 25 kebawah maka dia tidak boleh menikah
#jika wanita
    #ber umur 20 keatas maka dia boleh menikah
    
    #ber umur 20 kebawah maka dia tidak boleh menikah

#jika Gender yang dipilih tidak ada maka dia banci kaleng


if (a=="PRIA"):
    if (b>=x):
        print (" Boleh Menikah")
    else:
        print (" Belum Boleh Menikah")
elif (a=="WANITA"):
    if (b>=y):
        print (" Boleh menikah")
    else:
        print (" Belum Boleh Menikah")
else:
    print ("Lu Banci Njir?")