
kirmizi = "\u001b[31;1m"
yesil = "\u001b[32m"
sari = "\u001b[33;1m"
mavi ="\u001b[34;1m"









while True:
	print  (kirmizi + """
	===============
	1.sorular
	2. vize odevi
	3.final odevi
	===============
	""")

	tercih =int(input( "_______lutfen yapilacak islemi seciniz_______: "))


	if tercih == 1 :
	
		print(sari + """
			===============================================
			1. uc sayinin carpimini format ile ekrana basma
			2.index hesaplama
			3.km basina harcanan yakit hesabi
			4.kullanici bilgilerini ekrana yazma
			5.girilen degerlerin yer deisimi
			6.ucgen hipotenus hesabi
			================================================
			""")
			
		secim1 =int(input("_______lutfen islemi seciniz_______:"))

		if secim1== 1:
				a = float(input("lutfen birinci sayi degerini girin: "))

				b = float(input("lutfen ikinci sayi degerini girin: "))

				c = float(input("lutfen ucuncu sayi degerini girin: "))

				sayilarin_carpimi = a*b*c

				print("sayilarin_carpimi = {}").format(sayilarin_carpimi)
	
		elif secim1 ==2:
			
				kilo =float(input("lutfen kilonuzu giriniz: "))

				boy =float(input("lutfen boyunuzu giriniz: "))

				uzunluk = boy/100

				beden_index = (kilo/ (uzunluk*uzunluk))

				print("beden kitle index", beden_index)

		elif secim1 == 3:
			
				print ("araclarin km basina yaktigi deger degisebildigi icin kilometre basina gore yakilan benzin hesaplanmistir")


				alinan_yakit_fiyati = float(input("alinan yakitin fiyatini girin:"   ))

				alinan_yol = float(input("lutfen gidilen yolu yaziniz:"  ))

				km_basina_yakilan_benzin = (alinan_yakit_fiyati) / (alinan_yol)


				print("aracin km basina yaktigi yakit :",km_basina_yakilan_benzin,"tl")

		elif secim1 == 4:
		
				ad = input (" adinizi giriniz: ")

				soyad = input (" soyadinizi giriniz: ")

				numara = input ("telefon numarasini giriniz: ")

				print( "kisinin adi: {}\nkisinin soyadi {}\nkisinin numarasi {}" .format(ad,soyad,numara))


		elif secim1 == 5:
				a = float(input("birinci sayiyi gir: "))

				b = float(input("ikinci sayiyi gir: "))

				print("yeri deisecek sayilar",a,b)


				hafiza  = a

				a = b

				b = hafiza

				print("yer deisme sonucu = ", a,b)

		else:
		
				import math
				a = float(input("lutfen ucgenin dik kenarini giriniz:"))

 
				b = float(input("lutfen ucgenin diger kenarini giriniz:"))

				hipotenus = math.sqrt(a**2 + b**2)

				print ("hipotenusun degeri:",hipotenus)
 










	elif tercih ==2 :
	
		print(sari + """
		=========================================
		1.kare cevre ve alan hesabi                               
		2.dikdortgen cevre ve alan hesabi
		3.eskenar ucgen cevre ve alan hesabi
		4.daire
		5.kup
		6.dikdortgenler prizmasi
		7.kure
		8.silindir
		9.koni
		10.piramit
		=========================================
		""")



		import math
		pi=3.14
		secim =int(input("_______lutfen islemi seciniz_______: "))
	
		if secim == 1:
			
				kenar_uzunlugu = float(input('karenin bir kenari: '))

				cevre = kenar_uzunlugu* kenar_uzunlugu * kenar_uzunlugu *kenar_uzunlugu 

				alan = kenar_uzunlugu*kenar_uzunlugu

				print("cevreniz: ", cevre)

				print("alan: ", alan)

	
		elif secim == 2:
	
				kisa_kenar = float(input('dikdortgenin kisa kenari: '))
	
				uzun_kenar = float(input('dikdortgenin uzun kenari: '))
	
				cevre = 2*(kisa_kenar + uzun_kenar)
				alan = kisa_kenar * uzun_kenar
	
				print ("dikdortgenin cevresi = ",cevre)
	
				print("dikdortgenin alani = ",alan)      



		elif secim == 3:
		
	
			print (mavi + """
			++++++++++++++++++++++++++++		
			1.dik ucgen hesabi
			2.eskenar ucgen hesabi
			3.ikizkenar ucgen hesabi
			++++++++++++++++++++++++++++		
			""")

			islem=int(input("_______lutfen ucgen turunu seciniz_______:"))
	
			if islem ==1:
					ucgen_kenari_bir =float(input("birinci kenari giriniz:"))
			
					ucgen_kenari_iki =float(input("ikinci kenari giriniz:"))	

					ucgen_kenari_uc  =float(input("ucuncu kenari giriniz:"))

					dik_ucgen_alan = (ucgen_kenari_bir * ucgen_kenari_iki)/2

					dik_ucgen_cevre =(ucgen_kenari_bir + ucgen_kenari_iki + ucgen_kenari_uc)

					print("dik ucgenin alani =",dik_ucgen_alan)
					print("dik ucgenin cevresi =",dik_ucgen_cevre)

			elif islem ==2:	
	 
					ucgen_kenari =float(input("birinci kenari giriniz:")) 
				
					eskenar_ucgen_cevre = (ucgen_kenari * ucgen_kenari * ucgen_kenari)

					eskenar_ucgen_alan = (ucgen_kenari *ucgen_kenari) * (math.sqrt(3)/4)

					print("eskenar ucgenin cevresi :", eskenar_ucgen_cevre)
					print("eskenar ucgenin alani :", eskenar_ucgen_alan)
	

			elif islem ==3:
					ucgen_kenar_bir = float(input("birinci kenari giriniz:"))
					ucgen_kenar_iki = float(input("ikinci kenari giriniz:"))
					ucgen_kenar_uc = float(input("ucuncu kenari giriniz: "))
			
					s=(ucgen_kenar_bir + ucgen_kenar_iki + ucgen_kenar_uc)/2 
			
					ikizkenar_ucgen_cevre = (ucgen_kenar_bir +ucgen_kenar_iki + ucgen_kenar_uc)
					ikizkenar_ucgen_alan =  (math.sqrt((s * (s-ucgen_kenar_bir) * (s-ucgen_kenar_iki) * (s-ucgen_kenar_uc))))

					print("ikizkenar ucgenin cevresi :", ikizkenar_ucgen_cevre)
					print ("ikizkenar ucgenin alani :", ikizkenar_ucgen_alan)	

			else :
					print("boyle bir girdi yoktur")

		elif secim == 4:
			yaricap =float(input('dairenin yaricapi giriniz:'))
	
			cevre = 2*pi*yaricap
			alan = pi*(yaricap**2)
	
			print ("dairenin cevresi =",cevre)
			print ("dairenin alani =",alan)	

		elif secim == 5:
	
			kupun_kenari =float(input('kupun kenar uzunlugunu giriniz:'))
	
			yuzey_alani = 6*(kupun_kenari**2)
			hacim = kupun_kenari*kupun_kenari*kupun_kenari
	
			print ("kupun yuzey alani =",yuzey_alani)
			print ("kupun hacimi =",hacim)
		

		elif secim == 6:
		
			dikdortgenin_uzun_kenari =float(input('dikdortgenin uzun kenarini giriniz :'))
	
			dikdortgenin_kisa_kenari =float(input('dikdortgenin kisa kenarini giriniz :'))
	
			dikdortgenin_yuksek_kenari =float(input('dikdortgenin yuksekligini giriniz :'))

			yuzey_alani = 2*((dikdortgenin_uzun_kenari * dikdortgenin_kisa_kenari) +(dikdortgenin_kisa_kenari * dikdortgenin_yuksek_kenari)+(dikdortgenin_uzun_kenari*dikdortgenin_yuksek_kenari))
	
			hacim = dikdortgenin_uzun_kenari * dikdortgenin_kisa_kenari * dikdortgenin_yuksek_kenari
	
			print ("dikdortgenin yuzey alani =",yuzey_alani)
	
			print ("dikdortgenin hacimi =", hacim)

		elif secim ==7:
	
			yaricap = float(input("kurenin yaricapini giriniz :"))
	
			yuzey_alani = 4*pi*(yaricap**2)
			hacim =1.33*pi*(yaricap**3)
	
			print ("kurenin yuzey alani =",yuzey_alani)
	
			print ("kurenin hacimi =",hacim)




		elif secim == 8:
	
			yukseklik = float(input('silindirin yuksekligi: '))

			yaricap = float(input('silindirin yaricapini giriniz: '))
  
			hacim  = pi * yaricap * yaricap * yukseklik

			yuzey_alani = ((2*pi*yaricap) * yukseklik) + ((pi*yaricap**2)*2)

			print("silindirin hacimi: ", hacim)

			print("silindirin yuzey alani: ", yuzey_alani)
	
		elif secim ==9:
	
			yukseklik = float(input('koninin yuksekligini giriniz:'))
			yaricap = float(input('koninin yaricapini giriniz:'))
	
	
	
			hacim = 0.33*pi*((yaricap**2)*yukseklik)
	
			alan = (pi*yaricap)*(yaricap*(math.sqrt((yaricap**2) +(yukseklik**2))))
	
			print ("koninin hacimi:",hacim)
	
			print ("koninin alani :",alan)

		elif secim == 10:
		
			piramidin_birinci_kenari = float(input('piramidin birinci kenarini giriniz:'))

			piramidin_ikinci_kenari = float(input('piramidin ikinci kenarini giriniz:'))
	
			piramidin_yuksekligi = float(input('yuksekligi giriniz:'))

			hacim = 0.33 * (piramidin_birinci_kenari* piramidin_ikinci_kenari * piramidin_yuksekligi)

			alan = piramidin_birinci_kenari*(piramidin_birinci_kenari*(math.sqrt((piramidin_birinci_kenari**2)+(4*(piramidin_yuksekligi**2)))))

			print ("piramidin hacimi =",hacim)

			print ("piramidin alani =",alan)

		else:
			print ("boyle bir hesaplama yoktur")




	elif tercih==3:
		
		print(kirmizi+"""
				=======
				1.odev3
				2.odev4
				=======
				""")
		tercih2= input("___yapilacak islemi secin___:")
		
		if tercih2==1:
			
			print(sari +"""
					1.kitle-index hesabi v2
					2.buyuk sayi hesabi
					3.ogrenci not hesaplama
					4.geometrik hesap v2
					""")
		
			tercih4 =input("islemi seciniz:")
			
			if tercih4 ==1:
				print(yesil + """
							==================
							KITLE/INDEX HESABI
							==================""")

				kilo =int(float(input(kirmizi + "lutfen kilonuzu giriniz: ")))

				boy = int(float(input(kirmizi + "lutfen boyunuzu giriniz: ")))

				uzunluk = boy/100

				beden_kitle_index = (kilo/(uzunluk*uzunluk))

				print (sari + "index durumu",beden_kitle_index)

				if beden_kitle_index <18.50 :
					print(mavi + "zayifsin")

				elif beden_kitle_index >=18.50 and beden_kitle_index <25 :
					print(mavi + "normal")

				elif beden_kitle_index >=25 and beden_kitle_index<30 :
					print(mavi + "fazla kilolusunuz")

				else:
					print(mavi + "obezsin")
			
			
			
			
			elif tercih4==2:
				
				print(mavi + """

							============================
							EN BUYUK SAYI DEGERINI BULMA
							============================""")





				sayi1 = int(float(input(kirmizi + "lutfen birinci degeri giriniz:")))


				sayi2 = int(float(input(kirmizi + "lutfen ikinci degeri giriniz:")))


				sayi3 = int(float(input(kirmizi + "lutfen ucuncu degeri giriniz: ")))



				if (sayi1>sayi2 and sayi1>sayi3) :
	
					print(mavi + "en buyuk sayi:",sayi1)

				elif (sayi2>sayi1 and sayi2>sayi3):
	
					print(mavi + "en buyuk sayi:",sayi2)

				else:
					print(mavi + "en buyuk sayi:", sayi3) 
			
	

			elif tercih4 ==3:
				
				print(yesil + """
								*********************************
									OGRENCI NOT HESAPLAMA
								*********************************
								""")


				vize1 = int(float(input(kirmizi +"lutfen vizenin birinci notunu giriniz:")))


				vize2 = int(float(input(kirmizi + "lutfen vizenin ikinci notunu giriniz: ")))

				final = int(float(input(kirmizi + "lutfen final notunu giriniz: ")))

				a = float((vize1*30)/100) #vizenin %30 unu hesaplar


				b = float((vize2*30)/100) #ikinci vizenin %30 unu hesaplar.


				c = float((final*40)/100) #finalin %40 ini hesaplar.

				print (mavi + "birinci vizenin %30'u :", a)
				print(mavi + "ikinci vizenin %30'u :",b)

				print(mavi + "finalin %40'i :",c)

				notlarin_toplami = a+b+c

				print(sari + "not durumu: ",notlarin_toplami)

				if notlarin_toplami >= 90 and notlarin_toplami<=100:
					print(mavi + "Not Durumu:",'AA')


				elif notlarin_toplami >= 85 and notlarin_toplami <90:
					print(mavi + "Not Durummu:",'BA')


				elif notlarin_toplami >= 80 and notlarin_toplami < 85:
					print(mavi + "Not Durumu:",'BB')

				elif notlarin_toplami >= 75 and  notlarin_toplami< 80:
					print(mavi + "Not Durumu:",'CB')
	
				elif notlarin_toplami >= 70 and notlarin_toplami < 75:
					print(mavi + "Not Durumu:",'CC')

				elif notlarin_toplami >= 65 and notlarin_toplami < 70:
					print(mavi + "Not Durumu: ",'DC')

				elif notlarin_toplami >= 60 and notlarin_toplami < 65:
					print(mavi + "Not Durumu:",'DD')


				elif notlarin_toplami >= 55 and notlarin_toplami <60 :
					print(mavi + "Not Durumu: ",'FD')

				else :
					print(mavi + "Not Durumu: ",'FF')
			
			elif tercih4 == 4:
				print(sari + """
							==============================
								GEOMETRIK HESAP
							==============================	
													""")



				print(yesil + """
	
					1.ucgen hesabi
					2.dortgen hesabi
	
							""")


				secim = int (input(kirmizi + "lutfen isleminizi seciniz: "))


				if secim == 1 :
					k1 = int(float(input(mavi + "lutfen birinci kenari giriniz:")))

					k2= int(float(input(mavi + "lutfen ikinci kenari giriniz:")))

					k3= int(float(input(mavi + "lutfen ucuncu kenari giriniz:")))
	
		
					if abs(k2+k1)>k3 and  abs(k2+k3)>k1 and abs(k3+k1)>k2:
		
						if(k2==k1 and k2==k3):
							print(kirmizi + "eskenar ucgen belirtir")
	
		
						elif(k2==k1 and k2!=k3 ) :

							print(kirmizi + "ikizkenar ucgen belirtir")

	

						else:
							print(kirmizi +  "cesitkenar ucgen belirtir")
					else:
						print(kirmizi + "girilen degerler ucgen belirtmez")


				elif secim == 2:

					kenar1 = int(float(input(kirmizi + "birinci kenari girin:")))

					kenar2 = int(float(input(kirmizi + "ikinci kenari girin:")))

					kenar3 = int(float(input(kirmizi + "ucuncu kenari girin:")))

					kenar4 = int(float(input(kirmizi + "dorduncu kenari girin:")))

					if  (kenar1==kenar2 and kenar2==kenar3) :
		
						print(mavi + "kare belirtir")

					elif(kenar1==kenar2 and kenar3==kenar4 or kenar2 == kenar3 and kenar1==kenar4  ):

						print(mavi + "dikdortgen belirtir")

	
		
					else:
						print(mavi + "herhangi bir dortgen olabilir")


		elif tercih2== 2:
			print(kirmizi +"""
			=======================================================			
			1.Mukemmel sayi hesabi
			2.Armstrong sayi hesabi
			3.Carpim tablosu
			4.Sonsuz dongulu toplama	
			5.1'den 100' kadar olan sayilarin 3 katini ekrana yazma
			6.Cift sayilari listeye ekleme islemi
			=======================================================
			""")
			tercih5 = int(input("lutfen islemi seciniz:"))
			
			if tercih5 == 1:
					
				print(kirmizi + """
				====================
				MUKEMMEL SAYI HESABI
				====================""")
				deger = int(input(sari + "lutfen degeri girin:"))

				bolenler =list()

				toplam =0

				for hafiza in range(1,deger):
					if deger % hafiza == 0:
							bolenler.append(hafiza)

				for hafiza1 in bolenler:
					toplam += hafiza1
		
					if deger ==toplam :
						print(mavi + "girilen deger mukemmel sayidir")
	
					else:
						print("boyle bir islem yoktur!")
						

			
			elif tercih5 ==2:
					
				print(sari + """

				========================
				ARMSTRONG SAYI BELIRTME
				========================""")


				armstrong_degeri = int(input(kirmizi + "_______sayi degerini girin_______:"))                         #kullanicidan armstrong adi altinda deger alindi

				basamak_degeri = str(armstrong_degeri)                                       #basamak_degeri adinda bir degisken yaratildi ve kullanicidan alinan sayi stringe cevrildi

				basamak = len(basamak_degeri)                                              #basamak diye ikinci bir degisken olusturuldu ve basamak_degerindeki stringin uzunlugu alindi

				deger =list()                                                             #deger adinda bir liste olusturuldu

				deger.append(basamak)                                                    # deger listesinin icine basamak yani basamak degerinin uzunlugu yazdirildi 


																#print ile deger ekrana bastirildi


				if  deger == [3]:                                                    #eger deger 3 e esit ise fonksiyon acip icindeki islemin yapilmasi istendi

					deger1  = armstrong_degeri //100
					deger2  = (armstrong_degeri - deger1*100)//10
					deger3  = (armstrong_degeri - deger1*100 - deger2*10)
		
					hesaplama = (deger1**3) + (deger2**3) + (deger3**3)
		
					if hesaplama == armstrong_degeri:
				
						print(sari + "girilen deger armstrong sayisidir")
			
					else:
						print(sari + "girilen deger armstrong sayisi degilir!")

				elif deger ==[4]:
		
					deger1  = armstrong_degeri /1000				
					deger2 = (armstrong_degeri - deger1*1000)/100
					deger3  = (armstrong_degeri - deger1*1000 - deger2*100)/10
					deger4 = (armstrong_degeri - deger1*1000 - deger2*100 - deger3*10)
		
					hesaplama2 =(deger1**4) +(deger2**4)+(deger3**4)+(deger4**4)
		
					if hesaplama2 == armstrong_degeri :
			
						print(sari + "girilen deger bir armstrong sayiyisi belirtir")
			
					else:
						print(sari + "girilen deger bir armstrong sayisi belirtmez!")
			

				else:
					print(sari + "lutfen 3 veya 4 basamakli bir sayi giriniz!!")


			elif tercih5 ==3:
				
				print(mavi + """
					===============
					CARPIM TABLOSU
					===============""")
				for a in range(1,11):
	
					for b in range(1,11):
		
						print(a,"*",b, ":",a*b)


			elif tercih5 == 4:
				
				print(mavi +"""
					======================
					sonsuz dongulu toplama
					======================""")
				kullanicinin_girdigi_degerler = list()

				toplam = 0

				while True:

					kullanici_girdisi = int(input(mavi + "LUTFEN DEGER GIRIN  CIKMAK ICIN (0) TUSUNA BASIN:"))

					kullanicinin_girdigi_degerler.append(kullanici_girdisi)

					if  (kullanici_girdisi ==int("q")):

						print(sari + "Girdiginiz degerler: ", kullanicinin_girdigi_degerler)

						print(sari + "degerlerin toplami:", toplam)

						break


					elif (kullanici_girdisi > 0):
						toplam += (kullanici_girdisi)

					else:
						print("deger yok")


			elif tercih5 == 5:
				print(mavi + """
				======================================================

				1'den 100'e kadar olan sayilarin 3 katini ekrana yazma
				======================================================""")

				for deger in range(1,100):
					if (deger % 3 !=0):
						continue
					else:
						print (deger)
		

			elif tercih5 == 6:
				
				print(yesil + """
						============================
						CIFT SAYILARI LISTEYE EKLEME
						============================""")
				cift_sayilar=list()
				for hafiza in range(1,100):
	
					if hafiza % 2 == 0:
		
						cift_sayilar.append(hafiza)
		
				print (cift_sayilar)
	
	else:
		print("boyle bir islem yoktur!!")




















