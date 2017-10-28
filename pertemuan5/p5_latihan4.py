

orang = {
    'nama': 'Fandi',
    'alamat': 'Mataram',
    'phone': '087864486991',
    'umur': 29,
    'hobby': 'komputer, memanah, baca buku',
    'pekerjaan': 'swasta'
}

# mencetak isi dictionary dengan key 'umur'
print(orang.get('umur'))

# mencetak seluruh keys dari dictionary 
print(orang.keys())

# mencetak seluruh isi dari dictionary
print(orang.values())

# mencetak berdasarkan key dari dictionary
print(orang.get('alamat'))

# mengecek apakah ada key yang isi
#  di dalam dictionary
print(orang.has_key('no_ktp'))


# menghapus seluruh isi (key maupun values)
# dari dictionary
orang.clear()

print(orang)
