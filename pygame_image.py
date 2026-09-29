import os
import sys
import pygame as pg

os.chdir(os.path.dirname(os.path.abspath(__file__)))


def main():
    pg.display.set_caption("はばたけ！こうかとん")
    screen = pg.display.set_mode((800, 600))
    clock  = pg.time.Clock()
    bg_img = pg.image.load("fig/pg_bg.jpg")
    bg_img_hantenn = pg.image.load("fig/pg_bg.jpg") #練習8
    bg_img_hantenn = pg.transform.flip(bg_img_hantenn, True, False) #練習8
    kk_img = pg.image.load("fig/3.png") #練習3:こうかとん画像surfaceの作成
    kk_img = pg.transform.flip(kk_img, True, False) #こうかとん左右反転
    kk_rct = kk_img.get_rect() #練習10-1
    kk_rct.center = 300, 200 #練習10-2
    tmr = 0
    while True:
        for event in pg.event.get():
            if event.type == pg.QUIT: return

        x = (tmr%3200) #練習9
        screen.blit(bg_img, [-x, 0])
        screen.blit(bg_img_hantenn, [-x+1600, 0]) #練習7
        screen.blit(bg_img, [-x+3200, 0]) #練習9
        x_zahyou = 0 #演習課題2
        y_zahyou = 0
        key_lst = pg.key.get_pressed() #練習10-3
        if key_lst[pg.K_UP]: #練習10-4
            x_zahyou = 0
            y_zahyou = -1
        elif key_lst[pg.K_DOWN]:
            x_zahyou = 0
            y_zahyou = 1
        elif key_lst[pg.K_LEFT]:
            x_zahyou = -1
            y_zahyou = 0
        elif key_lst[pg.K_RIGHT]:
            x_zahyou = 2
            y_zahyou = 0
        kk_rct.move_ip(x_zahyou-1, y_zahyou)
        screen.blit(kk_img, kk_rct) #練習10-5
        pg.display.update()
        tmr += 1        
        clock.tick(200)


if __name__ == "__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()