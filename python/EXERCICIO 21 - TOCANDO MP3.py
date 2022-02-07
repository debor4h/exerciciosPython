#som
import pygame #utilizado para criar jogos, tem q instalar se ficar red
pygame.mixer.init() #iniciar o pygame
pygame.mixer.music.load('ariana21.mp3') #colocar o nome do arquivo
pygame.mixer.music.play() #aqui e para reproduzir
#e um loop para fazer a musica ser executada
#while(pygame.mixer.music.get_busy()): #get_busy() metodo usado para ver se a musica ta tocando
   # pass
input() #colocar
pygame.event.waint()