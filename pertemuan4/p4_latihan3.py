
# membuat variable array berbentuk list
makanan = []
status = True
while status == True:
    text_input = "Masukan Makanan ke dalam List: "
    isi_makanan = str(input(text_input))

    makanan.append(isi_makanan)
    print('Makanan "'+isi_makanan+'" sudah di inputkan')
    print()

    text_input2 = "Apakah ingin input lagi (Y): "
    lagi = input(text_input2)
    lagi = lagi.upper()

    if lagi == 'Y':
        status = True
    else:
        status = False
    
    # ini untuk bikin enter di tampilan
    print()

text_output1 = "Makanan yang telah di Inputkan: "
print(text_output1)
print()

index = 0
jumlah = len(makanan)

for idx in range(index, jumlah):
    nomer = idx+1
    text_output2 = str(nomer)+". "+str(makanan[idx])
    print(text_output2)
