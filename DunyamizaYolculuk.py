from GameIntro import * # Oyunun introsunun kodlarını içeren GameIntro.py import edildi
from GameStartScreen import * # Oyunun baslangıç ekranının kodlarını içeren GameStartScreen.py import edildi
import pygame # pygame kütüphanesi import edildi

pygame.init() # Farklı fonksiyonlar ve bolumler dahilinde oyunun çalışabilmesi için main dosyasında pygame modulleri initialize edilir

voice_control = False

intro( voice_control ) # intro fonksiyonu
start_screen( voice_control ) # baslangic ekranı fonksiyonu

