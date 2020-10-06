from selenium import webdriver
import time


class BeklemeSuresiException(Exception):
    """Raised when the input value is too small"""
    pass


class XPathNoneException(Exception):
    """Raised when the dersxPath None"""
    pass


class KullaniciAdiGirilmemisException(Exception):
    pass


class SifreGirilmemisException(Exception):
    pass


class DersAlmaBotu:
    webSayfasi = "https://obs.atauni.edu.tr"
    kullaniciAdiInputID = "UserName"
    sifreInputID = "Password"
    butonID = "btn_giris"
    dersAlmaSayfasi = "https://obs.atauni.edu.tr/moduller/sayfa/dersAlma/index"
    dersxPath = []
    sleepTime = 5

    def __init__(self):
        self.driver = webdriver.Firefox()
        # pass

    def beklemeSuresiniAyarla(self, value):
        if value > 1:
            self.sleepTime = value
        else:
            raise BeklemeSuresiException("1'den büyük bir değer giriniz.")

    def girisSayfasiniGoster(self):
        self.driver.get(self.webSayfasi)

    def girisYap(self, kullanici_adi, sifre):
        if not kullanici_adi:
            raise KullaniciAdiGirilmemisException('Kullanici adi girilmemis.')
        if not sifre:
            raise SifreGirilmemisException('Sifre girilmemis.')

        username_in = self.driver.find_element_by_id(self.kullaniciAdiInputID)
        pass_in = self.driver.find_element_by_id(self.sifreInputID)
        username_in.send_keys(kullanici_adi)
        time.sleep(1)
        pass_in.send_keys(sifre)
        time.sleep(1)
        login_btn = self.driver.find_element_by_id(self.butonID)
        login_btn.click()
        time.sleep(1)

    def menuSec(self, xpaths):
        menus = [self.driver.find_element_by_xpath(xpath) for xpath in xpaths]
        try:
            for menu in menus:
                menu.click()
                time.sleep(2)
        except:
            print('Menu seçilemedi')

    def dersAlmaSayfasiniGoster(self):
        self.driver.get(self.dersAlmaSayfasi)
        self.sayfayiKaydir()
        self.sayfayiKaydir()
        self.sayfayiKaydir()
        self.sayfayiKaydir()
        self.sayfayiKaydir()

    def dersleriAl(self):
        if not self.dersxPath:
            raise XPathNoneException("Derslerin xpath'lerini girmeniz gerkiyor.")
        dersler = [self.driver.find_element_by_xpath(xpath) for xpath in self.dersxPath]

        for ders in dersler:
            while not ders.get_attribute('checked'):
                ders.click()
                time.sleep(self.sleepTime)

    def sayfayiKaydir(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
        time.sleep(1)


bot = DersAlmaBotu()
bot.dersxPath = ['//*[@id="id_48896"]', '//*[@id="id_32611"]']
bot.girisSayfasiniGoster()
bot.girisYap("", "")
bot.dersAlmaSayfasiniGoster()
bot.dersleriAl()
