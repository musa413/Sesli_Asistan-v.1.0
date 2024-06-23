import speech_recognition as sr #çevrimiçi ve çevrim dışı bir şekilde çalışan konuşma tanıma kütüphanesi
from datetime import datetime #anlık zamanı öğrenmek için
import webbrowser # web browser açmak için
import time #bilgisayrı uyutmak için
from gtts import gTTS #text i ses e çevirmek için
from playsound import playsound#ses dosyasını çalmak için
import random#random bir sayı üretmek için
from random import choice#random bir değer seçmek için
import os#sistem ayarları değiştirmk için
from lxml import html#html dosyasını okumak için
import requests #istek göndermek için
import numpy as np
import cv2
import json # json dosyalarını okumak için
import feedparser #hava  durumunu çekmek için
import colorama #terminal ekranını özelleştirmek için
from colorama import Fore, Back, Style #Gerekli dosya ve sabitleri projemize dahil ettiğimize göre kullanım için gerekli init() fonksiyonunun çağırılması için.
import psutil
r=sr.Recognizer()#speech recognition ile alınan sesi r adlı değikene atıyoruz
colorama.init()
import pywhatkit


def record(ask = False):#record adlı bir fonksiyon oluşturuyoruz ve varsayılan olarak ask =false olarak ayarlıyouz
    with sr.Microphone() as source: #mikrofandan gelen veriyi işlem yapabilmek için source e tanımlıyoruz
        if ask:
            speak(ask)
            print(Fore.BLUE)
            print(ask)

        audio = r.listen(source) # dinlenilen source u audio ya atıyoruz
        voice = ''
        try:#
            voice = r.recognize_google(audio,language='tr-TR').lower()#Türkçe dinleme yapıp bunu voice e atıyoruz
        except sr.UnknownValueError:#gelen sesi tanımlayamazsa burası çalışıyor
            
            print(Fore.GREEN)
            print("Jarvis  = ne dedin, anlamadım , acaba tekrar edermisin")
            speak(" ne dedin, anlamadım , acaba tekrar edermisin")


        except sr.RequestError:# eğerki sistemle alakalı bir hata alırsak burası çalışıyoruz
            speak('Sistemin çalışmıyor')
            print(Fore.GREEN)
            print('Jarvis = Sistemin çalışmıyor')
        return voice #dinlediğimiz voice ı geri döndürüyoruz

def response(voice):#voice ile gelen veriyi sorgululamak için response adında bir fonkiyon
    if 'nasılsın' in voice:# eğer voice nin içinde nasılsın  diye bir değer varsa bunları yap
        #sözler adlı bir dizi tanımlıyoruz
        sozler = ["iyiyim sen nasılsın",
                "iyiyim sen nasılsın",
                "iyiyim sen nasılsın",
                
        ]
        secim=choice(sozler)#sozlerden birini karışık olarak seçilecek

        speak(secim)#seçilen söz seslendiriliecek
        print(Fore.GREEN)
        print("Jarvis  = "+secim)#seçilen söz yazdırılacak

    if 'naber'  in voice:# eğer voice nin içinde teşekkür ederim diye bir değer varsa bunları yap
        print(Fore.GREEN)
        print("Jarvis  = iyi senden naber")#ekrana yazılacak veri
        speak("iyi senden naber")#sesli bir şekilde söylenmesi için
    
    if 'iyiyim' in voice:# eğer voice nin içinde iyiyim diye bir değer varsa bunları yap
        print(Fore.GREEN)
        print("Jarvis  = iyi olmana sevindim senin için ne yapabilirim")#ekrana yazılacak veri
        speak("iyi olmana sevindim senin için ne yapabilirim")#sesli bir şekilde söylenmesi için
    
    if 'kötüyüm' in voice:# eğer voice nin içinde kötüyüm diye bir değer varsa bunları yap
        print(Fore.GREEN)
        print("Jarvis  = boşver iyi olmaya bak senin için birşey yapabilirmiyim")
        speak("boşver iyi olmaya bak senin için birşey yapabilirmiyim")

    if 'bugün nasılsın' in voice:
        print(Fore.GREEN)    
        print("Jarvis  = Günüm Çok güzeldi")
        speak("Günüm Çok güzeldi")

    if 'fıkra anlat' in voice:# eğer voice nin içinde Fıkra anlat diye bir değer varsa bunları yap
        #fıkralar adlı bir dizi tanımlıyoruz
        fıkralar = ["Temel aldığı bir daktiloyu bozuk diye geri götürdü. Satıcı Neresi bozuk, dün aldığında sağlamdı.Temel:İki tane a yok, saat yazamıyorum.",
                "Karınca Ve FilBir gün bir karınca bir file aşık olmuş. Annesi bu durumu onaylamamış  Karınca Bana değil karnımdakine acı, demiş.",
                "Bektaşi'ye sormuşlar. Dünya öküzün boynuzlarının üstünde duruyormuş, ne diyorsun bu işe? Valla onu bilmem ama buna inanan öküzlerin olduğunu biliyorum, demiş.",
                "Temel'in eldivenle yazı yazdığını görenler sormuş Niye eldivenli yazıyorsun zor olmuyor mu?  Zorluğuna zor ama el yazımın tanınmasını istemeyrum.",
                "Bir deli hastenisnde herkes zıplıyor, Temel yerinden kımıldamıyormuş  Biz patlamış mısırız, ben tavanın altına yapışmışım.",
                "Küçük çocuk okulun ilk günü sonunda eve döner. Annesi sorar;  Bugün okulda ne öğrendiniz? Çocuk cevaplar; Yeterli değil, yarın tekrar gitmem gerek"


        ]
        secimfık=choice(fıkralar)#sozlerden birini karışık olarak seçilecek wait()
    

        speak(secimfık)#seçilen söz seslendiriliecek
        print(Fore.GREEN)
        print("Jarvis  = "+secimfık)#seçilen söz ekrana yazılması için

    if 'hikaye anlat' in voice:# eğer voice nin içinde hikaye anlat diye bir değer varsa bunları yap
        #fıkralar adlı bir dizi tanımlıyoruz
        hikayeler=[
                "Bersisa diye bir alim varmış 200 sene abitlik yaptıktan sonra  sonsuz cehennemlik oldu şeytana secde etti. ne oldum değil ne olacağım demek lazım",
                "Bersisa diye bir alim varmış 200 sene abitlik yaptıktan sonra  sonsuz cehennemlik oldu şeytana secde etti. ne oldum değil ne olacağım demek lazım ",
                "Bersisa diye bir alim varmış 200 sene abitlik yaptıktan sonra  sonsuz cehennemlik oldu şeytana secde etti. ne oldum değil ne olacağım demek lazım "
        ]
        secimhikaye=choice(hikayeler)#hikayelerden birini karışık olarak seçilecek

        speak(secimhikaye)#seçilen hikaye seslendiriliecek
        print(Fore.GREEN)
        print("Jarvis  = "+secimhikaye)#seçilen hikaye ekrana yazılması için

    
    if 'neler yapabilirsin' in voice:# eğer voice nin içinde neler yapabilirsin diye bir değer varsa bunları yap
        speak('Allah izin verdikçe her şeyi yapabilirim')
        print(Fore.GREEN)
        print('Allah izin verdikçe her şeyi yapabilirim')

    if 'sen kimsin'  in voice:# eğer voice nin içinde sen kimsin diye bir değer varsa bunları yap
        print(Fore.GREEN)
        speak('Benim adım Jarvis, MUSA Hocamın çok emeği var üstümde çok severim kendisini')#selendirelecek
        print('Jarvis  = Benim adım Jarvis, MUSA Hocamın çok emeği var üstümde çok severim kendisini ')#ekrana yazılacak
        

    if 'saat kaç' in voice:# eğer voice nin içinde saat kaç diye bir değer varsa bunları yap
        speak(datetime.now().strftime('%H:%M:%S'))#datetime.now sayesinde anlık saati alıyoruz ve seslendiriyouz
        print(Fore.GREEN)
        print("Jarvis  = "+datetime.now().strftime('%H:%M:%S'))#datetime.now sayesinde anlık saati alıyoruz ve yazdırıyoruz

    if 'arama yap' in voice:# eğer voice nin içinde arama yap diye bir değer varsa bunları yap
        search = record('ne aramamı istersin')#record ile aranmasını istediğimiz kelimeyi yada cümleyi alıp search değişkenine tanımlıyouz
        url ='https://google.com/search?q='+search#https://google.com/search?q= adresine aldığımız search ı ekliyoruz ve url değişkenine tanımlıyouz
        webbrowser.get().open(url)#web browserı açıyouz ve  url değişkenini dönderiyouz
        speak(search+' için bulduğum sonuçlar')#sesli bir şekilde seslendirme yapıyouz
        print(Fore.GREEN)
        print("Jarvis  = "+search+' için bulduğum sonuçlar')#ekrana yazdırma yapıyouz
    
    if "youtube'da ara" in voice:# eğer voice nin içinde arama yap diye bir değer varsa bunları yap
        searchy = record('ne aramamı istersin')#record ile aranmasını istediğimiz kelimeyi yada cümleyi alıp searchy değişkenine tanımlıyouz
        urly ='https://www.youtube.com/results?search_query='+searchy#https://google.com/search?q= adresine aldığımız searchy ı ekliyoruz ve urly değişkenine tanımlıyouz
        webbrowser.get().open(urly)#web browserı açıyouz ve  urly değişkenini dönderiyouz
        speak(searchy+' için bulduğum sonuçlar')#sesli bir şekilde seslendirme yapıyouz
        print(Fore.GREEN)
        print("Jarvis = "+searchy+' için bulduğum sonuçlar')#ekrana yazdırma yapıyouz
    
    if 'hava durumu nedir' in voice:# eğer voice nin içinde hava durumu diye bir değer varsa bunları yap
        #feedparser ile link deki veriyi çekip parçalıyouz bunuda parse değişkenine tanımlıyouz
        parse = feedparser.parse("https://rss.accuweather.com/rss/liveweather_rss.asp?metric=1&locCode=EUR|TR|34000|ISTANBUL|")
        parse = parse["entries"][0]["summary"]
        parse = parse.split()
        havail=parse[2] #havaiiladlı adlı değişkene parsenin 3.değeri olan il adını tanımlıyoruz
        havadetay=parse[4] #havadetay adlı  değişkene parsenin 5. değeri olan dereceyi tanımlıyoruz
        speak(havail+" için hava"+havadetay+" derece")#sesli söyletiouz
        print(Fore.GREEN)
        print("Jarvis  = "+havail+" için hava"+havadetay+" derece")#ekrana yazdırıyouz
    


    if 'görüşürüz' in voice:# eğer voice nin içinde güle güle diye bir değer varsa bunları yap
        speak('görüşürüz')#sesli söyletiouz
        print(Fore.GREEN)
        print('Jarvis  = görüşürüz')#ekrana yazdırıyouz
        exit()# uygulamadan çıkış yapıyouz

    if "söylediğim her şeyi not et" in voice:
        speak("Dosya ismi ne olsun?")
        txtfile = record() + ".txt"
        speak("Hangi dilde kayıt istiyorsun?")
        dil = record()
        dil = dil.lower()
        if "türkçe" in dil:
            speak("Söylemeye başlayabilirsin.")
            while True:
                thetxt = record()
                if "not yazmayı bitir" in thetxt:
                    speak("Not tutma işlemi sonlandırıldı.")
                    f.close()
                    os.system("TASKKILL /F /IM Asistan.exe")
                f = open("notlar/"+txtfile, "a", encoding="utf-8")
                f.writelines(thetxt+" ")  
    
    if "not sil" in voice:
        speak("Hangi notu sileyim?")
        txtfile = record() + ".txt"
        notes = os.listdir(r"C:\Users\musas\OneDrive\Belgeler\Sesli Asistan")
        icermek = notes.__contains__(txtfile)
        if icermek:
            os.remove(r"C:\Users\musas\OneDrive\Belgeler\Sesli Asistan"+ txtfile)
            speak("İstediğin notu sildim.")
        else:
            speak("silmek istediğin dosya mevcut değil.")

    if "hangi gündeyiz" in voice or "günlerden ne" in voice:
        today = time.strftime("%A")
        today.capitalize()
        if today == "Monday":
            today = "Pazartesi"

        elif today == "Tuesday":
            today = "Salı"

        elif today == "Wednesday":
            today = "Çarşamba"

        elif today == "Thursday":
            today = "Perşembe"

        elif today == "Friday":
            today = "Cuma"

        elif today == "Saturday":
            today = "Cumartesi"

        elif today == "Sunday":
            today = "Pazar"

    
    if "pil yüzdesi kaç" in voice:
        pil = psutil.sensors_battery()
        yuzde = pil.percent
        speak(f"Kalan pil: yüzde{yuzde}")        

        speak(today)        

def speak(string):#speak adlı bir fonksiyon oluştuyouz 
    tts = gTTS(string,lang='tr')#sesi text e türkçe olarak çevirip tts adlı değişkene tanımlıyouz
    rand=random.randint(1,100)#random 1 ve 100 arası bir sayı üretip rand adlı değişkene tanımlıyouz bunun amacı bir hata ile karşılaşıp mp3 dosyası silinmezse üsütne yazmasın diye
    file= 'ses-'+str(rand)+'.mp3'#.mp3 uzantılı bir ses dosyası oluşturuyoruz
    tts.save(file)#dosyayı kayıt ediyouz
    playsound(file)#dosyayı okutuyoyz
    os.remove(file)#dosyayı siliyouz


  

print(Fore.RED)

#bunun tek amacı bir görsellik olması için
print('──────────────────────────────────')
print('──────────────────────────────────')
print('──────────────────────────────────')
print('──█████████▀───────────█████████▀─')
print('──────────────────────────────────')
print('─▄██▀────▀██▄─────────▄██▀────▀██▄')
print('─██────────██─────────██────────██')
print('─██───██───██─────────██───██───██')
print('─██────────██─────────██────────██')
print('──██▄────▄██───────────██▄────▄██─')
print('───▀██████▀─────────────▀██████▀──')
print('──────────────────────────────────')
print('──────────────────────────────────')
print('──────────────────────────────────')
print('───────────█████████████──────────')
print('──────────────────────────────────')
print('──────────────────────────────────')

speak('Buyrun Efendim')#ilk açılışta asiatanın bizi karşılaması için
print(Fore.GREEN)
print('Jarvis  = Buyrun Efendim')#ilk açılışta asiatanın bizi karşılamasını yazdırmak için
time.sleep(1)#uygulamyı 1 saniye uyutuyouz dinlemede karışıklık olmaması için
while 1:#tek bir komut aldıktan sonra kapanmaması için sonsuz döngü oluşturuyoruz
    voice=record()
    print(Fore.BLUE)
    print(voice)
    response(voice)
    print(Fore.GREEN)
    speak('başka bir isteğiniz var mıdır')
    print('başka bir isteğiniz var mıdır')
    




if 'kamerayı aç'  in voice:# eğer voice nin içinde sen kimsin diye bir değer varsa bunları yap
        print(Fore.GREEN)
        speak('Hemen açıyorum')#selendirelecek
        print('Hemen açıyorum')