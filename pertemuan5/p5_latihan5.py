
tabel = []

r1 = {
    'tanggal': '25/02/2017',
    'uraian': 'Beli Baju',
    'debet': 0,
    'kredit': 80000,
}
tabel.append(r1)

r2 = {
    'tanggal': '27/02/2017',
    'uraian': 'Beli Ayam',
    'debet': 0,
    'kredit': 100000,
}
tabel.append(r2)

r3 = {
    'tanggal': '28/02/2017',
    'uraian': 'Beli Bebek',
    'debet': 0,
    'kredit': 100000,
}
tabel.append(r3)

tlen = len(tabel)
for row in range(0, tlen):
    out = ""
    out = out + tabel[row]['tanggal'] + ' | ' 
    out = out + tabel[row]['uraian'] + ' | '
    out = out + str(tabel[row]['debet']) + ' | '
    out = out + str(tabel[row]['kredit'])
    print(out)





