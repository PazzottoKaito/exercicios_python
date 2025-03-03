#Programa para tocar uma música
import pygame

pygame.init()
pygame.mixer.music.load('musica.mp3')
pygame.mixer.music.play()

input("Pressione a tecla 'Enter' para parar a música.")
