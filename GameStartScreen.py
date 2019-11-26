import pygame , sys

def start_screen() :
    black = (0, 0, 0)

    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)  # uzerinde islem yapacagımız pencere  acilir
    screen_width = screen.get_width()  # ekran genişliği = 1366
    screen_height = screen.get_height()  # ekran yüksekliği = 768

    background_image_1 = pygame.image.load( r'C:\Users\CASPER\PycharmProjects\untitled\harita.jpg' )
    background_image_1 = pygame.transform.scale( background_image_1 , ( screen_width , screen_height ) )

    name_of_the_game = pygame.image.load( r'C:\Users\CASPER\PycharmProjects\untitled\name_of_the_game.png' )
    name_of_the_game = pygame.transform.scale( name_of_the_game , ( 780 , 143 ) )

    atlas_kategorisi_image = pygame.image.load( r'C:\Users\CASPER\PycharmProjects\untitled\atlas_kategori_image.png' )
    atlas_kategorisi_image = pygame.transform.scale( atlas_kategorisi_image , ( 300 , 300 ) )

    dunya_atlasi_yazisi = pygame.image.load( r'C:\Users\CASPER\PycharmProjects\untitled\dunya_atlasi_yazisi.png' )
    dunya_atlasi_yazisi = pygame.transform.scale( dunya_atlasi_yazisi , ( 300 , 50 ) )

    quiz_kategorisi_image = pygame.image.load( r'C:\Users\CASPER\PycharmProjects\untitled\quiz_kategori_image.png' )
    quiz_kategorisi_image = pygame.transform.scale( quiz_kategorisi_image , ( 300 , 300 ) )

    quiz_yazisi = pygame.image.load( r'C:\Users\CASPER\PycharmProjects\untitled\quiz_yazisi.png' )
    quiz_yazisi = pygame.transform.scale( quiz_yazisi , ( 300 , 50 ) )

    sound = pygame.mixer.Sound('start_screen_sound.wav')
    sound.play()

    get_out = True

    while get_out :
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                sys.exit()

        screen.fill( black )
        screen.blit( background_image_1 , ( 0 , 0 ) )
        screen.blit( name_of_the_game , pygame.rect.Rect( 290 , 100 , 1000 , 200 ) )
        screen.blit( atlas_kategorisi_image , pygame.rect.Rect( 250 , 350 , 550 , 650) )
        screen.blit( dunya_atlasi_yazisi , pygame.rect.Rect( 250 , 650 , 560 , 710 ) )
        screen.blit( quiz_kategorisi_image , pygame.rect.Rect( 800 , 350 , 1100 , 650 ) )
        screen.blit( quiz_yazisi , pygame.rect.Rect( 800 , 650 , 1110 , 710 ) )

        pygame.display.update()

    pygame.quit()
