import pygame, psutil, platform, sys

# Config
largura_tela = 800
altura_tela = 600
tela = pygame.display.set_mode((largura_tela, altura_tela))
pygame.display.init()
alto = 50
largura = largura_tela - 2*20

# Cores
verde = (0, 255, 0)
preto = (0, 0, 0)
vermelho = (255, 0, 0)
branco = (255, 255, 255)

# Definições de superfícies das barras
s1 = pygame.surface.Surface((largura_tela, altura_tela/4))
s2 = pygame.surface.Surface((largura_tela, altura_tela/4))
s3 = pygame.surface.Surface((largura_tela, altura_tela/4))
s4 = pygame.surface.Surface((largura_tela, altura_tela/4))

# Fonte da letra e tamanho
pygame.font.init()
font = pygame.font.Font(None, 28)

def Memoria():
    mem = psutil.virtual_memory()
    return mem
    
def CPU():
    cpu = psutil.cpu_percent()
    return cpu

def Disco():
    disco = psutil.disk_usage('.')
    return disco

def IP():
    ip = psutil.net_if_addrs()
    return ip

# Mostrando o uso da memória
def uso_memoria():
    mem = Memoria()
    larg = largura_tela - 2*20
    s1.fill(preto)
    pygame.draw.rect(s1, branco, (20, 50, larg, 70))
    tela.blit(s1,(0,0))
    larg = larg*mem.percent/100
    pygame.draw.rect(s1, verde, (20, 50, larg, 70))
    tela.blit(s1,(0,0))
    total = round(mem.total/(1024 * 1024 * 1024),2)
    texto_barra = "Uso da memória (Total: "+ str(total) + "GB):"
    text = font.render(texto_barra, 1, branco)
    tela.blit(text, (20, 10))
    
def uso_cpu():
    cpu = CPU()
    largura = largura_tela - 2*20
    s2.fill(preto)
    pygame.draw.rect(s2, branco,(20, 50, largura, 70))
    tela.blit(s2,(0, altura_tela / 4))
    largura = largura * cpu/100
    pygame.draw.rect(s2, verde, (20, 50, largura, 70))
    tela.blit(s2,(0, altura_tela / 4))
    texto_barra = "Uso da CPU (" + str(cpu) +" %):"
    texto_proc = "Cpu: (" + str(platform.processor()) +"):"
    text = font.render(texto_barra, 1, branco)
    text_proc = font.render(texto_proc, 1, branco)
    tela.blit(text, (20, (altura_tela / 4)))
    tela.blit(text_proc, (20, (altura_tela / 4) + 25))
    
def uso_hd():
    disco = Disco()
    largura = largura_tela - 2*20
    s3.fill(preto)
    pygame.draw.rect(s3, branco,(20, 50, largura, 70))
    tela.blit(s3,(0, 2 *altura_tela / 4))
    largura = largura *disco.percent / 100
    pygame.draw.rect(s3, verde,(20, 50, largura, 70))
    tela.blit(s3,(0, 2*altura_tela / 4))
    texto_barra = "Uso do Disco (" + str(disco.percent)+" %):"
    text = font.render(texto_barra, 1, branco)
    tela.blit(text, (20, (2*altura_tela / 4)))
    

def num_ip():
    ip = IP()
    s4.fill(preto)
    tela.blit(s4,(0, 3*altura_tela / 4))
    texto_barra = "Número IP: ("+ str(psutil.net_if_addrs)
    text = font.render(texto_barra, 1, branco)
    tela.blit(text, (20, (3*altura_tela /4)))
    
    
# O que será feito
pygame.display.set_caption("Performance")

# Relógio
clock = pygame.time.Clock()

# Contador de tempo
cont = 60

terminou = False
while not terminou:
    # Eventos do mouse
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            terminou = True
    
    if cont == 60:
        uso_memoria()
        uso_cpu()
        uso_hd()
        num_ip()
        cont = 0
    
    # Atualização da tela
    pygame.display.update()
    
    # Frames por s/
    clock.tick(60)
    cont = cont + 1
    
# End pygame
pygame.display.quit()
