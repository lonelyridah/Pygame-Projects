from GameStartScreen import *
from QuizClass_and_Methods import *
import pygame

class Screen() :
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

    #######################################################################
    ################### Harita Fonksiyonu #################################
    #######################################################################

    def harita(self):
        LEFT = 1  # mouse sol click

        screen_width = self.screen.get_width()  # ekran genişliği = 1366
        screen_height = self.screen.get_height()

        background_image_1 = pygame.image.load(r'C:\Users\CASPER\PycharmProjects\untitled\indir.jpg')
        background_image_1 = pygame.transform.scale(background_image_1, (screen_width, screen_height))

        back_button_image = pygame.image.load(r'C:\Users\CASPER\PycharmProjects\untitled\Quiz_Images\back_button_image.png')
        back_button_image = pygame.transform.scale(back_button_image, (50, 50))

        get_out = True

        while get_out:
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

            self.screen.blit(background_image_1, (0, 0))
            self.screen.blit(back_button_image, (40, 10, 90, 60))

            pygame.display.update()

    #######################################################################
    ################### Quiz Ana Ekran Fonksiyonu #########################
    #######################################################################

    def quiz(self, voice_control):
        LEFT = 1  # mouse sol click

        #Pencere nesnelerinin tanimlanmasi
        bayrak_kategori_screen = QuizScreen("Bayraklar")
        sekil_kategori_screen = QuizScreen("Sekiller")
        sehir_kategori_screen = QuizScreen("Sehirler")
        cografya_kategori_screen = QuizScreen("Cografya")
        mimari_kategori_screen = QuizScreen("Mimari")
        kulturel_kategori_screen = QuizScreen("Kulturel")
        stats_kategori_screen = QuizScreen("Stats")

        screen_width = self.screen.get_width()  # ekran genişliği = 1366
        screen_height = self.screen.get_height()  # ekran yüksekliği = 768

        # Arkaplan resmi
        background_image_1 = pygame.image.load(r'C:\Users\CASPER\PycharmProjects\untitled\Quiz_Images\quiz.jpg')
        background_image_1 = pygame.transform.scale(background_image_1, (screen_width, screen_height))

        # Kategori resimleri
        bayrak_kategori_image = pygame.image.load(r'C:\Users\CASPER\PycharmProjects\untitled\Quiz_Images\bayrak_kategori_image.jpg')
        bayrak_kategori_image = pygame.transform.scale(bayrak_kategori_image, (250, 250))

        sekil_kategori_image = pygame.image.load(r'C:\Users\CASPER\PycharmProjects\untitled\Quiz_Images\sekil_kategori_image.jpg')
        sekil_kategori_image = pygame.transform.scale(sekil_kategori_image, (250, 250))

        sehir_kategori_image = pygame.image.load(r'C:\Users\CASPER\PycharmProjects\untitled\Quiz_Images\sehir_kategori_image.jpg')
        sehir_kategori_image = pygame.transform.scale(sehir_kategori_image, (250, 250))

        cografya_kategori_image = pygame.image.load(r'C:\Users\CASPER\PycharmProjects\untitled\Quiz_Images\cografya_kategori_image.jpg')
        cografya_kategori_image = pygame.transform.scale(cografya_kategori_image, (250, 250))

        mimari_kategori_image = pygame.image.load(r'C:\Users\CASPER\PycharmProjects\untitled\Quiz_Images\mimari_kategori_image.jpg')
        mimari_kategori_image = pygame.transform.scale(mimari_kategori_image, (250, 250))

        kulturel_kategori_image = pygame.image.load(r'C:\Users\CASPER\PycharmProjects\untitled\Quiz_Images\kulturel_kategori_image.jpg')
        kulturel_kategori_image = pygame.transform.scale(kulturel_kategori_image, (250, 250))

        # Yazi resimleri
        bayrak_yazisi = pygame.image.load(r'C:\Users\CASPER\PycharmProjects\untitled\Quiz_Images\Quiz_Name_Images\bayraklar.png')
        bayrak_yazisi = pygame.transform.scale(bayrak_yazisi, (250, 70))

        sekiller_yazisi = pygame.image.load(r'C:\Users\CASPER\PycharmProjects\untitled\Quiz_Images\Quiz_Name_Images\sekiller.png')
        sekiller_yazisi = pygame.transform.scale(sekiller_yazisi, (250, 70))

        sehirler_yazisi = pygame.image.load(r'C:\Users\CASPER\PycharmProjects\untitled\Quiz_Images\Quiz_Name_Images\sehirler.png')
        sehirler_yazisi = pygame.transform.scale(sehirler_yazisi, (250, 70))

        cografya_yazisi = pygame.image.load(r'C:\Users\CASPER\PycharmProjects\untitled\Quiz_Images\Quiz_Name_Images\cografya.png')
        cografya_yazisi = pygame.transform.scale(cografya_yazisi, (250, 70))

        mimari_yazisi = pygame.image.load(r'C:\Users\CASPER\PycharmProjects\untitled\Quiz_Images\Quiz_Name_Images\mimari.png')
        mimari_yazisi = pygame.transform.scale(mimari_yazisi, (250, 70))

        kulturler_yazisi = pygame.image.load(r'C:\Users\CASPER\PycharmProjects\untitled\Quiz_Images\Quiz_Name_Images\kulturler.png')
        kulturler_yazisi = pygame.transform.scale(kulturler_yazisi, (250, 70))

        #Iconlar
        back_button_image = pygame.image.load(r'C:\Users\CASPER\PycharmProjects\untitled\Quiz_Images\back_button_image.png')
        back_button_image = pygame.transform.scale(back_button_image , ( 50 , 50))

        stats_image = pygame.image.load(r'C:\Users\CASPER\PycharmProjects\untitled\Quiz_Images\stats_image.png')
        stats_image = pygame.transform.scale(stats_image, (90,90))

        quiz_sound = False

        get_out = True

        while get_out:
            bayrak_kategori_screen.screen_update()
            sekil_kategori_screen.screen_update()
            sehir_kategori_screen.screen_update()
            cografya_kategori_screen.screen_update()
            mimari_kategori_screen.screen_update()
            kulturel_kategori_screen.screen_update()
            stats_kategori_screen.screen_update()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN and event.button == LEFT:
                    mouse = pygame.mouse.get_pos()

                    if ( 40 < mouse[0] < 90 and 10 < mouse[1] < 60 ):  #Back Button Pressed
                        get_out = False
                    elif ( 125 < mouse[0] < 375 and 60 < mouse[1] < 380 ): #Bayrak Kategori Pressed
                        screen = bayrak_kategori_screen.make_current()
                        bayrak_kategori_screen.bayrak_acilis_ekrani()
                        puan = bayrak_kategori_screen.bayrak_sorulari(quiz_sound)
                        bayrak_kategori_screen.sonuc_ekrani(puan)
                        bayrak_kategori_screen.end_current()
                    elif ( 525 < mouse[0] < 775 and 60 < mouse[1] < 380 ): #Sekil Kategori Pressed
                        screen = sekil_kategori_screen.make_current()
                        sekil_kategori_screen.sekil_acilis_ekrani()
                        puan = sekil_kategori_screen.sekil_sorulari(quiz_sound)
                        sekil_kategori_screen.sonuc_ekrani(puan)
                        sekil_kategori_screen.end_current()
                    elif ( 925 < mouse[0] < 1175 and 60 < mouse[1] < 380 ): #Sehir Kategori Pressed
                        screen = sehir_kategori_screen.make_current()
                        sehir_kategori_screen.sehir_acilis_ekrani()
                        puan = sehir_kategori_screen.sehir_sorulari(quiz_sound)
                        sehir_kategori_screen.sonuc_ekrani(puan)
                        sehir_kategori_screen.end_current()
                    elif ( 125 < mouse[0] < 375 and 405 < mouse[1] < 725 ): #Cografya Kategori Pressed
                        screen = cografya_kategori_screen.make_current()
                        cografya_kategori_screen.cografya_acilis_ekrani()
                        puan = cografya_kategori_screen.cografya_sorulari(quiz_sound)
                        cografya_kategori_screen.sonuc_ekrani(puan)
                        cografya_kategori_screen.end_current()
                    elif ( 525 < mouse[0] < 775 and 405 < mouse[1] < 725 ): #Mimari Kategori Pressed
                        screen = mimari_kategori_screen.make_current()
                        mimari_kategori_screen.mimari_acilis_ekrani()
                        puan = mimari_kategori_screen.mimari_sorulari(quiz_sound)
                        mimari_kategori_screen.sonuc_ekrani(puan)
                        mimari_kategori_screen.end_current()
                    elif ( 925 < mouse[0] < 1175 and 405 < mouse[1] < 725 ): #Kültürel Kategori Pressed
                        screen = kulturel_kategori_screen.make_current()
                        kulturel_kategori_screen.kultur_acilis_ekrani()
                        puan = kulturel_kategori_screen.kultur_sorulari(quiz_sound)
                        kulturel_kategori_screen.sonuc_ekrani(puan)
                        kulturel_kategori_screen.end_current()
                    elif ( 1220 < mouse[0] < 1310 and 430 < mouse[1] < 520 ): #Stats Pressed
                        screen = stats_kategori_screen.make_current()
                        stats_kategori_screen.stats_screen()
                        stats_kategori_screen.end_current()

            self.screen.blit(background_image_1, (0, 0))

            self.screen.blit(bayrak_kategori_image, pygame.rect.Rect(125, 60, 375, 310))
            self.screen.blit(sekil_kategori_image, pygame.rect.Rect(525, 60, 775, 310))
            self.screen.blit(sehir_kategori_image, pygame.rect.Rect(925, 60, 1175, 310))
            self.screen.blit(cografya_kategori_image, pygame.rect.Rect(125, 405, 375, 655))
            self.screen.blit(mimari_kategori_image, pygame.rect.Rect(525, 405, 775, 655))
            self.screen.blit(kulturel_kategori_image, pygame.rect.Rect(925, 405, 1175, 655))

            self.screen.blit(bayrak_yazisi, pygame.rect.Rect(125, 310, 375, 380))
            self.screen.blit(sekiller_yazisi, pygame.rect.Rect(525, 310, 775, 380))
            self.screen.blit(sehirler_yazisi, pygame.rect.Rect(925, 310, 1175, 380))
            self.screen.blit(cografya_yazisi, pygame.rect.Rect(125, 655, 375, 725))
            self.screen.blit(mimari_yazisi, pygame.rect.Rect(525, 655, 775, 725))
            self.screen.blit(kulturler_yazisi, pygame.rect.Rect(925, 655, 1175, 725))

            self.screen.blit(back_button_image, pygame.rect.Rect(40, 10, 90, 60))
            self.screen.blit(stats_image, pygame.rect.Rect(1220, 430, 1310, 520))

            pygame.display.update()
