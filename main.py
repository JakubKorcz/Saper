import pygame, sys, random, time

screen = pygame.display.set_mode((980, 980))
pygame.display.set_caption('Saper by Jakub Korcz')
jasnoniebieski = (121, 255, 255)
ciemnoniebieski = (14, 20, 248)
size = 16
hpole_gry = [[0] * size for i in range(size)]
pg = [[" "] * size for i in range(size)]
pygame.font.init()
filepath="rekord.txt"
filepath1="iloscwinow.txt"

def plik(czas):
    f = open(filepath, "r", encoding="utf-8")
    a = int(f.read())
    if czas <= int(a):
        rekord = czas
        f.close()
        f = open(filepath, "w", encoding="utf-8")
        f.write(str(rekord))
        f.close()
    f1=open(filepath1, "r", encoding="utf-8")
    a = int(f1.read())
    a+=1
    f1.close()
    f1 = open(filepath1, "w", encoding="utf-8")
    f1.write(str(a))
    f1.close()

def show_win(czas):
    screen.fill(jasnoniebieski)
    f = open(filepath, "r", encoding="utf-8")
    c = int(f.read())
    f1 = open(filepath1, "r", encoding="utf-8")
    d = int(f1.read())
    d+=1
    font = pygame.font.SysFont("Cascadia code", 200)
    napis = font.render("YOU WIN!!", 1, (243, 12, 12))
    screen.blit(napis, (100, 10))
    plik(czas)
    font = pygame.font.SysFont("Cascadia code", 80)
    n1 = font.render("Gratulacje wygrałeś sapera" , 1, (0,0,0))
    screen.blit(n1, (110, 240))
    n2 = font.render("stworzonego przez Jakuba Korcza!!!", 1, (0,0,0))
    screen.blit(n2, (10, 320))
    n3=font.render("To twoje "+str(d)+" zwycięstwo!!!" , 1, (0,0,0))
    screen.blit(n3, (150, 400))
    n4 = font.render("Zajeło ci to "+str(czas)+" sekund", 1, (0, 0, 0))
    screen.blit(n4, (200, 480))
    if czas < c:
        n5 = font.render("To jest nowy rekord!!!", 1, (0, 0, 0))
        screen.blit(n5, (200, 560))
    pygame.display.flip()
    time.sleep(5)
    show_game_over()

def show_game_over():
    screen.fill(jasnoniebieski)
    refresh= pygame.image.load('refresh.png')
    screen.blit(refresh, (320, 320))
    pygame.display.flip()
    time.sleep(2)
    main()

def rysowanie_planszy(size):
    font = pygame.font.SysFont("Cascadia code", 40)
    f = open(filepath, "r", encoding="utf-8")
    c = int(f.read())
    f1 = open(filepath1, "r", encoding="utf-8")
    d = int(f1.read())
    screen.fill(jasnoniebieski)
    puchar = pygame.image.load('puchar.png')
    screen.blit(puchar, (15, 610))
    pygame.draw.rect(screen, (240,2,2),pygame.Rect((5,170),(90,60)),3)
    pygame.draw.rect(screen, (0,0,0), pygame.Rect((5, 250), (90, 150)), 3)
    pygame.draw.rect(screen, (230, 183, 94), pygame.Rect((5, 423), (90, 150)), 3)
    pygame.draw.rect(screen, (0,0,0), pygame.Rect((5, 600), (90, 150)), 3)
    pygame.draw.rect(screen, (0,0,0), pygame.Rect((8, 426), (84, 144)), 2)
    rekord = font.render(str(c), 1, (230, 183, 94))
    screen.blit(rekord, (28, 520))
    iloscw = font.render(str(d), 1, (0,0,0))
    screen.blit(iloscw, (30, 700))
    korona = pygame.image.load('korona.png')
    flaga = pygame.image.load('flaga.jpg')
    zegar = pygame.image.load('zegar.png')
    screen.blit(zegar, (20, 260))
    screen.blit(korona, (10, 430))
    screen.blit(flaga, (10 ,180))
    for i in range(size):
        for j in range(size):
            pygame.draw.rect(screen, ciemnoniebieski, pygame.Rect((100 + j * 50, 150 + i * 50), (50, 50)), 2)

def abc(l, pg, a, b, size):
    pg[a][b] = l[a][b]
    if pg[a][b] == 0:
        for x, y in [[1, 0], [1, 1], [1, -1], [0, 1], [0, -1], [-1, 1], [-1, 0], [-1, -1]]:
            if 0 <= a + x < size and 0 <= b + y < size:
                if pg[a + x][b + y] == " ":
                    abc(l, pg, a + x, b + y, size)

def czy_wygrane(h,p,s,bom):
    licznik=0
    licznikb=0
    for x in range(s):
        for y in range(s):
            if h[x][y]==p[x][y] and h[x][y]!="*":
                licznik+=1
            if h[x][y]=='*' and p[x][y]=="f":
                licznikb+=1
    if licznik >= s * s - bom or licznikb>=bom:
        return 1

def wybor_miejsc_na_bomby(s, b):
    il_pol = s * s
    l = []
    while len(l) < b:
        miejsce_na_bombe = random.randint(0, il_pol - 1)
        if miejsce_na_bombe not in l:
            l.append(miejsce_na_bombe)
    return l

def dodaj_flage(pg,a,b,l):
    pg[a][b]='f'
    l-=1
    return l

def usun_flage(pg,a,b,l):
    pg[a][b] = ' '
    l+=1
    return l


def main():
    bomba = 40
    hpole_gry = [[0] * size for i in range(size)]
    pg = [[" "] * size for i in range(size)]
    clock=pygame.time.Clock()
    PLAY = 1
    delta = 0.0
    licznik_flag=bomba
    for z in wybor_miejsc_na_bomby(size, bomba):
        x = int(z / size)
        y = z % size
        hpole_gry[x][y] = "*"
        for a, b in [[1, 0], [1, 1], [1, -1], [0, 1], [0, -1], [-1, 1], [-1, 0], [-1, -1]]:
            if 0 <= x + a < size and 0 <= y + b < size:
                if hpole_gry[x + a][y + b] != "*":
                    hpole_gry[x + a][y + b] += 1

    while PLAY:
        # obsługa zdarzeń

        rysowanie_planszy(size)
        font = pygame.font.SysFont("Cascadia code", 40)
        fontsa = pygame.font.SysFont("Cascadia code", 200)
        delta += clock.tick()
        czas=int(delta/1000)
        czasm = font.render(str(czas), 1, (0, 0, 0))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit(0)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:  # jeżeli naciśnięto 1. przycisk
                    mouseX, mouseY = event.pos  # rozpakowanie tupli
                    # wylicz indeks klikniętego pola
                    pole = int((mouseX - 100) / 50) + int((mouseY - 150) / 50) * size
                    a = int(pole / 16)
                    b = int(pole % 16)
                    if 100 < mouseX < 900 and 150 < mouseY < 950:
                        if pg[a][b] != 'f':
                            abc(hpole_gry, pg, a, b, size)
                elif event.button == 3:
                    mouseX, mouseY = event.pos
                    pole = int((mouseX - 100) / 50) + int((mouseY - 150) / 50) * size
                    a = int(pole / 16)
                    b = int(pole % 16)
                    if 100 < mouseX < 900 and 150 < mouseY < 950:
                        if pg[a][b] == "f" :
                            licznik_flag=usun_flage(pg, a, b,licznik_flag)
                        elif pg[a][b] == " " and licznik_flag>=1:
                            licznik_flag=dodaj_flage(pg, a, b,licznik_flag)

        for x in range(size):
            for y in range(size):
                X1 = (50 * x) + 165
                X2 = (50 * y) + 120
                if pg[x][y] == "f":
                    flaga = pygame.image.load('flaga.jpg')
                    screen.blit(flaga, (X2 - 15, X1 - 10))
                elif pg[x][y] == "*":
                    screen.blit(czasm, (36, 340))
                    lflag = font.render(str(licznik_flag), 1, (243, 12, 12))
                    screen.blit(lflag, (50, 188))
                    bomba = pygame.image.load('bomba1.jpg')
                    screen.blit(bomba, (X2 - 15, X1 - 10))
                    napis = fontsa.render("YOU LOST!!", 1, (243, 12, 12))
                    screen.blit(napis, (100, 10))
                    for w in range(size):
                        for z in range(size):
                            if pg[w][z]=="f":
                                flaga = pygame.image.load('flaga.jpg')
                                screen.blit(flaga, ((50 *z) + 120 - 15, (50 * w) + 165 - 10))
                            else:
                                label = font.render(str(pg[w][z]), 1, (13, 82, 242))
                                screen.blit(label, ((50 * z) + 120, (50 * w) + 165))
                            if hpole_gry[w][z] == "*":
                                screen.blit(bomba, ( (50 * z) + 120- 15, (50 * w) + 165 - 10))
                            pygame.display.flip()
                    time.sleep(2)
                    show_game_over()
                elif str(pg[x][y]).isdigit():
                    label = font.render(str(pg[x][y]), 1, (13, 82, 242))
                    screen.blit(label, (X2, X1))
        font = pygame.font.SysFont("Cascadia code", 40)
        screen.blit(czasm, (36, 340))
        lflag = font.render(str(licznik_flag), 1, (243, 12, 12))
        screen.blit(lflag, (50, 188))
        if czy_wygrane(hpole_gry,pg,size,bomba):
            show_win(czas)
        pygame.display.flip()

main()
