from GameStartScreen import *
import time , random , pygame , sys
from Resim_adresleri import *

class QuizScreen() :
    def __init__(self , title , fill = ( 0 , 0 , 0 ) ):
        self.title = title
        self.fill = fill
        self.current = False
    def make_current(self):
        pygame.display.set_caption(self.title)
        self.current = True
        self.screen = pygame.display.set_mode( (0,0) , pygame.FULLSCREEN )
    def end_current(self):
        self.current = False
    def check_update(self):
        return self.current
    def screen_update(self):
        if ( self.current ):
            self.screen.fill(self.fill)
    def return_title(self):
        return self.screen
    def get_width(self):
        return 1366
    def get_height(self):
        return 768

    def bayrak_acilis_ekrani(self):
        screen_width = self.screen.get_width()  # ekran genişliği = 1366
        screen_height = self.screen.get_height()  # ekran yüksekliği = 768

        # Arkaplan resmi
        background_image = pygame.image.load(r'C:\Users\CASPER\PycharmProjects\untitled\Sorular_Images\acilis_ekranlari\bayrak_acilis_image.jpg')
        background_image = pygame.transform.scale(background_image, (screen_width, screen_height))

        get_out = True

        now = time.time()  # süre basladı
        end_time = now + 2  # iki saniye sonra süre bitecek

        while get_out:  # pencerenin ekranda kalması için gerekli infinite loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()  # bu for dongusu içine bir şey yazılmaz. pencereye basıldıgında hata alınmamasını sağlar
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        sys.exit()

            self.screen.blit(background_image,(0,0))

            if time.time() > end_time:
                get_out = False  # eğer süre aşıldıysa çık

            pygame.display.update()  # pencere update edilir

    #############################################################################
    #############################################################################
    def siklar_image_blit(self,cevap_numarasi,dogru_cevap,notr_cevap,pushed_true):

        ##Birinci şık ile ilgili işlemler
        if cevap_numarasi == 1 and pushed_true == True:
            self.screen.blit(dogru_cevap, pygame.rect.Rect(153, 390, 673, 560))  # 1.şık
            self.screen.blit(notr_cevap, pygame.rect.Rect(688, 390, 1208, 560))  # 2.şık
            self.screen.blit(notr_cevap, pygame.rect.Rect(153, 570, 673, 740))  # 3.şık
            self.screen.blit(notr_cevap, pygame.rect.Rect(688, 570, 1208, 740))  # 4.şık
        elif cevap_numarasi == 1 and pushed_true == False:
            self.screen.blit(notr_cevap, pygame.rect.Rect(153, 390, 673, 560))  # 1.şık
            self.screen.blit(notr_cevap, pygame.rect.Rect(688, 390, 1208, 560))  # 2.şık
            self.screen.blit(notr_cevap, pygame.rect.Rect(153, 570, 673, 740))  # 3.şık
            self.screen.blit(notr_cevap, pygame.rect.Rect(688, 570, 1208, 740))  # 4.şık

        ##İkinci şık ile ilgili işlemler
        elif cevap_numarasi == 2 and pushed_true == True:
            self.screen.blit(dogru_cevap, pygame.rect.Rect(688, 390, 1208, 560))  # 2.şık
            self.screen.blit(notr_cevap, pygame.rect.Rect(153, 390, 673, 560))  # 1.şık
            self.screen.blit(notr_cevap, pygame.rect.Rect(153, 570, 673, 740))  # 3.şık
            self.screen.blit(notr_cevap, pygame.rect.Rect(688, 570, 1208, 740))  # 4.şık
        elif cevap_numarasi == 2 and pushed_true == False:
            self.screen.blit(notr_cevap, pygame.rect.Rect(153, 390, 673, 560))  # 1.şık
            self.screen.blit(notr_cevap, pygame.rect.Rect(688, 390, 1208, 560))  # 2.şık
            self.screen.blit(notr_cevap, pygame.rect.Rect(153, 570, 673, 740))  # 3.şık
            self.screen.blit(notr_cevap, pygame.rect.Rect(688, 570, 1208, 740))  # 4.şık

        ##Üçüncü şık ile ilgili işlemler
        elif cevap_numarasi == 3 and pushed_true == True:
            self.screen.blit(dogru_cevap, pygame.rect.Rect(153, 570, 673, 740))  # 3.şık
            self.screen.blit(notr_cevap, pygame.rect.Rect(153, 390, 673, 560))  # 1.şık
            self.screen.blit(notr_cevap, pygame.rect.Rect(688, 390, 1208, 560))  # 2.şık
            self.screen.blit(notr_cevap, pygame.rect.Rect(688, 570, 1208, 740))  # 4.şık
        elif cevap_numarasi == 3 and pushed_true == False:
            self.screen.blit(notr_cevap, pygame.rect.Rect(153, 390, 673, 560))  # 1.şık
            self.screen.blit(notr_cevap, pygame.rect.Rect(688, 390, 1208, 560))  # 2.şık
            self.screen.blit(notr_cevap, pygame.rect.Rect(153, 570, 673, 740))  # 3.şık
            self.screen.blit(notr_cevap, pygame.rect.Rect(688, 570, 1208, 740))  # 4.şık

        ##Dördüncü şık ile ilgili işlemler
        elif cevap_numarasi == 4 and pushed_true == True:
            self.screen.blit(dogru_cevap, pygame.rect.Rect(688, 570, 1208, 740))  # 4.şık
            self.screen.blit(notr_cevap, pygame.rect.Rect(153, 390, 673, 560))  # 1.şık
            self.screen.blit(notr_cevap, pygame.rect.Rect(688, 390, 1208, 560))  # 2.şık
            self.screen.blit(notr_cevap, pygame.rect.Rect(153, 570, 673, 740))  # 3.şık
        elif cevap_numarasi == 4 and pushed_true == False:
            self.screen.blit(notr_cevap, pygame.rect.Rect(153, 390, 673, 560))  # 1.şık
            self.screen.blit(notr_cevap, pygame.rect.Rect(688, 390, 1208, 560))  # 2.şık
            self.screen.blit(notr_cevap, pygame.rect.Rect(153, 570, 673, 740))  # 3.şık
            self.screen.blit(notr_cevap, pygame.rect.Rect(688, 570, 1208, 740))  # 4.şık
    #############################################################################
    #############################################################################

    def cevaplar_image_blit(self,cevap_numarasi,pushed_true,font,cevap,diger_sik_1,diger_sik_2,diger_sik_3,black,renkler,siklar):
        if cevap_numarasi == 1 and pushed_true == True:
            birinci_sik_renk = renkler[1]
            cevap_yazi = font.render(cevap, 1, black, birinci_sik_renk)
            diger_sik_1_yazi = font.render(diger_sik_1, 1, black, renkler[0])
            diger_sik_2_yazi = font.render(diger_sik_2, 1, black, renkler[0])
            diger_sik_3_yazi = font.render(diger_sik_3, 1, black, renkler[0])

            self.screen.blit(cevap_yazi, siklar[cevap_numarasi - 1])
            self.screen.blit(diger_sik_1_yazi, siklar[1])
            self.screen.blit(diger_sik_2_yazi, siklar[2])
            self.screen.blit(diger_sik_3_yazi, siklar[3])
        elif cevap_numarasi == 1 and pushed_true == False:
            cevap_yazi = font.render(cevap, 1, black, renkler[0])
            diger_sik_1_yazi = font.render(diger_sik_1, 1, black, renkler[0])
            diger_sik_2_yazi = font.render(diger_sik_2, 1, black, renkler[0])
            diger_sik_3_yazi = font.render(diger_sik_3, 1, black, renkler[0])

            self.screen.blit(cevap_yazi, siklar[cevap_numarasi - 1])
            self.screen.blit(diger_sik_1_yazi, siklar[1])
            self.screen.blit(diger_sik_2_yazi, siklar[2])
            self.screen.blit(diger_sik_3_yazi, siklar[3])
        elif cevap_numarasi == 2 and pushed_true == True:
            ikinci_sik_renk = renkler[1]
            cevap_yazi = font.render(cevap, 1, black, ikinci_sik_renk)
            diger_sik_1_yazi = font.render(diger_sik_1, 1, black, renkler[0])
            diger_sik_2_yazi = font.render(diger_sik_2, 1, black, renkler[0])
            diger_sik_3_yazi = font.render(diger_sik_3, 1, black, renkler[0])

            self.screen.blit(cevap_yazi, siklar[cevap_numarasi - 1])
            self.screen.blit(diger_sik_1_yazi, siklar[0])
            self.screen.blit(diger_sik_2_yazi, siklar[2])
            self.screen.blit(diger_sik_3_yazi, siklar[3])
        elif cevap_numarasi == 2 and pushed_true == False:
            cevap_yazi = font.render(cevap, 1, black, renkler[0])
            diger_sik_1_yazi = font.render(diger_sik_1, 1, black, renkler[0])
            diger_sik_2_yazi = font.render(diger_sik_2, 1, black, renkler[0])
            diger_sik_3_yazi = font.render(diger_sik_3, 1, black, renkler[0])

            self.screen.blit(cevap_yazi, siklar[cevap_numarasi - 1])
            self.screen.blit(diger_sik_1_yazi, siklar[0])
            self.screen.blit(diger_sik_2_yazi, siklar[2])
            self.screen.blit(diger_sik_3_yazi, siklar[3])
        elif cevap_numarasi == 3 and pushed_true == True:
            ucuncu_sik_renk = renkler[1]
            cevap_yazi = font.render(cevap, 1, black, ucuncu_sik_renk)
            diger_sik_1_yazi = font.render(diger_sik_1, 1, black, renkler[0])
            diger_sik_2_yazi = font.render(diger_sik_2, 1, black, renkler[0])
            diger_sik_3_yazi = font.render(diger_sik_3, 1, black, renkler[0])

            self.screen.blit(cevap_yazi, siklar[cevap_numarasi - 1])
            self.screen.blit(diger_sik_1_yazi, siklar[0])
            self.screen.blit(diger_sik_2_yazi, siklar[1])
            self.screen.blit(diger_sik_3_yazi, siklar[3])
        elif cevap_numarasi ==  3 and pushed_true == False:
            cevap_yazi = font.render(cevap, 1, black, renkler[0])
            diger_sik_1_yazi = font.render(diger_sik_1, 1, black, renkler[0])
            diger_sik_2_yazi = font.render(diger_sik_2, 1, black, renkler[0])
            diger_sik_3_yazi = font.render(diger_sik_3, 1, black, renkler[0])

            self.screen.blit(cevap_yazi, siklar[cevap_numarasi - 1])
            self.screen.blit(diger_sik_1_yazi, siklar[0])
            self.screen.blit(diger_sik_2_yazi, siklar[1])
            self.screen.blit(diger_sik_3_yazi, siklar[3])
        elif cevap_numarasi == 4 and pushed_true == True:
            dorduncu_sik_renk = renkler[1]
            cevap_yazi = font.render(cevap, 1, black, dorduncu_sik_renk)
            diger_sik_1_yazi = font.render(diger_sik_1, 1, black, renkler[0])
            diger_sik_2_yazi = font.render(diger_sik_2, 1, black, renkler[0])
            diger_sik_3_yazi = font.render(diger_sik_3, 1, black, renkler[0])

            self.screen.blit(cevap_yazi, siklar[cevap_numarasi - 1])
            self.screen.blit(diger_sik_1_yazi, siklar[0])
            self.screen.blit(diger_sik_2_yazi, siklar[1])
            self.screen.blit(diger_sik_3_yazi, siklar[2])
        elif cevap_numarasi == 4 and pushed_true == False:
            cevap_yazi = font.render(cevap, 1, black, renkler[0])
            diger_sik_1_yazi = font.render(diger_sik_1, 1, black, renkler[0])
            diger_sik_2_yazi = font.render(diger_sik_2, 1, black, renkler[0])
            diger_sik_3_yazi = font.render(diger_sik_3, 1, black, renkler[0])

            self.screen.blit(cevap_yazi, siklar[cevap_numarasi - 1])
            self.screen.blit(diger_sik_1_yazi, siklar[0])
            self.screen.blit(diger_sik_2_yazi, siklar[1])
            self.screen.blit(diger_sik_3_yazi, siklar[2])

    #############################################################################
    #######################Bayrak Sorulari#######################################
    #############################################################################

    def bayrak_sorulari(self, quiz_sound):
        LEFT = 1  # mouse sol click

        black = (0,0,0)
        soru_resmi_boyutu = (435, 290)

        #####################################
        notr_cevap_rengi = (171, 165, 151)
        dogru_cevap_rengi = (57, 255, 20)
        yanlis_cevap_rengi = (255, 8, 10)

        #Şıkların rengi için tuple kullandım
        renkler = ( notr_cevap_rengi , dogru_cevap_rengi , yanlis_cevap_rengi )
        ###########################################
        ###########################################
        birinci_sik_koord = (220,450) #1.şıkkın koordinatları
        ikinci_sik_koord = (755,450) #2.şıkkın koordinatları
        ucuncu_sik_koord = (220,630) #3.şıkkın koordinatları
        dorduncu_sik_koord = (755,630) #4.şıkkın koordinatları

        #rastgele belirlenecek şıklar için tuple kullandım
        siklar = ( birinci_sik_koord , ikinci_sik_koord , ucuncu_sik_koord , dorduncu_sik_koord )
        ############################################
        ############################################
        birinci_sik_renk = renkler[0]
        ikinci_sik_renk = renkler[0]
        ucuncu_sik_renk = renkler[0]
        dorduncu_sik_renk = renkler[0]
        ##Default olarak şıkların rengi belirleniyor##
        ##############################################

        screen_width = self.screen.get_width()  # ekran genişliği = 1366
        screen_height = self.screen.get_height()  # ekran yüksekliği = 768

        # Arkaplan resmi
        background_image = pygame.image.load(r'C:\Users\CASPER\PycharmProjects\untitled\Sorular_Images\background_image.jpg')
        background_image = pygame.transform.scale(background_image, (screen_width, screen_height))

        # Soru kutucugu resmi
        soru_kutucugu = pygame.image.load(r'C:\Users\CASPER\PycharmProjects\untitled\Sorular_Images\soru.png')
        soru_kutucugu = pygame.transform.scale(soru_kutucugu, (1060,380))

        # Şık kutucuklarının resimleri
        notr_cevap = pygame.image.load(r'C:\Users\CASPER\PycharmProjects\untitled\Sorular_Images\notr_cevap.png')
        notr_cevap = pygame.transform.scale(notr_cevap, (520,170))

        dogru_cevap = pygame.image.load(r'C:\Users\CASPER\PycharmProjects\untitled\Sorular_Images\dogru_cevap.png')
        dogru_cevap = pygame.transform.scale(dogru_cevap, (520,170))

        yanlis_cevap = pygame.image.load(r'C:\Users\CASPER\PycharmProjects\untitled\Sorular_Images\yanlis_cevap.png')
        yanlis_cevap = pygame.transform.scale(yanlis_cevap, (520,170))

        font = pygame.font.SysFont("C:\Windows\Fonts\constanz.ttf", 72, True, True)
                                    # yazı tipi , punto , bold mu , italik mi

        #Rastgele bayrak belirlemek için bir liste açıyoruz
        random_bayrak_numaralari = list()
        random_bayrak_numaralari = bayrak_numara_degerleri

        bayrak_numarasi = random.randint(1,30) #Rastgele bir bayrak secilir
        random_bayrak_numaralari.remove(bayrak_numarasi) #Bayrağın tekrar seçilmemesi için numarasi listeden çıkarılır

        diger_sik_1_numarasi = random.randint(1,30)
        while diger_sik_1_numarasi == bayrak_numarasi :
            diger_sik_1_numarasi = random.randint(1,30) #Aynı değerin gelmemesi için

        diger_sik_2_numarasi = random.randint(1,30)
        while diger_sik_2_numarasi == bayrak_numarasi or diger_sik_2_numarasi == diger_sik_1_numarasi :
            diger_sik_2_numarasi = random.randint(1,30) #Aynı değerin gelmemesi için

        diger_sik_3_numarasi = random.randint(1,30)
        while diger_sik_3_numarasi == bayrak_numarasi or diger_sik_3_numarasi == diger_sik_2_numarasi or diger_sik_3_numarasi == diger_sik_1_numarasi:
            diger_sik_3_numarasi = random.randint(1,30) #Aynı değerin gelmemesi için

        cevap_numarasi = random.randint(1,4) #Doğru cevap için rastgele bir şık seçilir

        kalan_soru_sayisi = 30  #Toplam soru sayısının değeri tutuluyor
        puan = 0

        get_out = True
        pushed_true = False
        pushed_false = False

        while get_out:
            self.screen.blit(background_image, (0, 0))
            self.screen.blit(soru_kutucugu, pygame.rect.Rect(153,5,1213,385))

            bayrak_adresi = bayrak_numaralar.get(bayrak_numarasi)
            diger_sik_1_adresi = bayrak_numaralar.get(diger_sik_1_numarasi)
            diger_sik_2_adresi = bayrak_numaralar.get(diger_sik_2_numarasi)
            diger_sik_3_adresi = bayrak_numaralar.get(diger_sik_3_numarasi)

            soru_resmi = pygame.image.load(bayrak_adresi)
            soru_resmi = pygame.transform.scale(soru_resmi, soru_resmi_boyutu)
            self.screen.blit(soru_resmi, pygame.rect.Rect(466, 50, 901, 340))

            #cevap ve diğer şıkların değerleri alınır
            cevap = bayrak_cevaplar.get(bayrak_adresi)
            diger_sik_1 = bayrak_cevaplar.get(diger_sik_1_adresi)
            diger_sik_2 = bayrak_cevaplar.get(diger_sik_2_adresi)
            diger_sik_3 = bayrak_cevaplar.get(diger_sik_3_adresi)

            ###############Cevap 1. şıkta####################
            if cevap_numarasi == 1 and pushed_true == True :
                self.siklar_image_blit(cevap_numarasi,dogru_cevap,notr_cevap,pushed_true)
                self.cevaplar_image_blit(cevap_numarasi,pushed_true,font,cevap,diger_sik_1,diger_sik_2,diger_sik_3,black,renkler,siklar)
            elif cevap_numarasi == 1 and pushed_true == False :
                self.siklar_image_blit(cevap_numarasi, dogru_cevap,notr_cevap, pushed_true)
                self.cevaplar_image_blit(cevap_numarasi,pushed_true,font,cevap,diger_sik_1,diger_sik_2,diger_sik_3,black,renkler,siklar)

            ###############Cevap 2. şıkta####################
            if cevap_numarasi == 2 and pushed_true == True :
                self.siklar_image_blit(cevap_numarasi,dogru_cevap,notr_cevap,pushed_true)
                self.cevaplar_image_blit(cevap_numarasi,pushed_true,font,cevap,diger_sik_1,diger_sik_2,diger_sik_3,black,renkler,siklar)
            elif cevap_numarasi == 2 and pushed_true == False :
                self.siklar_image_blit(cevap_numarasi, dogru_cevap,notr_cevap, pushed_true)
                self.cevaplar_image_blit(cevap_numarasi,pushed_true,font,cevap,diger_sik_1,diger_sik_2,diger_sik_3,black,renkler,siklar)

            ###############Cevap 3. şıkta####################
            if cevap_numarasi == 3 and pushed_true == True :
                self.siklar_image_blit(cevap_numarasi, dogru_cevap,notr_cevap, pushed_true)
                self.cevaplar_image_blit(cevap_numarasi,pushed_true,font,cevap,diger_sik_1,diger_sik_2,diger_sik_3,black,renkler,siklar)
            elif cevap_numarasi == 3 and pushed_true == False :
                self.siklar_image_blit(cevap_numarasi, dogru_cevap,notr_cevap, pushed_true)
                self.cevaplar_image_blit(cevap_numarasi,pushed_true,font,cevap,diger_sik_1,diger_sik_2,diger_sik_3,black,renkler,siklar)

            ###############Cevap 4. şıkta####################
            if cevap_numarasi == 4 and pushed_true == True :
                self.siklar_image_blit(cevap_numarasi, dogru_cevap,notr_cevap, pushed_true)
                self.cevaplar_image_blit(cevap_numarasi,pushed_true,font,cevap,diger_sik_1,diger_sik_2,diger_sik_3,black,renkler,siklar)
            elif cevap_numarasi == 4 and pushed_true == False :
                self.siklar_image_blit(cevap_numarasi, dogru_cevap,notr_cevap, pushed_true)
                self.cevaplar_image_blit(cevap_numarasi,pushed_true,font,cevap,diger_sik_1,diger_sik_2,diger_sik_3,black,renkler,siklar)


            ####Mouse click eventi için sorgu işlemleri
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == LEFT:
                    mouse = pygame.mouse.get_pos()

                    if ( 153 < mouse[0] < 673 and 390 < mouse[1] < 560 ) :
                        if cevap_numarasi == 1 :
                            puan = puan + 100

                            pushed_true = True
                            self.siklar_image_blit(cevap_numarasi,dogru_cevap,notr_cevap,pushed_true)
                            self.cevaplar_image_blit(cevap_numarasi,pushed_true,font,cevap,diger_sik_1,diger_sik_2,diger_sik_3,black,renkler,siklar)

                            bayrak_numarasi = random.randint(1, 30)  # Rastgele bir bayrak secilir
                            while bayrak_numarasi not in random_bayrak_numaralari :
                                bayrak_numarasi = random.randint(1, 30)  # Rastgele bir bayrak secilir
                            random_bayrak_numaralari.remove(bayrak_numarasi)  # Bayrağın tekrar seçilmemesi için numarasi listeden çıkarılır

                            kalan_soru_sayisi -= 1
                            pushed_true = False

                            diger_sik_1_numarasi = random.randint(1, 30)
                            while diger_sik_1_numarasi == bayrak_numarasi:
                                diger_sik_1_numarasi = random.randint(1, 30)  # Aynı değerin gelmemesi için

                            diger_sik_2_numarasi = random.randint(1, 30)
                            while diger_sik_2_numarasi == bayrak_numarasi or diger_sik_2_numarasi == diger_sik_1_numarasi:
                                diger_sik_2_numarasi = random.randint(1, 30)  # Aynı değerin gelmemesi için

                            diger_sik_3_numarasi = random.randint(1, 30)
                            while diger_sik_3_numarasi == bayrak_numarasi or diger_sik_3_numarasi == diger_sik_2_numarasi or diger_sik_3_numarasi == diger_sik_1_numarasi:
                                diger_sik_3_numarasi = random.randint(1, 30)  # Aynı değerin gelmemesi için

                            cevap_numarasi = random.randint(1, 4)  # Doğru cevap için rastgele bir şık seçilir
                        else:
                            bayrak_numarasi = random.randint(1, 30)  # Rastgele bir bayrak secilir
                            while bayrak_numarasi not in random_bayrak_numaralari:
                                bayrak_numarasi = random.randint(1, 30)  # Rastgele bir bayrak secilir
                            random_bayrak_numaralari.remove(bayrak_numarasi)  # Bayrağın tekrar seçilmemesi için numarasi listeden çıkarılır

                            kalan_soru_sayisi -= 1
                            pushed_true = False

                            diger_sik_1_numarasi = random.randint(1, 30)
                            while diger_sik_1_numarasi == bayrak_numarasi:
                                diger_sik_1_numarasi = random.randint(1, 30)  # Aynı değerin gelmemesi için

                            diger_sik_2_numarasi = random.randint(1, 30)
                            while diger_sik_2_numarasi == bayrak_numarasi or diger_sik_2_numarasi == diger_sik_1_numarasi:
                                diger_sik_2_numarasi = random.randint(1, 30)  # Aynı değerin gelmemesi için

                            diger_sik_3_numarasi = random.randint(1, 30)
                            while diger_sik_3_numarasi == bayrak_numarasi or diger_sik_3_numarasi == diger_sik_2_numarasi or diger_sik_3_numarasi == diger_sik_1_numarasi:
                                diger_sik_3_numarasi = random.randint(1, 30)  # Aynı değerin gelmemesi için

                            cevap_numarasi = random.randint(1, 4)  # Doğru cevap için rastgele bir şık seçilir

                    elif ( 688 < mouse[0] < 1208 and 390 < mouse[1] < 560 ) :
                        if cevap_numarasi == 2 :
                            puan = puan + 100

                            pushed_true = True
                            self.siklar_image_blit(cevap_numarasi,dogru_cevap,notr_cevap,pushed_true)
                            self.cevaplar_image_blit(cevap_numarasi,pushed_true,font,cevap,diger_sik_1,diger_sik_2,diger_sik_3,black,renkler,siklar)

                            bayrak_numarasi = random.randint(1, 30)  # Rastgele bir bayrak secilir
                            while bayrak_numarasi not in random_bayrak_numaralari:
                                bayrak_numarasi = random.randint(1, 30)  # Rastgele bir bayrak secilir
                            random_bayrak_numaralari.remove(bayrak_numarasi)  # Bayrağın tekrar seçilmemesi için numarasi listeden çıkarılır

                            kalan_soru_sayisi -= 1
                            pushed_true = False

                            diger_sik_1_numarasi = random.randint(1, 30)
                            while diger_sik_1_numarasi == bayrak_numarasi:
                                diger_sik_1_numarasi = random.randint(1, 30)  # Aynı değerin gelmemesi için

                            diger_sik_2_numarasi = random.randint(1, 30)
                            while diger_sik_2_numarasi == bayrak_numarasi or diger_sik_2_numarasi == diger_sik_1_numarasi:
                                diger_sik_2_numarasi = random.randint(1, 30)  # Aynı değerin gelmemesi için

                            diger_sik_3_numarasi = random.randint(1, 30)
                            while diger_sik_3_numarasi == bayrak_numarasi or diger_sik_3_numarasi == diger_sik_2_numarasi or diger_sik_3_numarasi == diger_sik_1_numarasi:
                                diger_sik_3_numarasi = random.randint(1, 30)  # Aynı değerin gelmemesi için

                            cevap_numarasi = random.randint(1, 4)  # Doğru cevap için rastgele bir şık seçilir
                        else:
                            bayrak_numarasi = random.randint(1, 30)  # Rastgele bir bayrak secilir
                            while bayrak_numarasi not in random_bayrak_numaralari:
                                bayrak_numarasi = random.randint(1, 30)  # Rastgele bir bayrak secilir
                            random_bayrak_numaralari.remove(bayrak_numarasi)  # Bayrağın tekrar seçilmemesi için numarasi listeden çıkarılır

                            kalan_soru_sayisi -= 1
                            pushed_true = False

                            diger_sik_1_numarasi = random.randint(1, 30)
                            while diger_sik_1_numarasi == bayrak_numarasi:
                                diger_sik_1_numarasi = random.randint(1, 30)  # Aynı değerin gelmemesi için

                            diger_sik_2_numarasi = random.randint(1, 30)
                            while diger_sik_2_numarasi == bayrak_numarasi or diger_sik_2_numarasi == diger_sik_1_numarasi:
                                diger_sik_2_numarasi = random.randint(1, 30)  # Aynı değerin gelmemesi için

                            diger_sik_3_numarasi = random.randint(1, 30)
                            while diger_sik_3_numarasi == bayrak_numarasi or diger_sik_3_numarasi == diger_sik_2_numarasi or diger_sik_3_numarasi == diger_sik_1_numarasi:
                                diger_sik_3_numarasi = random.randint(1, 30)  # Aynı değerin gelmemesi için

                            cevap_numarasi = random.randint(1, 4)  # Doğru cevap için rastgele bir şık seçilir
                    elif ( 153 < mouse[0] < 673 and 570 < mouse[1] < 740 ) :
                        if cevap_numarasi == 3 :
                            puan = puan + 100

                            pushed_true = True
                            self.siklar_image_blit(cevap_numarasi, dogru_cevap,notr_cevap,pushed_true)
                            self.cevaplar_image_blit(cevap_numarasi,pushed_true,font,cevap,diger_sik_1,diger_sik_2,diger_sik_3,black,renkler,siklar)

                            bayrak_numarasi = random.randint(1, 30)  # Rastgele bir bayrak secilir
                            while bayrak_numarasi not in random_bayrak_numaralari:
                                bayrak_numarasi = random.randint(1, 30)  # Rastgele bir bayrak secilir
                            random_bayrak_numaralari.remove(bayrak_numarasi)  # Bayrağın tekrar seçilmemesi için numarasi listeden çıkarılır

                            kalan_soru_sayisi -= 1
                            pushed_true = False

                            diger_sik_1_numarasi = random.randint(1, 30)
                            while diger_sik_1_numarasi == bayrak_numarasi:
                                diger_sik_1_numarasi = random.randint(1, 30)  # Aynı değerin gelmemesi için

                            diger_sik_2_numarasi = random.randint(1, 30)
                            while diger_sik_2_numarasi == bayrak_numarasi or diger_sik_2_numarasi == diger_sik_1_numarasi:
                                diger_sik_2_numarasi = random.randint(1, 30)  # Aynı değerin gelmemesi için

                            diger_sik_3_numarasi = random.randint(1, 30)
                            while diger_sik_3_numarasi == bayrak_numarasi or diger_sik_3_numarasi == diger_sik_2_numarasi or diger_sik_3_numarasi == diger_sik_1_numarasi:
                                diger_sik_3_numarasi = random.randint(1, 30)  # Aynı değerin gelmemesi için

                            cevap_numarasi = random.randint(1, 4)  # Doğru cevap için rastgele bir şık seçilir
                        else:
                            bayrak_numarasi = random.randint(1, 30)  # Rastgele bir bayrak secilir
                            while bayrak_numarasi not in random_bayrak_numaralari:
                                bayrak_numarasi = random.randint(1, 30)  # Rastgele bir bayrak secilir
                            random_bayrak_numaralari.remove(bayrak_numarasi)  # Bayrağın tekrar seçilmemesi için numarasi listeden çıkarılır

                            kalan_soru_sayisi -= 1
                            pushed_true = False

                            diger_sik_1_numarasi = random.randint(1, 30)
                            while diger_sik_1_numarasi == bayrak_numarasi:
                                diger_sik_1_numarasi = random.randint(1, 30)  # Aynı değerin gelmemesi için

                            diger_sik_2_numarasi = random.randint(1, 30)
                            while diger_sik_2_numarasi == bayrak_numarasi or diger_sik_2_numarasi == diger_sik_1_numarasi:
                                diger_sik_2_numarasi = random.randint(1, 30)  # Aynı değerin gelmemesi için

                            diger_sik_3_numarasi = random.randint(1, 30)
                            while diger_sik_3_numarasi == bayrak_numarasi or diger_sik_3_numarasi == diger_sik_2_numarasi or diger_sik_3_numarasi == diger_sik_1_numarasi:
                                diger_sik_3_numarasi = random.randint(1, 30)  # Aynı değerin gelmemesi için

                            cevap_numarasi = random.randint(1, 4)  # Doğru cevap için rastgele bir şık seçilir
                    elif ( 688 < mouse[0] < 1208 and 570 < mouse[1] < 740 ) :
                        if cevap_numarasi == 4 :
                            puan = puan + 100

                            pushed_true = True
                            self.siklar_image_blit(cevap_numarasi, dogru_cevap,notr_cevap,pushed_true)
                            self.cevaplar_image_blit(cevap_numarasi,pushed_true,font,cevap,diger_sik_1,diger_sik_2,diger_sik_3,black,renkler,siklar)

                            bayrak_numarasi = random.randint(1, 30)  # Rastgele bir bayrak secilir
                            while bayrak_numarasi not in random_bayrak_numaralari:
                                bayrak_numarasi = random.randint(1, 30)  # Rastgele bir bayrak secilir
                            random_bayrak_numaralari.remove(bayrak_numarasi)  # Bayrağın tekrar seçilmemesi için numarasi listeden çıkarılır

                            kalan_soru_sayisi -= 1
                            pushed_true = False

                            diger_sik_1_numarasi = random.randint(1, 30)
                            while diger_sik_1_numarasi == bayrak_numarasi:
                                diger_sik_1_numarasi = random.randint(1, 30)  # Aynı değerin gelmemesi için

                            diger_sik_2_numarasi = random.randint(1, 30)
                            while diger_sik_2_numarasi == bayrak_numarasi or diger_sik_2_numarasi == diger_sik_1_numarasi:
                                diger_sik_2_numarasi = random.randint(1, 30)  # Aynı değerin gelmemesi için

                            diger_sik_3_numarasi = random.randint(1, 30)
                            while diger_sik_3_numarasi == bayrak_numarasi or diger_sik_3_numarasi == diger_sik_2_numarasi or diger_sik_3_numarasi == diger_sik_1_numarasi:
                                diger_sik_3_numarasi = random.randint(1, 30)  # Aynı değerin gelmemesi için

                            cevap_numarasi = random.randint(1, 4)  # Doğru cevap için rastgele bir şık seçilir
                        else:
                            bayrak_numarasi = random.randint(1, 30)  # Rastgele bir bayrak secilir
                            while bayrak_numarasi not in random_bayrak_numaralari:
                                bayrak_numarasi = random.randint(1, 30)  # Rastgele bir bayrak secilir
                            random_bayrak_numaralari.remove(bayrak_numarasi)  # Bayrağın tekrar seçilmemesi için numarasi listeden çıkarılır

                            kalan_soru_sayisi -= 1
                            pushed_true = False

                            diger_sik_1_numarasi = random.randint(1, 30)
                            while diger_sik_1_numarasi == bayrak_numarasi:
                                diger_sik_1_numarasi = random.randint(1, 30)  # Aynı değerin gelmemesi için

                            diger_sik_2_numarasi = random.randint(1, 30)
                            while diger_sik_2_numarasi == bayrak_numarasi or diger_sik_2_numarasi == diger_sik_1_numarasi:
                                diger_sik_2_numarasi = random.randint(1, 30)  # Aynı değerin gelmemesi için

                            diger_sik_3_numarasi = random.randint(1, 30)
                            while diger_sik_3_numarasi == bayrak_numarasi or diger_sik_3_numarasi == diger_sik_2_numarasi or diger_sik_3_numarasi == diger_sik_1_numarasi:
                                diger_sik_3_numarasi = random.randint(1, 30)  # Aynı değerin gelmemesi için

                            cevap_numarasi = random.randint(1, 4)  # Doğru cevap için rastgele bir şık seçilir

            if ( len(random_bayrak_numaralari) == 0 ):  #Sorular bitince çıkmak için
                get_out = False

            pygame.display.update()

        return puan

    ##############################################################################################
    ##################################PUAN EKRANI#################################################
    ##############################################################################################

    def sonuc_ekrani(self,puan):
        dosya = open(r'C:\Users\CASPER\PycharmProjects\untitled\skorlar.txt' , "r+" )
        dosya.write(str(puan))
        dosya.close()

        black = (0,0,0)
        background_rengi = (0, 255, 127)

        screen_width = self.screen.get_width()  # ekran genişliği = 1366
        screen_height = self.screen.get_height()  # ekran yüksekliği = 768

        font = pygame.font.SysFont("C:\Windows\Fonts\constanz.ttf", 110 , True, True)
        yazi = font.render("TEBRIKLER.. Puaniniz :: %s" % str(puan), 1, black, background_rengi)

        get_out = True

        now = time.time()  # süre basladı
        end_time = now + 3.5  # 3,5 saniye sonra süre bitecek

        while get_out :
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()  # bu for dongusu içine bir şey yazılmaz. pencereye basıldıgında hata alınmamasını sağlar
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        sys.exit()

            self.screen.fill(background_rengi)
            self.screen.blit(yazi,(50,350))

            if time.time() > end_time:
                get_out = False  # eğer süre aşıldıysa çık

            pygame.display.update()  # pencere update edilir

    ################################################################################################
    ##################################ŞEKİL EKRANI FONKSİYONLARI####################################
    ################################################################################################

    def sekil_acilis_ekrani(self):
        screen_width = self.screen.get_width()  # ekran genişliği = 1366
        screen_height = self.screen.get_height()  # ekran yüksekliği = 768

        # Arkaplan resmi
        background_image = pygame.image.load(
            r'C:\Users\CASPER\PycharmProjects\untitled\Sorular_Images\acilis_ekranlari\sekil_acilis_image.jpg')
        background_image = pygame.transform.scale(background_image, (screen_width, screen_height))

        get_out = True

        now = time.time()  # süre basladı
        end_time = now + 2  # iki saniye sonra süre bitecek

        while get_out:  # pencerenin ekranda kalması için gerekli infinite loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()  # bu for dongusu içine bir şey yazılmaz. pencereye basıldıgında hata alınmamasını sağlar
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        sys.exit()

            self.screen.blit(background_image, (0, 0))

            if time.time() > end_time:
                get_out = False  # eğer süre aşıldıysa çık

            pygame.display.update()  # pencere update edilir

    def sekil_sorulari(self, quiz_sound):
        LEFT = 1  # mouse sol click

        black = (0,0,0)
        soru_resmi_boyutu = (435, 290)

        #####################################
        notr_cevap_rengi = (171, 165, 151)
        dogru_cevap_rengi = (57, 255, 20)
        yanlis_cevap_rengi = (255, 8, 10)

        #Şıkların rengi için tuple kullandım
        renkler = ( notr_cevap_rengi , dogru_cevap_rengi , yanlis_cevap_rengi )
        ###########################################
        ###########################################
        birinci_sik_koord = (220,450) #1.şıkkın koordinatları
        ikinci_sik_koord = (755,450) #2.şıkkın koordinatları
        ucuncu_sik_koord = (220,630) #3.şıkkın koordinatları
        dorduncu_sik_koord = (755,630) #4.şıkkın koordinatları

        #rastgele belirlenecek şıklar için tuple kullandım
        siklar = ( birinci_sik_koord , ikinci_sik_koord , ucuncu_sik_koord , dorduncu_sik_koord )
        ############################################
        ############################################
        birinci_sik_renk = renkler[0]
        ikinci_sik_renk = renkler[0]
        ucuncu_sik_renk = renkler[0]
        dorduncu_sik_renk = renkler[0]
        ##Default olarak şıkların rengi belirleniyor##
        ##############################################

        screen_width = self.screen.get_width()  # ekran genişliği = 1366
        screen_height = self.screen.get_height()  # ekran yüksekliği = 768

        # Arkaplan resmi
        background_image = pygame.image.load(r'C:\Users\CASPER\PycharmProjects\untitled\Sorular_Images\background_image.jpg')
        background_image = pygame.transform.scale(background_image, (screen_width, screen_height))

        # Soru kutucugu resmi
        soru_kutucugu = pygame.image.load(r'C:\Users\CASPER\PycharmProjects\untitled\Sorular_Images\soru.png')
        soru_kutucugu = pygame.transform.scale(soru_kutucugu, (1060,380))

        # Şık kutucuklarının resimleri
        notr_cevap = pygame.image.load(r'C:\Users\CASPER\PycharmProjects\untitled\Sorular_Images\notr_cevap.png')
        notr_cevap = pygame.transform.scale(notr_cevap, (520,170))

        dogru_cevap = pygame.image.load(r'C:\Users\CASPER\PycharmProjects\untitled\Sorular_Images\dogru_cevap.png')
        dogru_cevap = pygame.transform.scale(dogru_cevap, (520,170))

        yanlis_cevap = pygame.image.load(r'C:\Users\CASPER\PycharmProjects\untitled\Sorular_Images\yanlis_cevap.png')
        yanlis_cevap = pygame.transform.scale(yanlis_cevap, (520,170))

        font = pygame.font.SysFont("C:\Windows\Fonts\constanz.ttf", 72, True, True)
                                    # yazı tipi , punto , bold mu , italik mi

        #Rastgele bayrak belirlemek için bir liste açıyoruz
        random_sekil_numaralari = list()
        random_sekil_numaralari = sekil_numara_degerleri

        sekil_numarasi = random.randint(1,30) #Rastgele bir bayrak secilir
        random_sekil_numaralari.remove(sekil_numarasi) #Bayrağın tekrar seçilmemesi için numarasi listeden çıkarılır

        diger_sik_1_numarasi = random.randint(1,30)
        while diger_sik_1_numarasi == sekil_numarasi :
            diger_sik_1_numarasi = random.randint(1,30) #Aynı değerin gelmemesi için

        diger_sik_2_numarasi = random.randint(1,30)
        while diger_sik_2_numarasi == sekil_numarasi or diger_sik_2_numarasi == diger_sik_1_numarasi :
            diger_sik_2_numarasi = random.randint(1,30) #Aynı değerin gelmemesi için

        diger_sik_3_numarasi = random.randint(1,30)
        while diger_sik_3_numarasi == sekil_numarasi or diger_sik_3_numarasi == diger_sik_2_numarasi or diger_sik_3_numarasi == diger_sik_1_numarasi:
            diger_sik_3_numarasi = random.randint(1,30) #Aynı değerin gelmemesi için

        cevap_numarasi = random.randint(1,4) #Doğru cevap için rastgele bir şık seçilir

        kalan_soru_sayisi = 30  #Toplam soru sayısının değeri tutuluyor
        puan = 0

        get_out = True
        pushed_true = False
        pushed_false = False

        while get_out:
            self.screen.blit(background_image, (0, 0))
            self.screen.blit(soru_kutucugu, pygame.rect.Rect(153,5,1213,385))

            sekil_adresi = sekil_numaralar.get(sekil_numarasi)
            diger_sik_1_adresi = sekil_numaralar.get(diger_sik_1_numarasi)
            diger_sik_2_adresi = sekil_numaralar.get(diger_sik_2_numarasi)
            diger_sik_3_adresi = sekil_numaralar.get(diger_sik_3_numarasi)

            soru_resmi = pygame.image.load(sekil_adresi)
            soru_resmi = pygame.transform.scale(soru_resmi, soru_resmi_boyutu)
            self.screen.blit(soru_resmi, pygame.rect.Rect(466, 50, 901, 340))

            #cevap ve diğer şıkların değerleri alınır
            cevap = sekil_cevaplar.get(sekil_adresi)
            diger_sik_1 = sekil_cevaplar.get(diger_sik_1_adresi)
            diger_sik_2 = sekil_cevaplar.get(diger_sik_2_adresi)
            diger_sik_3 = sekil_cevaplar.get(diger_sik_3_adresi)

            ###############Cevap 1. şıkta####################
            if cevap_numarasi == 1 and pushed_true == True :
                self.siklar_image_blit(cevap_numarasi,dogru_cevap,notr_cevap,pushed_true)
                self.cevaplar_image_blit(cevap_numarasi,pushed_true,font,cevap,diger_sik_1,diger_sik_2,diger_sik_3,black,renkler,siklar)
            elif cevap_numarasi == 1 and pushed_true == False :
                self.siklar_image_blit(cevap_numarasi, dogru_cevap,notr_cevap, pushed_true)
                self.cevaplar_image_blit(cevap_numarasi,pushed_true,font,cevap,diger_sik_1,diger_sik_2,diger_sik_3,black,renkler,siklar)

            ###############Cevap 2. şıkta####################
            if cevap_numarasi == 2 and pushed_true == True :
                self.siklar_image_blit(cevap_numarasi,dogru_cevap,notr_cevap,pushed_true)
                self.cevaplar_image_blit(cevap_numarasi,pushed_true,font,cevap,diger_sik_1,diger_sik_2,diger_sik_3,black,renkler,siklar)
            elif cevap_numarasi == 2 and pushed_true == False :
                self.siklar_image_blit(cevap_numarasi, dogru_cevap,notr_cevap, pushed_true)
                self.cevaplar_image_blit(cevap_numarasi,pushed_true,font,cevap,diger_sik_1,diger_sik_2,diger_sik_3,black,renkler,siklar)

            ###############Cevap 3. şıkta####################
            if cevap_numarasi == 3 and pushed_true == True :
                self.siklar_image_blit(cevap_numarasi, dogru_cevap,notr_cevap, pushed_true)
                self.cevaplar_image_blit(cevap_numarasi,pushed_true,font,cevap,diger_sik_1,diger_sik_2,diger_sik_3,black,renkler,siklar)
            elif cevap_numarasi == 3 and pushed_true == False :
                self.siklar_image_blit(cevap_numarasi, dogru_cevap,notr_cevap, pushed_true)
                self.cevaplar_image_blit(cevap_numarasi,pushed_true,font,cevap,diger_sik_1,diger_sik_2,diger_sik_3,black,renkler,siklar)

            ###############Cevap 4. şıkta####################
            if cevap_numarasi == 4 and pushed_true == True :
                self.siklar_image_blit(cevap_numarasi, dogru_cevap,notr_cevap, pushed_true)
                self.cevaplar_image_blit(cevap_numarasi,pushed_true,font,cevap,diger_sik_1,diger_sik_2,diger_sik_3,black,renkler,siklar)
            elif cevap_numarasi == 4 and pushed_true == False :
                self.siklar_image_blit(cevap_numarasi, dogru_cevap,notr_cevap, pushed_true)
                self.cevaplar_image_blit(cevap_numarasi,pushed_true,font,cevap,diger_sik_1,diger_sik_2,diger_sik_3,black,renkler,siklar)


            ####Mouse click eventi için sorgu işlemleri
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == LEFT:
                    mouse = pygame.mouse.get_pos()

                    if ( 153 < mouse[0] < 673 and 390 < mouse[1] < 560 ) :
                        if cevap_numarasi == 1 :
                            puan = puan + 100

                            pushed_true = True
                            self.siklar_image_blit(cevap_numarasi,dogru_cevap,notr_cevap,pushed_true)
                            self.cevaplar_image_blit(cevap_numarasi,pushed_true,font,cevap,diger_sik_1,diger_sik_2,diger_sik_3,black,renkler,siklar)

                            sekil_numarasi = random.randint(1, 30)  # Rastgele bir bayrak secilir
                            while sekil_numarasi not in random_sekil_numaralari :
                                sekil_numarasi = random.randint(1, 30)  # Rastgele bir bayrak secilir
                            random_sekil_numaralari.remove(sekil_numarasi)  # Bayrağın tekrar seçilmemesi için numarasi listeden çıkarılır

                            kalan_soru_sayisi -= 1
                            pushed_true = False

                            diger_sik_1_numarasi = random.randint(1, 30)
                            while diger_sik_1_numarasi == sekil_numarasi:
                                diger_sik_1_numarasi = random.randint(1, 30)  # Aynı değerin gelmemesi için

                            diger_sik_2_numarasi = random.randint(1, 30)
                            while diger_sik_2_numarasi == sekil_numarasi or diger_sik_2_numarasi == diger_sik_1_numarasi:
                                diger_sik_2_numarasi = random.randint(1, 30)  # Aynı değerin gelmemesi için

                            diger_sik_3_numarasi = random.randint(1, 30)
                            while diger_sik_3_numarasi == sekil_numarasi or diger_sik_3_numarasi == diger_sik_2_numarasi or diger_sik_3_numarasi == diger_sik_1_numarasi:
                                diger_sik_3_numarasi = random.randint(1, 30)  # Aynı değerin gelmemesi için

                            cevap_numarasi = random.randint(1, 4)  # Doğru cevap için rastgele bir şık seçilir
                        else:
                            sekil_numarasi = random.randint(1, 30)  # Rastgele bir bayrak secilir
                            while sekil_numarasi not in random_sekil_numaralari:
                                sekil_numarasi = random.randint(1, 30)  # Rastgele bir bayrak secilir
                            random_sekil_numaralari.remove(sekil_numarasi)  # Bayrağın tekrar seçilmemesi için numarasi listeden çıkarılır

                            kalan_soru_sayisi -= 1
                            pushed_true = False

                            diger_sik_1_numarasi = random.randint(1, 30)
                            while diger_sik_1_numarasi == sekil_numarasi:
                                diger_sik_1_numarasi = random.randint(1, 30)  # Aynı değerin gelmemesi için

                            diger_sik_2_numarasi = random.randint(1, 30)
                            while diger_sik_2_numarasi == sekil_numarasi or diger_sik_2_numarasi == diger_sik_1_numarasi:
                                diger_sik_2_numarasi = random.randint(1, 30)  # Aynı değerin gelmemesi için

                            diger_sik_3_numarasi = random.randint(1, 30)
                            while diger_sik_3_numarasi == sekil_numarasi or diger_sik_3_numarasi == diger_sik_2_numarasi or diger_sik_3_numarasi == diger_sik_1_numarasi:
                                diger_sik_3_numarasi = random.randint(1, 30)  # Aynı değerin gelmemesi için

                            cevap_numarasi = random.randint(1, 4)  # Doğru cevap için rastgele bir şık seçilir
                    elif ( 688 < mouse[0] < 1208 and 390 < mouse[1] < 560 ) :
                        if cevap_numarasi == 2 :
                            puan = puan + 100

                            pushed_true = True
                            self.siklar_image_blit(cevap_numarasi, dogru_cevap, notr_cevap, pushed_true)
                            self.cevaplar_image_blit(cevap_numarasi, pushed_true, font, cevap, diger_sik_1, diger_sik_2,
                                                     diger_sik_3, black, renkler, siklar)

                            sekil_numarasi = random.randint(1, 30)  # Rastgele bir bayrak secilir
                            while sekil_numarasi not in random_sekil_numaralari:
                                sekil_numarasi = random.randint(1, 30)  # Rastgele bir bayrak secilir
                            random_sekil_numaralari.remove(
                                sekil_numarasi)  # Bayrağın tekrar seçilmemesi için numarasi listeden çıkarılır

                            kalan_soru_sayisi -= 1
                            pushed_true = False

                            diger_sik_1_numarasi = random.randint(1, 30)
                            while diger_sik_1_numarasi == sekil_numarasi:
                                diger_sik_1_numarasi = random.randint(1, 30)  # Aynı değerin gelmemesi için

                            diger_sik_2_numarasi = random.randint(1, 30)
                            while diger_sik_2_numarasi == sekil_numarasi or diger_sik_2_numarasi == diger_sik_1_numarasi:
                                diger_sik_2_numarasi = random.randint(1, 30)  # Aynı değerin gelmemesi için

                            diger_sik_3_numarasi = random.randint(1, 30)
                            while diger_sik_3_numarasi == sekil_numarasi or diger_sik_3_numarasi == diger_sik_2_numarasi or diger_sik_3_numarasi == diger_sik_1_numarasi:
                                diger_sik_3_numarasi = random.randint(1, 30)  # Aynı değerin gelmemesi için

                            cevap_numarasi = random.randint(1, 4)  # Doğru cevap için rastgele bir şık seçilir
                        else:
                            sekil_numarasi = random.randint(1, 30)  # Rastgele bir bayrak secilir
                            while sekil_numarasi not in random_sekil_numaralari:
                                sekil_numarasi = random.randint(1, 30)  # Rastgele bir bayrak secilir
                            random_sekil_numaralari.remove(
                                sekil_numarasi)  # Bayrağın tekrar seçilmemesi için numarasi listeden çıkarılır

                            kalan_soru_sayisi -= 1
                            pushed_true = False

                            diger_sik_1_numarasi = random.randint(1, 30)
                            while diger_sik_1_numarasi == sekil_numarasi:
                                diger_sik_1_numarasi = random.randint(1, 30)  # Aynı değerin gelmemesi için

                            diger_sik_2_numarasi = random.randint(1, 30)
                            while diger_sik_2_numarasi == sekil_numarasi or diger_sik_2_numarasi == diger_sik_1_numarasi:
                                diger_sik_2_numarasi = random.randint(1, 30)  # Aynı değerin gelmemesi için

                            diger_sik_3_numarasi = random.randint(1, 30)
                            while diger_sik_3_numarasi == sekil_numarasi or diger_sik_3_numarasi == diger_sik_2_numarasi or diger_sik_3_numarasi == diger_sik_1_numarasi:
                                diger_sik_3_numarasi = random.randint(1, 30)  # Aynı değerin gelmemesi için

                            cevap_numarasi = random.randint(1, 4)  # Doğru cevap için rastgele bir şık seçilir
                    elif ( 153 < mouse[0] < 673 and 570 < mouse[1] < 740 ) :
                        if cevap_numarasi == 3 :
                            puan = puan + 100

                            pushed_true = True
                            self.siklar_image_blit(cevap_numarasi, dogru_cevap, notr_cevap, pushed_true)
                            self.cevaplar_image_blit(cevap_numarasi, pushed_true, font, cevap, diger_sik_1, diger_sik_2,
                                                     diger_sik_3, black, renkler, siklar)

                            sekil_numarasi = random.randint(1, 30)  # Rastgele bir bayrak secilir
                            while sekil_numarasi not in random_sekil_numaralari:
                                sekil_numarasi = random.randint(1, 30)  # Rastgele bir bayrak secilir
                            random_sekil_numaralari.remove(
                                sekil_numarasi)  # Bayrağın tekrar seçilmemesi için numarasi listeden çıkarılır

                            kalan_soru_sayisi -= 1
                            pushed_true = False

                            diger_sik_1_numarasi = random.randint(1, 30)
                            while diger_sik_1_numarasi == sekil_numarasi:
                                diger_sik_1_numarasi = random.randint(1, 30)  # Aynı değerin gelmemesi için

                            diger_sik_2_numarasi = random.randint(1, 30)
                            while diger_sik_2_numarasi == sekil_numarasi or diger_sik_2_numarasi == diger_sik_1_numarasi:
                                diger_sik_2_numarasi = random.randint(1, 30)  # Aynı değerin gelmemesi için

                            diger_sik_3_numarasi = random.randint(1, 30)
                            while diger_sik_3_numarasi == sekil_numarasi or diger_sik_3_numarasi == diger_sik_2_numarasi or diger_sik_3_numarasi == diger_sik_1_numarasi:
                                diger_sik_3_numarasi = random.randint(1, 30)  # Aynı değerin gelmemesi için

                            cevap_numarasi = random.randint(1, 4)  # Doğru cevap için rastgele bir şık seçilir
                        else:
                            sekil_numarasi = random.randint(1, 30)  # Rastgele bir bayrak secilir
                            while sekil_numarasi not in random_sekil_numaralari:
                                sekil_numarasi = random.randint(1, 30)  # Rastgele bir bayrak secilir
                            random_sekil_numaralari.remove(
                                sekil_numarasi)  # Bayrağın tekrar seçilmemesi için numarasi listeden çıkarılır

                            kalan_soru_sayisi -= 1
                            pushed_true = False

                            diger_sik_1_numarasi = random.randint(1, 30)
                            while diger_sik_1_numarasi == sekil_numarasi:
                                diger_sik_1_numarasi = random.randint(1, 30)  # Aynı değerin gelmemesi için

                            diger_sik_2_numarasi = random.randint(1, 30)
                            while diger_sik_2_numarasi == sekil_numarasi or diger_sik_2_numarasi == diger_sik_1_numarasi:
                                diger_sik_2_numarasi = random.randint(1, 30)  # Aynı değerin gelmemesi için

                            diger_sik_3_numarasi = random.randint(1, 30)
                            while diger_sik_3_numarasi == sekil_numarasi or diger_sik_3_numarasi == diger_sik_2_numarasi or diger_sik_3_numarasi == diger_sik_1_numarasi:
                                diger_sik_3_numarasi = random.randint(1, 30)  # Aynı değerin gelmemesi için

                            cevap_numarasi = random.randint(1, 4)  # Doğru cevap için rastgele bir şık seçilir
                    elif ( 688 < mouse[0] < 1208 and 570 < mouse[1] < 740 ) :
                        if cevap_numarasi == 4 :
                            puan = puan + 100

                            pushed_true = True
                            self.siklar_image_blit(cevap_numarasi, dogru_cevap, notr_cevap, pushed_true)
                            self.cevaplar_image_blit(cevap_numarasi, pushed_true, font, cevap, diger_sik_1, diger_sik_2,
                                                     diger_sik_3, black, renkler, siklar)

                            sekil_numarasi = random.randint(1, 30)  # Rastgele bir bayrak secilir
                            while sekil_numarasi not in random_sekil_numaralari:
                                sekil_numarasi = random.randint(1, 30)  # Rastgele bir bayrak secilir
                            random_sekil_numaralari.remove(
                                sekil_numarasi)  # Bayrağın tekrar seçilmemesi için numarasi listeden çıkarılır

                            kalan_soru_sayisi -= 1
                            pushed_true = False

                            diger_sik_1_numarasi = random.randint(1, 30)
                            while diger_sik_1_numarasi == sekil_numarasi:
                                diger_sik_1_numarasi = random.randint(1, 30)  # Aynı değerin gelmemesi için

                            diger_sik_2_numarasi = random.randint(1, 30)
                            while diger_sik_2_numarasi == sekil_numarasi or diger_sik_2_numarasi == diger_sik_1_numarasi:
                                diger_sik_2_numarasi = random.randint(1, 30)  # Aynı değerin gelmemesi için

                            diger_sik_3_numarasi = random.randint(1, 30)
                            while diger_sik_3_numarasi == sekil_numarasi or diger_sik_3_numarasi == diger_sik_2_numarasi or diger_sik_3_numarasi == diger_sik_1_numarasi:
                                diger_sik_3_numarasi = random.randint(1, 30)  # Aynı değerin gelmemesi için

                            cevap_numarasi = random.randint(1, 4)  # Doğru cevap için rastgele bir şık seçilir
                        else:
                            sekil_numarasi = random.randint(1, 30)  # Rastgele bir bayrak secilir
                            while sekil_numarasi not in random_sekil_numaralari:
                                sekil_numarasi = random.randint(1, 30)  # Rastgele bir bayrak secilir
                            random_sekil_numaralari.remove(
                                sekil_numarasi)  # Bayrağın tekrar seçilmemesi için numarasi listeden çıkarılır

                            kalan_soru_sayisi -= 1
                            pushed_true = False

                            diger_sik_1_numarasi = random.randint(1, 30)
                            while diger_sik_1_numarasi == sekil_numarasi:
                                diger_sik_1_numarasi = random.randint(1, 30)  # Aynı değerin gelmemesi için

                            diger_sik_2_numarasi = random.randint(1, 30)
                            while diger_sik_2_numarasi == sekil_numarasi or diger_sik_2_numarasi == diger_sik_1_numarasi:
                                diger_sik_2_numarasi = random.randint(1, 30)  # Aynı değerin gelmemesi için

                            diger_sik_3_numarasi = random.randint(1, 30)
                            while diger_sik_3_numarasi == sekil_numarasi or diger_sik_3_numarasi == diger_sik_2_numarasi or diger_sik_3_numarasi == diger_sik_1_numarasi:
                                diger_sik_3_numarasi = random.randint(1, 30)  # Aynı değerin gelmemesi için

                            cevap_numarasi = random.randint(1, 4)  # Doğru cevap için rastgele bir şık seçilir

            if ( len(random_sekil_numaralari) == 0 ):  #Sorular bitince çıkmak için
                get_out = False

            pygame.display.update()

        return puan
    #############################################################################################
    ###########################SEHİR FONKSİYONLARI###############################################
    #############################################################################################

    def sehir_acilis_ekrani(self):
        screen_width = self.screen.get_width()  # ekran genişliği = 1366
        screen_height = self.screen.get_height()  # ekran yüksekliği = 768

        # Arkaplan resmi
        background_image = pygame.image.load(r'C:\Users\CASPER\PycharmProjects\untitled\Sorular_Images\acilis_ekranlari\sehir_acilis_image.jpg')
        background_image = pygame.transform.scale(background_image, (screen_width, screen_height))

        get_out = True

        now = time.time()  # süre basladı
        end_time = now + 2  # iki saniye sonra süre bitecek

        while get_out:  # pencerenin ekranda kalması için gerekli infinite loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()  # bu for dongusu içine bir şey yazılmaz. pencereye basıldıgında hata alınmamasını sağlar
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        sys.exit()

            self.screen.blit(background_image,(0,0))

            if time.time() > end_time:
                get_out = False  # eğer süre aşıldıysa çık

            pygame.display.update()  # pencere update edilir

    ##################################################################################
    ##################################################################################

    def sehir_sorulari(self, quiz_sound):
        LEFT = 1  # mouse sol click

        black = (0,0,0)
        soru_resmi_boyutu = (1060, 380)

        #####################################
        notr_cevap_rengi = (171, 165, 151)
        dogru_cevap_rengi = (57, 255, 20)
        yanlis_cevap_rengi = (255, 8, 10)

        #Şıkların rengi için tuple kullandım
        renkler = ( notr_cevap_rengi , dogru_cevap_rengi , yanlis_cevap_rengi )
        ###########################################
        ###########################################
        birinci_sik_koord = (220,450) #1.şıkkın koordinatları
        ikinci_sik_koord = (755,450) #2.şıkkın koordinatları
        ucuncu_sik_koord = (220,630) #3.şıkkın koordinatları
        dorduncu_sik_koord = (755,630) #4.şıkkın koordinatları

        #rastgele belirlenecek şıklar için tuple kullandım
        siklar = ( birinci_sik_koord , ikinci_sik_koord , ucuncu_sik_koord , dorduncu_sik_koord )
        ############################################
        ############################################
        birinci_sik_renk = renkler[0]
        ikinci_sik_renk = renkler[0]
        ucuncu_sik_renk = renkler[0]
        dorduncu_sik_renk = renkler[0]
        ##Default olarak şıkların rengi belirleniyor##
        ##############################################

        screen_width = self.screen.get_width()  # ekran genişliği = 1366
        screen_height = self.screen.get_height()  # ekran yüksekliği = 768

        # Arkaplan resmi
        background_image = pygame.image.load(r'C:\Users\CASPER\PycharmProjects\untitled\Sorular_Images\background_image.jpg')
        background_image = pygame.transform.scale(background_image, (screen_width, screen_height))

        # Şık kutucuklarının resimleri
        notr_cevap = pygame.image.load(r'C:\Users\CASPER\PycharmProjects\untitled\Sorular_Images\notr_cevap.png')
        notr_cevap = pygame.transform.scale(notr_cevap, (520,170))

        dogru_cevap = pygame.image.load(r'C:\Users\CASPER\PycharmProjects\untitled\Sorular_Images\dogru_cevap.png')
        dogru_cevap = pygame.transform.scale(dogru_cevap, (520,170))

        yanlis_cevap = pygame.image.load(r'C:\Users\CASPER\PycharmProjects\untitled\Sorular_Images\yanlis_cevap.png')
        yanlis_cevap = pygame.transform.scale(yanlis_cevap, (520,170))

        font = pygame.font.SysFont("C:\Windows\Fonts\constanz.ttf", 72, True, True)
                                    # yazı tipi , punto , bold mu , italik mi

        #Rastgele bayrak belirlemek için bir liste açıyoruz
        random_sehir_numaralari = list()
        random_sehir_numaralari = sehir_numara_degerleri

        sehir_numarasi = random.randint(1,15) #Rastgele bir bayrak secilir
        random_sehir_numaralari.remove(sehir_numarasi) #Bayrağın tekrar seçilmemesi için numarasi listeden çıkarılır

        diger_sik_1_numarasi = random.randint(1,15)
        while diger_sik_1_numarasi == sehir_numarasi :
            diger_sik_1_numarasi = random.randint(1,15) #Aynı değerin gelmemesi için

        diger_sik_2_numarasi = random.randint(1,15)
        while diger_sik_2_numarasi == sehir_numarasi or diger_sik_2_numarasi == diger_sik_1_numarasi :
            diger_sik_2_numarasi = random.randint(1,15) #Aynı değerin gelmemesi için

        diger_sik_3_numarasi = random.randint(1,15)
        while diger_sik_3_numarasi == sehir_numarasi or diger_sik_3_numarasi == diger_sik_2_numarasi or diger_sik_3_numarasi == diger_sik_1_numarasi:
            diger_sik_3_numarasi = random.randint(1,15) #Aynı değerin gelmemesi için

        cevap_numarasi = random.randint(1,4) #Doğru cevap için rastgele bir şık seçilir

        kalan_soru_sayisi = 15  #Toplam soru sayısının değeri tutuluyor
        puan = 0

        get_out = True
        pushed_true = False
        pushed_false = False

        while get_out:
            self.screen.blit(background_image, (0, 0))

            sehir_adresi = sehir_numaralar.get(sehir_numarasi)
            diger_sik_1_adresi = sehir_numaralar.get(diger_sik_1_numarasi)
            diger_sik_2_adresi = sehir_numaralar.get(diger_sik_2_numarasi)
            diger_sik_3_adresi = sehir_numaralar.get(diger_sik_3_numarasi)

            soru_resmi = pygame.image.load(sehir_adresi)
            soru_resmi = pygame.transform.scale(soru_resmi, soru_resmi_boyutu)
            self.screen.blit(soru_resmi, pygame.rect.Rect(153,5,1213,385))

            #cevap ve diğer şıkların değerleri alınır
            cevap = sehir_cevaplar.get(sehir_adresi)
            diger_sik_1 = sehir_cevaplar.get(diger_sik_1_adresi)
            diger_sik_2 = sehir_cevaplar.get(diger_sik_2_adresi)
            diger_sik_3 = sehir_cevaplar.get(diger_sik_3_adresi)

            ###############Cevap 1. şıkta####################
            if cevap_numarasi == 1 and pushed_true == True :
                self.siklar_image_blit(cevap_numarasi,dogru_cevap,notr_cevap,pushed_true)
                self.cevaplar_image_blit(cevap_numarasi,pushed_true,font,cevap,diger_sik_1,diger_sik_2,diger_sik_3,black,renkler,siklar)
            elif cevap_numarasi == 1 and pushed_true == False :
                self.siklar_image_blit(cevap_numarasi, dogru_cevap,notr_cevap, pushed_true)
                self.cevaplar_image_blit(cevap_numarasi,pushed_true,font,cevap,diger_sik_1,diger_sik_2,diger_sik_3,black,renkler,siklar)

            ###############Cevap 2. şıkta####################
            if cevap_numarasi == 2 and pushed_true == True :
                self.siklar_image_blit(cevap_numarasi,dogru_cevap,notr_cevap,pushed_true)
                self.cevaplar_image_blit(cevap_numarasi,pushed_true,font,cevap,diger_sik_1,diger_sik_2,diger_sik_3,black,renkler,siklar)
            elif cevap_numarasi == 2 and pushed_true == False :
                self.siklar_image_blit(cevap_numarasi, dogru_cevap,notr_cevap, pushed_true)
                self.cevaplar_image_blit(cevap_numarasi,pushed_true,font,cevap,diger_sik_1,diger_sik_2,diger_sik_3,black,renkler,siklar)

            ###############Cevap 3. şıkta####################
            if cevap_numarasi == 3 and pushed_true == True :
                self.siklar_image_blit(cevap_numarasi, dogru_cevap,notr_cevap, pushed_true)
                self.cevaplar_image_blit(cevap_numarasi,pushed_true,font,cevap,diger_sik_1,diger_sik_2,diger_sik_3,black,renkler,siklar)
            elif cevap_numarasi == 3 and pushed_true == False :
                self.siklar_image_blit(cevap_numarasi, dogru_cevap,notr_cevap, pushed_true)
                self.cevaplar_image_blit(cevap_numarasi,pushed_true,font,cevap,diger_sik_1,diger_sik_2,diger_sik_3,black,renkler,siklar)

            ###############Cevap 4. şıkta####################
            if cevap_numarasi == 4 and pushed_true == True :
                self.siklar_image_blit(cevap_numarasi, dogru_cevap,notr_cevap, pushed_true)
                self.cevaplar_image_blit(cevap_numarasi,pushed_true,font,cevap,diger_sik_1,diger_sik_2,diger_sik_3,black,renkler,siklar)
            elif cevap_numarasi == 4 and pushed_true == False :
                self.siklar_image_blit(cevap_numarasi, dogru_cevap,notr_cevap, pushed_true)
                self.cevaplar_image_blit(cevap_numarasi,pushed_true,font,cevap,diger_sik_1,diger_sik_2,diger_sik_3,black,renkler,siklar)


            ####Mouse click eventi için sorgu işlemleri
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == LEFT:
                    mouse = pygame.mouse.get_pos()

                    if ( 153 < mouse[0] < 673 and 390 < mouse[1] < 560 ) :
                        if cevap_numarasi == 1 :
                            puan = puan + 100

                            pushed_true = True
                            self.siklar_image_blit(cevap_numarasi,dogru_cevap,notr_cevap,pushed_true)
                            self.cevaplar_image_blit(cevap_numarasi,pushed_true,font,cevap,diger_sik_1,diger_sik_2,diger_sik_3,black,renkler,siklar)

                            sehir_numarasi = random.randint(1, 15)  # Rastgele bir bayrak secilir
                            while sehir_numarasi not in random_sehir_numaralari :
                                sehir_numarasi = random.randint(1, 15)  # Rastgele bir bayrak secilir
                            random_sehir_numaralari.remove(sehir_numarasi)  # Bayrağın tekrar seçilmemesi için numarasi listeden çıkarılır

                            kalan_soru_sayisi -= 1
                            pushed_true = False

                            diger_sik_1_numarasi = random.randint(1, 15)
                            while diger_sik_1_numarasi == sehir_numarasi:
                                diger_sik_1_numarasi = random.randint(1, 15)  # Aynı değerin gelmemesi için

                            diger_sik_2_numarasi = random.randint(1, 15)
                            while diger_sik_2_numarasi == sehir_numarasi or diger_sik_2_numarasi == diger_sik_1_numarasi:
                                diger_sik_2_numarasi = random.randint(1, 15)  # Aynı değerin gelmemesi için

                            diger_sik_3_numarasi = random.randint(1, 15)
                            while diger_sik_3_numarasi == sehir_numarasi or diger_sik_3_numarasi == diger_sik_2_numarasi or diger_sik_3_numarasi == diger_sik_1_numarasi:
                                diger_sik_3_numarasi = random.randint(1, 15)  # Aynı değerin gelmemesi için

                            cevap_numarasi = random.randint(1, 4)  # Doğru cevap için rastgele bir şık seçilir
                        else:
                            sehir_numarasi = random.randint(1, 15)  # Rastgele bir bayrak secilir
                            while sehir_numarasi not in random_sehir_numaralari:
                                sehir_numarasi = random.randint(1, 15)  # Rastgele bir bayrak secilir
                            random_sehir_numaralari.remove(sehir_numarasi)  # Bayrağın tekrar seçilmemesi için numarasi listeden çıkarılır

                            kalan_soru_sayisi -= 1
                            pushed_true = False

                            diger_sik_1_numarasi = random.randint(1, 15)
                            while diger_sik_1_numarasi == sehir_numarasi:
                                diger_sik_1_numarasi = random.randint(1, 15)  # Aynı değerin gelmemesi için

                            diger_sik_2_numarasi = random.randint(1, 15)
                            while diger_sik_2_numarasi == sehir_numarasi or diger_sik_2_numarasi == diger_sik_1_numarasi:
                                diger_sik_2_numarasi = random.randint(1, 15)  # Aynı değerin gelmemesi için

                            diger_sik_3_numarasi = random.randint(1, 15)
                            while diger_sik_3_numarasi == sehir_numarasi or diger_sik_3_numarasi == diger_sik_2_numarasi or diger_sik_3_numarasi == diger_sik_1_numarasi:
                                diger_sik_3_numarasi = random.randint(1, 15)  # Aynı değerin gelmemesi için

                            cevap_numarasi = random.randint(1, 4)  # Doğru cevap için rastgele bir şık seçilir

                    elif ( 688 < mouse[0] < 1208 and 390 < mouse[1] < 560 ) :
                        if cevap_numarasi == 2 :
                            puan = puan + 100

                            pushed_true = True
                            self.siklar_image_blit(cevap_numarasi, dogru_cevap, notr_cevap, pushed_true)
                            self.cevaplar_image_blit(cevap_numarasi, pushed_true, font, cevap, diger_sik_1, diger_sik_2,
                                                     diger_sik_3, black, renkler, siklar)

                            sehir_numarasi = random.randint(1, 15)  # Rastgele bir bayrak secilir
                            while sehir_numarasi not in random_sehir_numaralari:
                                sehir_numarasi = random.randint(1, 15)  # Rastgele bir bayrak secilir
                            random_sehir_numaralari.remove(
                                sehir_numarasi)  # Bayrağın tekrar seçilmemesi için numarasi listeden çıkarılır

                            kalan_soru_sayisi -= 1
                            pushed_true = False

                            diger_sik_1_numarasi = random.randint(1, 15)
                            while diger_sik_1_numarasi == sehir_numarasi:
                                diger_sik_1_numarasi = random.randint(1, 15)  # Aynı değerin gelmemesi için

                            diger_sik_2_numarasi = random.randint(1, 15)
                            while diger_sik_2_numarasi == sehir_numarasi or diger_sik_2_numarasi == diger_sik_1_numarasi:
                                diger_sik_2_numarasi = random.randint(1, 15)  # Aynı değerin gelmemesi için

                            diger_sik_3_numarasi = random.randint(1, 15)
                            while diger_sik_3_numarasi == sehir_numarasi or diger_sik_3_numarasi == diger_sik_2_numarasi or diger_sik_3_numarasi == diger_sik_1_numarasi:
                                diger_sik_3_numarasi = random.randint(1, 15)  # Aynı değerin gelmemesi için

                            cevap_numarasi = random.randint(1, 4)  # Doğru cevap için rastgele bir şık seçilir
                        else:
                            sehir_numarasi = random.randint(1, 15)  # Rastgele bir bayrak secilir
                            while sehir_numarasi not in random_sehir_numaralari:
                                sehir_numarasi = random.randint(1, 15)  # Rastgele bir bayrak secilir
                            random_sehir_numaralari.remove(
                                sehir_numarasi)  # Bayrağın tekrar seçilmemesi için numarasi listeden çıkarılır

                            kalan_soru_sayisi -= 1
                            pushed_true = False

                            diger_sik_1_numarasi = random.randint(1, 15)
                            while diger_sik_1_numarasi == sehir_numarasi:
                                diger_sik_1_numarasi = random.randint(1, 15)  # Aynı değerin gelmemesi için

                            diger_sik_2_numarasi = random.randint(1, 15)
                            while diger_sik_2_numarasi == sehir_numarasi or diger_sik_2_numarasi == diger_sik_1_numarasi:
                                diger_sik_2_numarasi = random.randint(1, 15)  # Aynı değerin gelmemesi için

                            diger_sik_3_numarasi = random.randint(1, 15)
                            while diger_sik_3_numarasi == sehir_numarasi or diger_sik_3_numarasi == diger_sik_2_numarasi or diger_sik_3_numarasi == diger_sik_1_numarasi:
                                diger_sik_3_numarasi = random.randint(1, 15)  # Aynı değerin gelmemesi için

                            cevap_numarasi = random.randint(1, 4)  # Doğru cevap için rastgele bir şık seçilir

                    elif ( 153 < mouse[0] < 673 and 570 < mouse[1] < 740 ) :
                        if cevap_numarasi == 3 :
                            puan = puan + 100

                            pushed_true = True
                            self.siklar_image_blit(cevap_numarasi, dogru_cevap, notr_cevap, pushed_true)
                            self.cevaplar_image_blit(cevap_numarasi, pushed_true, font, cevap, diger_sik_1, diger_sik_2,
                                                     diger_sik_3, black, renkler, siklar)

                            sehir_numarasi = random.randint(1, 15)  # Rastgele bir bayrak secilir
                            while sehir_numarasi not in random_sehir_numaralari:
                                sehir_numarasi = random.randint(1, 15)  # Rastgele bir bayrak secilir
                            random_sehir_numaralari.remove(
                                sehir_numarasi)  # Bayrağın tekrar seçilmemesi için numarasi listeden çıkarılır

                            kalan_soru_sayisi -= 1
                            pushed_true = False

                            diger_sik_1_numarasi = random.randint(1, 15)
                            while diger_sik_1_numarasi == sehir_numarasi:
                                diger_sik_1_numarasi = random.randint(1, 15)  # Aynı değerin gelmemesi için

                            diger_sik_2_numarasi = random.randint(1, 15)
                            while diger_sik_2_numarasi == sehir_numarasi or diger_sik_2_numarasi == diger_sik_1_numarasi:
                                diger_sik_2_numarasi = random.randint(1, 15)  # Aynı değerin gelmemesi için

                            diger_sik_3_numarasi = random.randint(1, 15)
                            while diger_sik_3_numarasi == sehir_numarasi or diger_sik_3_numarasi == diger_sik_2_numarasi or diger_sik_3_numarasi == diger_sik_1_numarasi:
                                diger_sik_3_numarasi = random.randint(1, 15)  # Aynı değerin gelmemesi için

                            cevap_numarasi = random.randint(1, 4)  # Doğru cevap için rastgele bir şık seçilir
                        else:
                            sehir_numarasi = random.randint(1, 15)  # Rastgele bir bayrak secilir
                            while sehir_numarasi not in random_sehir_numaralari:
                                sehir_numarasi = random.randint(1, 15)  # Rastgele bir bayrak secilir
                            random_sehir_numaralari.remove(
                                sehir_numarasi)  # Bayrağın tekrar seçilmemesi için numarasi listeden çıkarılır

                            kalan_soru_sayisi -= 1
                            pushed_true = False

                            diger_sik_1_numarasi = random.randint(1, 15)
                            while diger_sik_1_numarasi == sehir_numarasi:
                                diger_sik_1_numarasi = random.randint(1, 15)  # Aynı değerin gelmemesi için

                            diger_sik_2_numarasi = random.randint(1, 15)
                            while diger_sik_2_numarasi == sehir_numarasi or diger_sik_2_numarasi == diger_sik_1_numarasi:
                                diger_sik_2_numarasi = random.randint(1, 15)  # Aynı değerin gelmemesi için

                            diger_sik_3_numarasi = random.randint(1, 15)
                            while diger_sik_3_numarasi == sehir_numarasi or diger_sik_3_numarasi == diger_sik_2_numarasi or diger_sik_3_numarasi == diger_sik_1_numarasi:
                                diger_sik_3_numarasi = random.randint(1, 15)  # Aynı değerin gelmemesi için

                            cevap_numarasi = random.randint(1, 4)  # Doğru cevap için rastgele bir şık seçilir

                    elif ( 688 < mouse[0] < 1208 and 570 < mouse[1] < 740 ) :
                        if cevap_numarasi == 4 :
                            puan = puan + 100

                            pushed_true = True
                            self.siklar_image_blit(cevap_numarasi, dogru_cevap, notr_cevap, pushed_true)
                            self.cevaplar_image_blit(cevap_numarasi, pushed_true, font, cevap, diger_sik_1, diger_sik_2,
                                                     diger_sik_3, black, renkler, siklar)

                            sehir_numarasi = random.randint(1, 15)  # Rastgele bir bayrak secilir
                            while sehir_numarasi not in random_sehir_numaralari:
                                sehir_numarasi = random.randint(1, 15)  # Rastgele bir bayrak secilir
                            random_sehir_numaralari.remove(
                                sehir_numarasi)  # Bayrağın tekrar seçilmemesi için numarasi listeden çıkarılır

                            kalan_soru_sayisi -= 1
                            pushed_true = False

                            diger_sik_1_numarasi = random.randint(1, 15)
                            while diger_sik_1_numarasi == sehir_numarasi:
                                diger_sik_1_numarasi = random.randint(1, 15)  # Aynı değerin gelmemesi için

                            diger_sik_2_numarasi = random.randint(1, 15)
                            while diger_sik_2_numarasi == sehir_numarasi or diger_sik_2_numarasi == diger_sik_1_numarasi:
                                diger_sik_2_numarasi = random.randint(1, 15)  # Aynı değerin gelmemesi için

                            diger_sik_3_numarasi = random.randint(1, 15)
                            while diger_sik_3_numarasi == sehir_numarasi or diger_sik_3_numarasi == diger_sik_2_numarasi or diger_sik_3_numarasi == diger_sik_1_numarasi:
                                diger_sik_3_numarasi = random.randint(1,15)  # Aynı değerin gelmemesi için

                            cevap_numarasi = random.randint(1, 4)  # Doğru cevap için rastgele bir şık seçilir
                        else:
                            sehir_numarasi = random.randint(1, 15)  # Rastgele bir bayrak secilir
                            while sehir_numarasi not in random_sehir_numaralari:
                                sehir_numarasi = random.randint(1, 15)  # Rastgele bir bayrak secilir
                            random_sehir_numaralari.remove(
                                sehir_numarasi)  # Bayrağın tekrar seçilmemesi için numarasi listeden çıkarılır

                            kalan_soru_sayisi -= 1
                            pushed_true = False

                            diger_sik_1_numarasi = random.randint(1, 15)
                            while diger_sik_1_numarasi == sehir_numarasi:
                                diger_sik_1_numarasi = random.randint(1, 15)  # Aynı değerin gelmemesi için

                            diger_sik_2_numarasi = random.randint(1, 15)
                            while diger_sik_2_numarasi == sehir_numarasi or diger_sik_2_numarasi == diger_sik_1_numarasi:
                                diger_sik_2_numarasi = random.randint(1, 15)  # Aynı değerin gelmemesi için

                            diger_sik_3_numarasi = random.randint(1, 15)
                            while diger_sik_3_numarasi == sehir_numarasi or diger_sik_3_numarasi == diger_sik_2_numarasi or diger_sik_3_numarasi == diger_sik_1_numarasi:
                                diger_sik_3_numarasi = random.randint(1, 15)  # Aynı değerin gelmemesi için

                            cevap_numarasi = random.randint(1, 4)  # Doğru cevap için rastgele bir şık seçilir

            if ( len(random_sehir_numaralari) == 0 ):  #Sorular bitince çıkmak için
                get_out = False

            pygame.display.update()

        return puan

    #############################################################################################
    ###########################COGRAFYA FONKSİYONLARI###############################################
    #############################################################################################

    def cografya_acilis_ekrani(self):
        screen_width = self.screen.get_width()  # ekran genişliği = 1366
        screen_height = self.screen.get_height()  # ekran yüksekliği = 768

        # Arkaplan resmi
        background_image = pygame.image.load(
            r'C:\Users\CASPER\PycharmProjects\untitled\Sorular_Images\acilis_ekranlari\cografya_acilis_image.jpg')
        background_image = pygame.transform.scale(background_image, (screen_width, screen_height))

        get_out = True

        now = time.time()  # süre basladı
        end_time = now + 2  # iki saniye sonra süre bitecek

        while get_out:  # pencerenin ekranda kalması için gerekli infinite loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()  # bu for dongusu içine bir şey yazılmaz. pencereye basıldıgında hata alınmamasını sağlar
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        sys.exit()

            self.screen.blit(background_image, (0, 0))

            if time.time() > end_time:
                get_out = False  # eğer süre aşıldıysa çık

            pygame.display.update()  # pencere update edilir

    ##################################################################################
    ##################################################################################

    def cografya_sorulari(self, quiz_sound):
        LEFT = 1  # mouse sol click

        black = (0,0,0)
        soru_resmi_boyutu = (1060, 380)

        #####################################
        notr_cevap_rengi = (171, 165, 151)
        dogru_cevap_rengi = (57, 255, 20)
        yanlis_cevap_rengi = (255, 8, 10)

        #Şıkların rengi için tuple kullandım
        renkler = ( notr_cevap_rengi , dogru_cevap_rengi , yanlis_cevap_rengi )
        ###########################################
        ###########################################
        birinci_sik_koord = (220,450) #1.şıkkın koordinatları
        ikinci_sik_koord = (755,450) #2.şıkkın koordinatları
        ucuncu_sik_koord = (220,630) #3.şıkkın koordinatları
        dorduncu_sik_koord = (755,630) #4.şıkkın koordinatları

        #rastgele belirlenecek şıklar için tuple kullandım
        siklar = ( birinci_sik_koord , ikinci_sik_koord , ucuncu_sik_koord , dorduncu_sik_koord )
        ############################################
        ############################################
        birinci_sik_renk = renkler[0]
        ikinci_sik_renk = renkler[0]
        ucuncu_sik_renk = renkler[0]
        dorduncu_sik_renk = renkler[0]
        ##Default olarak şıkların rengi belirleniyor##
        ##############################################

        screen_width = self.screen.get_width()  # ekran genişliği = 1366
        screen_height = self.screen.get_height()  # ekran yüksekliği = 768

        # Arkaplan resmi
        background_image = pygame.image.load(r'C:\Users\CASPER\PycharmProjects\untitled\Sorular_Images\background_image.jpg')
        background_image = pygame.transform.scale(background_image, (screen_width, screen_height))

        # Şık kutucuklarının resimleri
        notr_cevap = pygame.image.load(r'C:\Users\CASPER\PycharmProjects\untitled\Sorular_Images\notr_cevap.png')
        notr_cevap = pygame.transform.scale(notr_cevap, (520,170))

        dogru_cevap = pygame.image.load(r'C:\Users\CASPER\PycharmProjects\untitled\Sorular_Images\dogru_cevap.png')
        dogru_cevap = pygame.transform.scale(dogru_cevap, (520,170))

        yanlis_cevap = pygame.image.load(r'C:\Users\CASPER\PycharmProjects\untitled\Sorular_Images\yanlis_cevap.png')
        yanlis_cevap = pygame.transform.scale(yanlis_cevap, (520,170))

        font = pygame.font.SysFont("C:\Windows\Fonts\constanz.ttf", 72, True, True)
                                    # yazı tipi , punto , bold mu , italik mi

        #Rastgele bayrak belirlemek için bir liste açıyoruz
        random_cografya_numaralari = list()
        random_cografya_numaralari = cografya_numara_degerleri

        cografya_numarasi = random.randint(1,15) #Rastgele bir bayrak secilir
        random_cografya_numaralari.remove(cografya_numarasi) #Bayrağın tekrar seçilmemesi için numarasi listeden çıkarılır

        diger_sik_1_numarasi = random.randint(1,15)
        while diger_sik_1_numarasi == cografya_numarasi :
            diger_sik_1_numarasi = random.randint(1,15) #Aynı değerin gelmemesi için

        diger_sik_2_numarasi = random.randint(1,15)
        while diger_sik_2_numarasi == cografya_numarasi or diger_sik_2_numarasi == diger_sik_1_numarasi :
            diger_sik_2_numarasi = random.randint(1,15) #Aynı değerin gelmemesi için

        diger_sik_3_numarasi = random.randint(1,15)
        while diger_sik_3_numarasi == cografya_numarasi or diger_sik_3_numarasi == diger_sik_2_numarasi or diger_sik_3_numarasi == diger_sik_1_numarasi:
            diger_sik_3_numarasi = random.randint(1,15) #Aynı değerin gelmemesi için

        cevap_numarasi = random.randint(1,4) #Doğru cevap için rastgele bir şık seçilir

        kalan_soru_sayisi = 15  #Toplam soru sayısının değeri tutuluyor
        puan = 0

        get_out = True
        pushed_true = False
        pushed_false = False

        while get_out:
            self.screen.blit(background_image, (0, 0))

            cografya_adresi = cografya_numaralar.get(cografya_numarasi)
            diger_sik_1_adresi = cografya_numaralar.get(diger_sik_1_numarasi)
            diger_sik_2_adresi = cografya_numaralar.get(diger_sik_2_numarasi)
            diger_sik_3_adresi = cografya_numaralar.get(diger_sik_3_numarasi)

            soru_resmi = pygame.image.load(cografya_adresi)
            soru_resmi = pygame.transform.scale(soru_resmi, soru_resmi_boyutu)
            self.screen.blit(soru_resmi, pygame.rect.Rect(153,5,1213,385))

            #cevap ve diğer şıkların değerleri alınır
            cevap = cografya_cevaplar.get(cografya_adresi)
            diger_sik_1 = cografya_cevaplar.get(diger_sik_1_adresi)
            diger_sik_2 = cografya_cevaplar.get(diger_sik_2_adresi)
            diger_sik_3 = cografya_cevaplar.get(diger_sik_3_adresi)

            ###############Cevap 1. şıkta####################
            if cevap_numarasi == 1 and pushed_true == True :
                self.siklar_image_blit(cevap_numarasi,dogru_cevap,notr_cevap,pushed_true)
                self.cevaplar_image_blit(cevap_numarasi,pushed_true,font,cevap,diger_sik_1,diger_sik_2,diger_sik_3,black,renkler,siklar)
            elif cevap_numarasi == 1 and pushed_true == False :
                self.siklar_image_blit(cevap_numarasi, dogru_cevap,notr_cevap, pushed_true)
                self.cevaplar_image_blit(cevap_numarasi,pushed_true,font,cevap,diger_sik_1,diger_sik_2,diger_sik_3,black,renkler,siklar)

            ###############Cevap 2. şıkta####################
            if cevap_numarasi == 2 and pushed_true == True :
                self.siklar_image_blit(cevap_numarasi,dogru_cevap,notr_cevap,pushed_true)
                self.cevaplar_image_blit(cevap_numarasi,pushed_true,font,cevap,diger_sik_1,diger_sik_2,diger_sik_3,black,renkler,siklar)
            elif cevap_numarasi == 2 and pushed_true == False :
                self.siklar_image_blit(cevap_numarasi, dogru_cevap,notr_cevap, pushed_true)
                self.cevaplar_image_blit(cevap_numarasi,pushed_true,font,cevap,diger_sik_1,diger_sik_2,diger_sik_3,black,renkler,siklar)

            ###############Cevap 3. şıkta####################
            if cevap_numarasi == 3 and pushed_true == True :
                self.siklar_image_blit(cevap_numarasi, dogru_cevap,notr_cevap, pushed_true)
                self.cevaplar_image_blit(cevap_numarasi,pushed_true,font,cevap,diger_sik_1,diger_sik_2,diger_sik_3,black,renkler,siklar)
            elif cevap_numarasi == 3 and pushed_true == False :
                self.siklar_image_blit(cevap_numarasi, dogru_cevap,notr_cevap, pushed_true)
                self.cevaplar_image_blit(cevap_numarasi,pushed_true,font,cevap,diger_sik_1,diger_sik_2,diger_sik_3,black,renkler,siklar)

            ###############Cevap 4. şıkta####################
            if cevap_numarasi == 4 and pushed_true == True :
                self.siklar_image_blit(cevap_numarasi, dogru_cevap,notr_cevap, pushed_true)
                self.cevaplar_image_blit(cevap_numarasi,pushed_true,font,cevap,diger_sik_1,diger_sik_2,diger_sik_3,black,renkler,siklar)
            elif cevap_numarasi == 4 and pushed_true == False :
                self.siklar_image_blit(cevap_numarasi, dogru_cevap,notr_cevap, pushed_true)
                self.cevaplar_image_blit(cevap_numarasi,pushed_true,font,cevap,diger_sik_1,diger_sik_2,diger_sik_3,black,renkler,siklar)


            ####Mouse click eventi için sorgu işlemleri
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == LEFT:
                    mouse = pygame.mouse.get_pos()

                    if ( 153 < mouse[0] < 673 and 390 < mouse[1] < 560 ) :
                        if cevap_numarasi == 1 :
                            puan = puan + 100

                            pushed_true = True
                            self.siklar_image_blit(cevap_numarasi,dogru_cevap,notr_cevap,pushed_true)
                            self.cevaplar_image_blit(cevap_numarasi,pushed_true,font,cevap,diger_sik_1,diger_sik_2,diger_sik_3,black,renkler,siklar)

                            cografya_numarasi = random.randint(1, 15)  # Rastgele bir bayrak secilir
                            while cografya_numarasi not in random_cografya_numaralari :
                                cografya_numarasi = random.randint(1, 15)  # Rastgele bir bayrak secilir
                            random_cografya_numaralari.remove(cografya_numarasi)  # Bayrağın tekrar seçilmemesi için numarasi listeden çıkarılır

                            kalan_soru_sayisi -= 1
                            pushed_true = False

                            diger_sik_1_numarasi = random.randint(1, 15)
                            while diger_sik_1_numarasi == cografya_numarasi:
                                diger_sik_1_numarasi = random.randint(1, 15)  # Aynı değerin gelmemesi için

                            diger_sik_2_numarasi = random.randint(1, 15)
                            while diger_sik_2_numarasi == cografya_numarasi or diger_sik_2_numarasi == diger_sik_1_numarasi:
                                diger_sik_2_numarasi = random.randint(1, 15)  # Aynı değerin gelmemesi için

                            diger_sik_3_numarasi = random.randint(1, 15)
                            while diger_sik_3_numarasi == cografya_numarasi or diger_sik_3_numarasi == diger_sik_2_numarasi or diger_sik_3_numarasi == diger_sik_1_numarasi:
                                diger_sik_3_numarasi = random.randint(1, 15)  # Aynı değerin gelmemesi için

                            cevap_numarasi = random.randint(1, 4)  # Doğru cevap için rastgele bir şık seçilir
                        else:
                            cografya_numarasi = random.randint(1, 15)  # Rastgele bir bayrak secilir
                            while cografya_numarasi not in random_cografya_numaralari:
                                cografya_numarasi = random.randint(1, 15)  # Rastgele bir bayrak secilir
                            random_cografya_numaralari.remove(cografya_numarasi)  # Bayrağın tekrar seçilmemesi için numarasi listeden çıkarılır

                            kalan_soru_sayisi -= 1
                            pushed_true = False

                            diger_sik_1_numarasi = random.randint(1, 15)
                            while diger_sik_1_numarasi == cografya_numarasi:
                                diger_sik_1_numarasi = random.randint(1, 15)  # Aynı değerin gelmemesi için

                            diger_sik_2_numarasi = random.randint(1, 15)
                            while diger_sik_2_numarasi == cografya_numarasi or diger_sik_2_numarasi == diger_sik_1_numarasi:
                                diger_sik_2_numarasi = random.randint(1, 15)  # Aynı değerin gelmemesi için

                            diger_sik_3_numarasi = random.randint(1, 15)
                            while diger_sik_3_numarasi == cografya_numarasi or diger_sik_3_numarasi == diger_sik_2_numarasi or diger_sik_3_numarasi == diger_sik_1_numarasi:
                                diger_sik_3_numarasi = random.randint(1, 15)  # Aynı değerin gelmemesi için

                            cevap_numarasi = random.randint(1, 4)  # Doğru cevap için rastgele bir şık seçilir

                    elif ( 688 < mouse[0] < 1208 and 390 < mouse[1] < 560 ) :
                        if cevap_numarasi == 2 :
                            puan = puan + 100

                            pushed_true = True
                            self.siklar_image_blit(cevap_numarasi, dogru_cevap, notr_cevap, pushed_true)
                            self.cevaplar_image_blit(cevap_numarasi, pushed_true, font, cevap, diger_sik_1, diger_sik_2,
                                                     diger_sik_3, black, renkler, siklar)

                            cografya_numarasi = random.randint(1, 15)  # Rastgele bir bayrak secilir
                            while cografya_numarasi not in random_cografya_numaralari:
                                cografya_numarasi = random.randint(1, 15)  # Rastgele bir bayrak secilir
                            random_cografya_numaralari.remove(
                                cografya_numarasi)  # Bayrağın tekrar seçilmemesi için numarasi listeden çıkarılır

                            kalan_soru_sayisi -= 1
                            pushed_true = False

                            diger_sik_1_numarasi = random.randint(1, 15)
                            while diger_sik_1_numarasi == cografya_numarasi:
                                diger_sik_1_numarasi = random.randint(1, 15)  # Aynı değerin gelmemesi için

                            diger_sik_2_numarasi = random.randint(1, 15)
                            while diger_sik_2_numarasi == cografya_numarasi or diger_sik_2_numarasi == diger_sik_1_numarasi:
                                diger_sik_2_numarasi = random.randint(1, 15)  # Aynı değerin gelmemesi için

                            diger_sik_3_numarasi = random.randint(1, 15)
                            while diger_sik_3_numarasi == cografya_numarasi or diger_sik_3_numarasi == diger_sik_2_numarasi or diger_sik_3_numarasi == diger_sik_1_numarasi:
                                diger_sik_3_numarasi = random.randint(1, 15)  # Aynı değerin gelmemesi için

                            cevap_numarasi = random.randint(1, 4)  # Doğru cevap için rastgele bir şık seçilir
                        else:
                            cografya_numarasi = random.randint(1, 15)  # Rastgele bir bayrak secilir
                            while cografya_numarasi not in random_cografya_numaralari:
                                cografya_numarasi = random.randint(1, 15)  # Rastgele bir bayrak secilir
                            random_cografya_numaralari.remove(
                                cografya_numarasi)  # Bayrağın tekrar seçilmemesi için numarasi listeden çıkarılır

                            kalan_soru_sayisi -= 1
                            pushed_true = False

                            diger_sik_1_numarasi = random.randint(1, 15)
                            while diger_sik_1_numarasi == cografya_numarasi:
                                diger_sik_1_numarasi = random.randint(1, 15)  # Aynı değerin gelmemesi için

                            diger_sik_2_numarasi = random.randint(1, 15)
                            while diger_sik_2_numarasi == cografya_numarasi or diger_sik_2_numarasi == diger_sik_1_numarasi:
                                diger_sik_2_numarasi = random.randint(1, 15)  # Aynı değerin gelmemesi için

                            diger_sik_3_numarasi = random.randint(1, 15)
                            while diger_sik_3_numarasi == cografya_numarasi or diger_sik_3_numarasi == diger_sik_2_numarasi or diger_sik_3_numarasi == diger_sik_1_numarasi:
                                diger_sik_3_numarasi = random.randint(1, 15)  # Aynı değerin gelmemesi için

                            cevap_numarasi = random.randint(1, 4)  # Doğru cevap için rastgele bir şık seçilir

                    elif ( 153 < mouse[0] < 673 and 570 < mouse[1] < 740 ) :
                        if cevap_numarasi == 3 :
                            puan = puan + 100

                            pushed_true = True
                            self.siklar_image_blit(cevap_numarasi, dogru_cevap, notr_cevap, pushed_true)
                            self.cevaplar_image_blit(cevap_numarasi, pushed_true, font, cevap, diger_sik_1, diger_sik_2,
                                                     diger_sik_3, black, renkler, siklar)

                            cografya_numarasi = random.randint(1, 15)  # Rastgele bir bayrak secilir
                            while cografya_numarasi not in random_cografya_numaralari:
                                cografya_numarasi = random.randint(1, 15)  # Rastgele bir bayrak secilir
                            random_cografya_numaralari.remove(
                                cografya_numarasi)  # Bayrağın tekrar seçilmemesi için numarasi listeden çıkarılır

                            kalan_soru_sayisi -= 1
                            pushed_true = False

                            diger_sik_1_numarasi = random.randint(1, 15)
                            while diger_sik_1_numarasi == cografya_numarasi:
                                diger_sik_1_numarasi = random.randint(1, 15)  # Aynı değerin gelmemesi için

                            diger_sik_2_numarasi = random.randint(1, 15)
                            while diger_sik_2_numarasi == cografya_numarasi or diger_sik_2_numarasi == diger_sik_1_numarasi:
                                diger_sik_2_numarasi = random.randint(1, 15)  # Aynı değerin gelmemesi için

                            diger_sik_3_numarasi = random.randint(1, 15)
                            while diger_sik_3_numarasi == cografya_numarasi or diger_sik_3_numarasi == diger_sik_2_numarasi or diger_sik_3_numarasi == diger_sik_1_numarasi:
                                diger_sik_3_numarasi = random.randint(1, 15)  # Aynı değerin gelmemesi için

                            cevap_numarasi = random.randint(1, 4)  # Doğru cevap için rastgele bir şık seçilir
                        else:
                            cografya_numarasi = random.randint(1, 15)  # Rastgele bir bayrak secilir
                            while cografya_numarasi not in random_cografya_numaralari:
                                cografya_numarasi = random.randint(1, 15)  # Rastgele bir bayrak secilir
                            random_cografya_numaralari.remove(
                                cografya_numarasi)  # Bayrağın tekrar seçilmemesi için numarasi listeden çıkarılır

                            kalan_soru_sayisi -= 1
                            pushed_true = False

                            diger_sik_1_numarasi = random.randint(1, 15)
                            while diger_sik_1_numarasi == cografya_numarasi:
                                diger_sik_1_numarasi = random.randint(1, 15)  # Aynı değerin gelmemesi için

                            diger_sik_2_numarasi = random.randint(1, 15)
                            while diger_sik_2_numarasi == cografya_numarasi or diger_sik_2_numarasi == diger_sik_1_numarasi:
                                diger_sik_2_numarasi = random.randint(1, 15)  # Aynı değerin gelmemesi için

                            diger_sik_3_numarasi = random.randint(1, 15)
                            while diger_sik_3_numarasi == cografya_numarasi or diger_sik_3_numarasi == diger_sik_2_numarasi or diger_sik_3_numarasi == diger_sik_1_numarasi:
                                diger_sik_3_numarasi = random.randint(1, 15)  # Aynı değerin gelmemesi için

                            cevap_numarasi = random.randint(1, 4)  # Doğru cevap için rastgele bir şık seçilir

                    elif ( 688 < mouse[0] < 1208 and 570 < mouse[1] < 740 ) :
                        if cevap_numarasi == 4 :
                            puan = puan + 100

                            pushed_true = True
                            self.siklar_image_blit(cevap_numarasi, dogru_cevap, notr_cevap, pushed_true)
                            self.cevaplar_image_blit(cevap_numarasi, pushed_true, font, cevap, diger_sik_1, diger_sik_2,
                                                     diger_sik_3, black, renkler, siklar)

                            cografya_numarasi = random.randint(1, 15)  # Rastgele bir bayrak secilir
                            while cografya_numarasi not in random_cografya_numaralari:
                                cografya_numarasi = random.randint(1, 15)  # Rastgele bir bayrak secilir
                            random_cografya_numaralari.remove(
                                cografya_numarasi)  # Bayrağın tekrar seçilmemesi için numarasi listeden çıkarılır

                            kalan_soru_sayisi -= 1
                            pushed_true = False

                            diger_sik_1_numarasi = random.randint(1, 15)
                            while diger_sik_1_numarasi == cografya_numarasi:
                                diger_sik_1_numarasi = random.randint(1, 15)  # Aynı değerin gelmemesi için

                            diger_sik_2_numarasi = random.randint(1, 15)
                            while diger_sik_2_numarasi == cografya_numarasi or diger_sik_2_numarasi == diger_sik_1_numarasi:
                                diger_sik_2_numarasi = random.randint(1, 15)  # Aynı değerin gelmemesi için

                            diger_sik_3_numarasi = random.randint(1, 15)
                            while diger_sik_3_numarasi == cografya_numarasi or diger_sik_3_numarasi == diger_sik_2_numarasi or diger_sik_3_numarasi == diger_sik_1_numarasi:
                                diger_sik_3_numarasi = random.randint(1, 15)  # Aynı değerin gelmemesi için

                            cevap_numarasi = random.randint(1, 4)  # Doğru cevap için rastgele bir şık seçilir
                        else:
                            cografya_numarasi = random.randint(1, 15)  # Rastgele bir bayrak secilir
                            while cografya_numarasi not in random_cografya_numaralari:
                                cografya_numarasi = random.randint(1, 15)  # Rastgele bir bayrak secilir
                            random_cografya_numaralari.remove(
                                cografya_numarasi)  # Bayrağın tekrar seçilmemesi için numarasi listeden çıkarılır

                            kalan_soru_sayisi -= 1
                            pushed_true = False

                            diger_sik_1_numarasi = random.randint(1, 15)
                            while diger_sik_1_numarasi == cografya_numarasi:
                                diger_sik_1_numarasi = random.randint(1, 15)  # Aynı değerin gelmemesi için

                            diger_sik_2_numarasi = random.randint(1, 15)
                            while diger_sik_2_numarasi == cografya_numarasi or diger_sik_2_numarasi == diger_sik_1_numarasi:
                                diger_sik_2_numarasi = random.randint(1, 15)  # Aynı değerin gelmemesi için

                            diger_sik_3_numarasi = random.randint(1, 15)
                            while diger_sik_3_numarasi == cografya_numarasi or diger_sik_3_numarasi == diger_sik_2_numarasi or diger_sik_3_numarasi == diger_sik_1_numarasi:
                                diger_sik_3_numarasi = random.randint(1, 15)  # Aynı değerin gelmemesi için

                            cevap_numarasi = random.randint(1, 4)  # Doğru cevap için rastgele bir şık seçilir

            if ( len(random_cografya_numaralari) == 0 ):  #Sorular bitince çıkmak için
                get_out = False

            pygame.display.update()

        return puan

    ###############################################################################################
    ##########################Mimari Fonksiyonlari#################################################
    ###############################################################################################

    def mimari_acilis_ekrani(self):
        screen_width = self.screen.get_width()  # ekran genişliği = 1366
        screen_height = self.screen.get_height()  # ekran yüksekliği = 768

        # Arkaplan resmi
        background_image = pygame.image.load(r'C:\Users\CASPER\PycharmProjects\untitled\Sorular_Images\acilis_ekranlari\mimari_acilis_image.jpg')
        background_image = pygame.transform.scale(background_image, (screen_width, screen_height))

        get_out = True

        now = time.time()  # süre basladı
        end_time = now + 2  # iki saniye sonra süre bitecek

        while get_out:  # pencerenin ekranda kalması için gerekli infinite loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()  # bu for dongusu içine bir şey yazılmaz. pencereye basıldıgında hata alınmamasını sağlar
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        sys.exit()

            self.screen.blit(background_image,(0,0))

            if time.time() > end_time:
                get_out = False  # eğer süre aşıldıysa çık

            pygame.display.update()  # pencere update edilir

    def mimari_sorulari(self, quiz_sound):
        LEFT = 1  # mouse sol click

        black = (0,0,0)
        soru_resmi_boyutu = (435, 290)

        #####################################
        notr_cevap_rengi = (171, 165, 151)
        dogru_cevap_rengi = (57, 255, 20)
        yanlis_cevap_rengi = (255, 8, 10)

        #Şıkların rengi için tuple kullandım
        renkler = ( notr_cevap_rengi , dogru_cevap_rengi , yanlis_cevap_rengi )
        ###########################################
        ###########################################
        birinci_sik_koord = (220,450) #1.şıkkın koordinatları
        ikinci_sik_koord = (755,450) #2.şıkkın koordinatları
        ucuncu_sik_koord = (220,630) #3.şıkkın koordinatları
        dorduncu_sik_koord = (755,630) #4.şıkkın koordinatları

        #rastgele belirlenecek şıklar için tuple kullandım
        siklar = ( birinci_sik_koord , ikinci_sik_koord , ucuncu_sik_koord , dorduncu_sik_koord )
        ############################################
        ############################################
        birinci_sik_renk = renkler[0]
        ikinci_sik_renk = renkler[0]
        ucuncu_sik_renk = renkler[0]
        dorduncu_sik_renk = renkler[0]
        ##Default olarak şıkların rengi belirleniyor##
        ##############################################

        screen_width = self.screen.get_width()  # ekran genişliği = 1366
        screen_height = self.screen.get_height()  # ekran yüksekliği = 768

        # Arkaplan resmi
        background_image = pygame.image.load(r'C:\Users\CASPER\PycharmProjects\untitled\Sorular_Images\background_image.jpg')
        background_image = pygame.transform.scale(background_image, (screen_width, screen_height))

        # Soru kutucugu resmi
        soru_kutucugu = pygame.image.load(r'C:\Users\CASPER\PycharmProjects\untitled\Sorular_Images\soru.png')
        soru_kutucugu = pygame.transform.scale(soru_kutucugu, (1060,380))

        # Şık kutucuklarının resimleri
        notr_cevap = pygame.image.load(r'C:\Users\CASPER\PycharmProjects\untitled\Sorular_Images\notr_cevap.png')
        notr_cevap = pygame.transform.scale(notr_cevap, (520,170))

        dogru_cevap = pygame.image.load(r'C:\Users\CASPER\PycharmProjects\untitled\Sorular_Images\dogru_cevap.png')
        dogru_cevap = pygame.transform.scale(dogru_cevap, (520,170))

        yanlis_cevap = pygame.image.load(r'C:\Users\CASPER\PycharmProjects\untitled\Sorular_Images\yanlis_cevap.png')
        yanlis_cevap = pygame.transform.scale(yanlis_cevap, (520,170))

        font = pygame.font.SysFont("C:\Windows\Fonts\constanz.ttf", 72, True, True)
                                    # yazı tipi , punto , bold mu , italik mi

        #Rastgele bayrak belirlemek için bir liste açıyoruz
        random_mimari_numaralari = list()
        random_mimari_numaralari = mimari_numara_degerleri

        mimari_numarasi = random.randint(1,15) #Rastgele bir bayrak secilir
        random_mimari_numaralari.remove(mimari_numarasi) #Bayrağın tekrar seçilmemesi için numarasi listeden çıkarılır

        diger_sik_1_numarasi = random.randint(1,15)
        while diger_sik_1_numarasi == mimari_numarasi :
            diger_sik_1_numarasi = random.randint(1,15) #Aynı değerin gelmemesi için

        diger_sik_2_numarasi = random.randint(1,15)
        while diger_sik_2_numarasi == mimari_numarasi or diger_sik_2_numarasi == diger_sik_1_numarasi :
            diger_sik_2_numarasi = random.randint(1,15) #Aynı değerin gelmemesi için

        diger_sik_3_numarasi = random.randint(1,15)
        while diger_sik_3_numarasi == mimari_numarasi or diger_sik_3_numarasi == diger_sik_2_numarasi or diger_sik_3_numarasi == diger_sik_1_numarasi:
            diger_sik_3_numarasi = random.randint(1,15) #Aynı değerin gelmemesi için

        cevap_numarasi = random.randint(1,4) #Doğru cevap için rastgele bir şık seçilir

        kalan_soru_sayisi = 15  #Toplam soru sayısının değeri tutuluyor
        puan = 0

        get_out = True
        pushed_true = False
        pushed_false = False

        while get_out:
            self.screen.blit(background_image, (0, 0))
            self.screen.blit(soru_kutucugu, pygame.rect.Rect(153,5,1213,385))

            mimari_adresi = mimari_numaralar.get(mimari_numarasi)
            diger_sik_1_adresi = mimari_numaralar.get(diger_sik_1_numarasi)
            diger_sik_2_adresi = mimari_numaralar.get(diger_sik_2_numarasi)
            diger_sik_3_adresi = mimari_numaralar.get(diger_sik_3_numarasi)

            soru_resmi = pygame.image.load(mimari_adresi)
            soru_resmi = pygame.transform.scale(soru_resmi, soru_resmi_boyutu)
            self.screen.blit(soru_resmi, pygame.rect.Rect(466, 50, 901, 340))

            #cevap ve diğer şıkların değerleri alınır
            cevap = mimari_cevaplar.get(mimari_adresi)
            diger_sik_1 = mimari_cevaplar.get(diger_sik_1_adresi)
            diger_sik_2 = mimari_cevaplar.get(diger_sik_2_adresi)
            diger_sik_3 = mimari_cevaplar.get(diger_sik_3_adresi)

            ###############Cevap 1. şıkta####################
            if cevap_numarasi == 1 and pushed_true == True :
                self.siklar_image_blit(cevap_numarasi,dogru_cevap,notr_cevap,pushed_true)
                self.cevaplar_image_blit(cevap_numarasi,pushed_true,font,cevap,diger_sik_1,diger_sik_2,diger_sik_3,black,renkler,siklar)
            elif cevap_numarasi == 1 and pushed_true == False :
                self.siklar_image_blit(cevap_numarasi, dogru_cevap,notr_cevap, pushed_true)
                self.cevaplar_image_blit(cevap_numarasi,pushed_true,font,cevap,diger_sik_1,diger_sik_2,diger_sik_3,black,renkler,siklar)

            ###############Cevap 2. şıkta####################
            if cevap_numarasi == 2 and pushed_true == True :
                self.siklar_image_blit(cevap_numarasi,dogru_cevap,notr_cevap,pushed_true)
                self.cevaplar_image_blit(cevap_numarasi,pushed_true,font,cevap,diger_sik_1,diger_sik_2,diger_sik_3,black,renkler,siklar)
            elif cevap_numarasi == 2 and pushed_true == False :
                self.siklar_image_blit(cevap_numarasi, dogru_cevap,notr_cevap, pushed_true)
                self.cevaplar_image_blit(cevap_numarasi,pushed_true,font,cevap,diger_sik_1,diger_sik_2,diger_sik_3,black,renkler,siklar)

            ###############Cevap 3. şıkta####################
            if cevap_numarasi == 3 and pushed_true == True :
                self.siklar_image_blit(cevap_numarasi, dogru_cevap,notr_cevap, pushed_true)
                self.cevaplar_image_blit(cevap_numarasi,pushed_true,font,cevap,diger_sik_1,diger_sik_2,diger_sik_3,black,renkler,siklar)
            elif cevap_numarasi == 3 and pushed_true == False :
                self.siklar_image_blit(cevap_numarasi, dogru_cevap,notr_cevap, pushed_true)
                self.cevaplar_image_blit(cevap_numarasi,pushed_true,font,cevap,diger_sik_1,diger_sik_2,diger_sik_3,black,renkler,siklar)

            ###############Cevap 4. şıkta####################
            if cevap_numarasi == 4 and pushed_true == True :
                self.siklar_image_blit(cevap_numarasi, dogru_cevap,notr_cevap, pushed_true)
                self.cevaplar_image_blit(cevap_numarasi,pushed_true,font,cevap,diger_sik_1,diger_sik_2,diger_sik_3,black,renkler,siklar)
            elif cevap_numarasi == 4 and pushed_true == False :
                self.siklar_image_blit(cevap_numarasi, dogru_cevap,notr_cevap, pushed_true)
                self.cevaplar_image_blit(cevap_numarasi,pushed_true,font,cevap,diger_sik_1,diger_sik_2,diger_sik_3,black,renkler,siklar)


            ####Mouse click eventi için sorgu işlemleri
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == LEFT:
                    mouse = pygame.mouse.get_pos()

                    if ( 153 < mouse[0] < 673 and 390 < mouse[1] < 560 ) :
                        if cevap_numarasi == 1 :
                            puan = puan + 100

                            pushed_true = True
                            self.siklar_image_blit(cevap_numarasi,dogru_cevap,notr_cevap,pushed_true)
                            self.cevaplar_image_blit(cevap_numarasi,pushed_true,font,cevap,diger_sik_1,diger_sik_2,diger_sik_3,black,renkler,siklar)

                            mimari_numarasi = random.randint(1, 15)  # Rastgele bir bayrak secilir
                            while mimari_numarasi not in random_mimari_numaralari :
                                mimari_numarasi = random.randint(1, 15)  # Rastgele bir bayrak secilir
                            random_mimari_numaralari.remove(mimari_numarasi)  # Bayrağın tekrar seçilmemesi için numarasi listeden çıkarılır

                            kalan_soru_sayisi -= 1
                            pushed_true = False

                            diger_sik_1_numarasi = random.randint(1,15)
                            while diger_sik_1_numarasi == mimari_numarasi:
                                diger_sik_1_numarasi = random.randint(1,15)  # Aynı değerin gelmemesi için

                            diger_sik_2_numarasi = random.randint(1, 15)
                            while diger_sik_2_numarasi == mimari_numarasi or diger_sik_2_numarasi == diger_sik_1_numarasi:
                                diger_sik_2_numarasi = random.randint(1, 15)  # Aynı değerin gelmemesi için

                            diger_sik_3_numarasi = random.randint(1, 15)
                            while diger_sik_3_numarasi == mimari_numarasi or diger_sik_3_numarasi == diger_sik_2_numarasi or diger_sik_3_numarasi == diger_sik_1_numarasi:
                                diger_sik_3_numarasi = random.randint(1, 15)  # Aynı değerin gelmemesi için

                            cevap_numarasi = random.randint(1, 4)  # Doğru cevap için rastgele bir şık seçilir
                        else:
                            mimari_numarasi = random.randint(1, 15)  # Rastgele bir bayrak secilir
                            while mimari_numarasi not in random_mimari_numaralari:
                                mimari_numarasi = random.randint(1, 15)  # Rastgele bir bayrak secilir
                            random_mimari_numaralari.remove(mimari_numarasi)  # Bayrağın tekrar seçilmemesi için numarasi listeden çıkarılır

                            kalan_soru_sayisi -= 1
                            pushed_true = False

                            diger_sik_1_numarasi = random.randint(1, 15)
                            while diger_sik_1_numarasi == mimari_numarasi:
                                diger_sik_1_numarasi = random.randint(1, 15)  # Aynı değerin gelmemesi için

                            diger_sik_2_numarasi = random.randint(1, 15)
                            while diger_sik_2_numarasi == mimari_numarasi or diger_sik_2_numarasi == diger_sik_1_numarasi:
                                diger_sik_2_numarasi = random.randint(1, 15)  # Aynı değerin gelmemesi için

                            diger_sik_3_numarasi = random.randint(1, 15)
                            while diger_sik_3_numarasi == mimari_numarasi or diger_sik_3_numarasi == diger_sik_2_numarasi or diger_sik_3_numarasi == diger_sik_1_numarasi:
                                diger_sik_3_numarasi = random.randint(1, 15)  # Aynı değerin gelmemesi için

                            cevap_numarasi = random.randint(1, 4)  # Doğru cevap için rastgele bir şık seçilir

                    elif ( 688 < mouse[0] < 1208 and 390 < mouse[1] < 560 ) :
                        if cevap_numarasi == 2 :
                            puan = puan + 100

                            pushed_true = True
                            self.siklar_image_blit(cevap_numarasi, dogru_cevap, notr_cevap, pushed_true)
                            self.cevaplar_image_blit(cevap_numarasi, pushed_true, font, cevap, diger_sik_1, diger_sik_2,
                                                     diger_sik_3, black, renkler, siklar)

                            mimari_numarasi = random.randint(1, 15)  # Rastgele bir bayrak secilir
                            while mimari_numarasi not in random_mimari_numaralari:
                                mimari_numarasi = random.randint(1, 15)  # Rastgele bir bayrak secilir
                            random_mimari_numaralari.remove(mimari_numarasi)  # Bayrağın tekrar seçilmemesi için numarasi listeden çıkarılır

                            kalan_soru_sayisi -= 1
                            pushed_true = False

                            diger_sik_1_numarasi = random.randint(1, 15)
                            while diger_sik_1_numarasi == mimari_numarasi:
                                diger_sik_1_numarasi = random.randint(1, 15)  # Aynı değerin gelmemesi için

                            diger_sik_2_numarasi = random.randint(1, 15)
                            while diger_sik_2_numarasi == mimari_numarasi or diger_sik_2_numarasi == diger_sik_1_numarasi:
                                diger_sik_2_numarasi = random.randint(1, 15)  # Aynı değerin gelmemesi için

                            diger_sik_3_numarasi = random.randint(1, 15)
                            while diger_sik_3_numarasi == mimari_numarasi or diger_sik_3_numarasi == diger_sik_2_numarasi or diger_sik_3_numarasi == diger_sik_1_numarasi:
                                diger_sik_3_numarasi = random.randint(1, 15)  # Aynı değerin gelmemesi için

                            cevap_numarasi = random.randint(1, 4)  # Doğru cevap için rastgele bir şık seçilir
                        else:
                            mimari_numarasi = random.randint(1, 15)  # Rastgele bir bayrak secilir
                            while mimari_numarasi not in random_mimari_numaralari:
                                mimari_numarasi = random.randint(1, 15)  # Rastgele bir bayrak secilir
                            random_mimari_numaralari.remove(
                                mimari_numarasi)  # Bayrağın tekrar seçilmemesi için numarasi listeden çıkarılır

                            kalan_soru_sayisi -= 1
                            pushed_true = False

                            diger_sik_1_numarasi = random.randint(1, 15)
                            while diger_sik_1_numarasi == mimari_numarasi:
                                diger_sik_1_numarasi = random.randint(1, 15)  # Aynı değerin gelmemesi için

                            diger_sik_2_numarasi = random.randint(1, 15)
                            while diger_sik_2_numarasi == mimari_numarasi or diger_sik_2_numarasi == diger_sik_1_numarasi:
                                diger_sik_2_numarasi = random.randint(1, 15)  # Aynı değerin gelmemesi için

                            diger_sik_3_numarasi = random.randint(1, 15)
                            while diger_sik_3_numarasi == mimari_numarasi or diger_sik_3_numarasi == diger_sik_2_numarasi or diger_sik_3_numarasi == diger_sik_1_numarasi:
                                diger_sik_3_numarasi = random.randint(1, 15)  # Aynı değerin gelmemesi için

                            cevap_numarasi = random.randint(1, 4)  # Doğru cevap için rastgele bir şık seçilir

                    elif ( 153 < mouse[0] < 673 and 570 < mouse[1] < 740 ) :
                        if cevap_numarasi == 3 :
                            puan = puan + 100

                            pushed_true = True
                            self.siklar_image_blit(cevap_numarasi, dogru_cevap, notr_cevap, pushed_true)
                            self.cevaplar_image_blit(cevap_numarasi, pushed_true, font, cevap, diger_sik_1, diger_sik_2,
                                                     diger_sik_3, black, renkler, siklar)

                            mimari_numarasi = random.randint(1, 15)  # Rastgele bir bayrak secilir
                            while mimari_numarasi not in random_mimari_numaralari:
                                mimari_numarasi = random.randint(1, 15)  # Rastgele bir bayrak secilir
                            random_mimari_numaralari.remove(
                                mimari_numarasi)  # Bayrağın tekrar seçilmemesi için numarasi listeden çıkarılır

                            kalan_soru_sayisi -= 1
                            pushed_true = False

                            diger_sik_1_numarasi = random.randint(1, 15)
                            while diger_sik_1_numarasi == mimari_numarasi:
                                diger_sik_1_numarasi = random.randint(1, 15)  # Aynı değerin gelmemesi için

                            diger_sik_2_numarasi = random.randint(1, 15)
                            while diger_sik_2_numarasi == mimari_numarasi or diger_sik_2_numarasi == diger_sik_1_numarasi:
                                diger_sik_2_numarasi = random.randint(1, 15)  # Aynı değerin gelmemesi için

                            diger_sik_3_numarasi = random.randint(1, 15)
                            while diger_sik_3_numarasi == mimari_numarasi or diger_sik_3_numarasi == diger_sik_2_numarasi or diger_sik_3_numarasi == diger_sik_1_numarasi:
                                diger_sik_3_numarasi = random.randint(1, 15)  # Aynı değerin gelmemesi için

                            cevap_numarasi = random.randint(1, 4)  # Doğru cevap için rastgele bir şık seçilir
                        else:
                            mimari_numarasi = random.randint(1, 15)  # Rastgele bir bayrak secilir
                            while mimari_numarasi not in random_mimari_numaralari:
                                mimari_numarasi = random.randint(1, 15)  # Rastgele bir bayrak secilir
                            random_mimari_numaralari.remove(mimari_numarasi)  # Bayrağın tekrar seçilmemesi için numarasi listeden çıkarılır

                            kalan_soru_sayisi -= 1
                            pushed_true = False

                            diger_sik_1_numarasi = random.randint(1, 15)
                            while diger_sik_1_numarasi == mimari_numarasi:
                                diger_sik_1_numarasi = random.randint(1, 15)  # Aynı değerin gelmemesi için

                            diger_sik_2_numarasi = random.randint(1, 15)
                            while diger_sik_2_numarasi == mimari_numarasi or diger_sik_2_numarasi == diger_sik_1_numarasi:
                                diger_sik_2_numarasi = random.randint(1, 15)  # Aynı değerin gelmemesi için

                            diger_sik_3_numarasi = random.randint(1, 15)
                            while diger_sik_3_numarasi == mimari_numarasi or diger_sik_3_numarasi == diger_sik_2_numarasi or diger_sik_3_numarasi == diger_sik_1_numarasi:
                                diger_sik_3_numarasi = random.randint(1, 15)  # Aynı değerin gelmemesi için

                            cevap_numarasi = random.randint(1, 4)  # Doğru cevap için rastgele bir şık seçilir

                    elif ( 688 < mouse[0] < 1208 and 570 < mouse[1] < 740 ) :
                        if cevap_numarasi == 4 :
                            puan = puan + 100

                            pushed_true = True
                            self.siklar_image_blit(cevap_numarasi, dogru_cevap, notr_cevap, pushed_true)
                            self.cevaplar_image_blit(cevap_numarasi, pushed_true, font, cevap, diger_sik_1, diger_sik_2,
                                                     diger_sik_3, black, renkler, siklar)

                            mimari_numarasi = random.randint(1, 15)  # Rastgele bir bayrak secilir
                            while mimari_numarasi not in random_mimari_numaralari:
                                mimari_numarasi = random.randint(1, 15)  # Rastgele bir bayrak secilir
                            random_mimari_numaralari.remove( mimari_numarasi)  # Bayrağın tekrar seçilmemesi için numarasi listeden çıkarılır

                            kalan_soru_sayisi -= 1
                            pushed_true = False

                            diger_sik_1_numarasi = random.randint(1, 15)
                            while diger_sik_1_numarasi == mimari_numarasi:
                                diger_sik_1_numarasi = random.randint(1, 15)  # Aynı değerin gelmemesi için

                            diger_sik_2_numarasi = random.randint(1, 15)
                            while diger_sik_2_numarasi == mimari_numarasi or diger_sik_2_numarasi == diger_sik_1_numarasi:
                                diger_sik_2_numarasi = random.randint(1, 15)  # Aynı değerin gelmemesi için

                            diger_sik_3_numarasi = random.randint(1, 15)
                            while diger_sik_3_numarasi == mimari_numarasi or diger_sik_3_numarasi == diger_sik_2_numarasi or diger_sik_3_numarasi == diger_sik_1_numarasi:
                                diger_sik_3_numarasi = random.randint(1, 15)  # Aynı değerin gelmemesi için

                            cevap_numarasi = random.randint(1, 4)  # Doğru cevap için rastgele bir şık seçilir
                        else:
                            mimari_numarasi = random.randint(1, 15)  # Rastgele bir bayrak secilir
                            while mimari_numarasi not in random_mimari_numaralari:
                                mimari_numarasi = random.randint(1, 15)  # Rastgele bir bayrak secilir
                            random_mimari_numaralari.remove(
                                mimari_numarasi)  # Bayrağın tekrar seçilmemesi için numarasi listeden çıkarılır

                            kalan_soru_sayisi -= 1
                            pushed_true = False

                            diger_sik_1_numarasi = random.randint(1, 15)
                            while diger_sik_1_numarasi == mimari_numarasi:
                                diger_sik_1_numarasi = random.randint(1, 15)  # Aynı değerin gelmemesi için

                            diger_sik_2_numarasi = random.randint(1, 15)
                            while diger_sik_2_numarasi == mimari_numarasi or diger_sik_2_numarasi == diger_sik_1_numarasi:
                                diger_sik_2_numarasi = random.randint(1, 15)  # Aynı değerin gelmemesi için

                            diger_sik_3_numarasi = random.randint(1, 15)
                            while diger_sik_3_numarasi == mimari_numarasi or diger_sik_3_numarasi == diger_sik_2_numarasi or diger_sik_3_numarasi == diger_sik_1_numarasi:
                                diger_sik_3_numarasi = random.randint(1, 15)  # Aynı değerin gelmemesi için

                            cevap_numarasi = random.randint(1, 4)  # Doğru cevap için rastgele bir şık seçilir

            if ( len(random_mimari_numaralari) == 0 ):  #Sorular bitince çıkmak için
                get_out = False

            pygame.display.update()

        return puan

    #############################################################################################
    ###########################Kulturel FONKSİYONLARI###############################################
    #############################################################################################

    def kultur_acilis_ekrani(self):
        screen_width = self.screen.get_width()  # ekran genişliği = 1366
        screen_height = self.screen.get_height()  # ekran yüksekliği = 768

        # Arkaplan resmi
        background_image = pygame.image.load(r'C:\Users\CASPER\PycharmProjects\untitled\Sorular_Images\acilis_ekranlari\kultur_acilis_image.jpg')
        background_image = pygame.transform.scale(background_image, (screen_width, screen_height))

        get_out = True

        now = time.time()  # süre basladı
        end_time = now + 2  # iki saniye sonra süre bitecek

        while get_out:  # pencerenin ekranda kalması için gerekli infinite loop
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()  # bu for dongusu içine bir şey yazılmaz. pencereye basıldıgında hata alınmamasını sağlar
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        sys.exit()

            self.screen.blit(background_image, (0, 0))

            if time.time() > end_time:
                get_out = False  # eğer süre aşıldıysa çık

            pygame.display.update()  # pencere update edilir

    ##################################################################################
    ##################################################################################

    def kultur_sorulari(self, quiz_sound):
        LEFT = 1  # mouse sol click

        black = (0,0,0)
        soru_resmi_boyutu = (1060, 380)

        #####################################
        notr_cevap_rengi = (171, 165, 151)
        dogru_cevap_rengi = (57, 255, 20)
        yanlis_cevap_rengi = (255, 8, 10)

        #Şıkların rengi için tuple kullandım
        renkler = ( notr_cevap_rengi , dogru_cevap_rengi , yanlis_cevap_rengi )
        ###########################################
        ###########################################
        birinci_sik_koord = (220,450) #1.şıkkın koordinatları
        ikinci_sik_koord = (755,450) #2.şıkkın koordinatları
        ucuncu_sik_koord = (220,630) #3.şıkkın koordinatları
        dorduncu_sik_koord = (755,630) #4.şıkkın koordinatları

        #rastgele belirlenecek şıklar için tuple kullandım
        siklar = ( birinci_sik_koord , ikinci_sik_koord , ucuncu_sik_koord , dorduncu_sik_koord )
        ############################################
        ############################################
        birinci_sik_renk = renkler[0]
        ikinci_sik_renk = renkler[0]
        ucuncu_sik_renk = renkler[0]
        dorduncu_sik_renk = renkler[0]
        ##Default olarak şıkların rengi belirleniyor##
        ##############################################

        screen_width = self.screen.get_width()  # ekran genişliği = 1366
        screen_height = self.screen.get_height()  # ekran yüksekliği = 768

        # Arkaplan resmi
        background_image = pygame.image.load(r'C:\Users\CASPER\PycharmProjects\untitled\Sorular_Images\background_image.jpg')
        background_image = pygame.transform.scale(background_image, (screen_width, screen_height))

        # Şık kutucuklarının resimleri
        notr_cevap = pygame.image.load(r'C:\Users\CASPER\PycharmProjects\untitled\Sorular_Images\notr_cevap.png')
        notr_cevap = pygame.transform.scale(notr_cevap, (520,170))

        dogru_cevap = pygame.image.load(r'C:\Users\CASPER\PycharmProjects\untitled\Sorular_Images\dogru_cevap.png')
        dogru_cevap = pygame.transform.scale(dogru_cevap, (520,170))

        yanlis_cevap = pygame.image.load(r'C:\Users\CASPER\PycharmProjects\untitled\Sorular_Images\yanlis_cevap.png')
        yanlis_cevap = pygame.transform.scale(yanlis_cevap, (520,170))

        font = pygame.font.SysFont("C:\Windows\Fonts\constanz.ttf", 72, True, True)
                                    # yazı tipi , punto , bold mu , italik mi

        #Rastgele bayrak belirlemek için bir liste açıyoruz
        random_kultur_numaralari = list()
        random_kultur_numaralari = kultur_numara_degerleri

        kultur_numarasi = random.randint(1,15) #Rastgele bir bayrak secilir
        random_kultur_numaralari.remove(kultur_numarasi) #Bayrağın tekrar seçilmemesi için numarasi listeden çıkarılır

        diger_sik_1_numarasi = random.randint(1,15)
        while diger_sik_1_numarasi == kultur_numarasi :
            diger_sik_1_numarasi = random.randint(1,15) #Aynı değerin gelmemesi için

        diger_sik_2_numarasi = random.randint(1,15)
        while diger_sik_2_numarasi == kultur_numarasi or diger_sik_2_numarasi == diger_sik_1_numarasi :
            diger_sik_2_numarasi = random.randint(1,15) #Aynı değerin gelmemesi için

        diger_sik_3_numarasi = random.randint(1,15)
        while diger_sik_3_numarasi == kultur_numarasi or diger_sik_3_numarasi == diger_sik_2_numarasi or diger_sik_3_numarasi == diger_sik_1_numarasi:
            diger_sik_3_numarasi = random.randint(1,15) #Aynı değerin gelmemesi için

        cevap_numarasi = random.randint(1,4) #Doğru cevap için rastgele bir şık seçilir

        kalan_soru_sayisi = 15  #Toplam soru sayısının değeri tutuluyor
        puan = 0

        get_out = True
        pushed_true = False
        pushed_false = False

        while get_out:
            self.screen.blit(background_image, (0, 0))

            kultur_adresi = kultur_numaralar.get(kultur_numarasi)
            diger_sik_1_adresi = kultur_numaralar.get(diger_sik_1_numarasi)
            diger_sik_2_adresi = kultur_numaralar.get(diger_sik_2_numarasi)
            diger_sik_3_adresi = kultur_numaralar.get(diger_sik_3_numarasi)

            soru_resmi = pygame.image.load(kultur_adresi)
            soru_resmi = pygame.transform.scale(soru_resmi, soru_resmi_boyutu)
            self.screen.blit(soru_resmi, pygame.rect.Rect(153,5,1213,385))

            #cevap ve diğer şıkların değerleri alınır
            cevap = kultur_cevaplar.get(kultur_adresi)
            diger_sik_1 = kultur_cevaplar.get(diger_sik_1_adresi)
            diger_sik_2 = kultur_cevaplar.get(diger_sik_2_adresi)
            diger_sik_3 = kultur_cevaplar.get(diger_sik_3_adresi)

            ###############Cevap 1. şıkta####################
            if cevap_numarasi == 1 and pushed_true == True :
                self.siklar_image_blit(cevap_numarasi,dogru_cevap,notr_cevap,pushed_true)
                self.cevaplar_image_blit(cevap_numarasi,pushed_true,font,cevap,diger_sik_1,diger_sik_2,diger_sik_3,black,renkler,siklar)
            elif cevap_numarasi == 1 and pushed_true == False :
                self.siklar_image_blit(cevap_numarasi, dogru_cevap,notr_cevap, pushed_true)
                self.cevaplar_image_blit(cevap_numarasi,pushed_true,font,cevap,diger_sik_1,diger_sik_2,diger_sik_3,black,renkler,siklar)

            ###############Cevap 2. şıkta####################
            if cevap_numarasi == 2 and pushed_true == True :
                self.siklar_image_blit(cevap_numarasi,dogru_cevap,notr_cevap,pushed_true)
                self.cevaplar_image_blit(cevap_numarasi,pushed_true,font,cevap,diger_sik_1,diger_sik_2,diger_sik_3,black,renkler,siklar)
            elif cevap_numarasi == 2 and pushed_true == False :
                self.siklar_image_blit(cevap_numarasi, dogru_cevap,notr_cevap, pushed_true)
                self.cevaplar_image_blit(cevap_numarasi,pushed_true,font,cevap,diger_sik_1,diger_sik_2,diger_sik_3,black,renkler,siklar)

            ###############Cevap 3. şıkta####################
            if cevap_numarasi == 3 and pushed_true == True :
                self.siklar_image_blit(cevap_numarasi, dogru_cevap,notr_cevap, pushed_true)
                self.cevaplar_image_blit(cevap_numarasi,pushed_true,font,cevap,diger_sik_1,diger_sik_2,diger_sik_3,black,renkler,siklar)
            elif cevap_numarasi == 3 and pushed_true == False :
                self.siklar_image_blit(cevap_numarasi, dogru_cevap,notr_cevap, pushed_true)
                self.cevaplar_image_blit(cevap_numarasi,pushed_true,font,cevap,diger_sik_1,diger_sik_2,diger_sik_3,black,renkler,siklar)

            ###############Cevap 4. şıkta####################
            if cevap_numarasi == 4 and pushed_true == True :
                self.siklar_image_blit(cevap_numarasi, dogru_cevap,notr_cevap, pushed_true)
                self.cevaplar_image_blit(cevap_numarasi,pushed_true,font,cevap,diger_sik_1,diger_sik_2,diger_sik_3,black,renkler,siklar)
            elif cevap_numarasi == 4 and pushed_true == False :
                self.siklar_image_blit(cevap_numarasi, dogru_cevap,notr_cevap, pushed_true)
                self.cevaplar_image_blit(cevap_numarasi,pushed_true,font,cevap,diger_sik_1,diger_sik_2,diger_sik_3,black,renkler,siklar)


            ####Mouse click eventi için sorgu işlemleri
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == LEFT:
                    mouse = pygame.mouse.get_pos()

                    if ( 153 < mouse[0] < 673 and 390 < mouse[1] < 560 ) :
                        if cevap_numarasi == 1 :
                            puan = puan + 100

                            pushed_true = True
                            self.siklar_image_blit(cevap_numarasi,dogru_cevap,notr_cevap,pushed_true)
                            self.cevaplar_image_blit(cevap_numarasi,pushed_true,font,cevap,diger_sik_1,diger_sik_2,diger_sik_3,black,renkler,siklar)

                            kultur_numarasi = random.randint(1, 15)  # Rastgele bir bayrak secilir
                            while kultur_numarasi not in random_kultur_numaralari :
                                kultur_numarasi = random.randint(1, 15)  # Rastgele bir bayrak secilir
                            random_kultur_numaralari.remove(kultur_numarasi)  # Bayrağın tekrar seçilmemesi için numarasi listeden çıkarılır

                            kalan_soru_sayisi -= 1
                            pushed_true = False

                            diger_sik_1_numarasi = random.randint(1, 15)
                            while diger_sik_1_numarasi == kultur_numarasi:
                                diger_sik_1_numarasi = random.randint(1, 15)  # Aynı değerin gelmemesi için

                            diger_sik_2_numarasi = random.randint(1, 15)
                            while diger_sik_2_numarasi == kultur_numarasi or diger_sik_2_numarasi == diger_sik_1_numarasi:
                                diger_sik_2_numarasi = random.randint(1, 15)  # Aynı değerin gelmemesi için

                            diger_sik_3_numarasi = random.randint(1, 15)
                            while diger_sik_3_numarasi == kultur_numarasi or diger_sik_3_numarasi == diger_sik_2_numarasi or diger_sik_3_numarasi == diger_sik_1_numarasi:
                                diger_sik_3_numarasi = random.randint(1, 15)  # Aynı değerin gelmemesi için

                            cevap_numarasi = random.randint(1, 4)  # Doğru cevap için rastgele bir şık seçilir
                        else:
                            kultur_numarasi = random.randint(1, 15)  # Rastgele bir bayrak secilir
                            while kultur_numarasi not in random_kultur_numaralari:
                                kultur_numarasi = random.randint(1, 15)  # Rastgele bir bayrak secilir
                            random_kultur_numaralari.remove(kultur_numarasi)  # Bayrağın tekrar seçilmemesi için numarasi listeden çıkarılır

                            kalan_soru_sayisi -= 1
                            pushed_true = False

                            diger_sik_1_numarasi = random.randint(1, 15)
                            while diger_sik_1_numarasi == kultur_numarasi:
                                diger_sik_1_numarasi = random.randint(1, 15)  # Aynı değerin gelmemesi için

                            diger_sik_2_numarasi = random.randint(1, 15)
                            while diger_sik_2_numarasi == kultur_numarasi or diger_sik_2_numarasi == diger_sik_1_numarasi:
                                diger_sik_2_numarasi = random.randint(1, 15)  # Aynı değerin gelmemesi için

                            diger_sik_3_numarasi = random.randint(1, 15)
                            while diger_sik_3_numarasi == kultur_numarasi or diger_sik_3_numarasi == diger_sik_2_numarasi or diger_sik_3_numarasi == diger_sik_1_numarasi:
                                diger_sik_3_numarasi = random.randint(1, 15)  # Aynı değerin gelmemesi için

                            cevap_numarasi = random.randint(1, 4)  # Doğru cevap için rastgele bir şık seçilir

                    elif ( 688 < mouse[0] < 1208 and 390 < mouse[1] < 560 ) :
                        if cevap_numarasi == 2 :
                            puan = puan + 100

                            pushed_true = True
                            self.siklar_image_blit(cevap_numarasi, dogru_cevap, notr_cevap, pushed_true)
                            self.cevaplar_image_blit(cevap_numarasi, pushed_true, font, cevap, diger_sik_1, diger_sik_2,
                                                     diger_sik_3, black, renkler, siklar)

                            kultur_numarasi = random.randint(1, 15)  # Rastgele bir bayrak secilir
                            while kultur_numarasi not in random_kultur_numaralari:
                                kultur_numarasi = random.randint(1, 15)  # Rastgele bir bayrak secilir
                            random_kultur_numaralari.remove(
                                kultur_numarasi)  # Bayrağın tekrar seçilmemesi için numarasi listeden çıkarılır

                            kalan_soru_sayisi -= 1
                            pushed_true = False

                            diger_sik_1_numarasi = random.randint(1, 15)
                            while diger_sik_1_numarasi == kultur_numarasi:
                                diger_sik_1_numarasi = random.randint(1, 15)  # Aynı değerin gelmemesi için

                            diger_sik_2_numarasi = random.randint(1, 15)
                            while diger_sik_2_numarasi == kultur_numarasi or diger_sik_2_numarasi == diger_sik_1_numarasi:
                                diger_sik_2_numarasi = random.randint(1, 15)  # Aynı değerin gelmemesi için

                            diger_sik_3_numarasi = random.randint(1, 15)
                            while diger_sik_3_numarasi == kultur_numarasi or diger_sik_3_numarasi == diger_sik_2_numarasi or diger_sik_3_numarasi == diger_sik_1_numarasi:
                                diger_sik_3_numarasi = random.randint(1, 15)  # Aynı değerin gelmemesi için

                            cevap_numarasi = random.randint(1, 4)  # Doğru cevap için rastgele bir şık seçilir
                        else:
                            kultur_numarasi = random.randint(1, 15)  # Rastgele bir bayrak secilir
                            while kultur_numarasi not in random_kultur_numaralari:
                                kultur_numarasi = random.randint(1, 15)  # Rastgele bir bayrak secilir
                            random_kultur_numaralari.remove(
                                kultur_numarasi)  # Bayrağın tekrar seçilmemesi için numarasi listeden çıkarılır

                            kalan_soru_sayisi -= 1
                            pushed_true = False

                            diger_sik_1_numarasi = random.randint(1, 15)
                            while diger_sik_1_numarasi == kultur_numarasi:
                                diger_sik_1_numarasi = random.randint(1, 15)  # Aynı değerin gelmemesi için

                            diger_sik_2_numarasi = random.randint(1, 15)
                            while diger_sik_2_numarasi == kultur_numarasi or diger_sik_2_numarasi == diger_sik_1_numarasi:
                                diger_sik_2_numarasi = random.randint(1, 15)  # Aynı değerin gelmemesi için

                            diger_sik_3_numarasi = random.randint(1, 15)
                            while diger_sik_3_numarasi == kultur_numarasi or diger_sik_3_numarasi == diger_sik_2_numarasi or diger_sik_3_numarasi == diger_sik_1_numarasi:
                                diger_sik_3_numarasi = random.randint(1, 15)  # Aynı değerin gelmemesi için

                            cevap_numarasi = random.randint(1, 4)  # Doğru cevap için rastgele bir şık seçilir

                    elif ( 153 < mouse[0] < 673 and 570 < mouse[1] < 740 ) :
                        if cevap_numarasi == 3 :
                            puan = puan + 100

                            pushed_true = True
                            self.siklar_image_blit(cevap_numarasi, dogru_cevap, notr_cevap, pushed_true)
                            self.cevaplar_image_blit(cevap_numarasi, pushed_true, font, cevap, diger_sik_1, diger_sik_2,
                                                     diger_sik_3, black, renkler, siklar)

                            kultur_numarasi = random.randint(1, 15)  # Rastgele bir bayrak secilir
                            while kultur_numarasi not in random_kultur_numaralari:
                                kultur_numarasi = random.randint(1, 15)  # Rastgele bir bayrak secilir
                            random_kultur_numaralari.remove(
                                kultur_numarasi)  # Bayrağın tekrar seçilmemesi için numarasi listeden çıkarılır

                            kalan_soru_sayisi -= 1
                            pushed_true = False

                            diger_sik_1_numarasi = random.randint(1, 15)
                            while diger_sik_1_numarasi == kultur_numarasi:
                                diger_sik_1_numarasi = random.randint(1, 15)  # Aynı değerin gelmemesi için

                            diger_sik_2_numarasi = random.randint(1, 15)
                            while diger_sik_2_numarasi == kultur_numarasi or diger_sik_2_numarasi == diger_sik_1_numarasi:
                                diger_sik_2_numarasi = random.randint(1, 15)  # Aynı değerin gelmemesi için

                            diger_sik_3_numarasi = random.randint(1, 15)
                            while diger_sik_3_numarasi == kultur_numarasi or diger_sik_3_numarasi == diger_sik_2_numarasi or diger_sik_3_numarasi == diger_sik_1_numarasi:
                                diger_sik_3_numarasi = random.randint(1, 15)  # Aynı değerin gelmemesi için

                            cevap_numarasi = random.randint(1, 4)  # Doğru cevap için rastgele bir şık seçilir
                        else:
                            kultur_numarasi = random.randint(1, 15)  # Rastgele bir bayrak secilir
                            while kultur_numarasi not in random_kultur_numaralari:
                                kultur_numarasi = random.randint(1, 15)  # Rastgele bir bayrak secilir
                            random_kultur_numaralari.remove(
                                kultur_numarasi)  # Bayrağın tekrar seçilmemesi için numarasi listeden çıkarılır

                            kalan_soru_sayisi -= 1
                            pushed_true = False

                            diger_sik_1_numarasi = random.randint(1, 15)
                            while diger_sik_1_numarasi == kultur_numarasi:
                                diger_sik_1_numarasi = random.randint(1, 15)  # Aynı değerin gelmemesi için

                            diger_sik_2_numarasi = random.randint(1, 15)
                            while diger_sik_2_numarasi == kultur_numarasi or diger_sik_2_numarasi == diger_sik_1_numarasi:
                                diger_sik_2_numarasi = random.randint(1, 15)  # Aynı değerin gelmemesi için

                            diger_sik_3_numarasi = random.randint(1, 15)
                            while diger_sik_3_numarasi == kultur_numarasi or diger_sik_3_numarasi == diger_sik_2_numarasi or diger_sik_3_numarasi == diger_sik_1_numarasi:
                                diger_sik_3_numarasi = random.randint(1, 15)  # Aynı değerin gelmemesi için

                            cevap_numarasi = random.randint(1, 4)  # Doğru cevap için rastgele bir şık seçilir

                    elif ( 688 < mouse[0] < 1208 and 570 < mouse[1] < 740 ) :
                        if cevap_numarasi == 4 :
                            puan = puan + 100

                            pushed_true = True
                            self.siklar_image_blit(cevap_numarasi, dogru_cevap, notr_cevap, pushed_true)
                            self.cevaplar_image_blit(cevap_numarasi, pushed_true, font, cevap, diger_sik_1, diger_sik_2,
                                                     diger_sik_3, black, renkler, siklar)

                            kultur_numarasi = random.randint(1, 15)  # Rastgele bir bayrak secilir
                            while kultur_numarasi not in random_kultur_numaralari:
                                kultur_numarasi = random.randint(1, 15)  # Rastgele bir bayrak secilir
                            random_kultur_numaralari.remove(
                                kultur_numarasi)  # Bayrağın tekrar seçilmemesi için numarasi listeden çıkarılır

                            kalan_soru_sayisi -= 1
                            pushed_true = False

                            diger_sik_1_numarasi = random.randint(1, 15)
                            while diger_sik_1_numarasi == kultur_numarasi:
                                diger_sik_1_numarasi = random.randint(1, 15)  # Aynı değerin gelmemesi için

                            diger_sik_2_numarasi = random.randint(1, 15)
                            while diger_sik_2_numarasi == kultur_numarasi or diger_sik_2_numarasi == diger_sik_1_numarasi:
                                diger_sik_2_numarasi = random.randint(1, 15)  # Aynı değerin gelmemesi için

                            diger_sik_3_numarasi = random.randint(1, 15)
                            while diger_sik_3_numarasi == kultur_numarasi or diger_sik_3_numarasi == diger_sik_2_numarasi or diger_sik_3_numarasi == diger_sik_1_numarasi:
                                diger_sik_3_numarasi = random.randint(1, 15)  # Aynı değerin gelmemesi için

                            cevap_numarasi = random.randint(1, 4)  # Doğru cevap için rastgele bir şık seçilir
                        else:
                            kultur_numarasi = random.randint(1, 15)  # Rastgele bir bayrak secilir
                            while kultur_numarasi not in random_kultur_numaralari:
                                kultur_numarasi = random.randint(1, 15)  # Rastgele bir bayrak secilir
                            random_kultur_numaralari.remove(
                                kultur_numarasi)  # Bayrağın tekrar seçilmemesi için numarasi listeden çıkarılır

                            kalan_soru_sayisi -= 1
                            pushed_true = False

                            diger_sik_1_numarasi = random.randint(1, 15)
                            while diger_sik_1_numarasi == kultur_numarasi:
                                diger_sik_1_numarasi = random.randint(1, 15)  # Aynı değerin gelmemesi için

                            diger_sik_2_numarasi = random.randint(1, 15)
                            while diger_sik_2_numarasi == kultur_numarasi or diger_sik_2_numarasi == diger_sik_1_numarasi:
                                diger_sik_2_numarasi = random.randint(1, 15)  # Aynı değerin gelmemesi için

                            diger_sik_3_numarasi = random.randint(1, 15)
                            while diger_sik_3_numarasi == kultur_numarasi or diger_sik_3_numarasi == diger_sik_2_numarasi or diger_sik_3_numarasi == diger_sik_1_numarasi:
                                diger_sik_3_numarasi = random.randint(1, 15)  # Aynı değerin gelmemesi için

                            cevap_numarasi = random.randint(1, 4)  # Doğru cevap için rastgele bir şık seçilir

            if ( len(random_kultur_numaralari) == 0 ):  #Sorular bitince çıkmak için
                get_out = False

            pygame.display.update()

        return puan

    def stats_screen(self):
        LEFT = 1  # mouse sol click

        black = (0, 0, 0)
        background_rengi = (0, 255, 127)

        back_button_image = pygame.image.load(r'C:\Users\CASPER\PycharmProjects\untitled\Quiz_Images\back_button_image.png')
        back_button_image = pygame.transform.scale(back_button_image, (50, 50))

        dosya = open(r'C:\Users\CASPER\PycharmProjects\untitled\skorlar.txt',"r")
        puan = dosya.readline()

        font = pygame.font.SysFont("C:\Windows\Fonts\constanz.ttf", 110 , True, True)
        yazi = font.render("EN YUKSEK SKOR :: %s" % puan, 1, black, background_rengi)

        get_out = True

        while get_out :
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == LEFT:
                    mouse = pygame.mouse.get_pos()

                    if ( 40 < mouse[0] < 90 and 10 < mouse[1] < 60 ):
                        get_out = False

            self.screen.blit(back_button_image, (40, 10, 90, 60))
            self.screen.blit(yazi,(50,350))

            pygame.display.update()