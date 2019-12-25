import pygame , sys , time # pygame , sys ve time  import edilir

def intro( voice_control ) :
    screen = pygame.display.set_mode((0, 0), pygame.FULLSCREEN)  # uzerinde islem yapacagımız pencere  acilir

    intro_image = pygame.image.load(r'C:\Users\CASPER\PycharmProjects\untitled\intro_screen_logo.png')
    intro_image = pygame.transform.scale(intro_image, (600, 600))

    sound = pygame.mixer.Sound('intro_screen_sound.wav')
    if voice_control :
        sound.play()

    intro_background_color = (7, 47, 65)  # intro resminin arka plan rengi

    get_out = True

    now = time.time()  # süre basladı
    end_time = now + 3  # üç saniye sonra süre bitecek

    while get_out:  # pencerenin ekranda kalması için gerekli infinite loop
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()  # bu for dongusu içine bir şey yazılmaz. pencereye basıldıgında hata alınmamasını sağlar
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    sys.exit()

        screen.fill(intro_background_color)
        screen.blit(intro_image, (370, 70) )

        if time.time() > end_time:
            get_out = False  # eğer süre aşıldıysa çık

        pygame.display.update()  # pencere update edilir
