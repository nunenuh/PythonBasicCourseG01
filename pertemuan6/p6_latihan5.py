def grade(nilai):
    out = ""
    if nilai>=90 and nilai <=100:
        out = "A"
    elif nilai>=80 and nilai<=89:
        out = "B+"
    elif nilai>=70 and nilai<=79:
        out = "B"
    elif nilai>=60 and nilai<=69:
        out = "C+d"
    elif nilai>=50 and nilai<=59:
        out = "C"
    elif nilai>=40 and nilai<=49:
        out ="D"
    elif nilai>=0 and nilai<=39:
        out ="E"
    else:
        out = "None" 
    return out

def grade_array(nilai_array):
    out = []
    jumlah = len(nilai_array)
    index = 0
    for idx in range(index, jumlah):
        nilai = nilai_array[idx]
        grd = grade(nilai)
        out.append(grd)
    return out


z = [89, 55, 72, 84, 32, 22, 55, 89, 76]
# output = grade(nilai)
# ["B+", "C", "B", "B+", "D"]
output = grade_array(z)
print(output)