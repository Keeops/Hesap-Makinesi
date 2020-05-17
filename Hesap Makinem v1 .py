def topla(sayi1, sayi2):
    return sayi1 + sayi2


def cikar(sayi1, sayi2):
    return sayi1 - sayi2


def carp(sayi1, sayi2):
    return sayi1 * sayi2


def bol(sayi1, sayi2):
    return sayi1 / sayi2


def kuvvetal(sayi1, sayi2):
    return sayi1 ** sayi2


def kokal(sayi1):
    return sayi1 ** 0.5


p = """{} İşleminden Çıkmak İçin Bir Boşluk Bırakıp Enter ı Tuşlayınız.
{} İşlemine Devam Etmek İçin Enter ı Tuşlayınız
>>>>"""

intro = """ 
(1) : Toplama İşlemi
(2) : Çıkarma İşlemi
(3) : Çarpma İşlemi
(4) : Bölme İşlemi
(5) : Kuvvet İşlemi
(6) : Karekök Hesaplama
(0) : Kapat
"""

while True:
    print("-" * 30)
    print(" " * 7, "Hesap Makinesi")
    print("-" * 30)
    print(" " * 9, "Made By Keops")
    print("-" * 30)

    print(intro)
    a = input("Yapmak İstediğiniz İşlemin Numarasını Giriniz: ")
    while a == "1":
        toplanacaklar = []
        while True:

            print("İşlemi Bitirmek İçin Enter'a Basabilirsiniz")
            b = input("Sayıyı Giriniz: ")
            if b == "":
                break
            toplanacaklar.append(int(b))

        while len(toplanacaklar) > 1:
            c = topla(toplanacaklar[0], toplanacaklar[1])
            del toplanacaklar[1]
            toplanacaklar[0] = c
        if len(toplanacaklar) == 0:
            break
        if len(toplanacaklar) == 1:

            c = toplanacaklar[0]
            print("Sonuç:", c)
            toplanacaklar = []

            d = input(p.format("Toplama", "Toplama"))

            if d == " ":
                break
            elif d == "":
                pass

    while a == "2":
        print("Çıkarma İşlemini Bitirmek İçin Enter'a Basabilirsiniz")
        b = input("Sayıyı Giriniz: ")
        if b == "":
            break
        c = input("Kaç Çıkaracaksınız?: ")

        d = cikar(float(b), float(c))
        print("Sonuç: ", d)

        e = input(p.format("Çıkarma", "Çıkarma"))

        if e == " ":
            break
        elif e == "":
            pass

    while a == "3":
        carpilacaklar = []

        while True:
            print("İşlemi Bitirmek İçin Enter'a Basabilirsiniz")
            b = input("Sayıyı Giriniz: ")

            if b == "":
                break

            carpilacaklar.append(float(b))

        while len(carpilacaklar) > 1:
            b = carp(carpilacaklar[0], carpilacaklar[1])

            del carpilacaklar[1]
            carpilacaklar[0] = b

        print("Sonuç: ", b)

        e = input(p.format("Çarpma", "Çarpma"))

        if e == " ":
            break
        elif e == "":
            pass

    while a == "4":
        print("İşlemi Bitirmek İçin Enter'a Basabilirsiniz")
        b = float(input("Bölüneni Giriniz: "))
        if b == "":
            break

        print("İşlemi Bitirmek İçin Enter'a Basabilirsiniz")
        c = float(input("Böleni Giriniz: "))
        if c == "":
            break

        d = bol(b, c)
        if b % c == 0:
            print(int(d))
        else:
            print(d)

        e = input(p.format("Bölme", "Bölme"))

        if e == " ":
            break
        elif e == "":
            pass

    while a == "5":
        print("İşlemi Bitirmek İçin Enter'a Basabilirsiniz")
        b = input("Tabanı Giriniz: ")

        if b == "":
            break

        print("İşlemi Bitirmek İçin Enter'a Basabilirsiniz")
        c = input("Kuvvetini Giriniz: ")

        if c == "":
            break

        b = float(b)
        c = float(c)
        print(kuvvetal(b, c))

        e = input(p.format("Karekök Alma", "Karekök Alma"))

        if e == " ":
            break
        elif e == "":
            pass

    while a == "6":
        print("İşlemi Bitirmek İçin Enter'a Basabilirsiniz")
        b = input("Karekökünü Almak İstediğiniz Sayıyı Giriniz: ")

        if b == "":
            break

        else:
            b = float(b)

        if b < 0.0:
            print("Karekökün İçerisi Negatif(-) Olamaz. ")

        else:
            print(kokal(b))

        e = input(p.format("Karekök Alma", "Karekök Alma"))

        if e == " ":
            break
        elif e == "":
            pass
    if a == "0":
        break