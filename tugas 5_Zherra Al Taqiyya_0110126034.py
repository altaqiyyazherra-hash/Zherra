# tugas no1
kendaraan = ["vario", "motor", 150, "pink", 2]
tambahan = [5000, "matic"]
kendaraan.extend(tambahan)
kendaraan.append("honda")
print(kendaraan)

# tugas no2
print("=== Alat hitung luas bangun datar")
print("Pilih 1 untuk menghitung luas persegi")
print("Pilih 2 untuk menghitung luas lingkaran")
print("Pilih 3 untuk menghitung luas segitiga")

pilihan = int (input("Masukkan pilihan (1/2/3)"))

match pilihan:
    case 1:
        s = int(input("Masukkan panjang sisi persegi: "))
        luas = s * s
        print(f"Luas persegi adalah: {luas}")
        
    case 2:
            r = int(input("Masukkan panjang jari-jari lingkaran: "))
            pi = 3.14
            luas = pi * r**2
            print(f"Luas lingkaran adalah: {luas}")
            
    case 3:
            a = int(input("Masukkan panjang alas segitiga:"))
            t = int(input("Masukkan panjang tinggi segitiga:"))
            luas = alas * tinggi / 2
            print(f"luas segitiga adalah: {luas}")
            
    case _:
        print("Masukkan pilihan dengan benar")
            