import pygame, sys
from ScreenClass_and_Methods import *

def start_screen(voice_control):
    LEFT = 1  # mouse sol click

    #Pencere nesnelerinin tanımlanmasi
    game_start_screen = Screen("Start")
    quiz_screen = Screen("Quiz")
    harita_screen = Screen("Harita")

    screen = game_start_screen.make_current()

    screen_width = game_start_screen.get_width()  # ekran genişliği = 1366
    screen_height = game_start_screen.get_height()  # ekran yüksekliği = 768

    # Ekrana yüklenecek resimler yazdırılır
    background_image_1 = pygame.image.load(r'C:\Users\CASPER\PycharmProjects\untitled\Start_Images\harita.jpg')
    background_image_1 = pygame.transform.scale(background_image_1, (screen_width, screen_height))

    name_of_the_game = pygame.image.load(r'C:\Users\CASPER\PycharmProjects\untitled\Start_Images\name_of_the_game.png')
    name_of_the_game = pygame.transform.scale(name_of_the_game, (780, 143))

    atlas_kategorisi_image = pygame.image.load(r'C:\Users\CASPER\PycharmProjects\untitled\Start_Images\atlas_kategori_image.png')
    atlas_kategorisi_image = pygame.transform.scale(atlas_kategorisi_image, (300, 300))

    dunya_atlasi_yazisi = pygame.image.load(r'C:\Users\CASPER\PycharmProjects\untitled\Start_Images\dunya_atlasi_yazisi.png')
    dunya_atlasi_yazisi = pygame.transform.scale(dunya_atlasi_yazisi, (300, 50))

    quiz_kategorisi_image = pygame.image.load(r'C:\Users\CASPER\PycharmProjects\untitled\Start_Images\quiz_kategori_image.png')
    quiz_kategorisi_image = pygame.transform.scale(quiz_kategorisi_image, (300, 300))

    quiz_yazisi = pygame.image.load(r'C:\Users\CASPER\PycharmProjects\untitled\Start_Images\quiz_yazisi.png')
    quiz_yazisi = pygame.transform.scale(quiz_yazisi, (300, 50))

    settings_image = pygame.image.load(r'C:\Users\CASPER\PycharmProjects\untitled\Start_Images\settings.png')
    settings_image = pygame.transform.scale(settings_image, (100, 100))

    settings__yazisi = pygame.image.load(r'C:\Users\CASPER\PycharmProjects\untitled\Start_Images\settings_yazisi.png')
    settings__yazisi = pygame.transform.scale(settings__yazisi, (150, 40))

    exit_button_image = pygame.image.load(r'C:\Users\CASPER\PycharmProjects\untitled\Start_Images\exit.jpg')
    exit_button_image = pygame.transform.scale(exit_button_image, (50, 50))

    sound = pygame.mixer.Sound(r'C:\Users\CASPER\PycharmProjects\untitled\Start_Images\start_screen_sound.wav')
    if voice_control:
        sound.play()

    get_out = True

    while get_out:
        game_start_screen.screen_update()
        quiz_screen.screen_update()
        harita_screen.screen_update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == LEFT:
                mouse = pygame.mouse.get_pos()

                if (250 < mouse[0] < 550 and 350 < mouse[1] < 650):
                    screen = harita_screen.make_current()
                    game_start_screen.end_current()
                    harita_screen.harita()
                    harita_screen.end_current()
                    screen = game_start_screen.make_current()
                elif (800 < mouse[0] < 1100 and 350 < mouse[1] < 650):
                    screen = quiz_screen.make_current()
                    game_start_screen.end_current()
                    quiz_screen.quiz(voice_control)
                    quiz_screen.end_current()
                    screen = game_start_screen.make_current()
                elif (40 < mouse[0] < 90 and 10 < mouse[1] < 60):
                    get_out = False

        game_start_screen.screen.blit(background_image_1, (0, 0))
        game_start_screen.screen.blit(name_of_the_game, pygame.rect.Rect(290, 100, 1000, 200))
        game_start_screen.screen.blit(atlas_kategorisi_image, pygame.rect.Rect(250, 350, 550, 650))
        game_start_screen.screen.blit(dunya_atlasi_yazisi, pygame.rect.Rect(250, 650, 560, 710))
        game_start_screen.screen.blit(quiz_kategorisi_image, pygame.rect.Rect(800, 350, 1100, 650))
        game_start_screen.screen.blit(quiz_yazisi, pygame.rect.Rect(800, 650, 1110, 710))
        game_start_screen.screen.blit(settings_image, pygame.rect.Rect(1165, 550, 1265, 650))
        game_start_screen.screen.blit(settings__yazisi, pygame.rect.Rect(1140, 650, 1260, 700))
        game_start_screen.screen.blit(exit_button_image, (40, 10, 90, 60))

        pygame.display.update()
