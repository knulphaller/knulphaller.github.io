<!-- 
.. title: Pythonda random modulu
.. slug: tsadfirandom-alqoritmlr-v-pythonda-random-modulu
.. date: 2014-09-02 12:35:54 UTC+05:00
.. tags: Python, Modullar
.. link: 
.. description: 
.. type: text
-->
Təsadüfi(random) alqoritmlər və Pythonda random modulu

Çoxdandır Pythonda istifadə olunan random modulunun yaratdığı verilənlərin hansı alqoritmə uyğun olaraq istehsal olunduğu haqqında maraqlanmaq istəyirdim. Amma nə isə vaxt olmurdu. Blogumda da ilk olaraq nə yazım deyə düşünürdüm. Təsadüfən qərara gəldim ki bu mövzu haqqında yazım.
<!-- TEASER_END: Davamını oxu -->


Ümumiyyətlə fəlsəfədə və fizikada determinizim qanunları deyilən qanunlar var ki bizim istifadə etdiyimiz cihazlar bu qanunlara tabedir.
#####Alqoritmlər
Hal-hazırda kompyuterlərdə istifadə olunan alqoritmlər psevdorandom alqoritmlər adlanır. Psevdorandom alqoritm hansısa riyazi bir düstura tabe olan alqoritmlərdir.
Bizim dilə tərcümə etməyə çalışsaq nisbi təsadüfi alqoritmlər. Bu alqoritmlər çox qəliz bir riyazi məntiqlə yığılıb və "əsl" təsadüfiliyə yaxın rəqəmlər istehsal edə bilirlər.
Ümumiyyətlə bunu da deyim ki riyazi əməliyyatlardan istifadə edərək random alqoritmlər yığmaq mümkündür lakin bunu hal-hazırda istifadə etdiyimiz deterministik komyputerlərdə istifadə etmək mümkün deyil.
Random alqoritmləri psevdorandom alqoritmlərdən ayıran tək fərq var: psevdorandom alqoritmlərə periodiklik məxsusdur. Yəni ki bir müddətdən sonra özlərini təkrar edirlər.
Çünki generator sabit bir yaddaşdan istifadə edir, periodik olmasa onda sistem işlədikcə daha çox yaddaş istifadə etməyə başlayacaq. Və sonsuza qədər bunu etməyə çalışacaq ki, bizim istifadə etdiyimiz kompyuterlər sabit yaddaşa malikdirlər.

###Pythonda Random modulu
Pythonda random rəqəmlər yaratmaq üçün random adlı modul var. Bir çox proqramlaşdırma dilləri kimi python da psevdorandom məlumatlar yaratmaq üçün [Mersenne twister](http://en.wikipedia.org/wiki/Mersenne_twister) PRNG-dan istifadə edir.

Keçək random modulunun istifadəsinə. Random modulunun bir çox yararlı funksiyaları var aşağıda misallarla bu funksiyaların izahını verməyə cəhd edəcəm.


#####Randint Funksiyası ##
Əgər biz random rəqəmlər yaratmaq istəyiriksə ``randint`` funksiyasından istifadə edə bilərik. ``randint`` funksiyası iki parametr qəbul edə bilir: başlanğıc nöqtə və son nötə. məsələn əgər biz pythondan 1-dən 10-a qədər olan rəqəmlər arasından təsadüfi bir rəqəm seçməsini istəsək ``randint`` funksiyası ilə belə edə bilərik:

	import random
	random.randint(1,10)

####Choice funksiyası####

Verilən siyahıdan random elementlər seçmək üçün istifadə olunur. Məsələn:

	import random
	random.choice(['alma', 'armud', 'nar', 'heyva'])


və ya

	import random
	mylist=['kitab', 'dəftər', 'karandaş', 'qələm']
	random.choice(mylist)



####Shuffle funksiyası
Verilən siyahıdakı elementləri random şəkildə sıralayaraq bizə təqdim edir. [Fisher-Yates](http://en.wikipedia.org/wiki/Fisher%E2%80%93Yates_shuffle "Fisher-Yates shuffle") alqoritminə əsaslanır.``choice`` funksiyası verilən siyahıdan təsadüfi bir element seçib bizə təqdim edir lakin ``shuffle`` funksiyası isə tam siyahını təsadüfi şəkildə sıralayır. Məsələn:

	import random
	mylist=(['alma', 'armud', 'nar', 'heyva'])
	random.shuffle(mylist)
	print(mylist)
	#Məndə alınan nəticə:['armud', 'nar', 'alma', 'heyva'], təbiiki sizdə tam fərqli olacaq

və ya

	import random
	x = [[i] for i in range(10)]
	random.shuffle(x)
	print(x)
	#Məndə alınan nəticə:[[4], [5], [1], [3], [2], [8], [6], [7], [9], [0]]

####Random funksiyası

Default olaraq 0.0 və 1.0 arasında bir rəqəm seçir. Amma əgər siz böyük rəqəm almaq istəyirsinizsə belə edə bilərsiz:

	import random
	random.random()*6000



####Randrange funksiyası
``randrange`` funksiyası verilmiş aralıqdakı rəqəmlərdən təsadüfi olaraq bir rəqəm seçir. 3 parametr qəbul edir.
Start - başlanğıc nöqtəsi
Stop - Son nöqtə
Step - Addım. Verilmiş aralıqda neçə addımdan bir element seçmək üçün.
Bəli parametrlərindəki step məsələsi bir az qəliz məsələdi. Amma daha yaxşı anlamaq üçün ``range()`` funksiyasına baxmalıyıq. Çünki eyni prinsiplə işləyirlər.
Bu funksiyaya alternativ olaraq ``random.choice(range(start, stop, step)`` funsksiyasından istifadə edə bilərik.

Random modulunun bir çox funksiyaları var lakin geniş şəkildə istifadə olunan funksiyaları yuxarıdakılar idi. Bu modul haqqında daha ətraflı məlumat əldə etmək istəyirsinizsə [modulun öz dokumentasiyasına](https://docs.python.org/3.4/library/random.html "Random module documentation")  baxmağınızı məsləhət görürəm.

