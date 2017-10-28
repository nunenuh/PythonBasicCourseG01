def grade(nilai):
    out = ""
    if nilai>=90 and nilai <=100:
        out = "A"
    elif nilai>=80 and nilai<=89:
        out = "B+"
    elif nilai>=70 and nilai<=79:
        out = "B"
    elif nilai>=60 and nilai<=69:
        out = "C+"
    elif nilai>=50 and nilai<=59:
        out = "C"
    elif nilai>=40 and nilai<=49:
        out ="D"
    elif nilai>=0 and nilai<=39:
        out ="E"
    else:
        out = "None" 
    return out



nilai_faris = 88
grade_faris = grade(nilai_faris)
print(grade_faris)

nilai_putra = 78
grade_putra = grade(nilai_putra)
print(grade_putra)



