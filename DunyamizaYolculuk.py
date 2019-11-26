from GameIntro import * # Oyunun introsunun kodlarını içeren GameIntro.py import edildi
from GameStartScreen import * # Oyunun baslangıç ekranının kodlarını içeren GameStartScreen.py import edildi
import pygame # pygame kütüphanesi import edildi

pygame.init() # Farklı fonksiyonlar ve bolumler dahilinde oyunun çalışabilmesi için main dosyasında pygame modulleri initialize edilir

intro() # intro fonksiyonu
start_screen() # baslangic ekranı fonksiyonu

#font = pygame.font.SysFont("Bauhaus 93",72 , False , True )  # ekrana yazdirilacak yazinin fontu ve puntosu belirtilir
                        #yazı tipi , punto , bold mu , italik mi
#merhaba = font.render("BASLIYORUZ",1,(255,0,0),( 100 , 100 , 100))  # ekrana yazilacak yazinin metin , renk gibi özellikleri belirtilir
                      #yazi stringi, anti alias , yazinin rengi , arka planin rengi
