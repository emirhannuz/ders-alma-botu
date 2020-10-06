# Firefox ve Firefox Webdriver yükleme
projenin çalışması için Firefox ve Firefox Webdriver'a ihtiyacınız olacak.
Firefox'u indirmek için -> https://www.mozilla.org/tr/firefox/new/
Firefox Webdriver'ı indirmek için ->https://github.com/mozilla/geckodriver/releases/tag/v0.27.0
bu sayfadan size uygun olan dosyayı indirdikten sonra zip içerisindeki **geckodriver.exe** dosyasını, python'ın bilgisayarınızda kurulu olduğu klasörün içine atınız.



# Selenium modülünü projeye dahil edin

    pip install selenium


# Ayarlar

Olur da inputların id'leri veya web sayfasının linki değişirse aşağıdaki gibi ayarlamaları yapın. Değişmemiş ise herhangi bir ayar yapmanıza gerek yok.

    bot = DersAlmaBotu()
    bot.webSayfasi          = "yeni web sayfasının linki"
    bot.kullaniciAdiInputID = "kullanıcı adı input'unun yeni id'si"
    bot.sifreInputID        = "sifre input'unun yeni id'si"
    bot.butonID             = "giriş butonunun yeni id'si"
    bot.dersAlmaSayfasi     = "yeni ders alma sayfasinin linki"
    bot.dersxPath           = ['ders1 xpath', 'ders2 xpath']

>**Not:** inputların id'lerini öğrenmek için kutucuğa sağ tıklayarak inceleye (ögeyi denetle) tıklayabilirsiniz.
>**input type="text" id="UserName" placeholder="T.C. / Kullanıcı Adı"** burada **id** özelliğinin sağ tarafındaki (UserName) metni alın  ve botta gerekli değişkenin değerini değiştirin.

>derslerin xpath'lerini ders alma kutucuğuna sağ tıklayarak incele(ögeyi denetle) dedikten sonra karşınıza gelen input etiketine de sağ tıklayarak copy>copy xpath seçeneğini seçerek alın. Aldığınız bu xpath'leri bot.dersxPath'e bir **liste(dizi)** şeklinde gönderin.

Bot derslerinizi 5 saniye aralıklarla almaya çalışacak. Süreyi kısaltmak veya arttırmak iserseniz beklemeSuresiniAyarla metoduna tam sayi değer göndererek süreyi istediğiniz şekilde ayarlayabilirsiniz.
    
    bot.beklemeSuresiniAyarla(3)

# Programı Çalıştırın

    bot.girisSayfasiniGoster()  
	bot.girisYap("kullanıcı adınız", "sifreniz")  
	bot.dersAlmaSayfasiniGoster()  
	bot.dersleriAl()
> Sisteme giriş yapabilmesi için girisYap metoduna kullanıcı adınızı ve şifrenizi gönderin.

 