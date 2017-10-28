tanggal = [
    '02/25/17',
    '02/25/17',
    '02/27/17',
    '02/27/17',
]

uraian = [
    'BL Paku',
    'BL Palu',
    'BL Kopi',
    'JL Web '
]

debet = [
    0,
    0,
    0,
    500000
]

kredit = [
    5000,
    12500,
    25000,
    0
]

jurnal = [
    tanggal,
    uraian,
    debet,
    kredit
]

ln = len(tanggal)
total_row = len(tanggal) 
total_col = len(jurnal)
row = 0
col = 0

for row in range(0,total_row):
    out = ""
    for col in range(0, total_col):
        out = out+' '+str(jurnal[col][row]) +' | '
    print(out)
