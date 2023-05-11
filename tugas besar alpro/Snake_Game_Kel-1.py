#import library
import pygame,random,time

#init
pygame.init()

#membuat variable warna
putih = (255, 255, 255)
hitam = (0, 0, 0)
merah = (213, 50, 80)
hijau = (0, 255, 0)

#ukuran display
lebar = 1000
tinggi = 600

layar = pygame.display.set_mode((lebar, tinggi))
pygame.display.set_caption('Game Ular by Kelompok 01') #memberi caption pada dsiplay / nama game

clock = pygame.time.Clock()

kepala_kotak = 10 #ukuran kepala ular
speed = 15 #kecepatan ular

font_style = pygame.font.SysFont("clanderon", 30)
skor_font = pygame.font.SysFont("clarendon", 40,bold=True) #font style untuk papan skor

#membuat fungsi(function) perhitungan skor
def skormu(skor):
    hitung_skor = skor_font.render("Skormu: " + str(skor), True, putih)
    layar.blit(hitung_skor, [0, 0])

#fungsi(function) menambah panjang ular
def our_snake(kepala_kotak, list_ular):
    for x in list_ular:
        pygame.draw.rect(layar, hijau, [x[0], x[1], kepala_kotak, kepala_kotak])

#fungsi(function) memberi pesan ketika game over
def pesan(psn, warna):
    komen = font_style.render(psn, True, warna)
    layar.blit(komen, [lebar / 6, tinggi / 3])

def gameLoop(): #mengulangi permainan
    kalah = False
    keluar = False 
    x1 = lebar / 2
    y1 = tinggi / 2
    arah_x = 0
    arah_y = 0
    badan = []
    panjang_ular = 1
    makan_x = round(random.randrange(0, lebar - kepala_kotak) / 10.0) * 10.0
    makan_y = round(random.randrange(0, tinggi - kepala_kotak) / 10.0) * 10.0

    while not kalah:

        while keluar == True:
            layar.fill(hitam)
            pesan("Game Over! Tekan 'spasi'-lanjut! Tekan 'Esc'-keluar", putih)
            skormu(panjang_ular - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        kalah = True
                        keluar = False
                    if event.key == pygame.K_SPACE:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                kalah = True
            if event.type == pygame.KEYDOWN: #arah keyboard
                if event.key == pygame.K_LEFT: #arah kiri
                    arah_x = -kepala_kotak
                    arah_y = 0
                elif event.key == pygame.K_RIGHT: #arah kanan
                    arah_x = kepala_kotak
                    arah_y = 0
                elif event.key == pygame.K_UP: #arah atas
                    arah_y = -kepala_kotak
                    arah_x = 0
                elif event.key == pygame.K_DOWN: #arah bawah
                    arah_y = kepala_kotak
                    arah_x = 0
                    
        if x1 >= lebar or x1 < 0 or y1 >= tinggi or y1 < 0:
            keluar = True
        x1 += arah_x
        y1 += arah_y
        layar.fill(hitam)
        pygame.draw.rect(layar, merah, [makan_x, makan_y, kepala_kotak, kepala_kotak])
        anggota_badan = []
        anggota_badan.append(x1)
        anggota_badan.append(y1)
        badan.append(anggota_badan)
        if len(badan) > panjang_ular:
            del badan[0]

        for x in badan[:-1]:
            if x == anggota_badan:
                keluar = True

        our_snake(kepala_kotak, badan)
        skormu(panjang_ular - 1)
 
        pygame.display.update()
 
        if x1 == makan_x and y1 == makan_y:
            makan_x = round(random.randrange(0, lebar - kepala_kotak) / 10.0) * 10.0
            makan_y = round(random.randrange(0, tinggi - kepala_kotak) / 10.0) * 10.0
            panjang_ular += 1
 
        clock.tick(speed)
 
    pygame.quit()
    quit()
 
 
gameLoop()