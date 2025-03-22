usia = float(input("masukan usia anda: "))

if usia > 0 and usia <=2:
    category = "Bayi"
elif usia >2 and usia <=5:
    category = "Balita"
elif usia >5 and usia <=12:
    category = "Anak - Anak"
elif usia >12 and usia <=18:
    category = "Remaja"
else:
    category = "Dewasa"
    
print ("usia anda %s, termasuk dalam category %s" % (usia, category))

    