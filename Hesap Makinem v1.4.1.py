def topla(sayi1,sayi2):
    return sayi1+sayi2

def cikar(sayi1,sayi2):
    return sayi1-sayi2

def carp(sayi1,sayi2):
    return sayi1*sayi2

def bol(sayi1,sayi2):
    return sayi1/sayi2

def kuvvetal(sayi1,sayi2):
    return sayi1**sayi2

def kokal(sayi1):
    return sayi1**0.5

def faktoriyelal(sayi1):
    if sayi1 < 0:
        print("Negatif Alamazsınız.")
    a=1
    for i in range(1,sayi1+1):
        a = i * a
    return a

def kombinasyonal(sayi1,sayi2):
    return faktoriyelal(sayi1) / (faktoriyelal(sayi2)*(faktoriyelal(sayi1-sayi2)))

def permutasyonal(sayi1,sayi2):
    return faktoriyelal(sayi1)/ (faktoriyelal(sayi1-sayi2))

def ekok(a,b):
    sonuc = 1
    bölen=2
    while True:
        if (a%bölen == 0 and b%bölen == 0):
            sonuc *= bölen
            a/=bölen
            b/=bölen
        elif (a%bölen == 0 and b%bölen != 0):
            sonuc *= bölen
            a/=bölen
        elif (a%bölen != 0 and b%bölen == 0 ):
            sonuc *= bölen
            b/=bölen
        else:
            bölen += 1
        if(a==1 and b==1):
            break 
    return sonuc

def ebob(a,b):
    sonuc=1
    bölen=2
    while True:
        if (a%bölen==0 and b%bölen==0):
            sonuc*=bölen
            a/=bölen
            b/=bölen
        elif (a%bölen==0 and b%bölen!=0):
            a/=bölen
        elif (a%bölen!=0 and b%bölen==0):
            b/=bölen
        else:
            bölen+=1
        if (a==1 and b==1):
            break
    return sonuc
def hipo(dik1,dik2):
    a=kokal(kuvvetal(dik1,2)+kuvvetal(dik2,2))
    return a
def sin(karsi,hipot):
    print(karsi/hipot)
def cos(komsu,hipot):
    print(komsu/hipot)
def tan(karsi,komsu):
    print(karsi/komsu)
def cot(komsu,karsi):
    print(komsu/karsi)

p="""{} İşleminden Çıkmak İçin Bir Boşluk Bırakıp Enter ı Tuşlayınız.
{} İşlemine Devam Etmek İçin Enter ı Tuşlayınız
>>>>"""

intro = """ 
(1) : Toplama İşlemi
(2) : Çıkarma İşlemi
(3) : Çarpma İşlemi
(4) : Bölme İşlemi
(5) : Kuvvet İşlemi
(6) : Karekök Hesaplama
(7) : Faktöriyel Hesaplama 
(8) : Kombinasyon Hesaplama
(9) : Permütasyon Hesaplama
(10): Ekok Hesaplama
(11): Ebob Hesaplama
(12): Trigonometri İşlemleri (Henüz Eklenmedi !!!)
(0) : Kapat
"""

while True:
    print("-"*30)
    print(" "*7,"Hesap Makinesi")
    print("-"*30)
    print(" "*7,"Made By Keops")
    print("-"*30)

    print(intro)
    a=input("Yapmak İstediğiniz İşlemin Numarasını Giriniz: ")
    while a == "1":
        toplanacaklar=[]   
        while True:

            print("İşlemi Bitirmek İçin Enter'a Basabilirsiniz")
            b = input("Sayıyı Giriniz: ")       
            if b == "":
                break
            toplanacaklar.append(int(b))
    
        while len(toplanacaklar)>1:
        
            c=topla(toplanacaklar[0],toplanacaklar[1])
            del toplanacaklar[1]
            toplanacaklar[0]=c
        if len(toplanacaklar)==0:
            break
        if len(toplanacaklar)==1:

            c=toplanacaklar[0]
            print("Sonuç:",c)
            toplanacaklar=[]
        
            d=input(p.format("Toplama","Toplama"))
            
            if d == " ":
                break
            elif d == "":
                pass

    while a == "2":
        print("Çıkarma İşlemini Bitirmek İçin Enter'a Basabilirsiniz")
        b=input("Sayıyı Giriniz: ")
        if b == "":
            break
        c=input("Kaç Çıkaracaksınız?: ")

        d=cikar(float(b),float(c))
        print("Sonuç: ",d)
    
        e=input(p.format("Çıkarma","Çıkarma"))
        
        if e == " ":
            break
        elif e == "":
            pass

    while a == "3":
        carpilacaklar=[]

        while True:
            print("İşlemi Bitirmek İçin Enter'a Basabilirsiniz")
            b=input("Sayıyı Giriniz: ")
       
            if b == "":
                break

            carpilacaklar.append(float(b))
    
        while len(carpilacaklar)>1:
            b=carp(carpilacaklar[0],carpilacaklar[1])
        
            del carpilacaklar[1]
            carpilacaklar[0]=b
   
        print("Sonuç: ",b)

        e=input(p.format("Çarpma","Çarpma"))
        
        if e == " ":
            break
        elif e == "":
            pass

    while a == "4":
        print("İşlemi Bitirmek İçin Enter'a Basabilirsiniz")
        b=float(input("Bölüneni Giriniz: "))
        if b == "":
            break

        print("İşlemi Bitirmek İçin Enter'a Basabilirsiniz")
        c=float(input("Böleni Giriniz: "))
        if c == "":
            break

        d = bol(b,c)
        if b%c == 0:
            print(int(d))
        else:
            print(d)
        
        e=input(p.format("Bölme","Bölme"))
        
        if e == " ":
            break
        elif e == "":
            pass

    while a == "5":
        print("İşlemi Bitirmek İçin Enter'a Basabilirsiniz")
        b=input("Tabanı Giriniz: ")
        
        if b == "":
            break
        
        print("İşlemi Bitirmek İçin Enter'a Basabilirsiniz")
        c=input("Kuvvetini Giriniz: ")
        
        if c == "":
            break

        b = float(b)
        c= float(c)
        print(kuvvetal(b,c))

        e=input(p.format("Karekök Alma","Karekök Alma"))
        
        if e == " ":
            break
        elif e == "":
            pass

    while a == "6":
        print("İşlemi Bitirmek İçin Enter'a Basabilirsiniz")
        b=input("Karekökünü Almak İstediğiniz Sayıyı Giriniz: ")
        
        if b == "":
            break

        else:
            b=float(b)
        
        if b<0.0:
            print("Karekökün İçerisi Negatif(-) Olamaz. ")
            
        else:
            print(kokal(b))
                
        
        e=input(p.format("Karekök Alma","Karekök Alma"))
        
        if e == " ":
            break
        elif e == "":
            pass
    
    while a =="7":
        print("İşlemi Bitirmek İçin Enter'a Basabilirsiniz.")
        s = input("Faktöriyelini Almak İstediğiniz Sayını Giriniz: ")

        if s == "":
            break
        else:
            s= int(s)
        
        sonuc = faktoriyelal(s)
        print("Sonuç: ",sonuc)

        d = input(p.format("Faktöriyel Alma","Faktöriyel Alma"))

        if d == " ":
            break
        
        elif d== "":
            pass
        
    while a == "8":
        print("İşlemi Bitirmek İçin Enter'a Basabilirsiniz.")
        b = input("Kombinasyonunu Almak İstediğiniz Sayıyı Giriniz: ")

        if b == "":
            break

        else:
            b = int(b)
        
        print("İşlemi Bitirmek İçin Enter'a Basabilirsiniz.")
        c = input("Kaçlı Kombinasyonunu Almak İstediğinizi Giriniz: ")

        if c=="":
            break

        else:
            c = int(c)

        print(kombinasyonal(b,c))

        e=input(p.format("Kombinasyon Alma","Kombinasyon Alma"))
        
        if e == " ":
            break
        elif e == "":
            pass
    
    while a == "9":
        print("İşlemi Bitirmek İçin Enter'a Basabilirsiniz.")
        b = input("Permütasyonunu Almak İstediğiniz Sayıyı Giriniz: ")

        if b == "":
            break

        else:
            b = int(b)
        
        print("İşlemi Bitirmek İçin Enter'a Basabilirsiniz.")
        c = input("Kaçlı Permütasyonunu Almak İstediğinizi Giriniz: ")

        if c=="":
            break

        else:
            c = int(c)

        print("Sonuç: ",permutasyonal(b,c))

        e=input(p.format("Permütasyon Alma","Permütasyon Alma"))
        
        if e == " ":
            break

        elif e == "":
            pass
    
    while a == "10":
        print("İşlemi Bitirmek İçin Enter'a Basabilirsiniz.")
        b = input("Ekokunu Almak İstediğiniz İlk Sayıyı Giriniz: ")

        if b == "":
            break

        else:
            b = int(b)
        
        print("İşlemi Bitirmek İçin Enter'a Basabilirsiniz.")
        c = input("Ekokunu Almak İstediğiniz İkinci Sayıyı Giriniz: ")

        if c=="":
            break

        else:
            c = int(c)
        
        print("Sonuç: ",ekok(b,c))

        d=input(p.format("Ekok Alma","Ekok Alma"))

        if d=="":
            pass

        elif d==" ":
            break
    
    while a == "11":
        print("İşlemi Bitirmek İçin Enter'a Basabilirsiniz.")
        b = input("Ebobunu Almak İstediğiniz İlk Sayıyı Giriniz: ")

        if b == "":
            break

        else:
            b = int(b)
        
        print("İşlemi Bitirmek İçin Enter'a Basabilirsiniz.")
        c = input("Ebobunu Almak İstediğiniz İkinci Sayıyı Giriniz: ")

        if c=="":
            break

        else:
            c = int(c)
        
        print("Sonuç: ",ebob(b,c))

        d=input(p.format("Ebob Alma","Ebob Alma"))

        if d=="":
            pass

        elif d==" ":
            break

    if a == "0":
        break