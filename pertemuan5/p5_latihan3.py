#File:p5_latihan3.py
dict1 = {
    'nama': 'Fandi',
    'alamat': 'Mataram',
    'phone': '087864486991',
    'umur': 29,
    'hobby': 'komputer, memanah, baca buku',
    'pekerjaan': 'swasta'
}

print(dict1['nama'])


dict2 = {
    'tanggal': [
        '02/25/17',
        '02/25/17',
        '02/27/17',
        '02/27/17',
    ],
    'uraian': [
        'BL Paku', 
        'BL Palu', 
        'BL Kopi', 
        'JL Web '
    ],
    'debet':[
        0,
        0,
        0,
        500000
    ],
    'kredit': [
        5000,
        12500,
        25000,
        0
    ]
}

print(dict2['tanggal'][0])