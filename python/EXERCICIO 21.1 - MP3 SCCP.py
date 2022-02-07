import pygame
pygame.mixer.init()#iniciar o pygame
pygame.mixer.music.load("sccp21.1.mp3")#aqui coloca o nome da musica sem espacos
pygame.mixer.music.play()#aqui e para reproduzir
input()
pygame.event.waint() #aqui ele espera a musica terminar. E como se fosse um stop
