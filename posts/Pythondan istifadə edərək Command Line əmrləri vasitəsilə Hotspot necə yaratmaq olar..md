<!-- 
.. title: Python, cmd və Hotspot. Pythonla Wifi Hotspot yaradaq.
.. slug: Pythondan istifadə edərək Command Line əmrləri vasitəsilə Hotspot necə yaratmaq olar.
.. date: 2014-09-06 01:36:29 UTC+05:00
.. tags: Python
.. link: 
.. description: 
.. type: text
-->
Python, cmd və Hotspot. Pythonla Wifi Hotspot yaradaq.

Kompyuterdə olan internetin digər cihazlara kompyuterin wifi adapteri ilə paylanmasına el arasında HotSpot deyirlər. Əgər siz wifi modemdən istifadə edirsinizsə təbiiki artıq buna ehtiyacınız qalmır. Amma mobil modemlərdən istifadə edənlər(elə biri də mən) gec tez belə bir metoda baş vururlar. Gəlin bir də bunu pythonla edək.

<!-- TEASER_END: Davamını oxu -->


Kompyuterdə olan internetin digər cihazlara kompyuterin wifi adapteri ilə paylanmasına el arasında HotSpot deyirlər. Əgər siz wifi modemdən istifadə edirsinizsə təbiiki artıq buna ehtiyacınız qalmır. Amma mobil modemlərdən istifadə edənlər(elə biri də mən) gec tez belə bir metoda baş vururlar. Mən də adətən bu metodlardan istifadə edirəm. Belə şəbəkəni paylamaq üçün bir çox programlar mövcuddur. Bu programlara misal olaraq Wifi Hotspot, Connectify, Maryfi kimi programları göstərə bilərik. Elə yaxın zamana qədər mən də bu programlardan istifadə edirdim. Lakin dəyişməyən şey bu programlarda çıxan problemlər olurdu. Adətən məndə bu programlar tez-tez donur, çox yaddaş yeyir ip confiqurasiyalara barmaq edir və s bir çox belə kiçik məsələlər ilə başımı ağrıdırdılar. Bir dostumun da mənə bu məsələdə şikayət etməsi məni vadar elədi ki bu məsələyə bir az ciddi yanaşım. Deməli belə, bu məsələdə demək olar ki mən bütün yollara baş vurdum. Ən effektiv həll yolu isə şəbəkəni elə Command Line-dan istifadə edərək yaratmaqdı qərarına gəldim. Lakin hər dəfə Kompyuteri açdıqdan sonra cmd-ni açıb əllə əmrlər yazmaq da bir az bezdirici idi. Axır ki məsələyə Pythonu da qatdım və məsələni kökündən həll elədim. Əvvəla bunu deyim ki, cmd ilə şəbəkəni paylamaq üçün aşağıdakı əmrlərdən istifadə edirdim:

	netsh wlan set hostednetwork mode=allow ssid=name key=password # Parolu və şəbəkənin görünən adını təyin etmək üçün.
	
	netsh wlan start hostednetwork #şəbəkəni işə salmaq üçün.
Hər dəfə bu əmrləri cmd-də yazmaq əvəzinə bu prosesi pythonla avtomatlaşdırdım. Dostum da istifadə edə bilsin deyə Tkinter vasitəsilə Gui də yığdım.
Bir az kobud oldu amma əsas odur ki işləyir :)

    #coding = utf-8
	#Wifi Hotspot Creator
	from tkinter import *
	import subprocess

	window = Tk()
	window.title('WIFI Hotspot Creator')
	window.resizable(False, False)

	ssid = Label(text="Wifi adı: ")
	ssid.grid(row=0, column=0, sticky="w")
	pasword = Label(text="Parol: ")
	pasword.grid(row=1, column=0, sticky="w")
	def wifi():
		ssid = entry.get()
    	parol = entry1.get()
    	subprocess.call('netsh wlan set hostednetwork mode=allow ssid={0} key={1}' .format(ssid, parol), shell=True)
    	subprocess.call('netsh wlan start hostednetwork', shell=True)
	entry = Entry()
	entry.grid(row=0, column=1, padx=10)
	entry1 = Entry(show='*')
	entry1.grid(row=1, column=1, padx=10)
	button = Button(text="Start", command=wifi)
	button.grid(padx=10, pady=10)
	def stop():
    	subprocess.call('netsh wlan stop hostednetwork', shell=True)
	button1 = Button(text='Stop', command=stop)
	button1.grid( row=2, column=2, padx = 10, pady = 10)

	mainloop()


[Programı yüklə](https://cloud.mail.ru/public/5bf036a3f713/Hotspot.zip)

İstifadə qaydası:

![Imgur](http://i.imgur.com/fP4HHlv.jpg?1)

Demək mən burda neynədim: demək olar ki heçnə. Sadəcə pythonun ``subprocess`` modulundan istifadə edərək  cmd əmrlərini yerinə yetirdim.
 Amma özünüzün əllə bir dəfə etməli olduğunuz bir şey var. Paylayacağınız connetionun Sharing parametrlərini tənzimləmək. Belə edə bilərsiniz:
Daxil olursunuz: Control Panel >> Network and Internet >> Network Connections bölməsinə(rusca: Панель управления>>Сеть и Интернет>>Сетевые подключения).

![connections](http://www.maryfi.com/images/all-connections.gif)

Şəkildə göründüyü kimi paylaşacağınız connectionu seçirsiniz:

![Propeties](http://www.maryfi.com/images/sharing-connection.gif)
Sonra:

![Sharing](http://www.maryfi.com/images/properties-window.gif)

Hansı connectionla paylaşacağınızı seçirsiniz:
Böyük ehtimalla bu sizdə Wireless Network Connection 2 olacaq(Microsoft Virtual WiFi Miniport Adapter)(rusca:Беспроводное сетевое соединение 2).

Settings bölməsinə daxil olursunuz.

![Go to Settings!](http://www.maryfi.com/images/choose-maryfi-connection.gif)

Aşağıdakı şəkildə göstərilənlərə quş qoyursuz. Daha doğrusu şəkildə hansılarda quş varsa siz də onu quşduyun:D

![Quşduyun :D](http://www.maryfi.com/images/services-to-share.gif)

Hər şeyə OK vurun. Və yüklədiyiniz zip faylını extract edin və bbc.exe faylını açın və istifadə edin.
Bu arada, bütün adapterlər dəstəklənmir. Dəstəklənən adapterlərin siyahısı:


- Atheros AR5xxx/AR9xxx cards, driver version 8.0.0.238
- Broadcom 4310-series (in many Dell laptops)
- Broadcom 4321AG/4322AG/43224AG WLAN Adapter, driver version 5.60.18.8
- D-link AirPlus G DWL-G510 Wireless PCI Adapter, driver version 3.0.1.0
- D-Link DWA-140 Range Booster N USB Adapter, driver version 3.0.3.0
- Dell 1510 Wireless N adapter, Broadcom  version, driver 5.60.18.8,
- Intel 5100/5300, WiFi Link 1000 BGN, driver version 13.0.0.107
- Linksys Dual-Band Wireless-N USB Network Adapter(WUSB600N), driver version 3.0.10.0
- Netgear 108 Mbit WG311T
- Ralink RT2870 (in many 802.11n USB dongles)
- Realtek RTL8187B (Win7 driver ver.1178)
- Realtek RTL8187SE (with the drivers that came with Windows 7)
- Realtek RTL8192u with 1370(Beta)
- Sitecom Wireless USB Adapter 54g WL-608, with Ralink RT2870 drivers, version 3.0.9.0

Bu da son. Uğurlar. 