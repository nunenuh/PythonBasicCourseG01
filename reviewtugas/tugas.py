#kinerja karyawan  (10-100) :
#jika karyawan dapat nilai < 30 
    # maka bintang 1
#jika karyawan dapat nilai >= 30
    #jika karyawan dapat nilai < 50
        # maka bintang 2
#jika karyawan dapat nilai >= 50
    #jika karyawan dapat nilai < 70
        # maka bintang 3
#jika karyawan dapat nilai >= 70
    #jika karyawan dapat nilai < 90
        # maka bintang 4
#jika karyawan dapat nilai >= 90
    #jika karyawan dapat nilai <= 100
        # maka bintang 5

    
print ('keterangan :')
print ('kinerja karyawan')
print (' ------------------------------------------------')
print ('|nilai 10-29 dapat bintang 1 = Kinerja Buruk     |')
print ('|nilai 30-49 dapat bintang 2 = Kinerja Kurang    |')
print ('|nilai 50-69 dapat bintang 3 = Kinerja Cukup     |')
print ('|nilai 70-89 dapat bintang 4 = Kinerja Baik      |')
print ('|nilai 90-100 dapat bintang 5 = Kinerja Memuaskan|')
print (' ------------------------------------------------')

a = int(input("Nilai Kinerja Karyawan (10-100) : "))
   
if a < 30: 
    print('Nilai: '+str(a))
    print ('Bintang 1')    
    b=0
    while(b<1):
        print('*') , #jika diberi koma, urutannya bisa kesamping, jika tidak kebawah
        b=b+1  
                
if a >= 30: 
    if a < 50:
        print('Nilai :' +str(a))
        print ('Bintang 2')
        b=0
        while(b<2):
            print('*') , 
            b=b+1  

if a >= 50:
    if a < 70:
        print('Nilai :' +str(a))
        print ('Bintang 3')
        b=0
        while(b<3):
            print('*') , 
            b=b+1  

if a >= 70: 
   if a < 90:
        print('Nilai :' +str(a))
        print ('Bintang 4')
        b=0
        while(b<4):
            print('*') , 
            b=b+1

if a >= 90:
  if a <= 100:
        print('Nilai :' +str(a))
        print ('Bintang 5')
        b=0
        while(b<5):
            print('*') ,
            b=b+1  

