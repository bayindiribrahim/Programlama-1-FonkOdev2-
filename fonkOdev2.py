while True:
    print('''
    1.Katma Değer Cirosu
    2.Müşterilerle Çalışma Süresi
    3.İşletme Karı
    4.Mobilya Şirketi(Ortalama Stok)
    5.Çıkış''')

    sec=int(input("Menüden seçtiğiniz işlem numarısını giriniz: "))

    if sec==1:
        def katmaDeger():
            topSatMik=int(input("Toplam satış miktarınızı giriniz: "))
            hamMaliyet=int(input("Hammadde maliyetinizi giriniz: "))
            bakOnaGid=int(input("Bakım onarım giderlerinizi giriniz: "))
            sevGid=int(input("Sevkiyat giderinizi giriniz: "))
            alinanHiz=int(input("Satın alınan hizmet giderlerinizi giriniz: "))
            global katDegCiro
            katDegCiro=topSatMik-(hamMaliyet+bakOnaGid+sevGid+alinanHiz)
        katmaDeger()

        if katDegCiro>=1000:
            print("İşletme katma değer cirosu yüksek.")
        elif 500<=katDegCiro<1000:
            print("İşletme katma değer cirosu normal.")
        else:
            print("İşletme katma değer cirosu düşük.")

    elif sec==2:
        sure16=170
        musteri16=50
        sure17=220
        musteri17=70

        def musCalisma16():
            global calismaSuresi16
            calismaSuresi16=sure16/musteri16
            print("2016 yılı müşterilerle çalışma süreniz:",calismaSuresi16)
        musCalisma16()
        def musCalisma17():
            global calismaSuresi17
            calismaSuresi17=sure17/musteri17
            print("2017 yılı müşterilerle çalışma süreniz:",calismaSuresi17)
        musCalisma17()
        def fark():
            yillarFark=calismaSuresi17-calismaSuresi16
            print("2017 ve 2016 yılları arasındaki müşterilerle çalışma süresi farkınız:",yillarFark)
        fark()

    elif sec==3:
        def ilk6gelir():
            yazGelir=int(input("Yazılım gelirinizi giriniz: "))
            finGelir=int(input("Finansman gelirinizi giriniz: "))
            urunGelir=int(input("Ürün satış gelirinizi giriniz: "))
            global i6gelir
            i6gelir=yazGelir+finGelir+urunGelir
            print("İlk 6 aylık gelir toplamınız",i6gelir,"TL")
        ilk6gelir()
        def ilk6gider():
            calMaas=int(input("Çalışan maaşlarının toplamını giriniz: "))
            kira=int(input("Kira giderlerinizi giriniz: "))
            bakMal=int(input("Bakım maliyetlerinizi giriniz: "))
            global i6gider
            i6gider=calMaas+kira+bakMal
            print("İlk 6 aylık gider toplamınız",i6gider,"TL")
        ilk6gider()
        def ilk6kar():
            global ilkKar
            ilkKar=i6gelir-i6gider
            print("İlk 6 aylık karınız:",ilkKar)
        ilk6kar()
        def son6gelir():
            yazGeliri=int(input("Yazılım gelirinizi giriniz: "))
            sponsor=int(input("Sponsorluk gelirinizi giriniz: "))
            eTic=int(input("E-ticaret gelirinizi giriniz: "))
            urSat=int(input("Ürün satış gelirinizi giriniz: "))
            global s6gelir
            s6gelir=yazGeliri+sponsor+eTic+urSat
            print("Son 6 aylık gelir toplamınız",s6gelir,"TL")
        son6gelir()
        def son6gider():
            calisanMaas=int(input("Çalışan maaşlarının toplamını giriniz: "))
            kiraa=int(input("Kira giderlerinizi giriniz: "))
            bakimMal=int(input("Bakım maliyetlerinizi giriniz: "))
            global s6gider
            s6gider=calisanMaas+kiraa+bakimMal
            print("Son 6 aylık gider toplamınız",s6gider,"TL")
        son6gider()
        def son6kar():
            global sonKar
            sonKar=s6gelir-s6gider
            print("Son 6 aylık karınız:",sonKar)
        son6kar()
        def kar():
            global karFark
            karFark=ilkKar-sonKar
            print("İlk 6 ay ve son 6 ay karlarınız arasındaki fark:",karFark)
        kar()

        if karFark>5000:
            print("İşletme çok karlı.")
        elif 1000<=karFark<5000:
            print("İşletme karı normal.")
        else:
            print("İşletme yeterince karda değil.")

    elif sec==4:
        def dBasiStok(koltuk,yatak,dolap):
            global basKoltuk
            basKoltuk=koltuk
            global basYatak
            basYatak=yatak
            global basDolap
            basDolap=dolap
            global ilkToplam
            ilkToplam=basKoltuk+basYatak+basDolap
            print("Dönembaşı stok toplamınız:",ilkToplam)
        dBasiStok(50,50,50)
        def dSonuStok():
            global sonKoltuk
            sonKoltuk=basKoltuk-25+10
            global sonYatak
            sonYatak=basYatak-20+15
            global sonDolap
            sonDolap=basDolap-10+5
            global sonToplam
            sonToplam=sonKoltuk+sonYatak+sonDolap
            print("Dönemsonu stok toplamınız:",sonToplam)
        dSonuStok()
        def ortStok():
            ortalama=(ilkToplam+sonToplam)/2
            print("1 senelik ortalama stok miktarınız:",ortalama)
        ortStok()

    elif sec==5:
        break

    else:
        print("Hatalı giriş yaptınız lütfen tekrar deneyiniz.")
