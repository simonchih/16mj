"""Build the precise, code-native mahjong sprites (no AI-generated tile symbols)."""
from pathlib import Path
import math
import os
os.environ.setdefault('SDL_VIDEODRIVER', 'dummy')
import pygame as pg

ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / 'Image'
S = 4
GOLD = (226, 184, 87)
RED = (163, 22, 24)
GREEN = (12, 99, 61)
BLUE = (22, 61, 108)
INK = (27, 38, 35)
pg.init()
pg.display.set_mode((1, 1))

def surface(w, h):
    return pg.Surface((w*S, h*S), pg.SRCALPHA)

def rect(im, color, box, radius=0, width=0):
    pg.draw.rect(im, color, tuple(round(v*S) for v in box), round(width*S), border_radius=round(radius*S))

def line(im, color, a, b, width=1):
    pg.draw.line(im, color, (round(a[0]*S), round(a[1]*S)), (round(b[0]*S), round(b[1]*S)), max(1, round(width*S)))

def circle(im, color, xy, r, width=0):
    pg.draw.circle(im, color, (round(xy[0]*S), round(xy[1]*S)), round(r*S), round(width*S))

def text(im, label, center, size, color):
    f = pg.font.Font(str(ROOT / 'wqy-zenhei.ttf'), round(size*S))
    t = f.render(label, True, color)
    im.blit(t, t.get_rect(center=(round(center[0]*S), round(center[1]*S))))

def save(im, name, size):
    pg.image.save(pg.transform.smoothscale(im, size), str(OUT / (name+'.png')))

def tile(back=False, size=(44, 53)):
    im = surface(*size)
    w, h = size
    rect(im, (0, 12, 8, 90), (2, 3, w-2, h-3), 5)
    rect(im, (10, 62, 39), (1, 2, w-3, h-3), 4)
    rect(im, (25, 114, 69), (2, 1, w-6, h-5), 4)
    rect(im, (190, 151, 73), (0, 0, 35, h-6), 4)
    rect(im, (247, 235, 200), (0.5, 0.5, 33, h-8), 4)
    # Narrow face keeps symbols visible with the legacy 34px overlapping pitch.
    rect(im, (255, 249, 227), (1.5, 1, 31, h-11), 3)
    line(im, (255, 255, 247), (4, 2), (28, 2), 1)
    line(im, (224, 205, 156), (32, 6), (32, h-13), 0.7)
    if back:
        rect(im, (7, 66, 43), (3, 3, 27, h-15), 3)
        rect(im, GOLD, (5, 5, 23, h-19), 2, 0.6)
        for y in range(10, h-17, 7):
            for x in (10, 17, 24):
                line(im, (48, 133, 88), (x-3, y), (x, y-3), 0.6)
                line(im, (48, 133, 88), (x, y-3), (x+3, y), 0.6)
        circle(im, GOLD, (16.5, (h-10)/2), 7, 0.6)
        text(im, '發', (16.5, (h-10)/2), 10, (249, 222, 145))
    return im

def dot(im, x, y, r, color):
    circle(im, (218, 201, 155), (x+0.3, y+0.5), r+0.4)
    circle(im, color, (x, y), r)
    circle(im, (248, 236, 193), (x, y), r*0.7, 0.5)
    circle(im, color, (x, y), r*0.37)
    circle(im, (255, 245, 208), (x-0.6, y-0.8), max(.4, r*.12))

def positions(n):
    return {
        1: [(17, 23)], 2: [(17, 12), (17, 33)],
        3: [(9, 10), (17, 23), (25, 36)],
        4: [(9, 12), (25, 12), (9, 33), (25, 33)],
        5: [(9, 10), (25, 10), (17, 23), (9, 36), (25, 36)],
        6: [(x,y) for y in (10,23,36) for x in (9,25)],
        7: [(8,8),(17,12),(26,16)] + [(x,y) for y in (26,37) for x in (9,25)],
        8: [(x,y) for y in (8,18,28,38) for x in (9,25)],
        9: [(x,y) for y in (10,23,36) for x in (7,17,27)],
    }[n]

def bamboo(im, x, y, n, color):
    height = 8 if n >= 7 else 10
    rect(im, (4, 51, 32), (x-2.6,y-height/2,5.2,height), 2)
    rect(im, color, (x-2.1,y-height/2,4.2,height-.7), 1.6)
    line(im, (161, 199, 134), (x-1,y-height/2+1), (x-1,y+height/2-1), .6)
    line(im, (243, 231, 180), (x-2.3,y), (x+2.3,y), .6)

def badge(label, size, active=False):
    w,h=size
    im=surface(w,h)
    rect(im, (0, 15, 10, 140), (1,2,w-1,h-2), 9)
    rect(im, (122, 87, 28), (0,0,w-2,h-2), 8)
    rect(im, (248, 218, 127), (1,1,w-4,h-4), 7)
    rect(im, (30, 107, 68) if active else (7, 47, 34), (2.5,2.5,w-7,h-7), 6)
    line(im, (148, 172, 111), (7,5), (w-11,5), .6)
    text(im, label, ((w-2)/2,(h-4)/2), min(w,h)*.60, (255,235,168))
    return im

def main():
    OUT.mkdir(exist_ok=True)
    for suit in ('t','s','w'):
        for n in range(1,10):
            im=tile()
            if suit=='w':
                text(im, '一二三四五六七八九'[n-1], (17,13), 18, INK)
                text(im, '萬', (17,33), 23, RED)
            elif suit=='t':
                if n==1:
                    dot(im,17,23,12,GREEN)
                    for i in range(8):
                        a=i*math.pi/4
                        circle(im, BLUE, (17+8*math.cos(a),23+8*math.sin(a)), 2)
                    dot(im,17,23,4,RED)
                else:
                    for i,(x,y) in enumerate(positions(n)):
                        dot(im,x,y,4.4 if n<8 else 3.7,(BLUE,RED,GREEN)[i%3])
            elif n==1:
                # Traditional one-bamboo bird, drawn as a jade peacock.
                for i in range(7):
                    a=math.pi*(.12+i*.125)
                    x,y=17+12*math.cos(a),26+13*math.sin(a)
                    line(im,GREEN,(17,24),(x,y),2)
                    dot(im,x,y,2,BLUE)
                circle(im,GREEN,(17,24),5)
                line(im,GREEN,(18,25),(20,12),3)
                circle(im,GREEN,(20,11),4)
                circle(im,(255,246,213),(21,10),1)
                line(im,RED,(23,12),(27,14),1.5)
                for x in (14,20): line(im,RED,(x,28),(x-2,39),1)
            else:
                for i,(x,y) in enumerate(positions(n)):
                    bamboo(im,x,y,n,RED if n in (5,7,9) and i==n//2 else GREEN)
            save(im,f'MJ{suit}{n}',(44,53))
    for prefix,labels,colors in [('f','東南西北',[INK]*4),('d','中發白',[RED,GREEN,BLUE])]:
        for n,label in enumerate(labels,1):
            im=tile()
            if label=='白':
                rect(im,BLUE,(6,7,22,31),2,2)
                rect(im,BLUE,(9,10,16,25),1,.5)
            else: text(im,label,(17,23),29,colors[n-1])
            save(im,f'MJ{prefix}{n}',(44,53))
    for n,label in enumerate('春夏秋冬梅蘭菊竹',1):
        im=tile()
        text(im,str((n-1)%4+1),(7,8),8,RED)
        text(im,label,(18,18),18,RED if n<5 else BLUE)
        line(im,GREEN,(13,39),(23,29),1)
        for i in range(5):
            a=i*math.tau/5
            circle(im, RED if n<5 else GOLD, (18+4*math.cos(a),33+4*math.sin(a)), 2)
        circle(im,GOLD,(18,33),1.5)
        save(im,f'MJh{n}',(44,53))
    for name in ('mjb','mjback'): save(tile(True,(42,50)),name,(42,50))
    for i,c in enumerate('東南西北'):
        for active,prefix in ((False,'l'),(True,'lred')):
            save(badge(c,(41,40),active),prefix+str(i),(41,40))
    for name,label,size in [('host','莊',(41,40)),('hu','胡',(50,50)),('50x50_hear','聽',(50,50)),('50x50_mjb','',(50,50)),('liu','流',(140,128)),('g','局',(131,140))]:
        save(badge(label,size),name,size)
    im=surface(50,61)
    pg.draw.polygon(im,(250,217,116),[(25*S,3*S),(16*S,20*S),(34*S,20*S)])
    pg.draw.polygon(im,(255,249,217),[(25*S,7*S),(21*S,17*S),(29*S,17*S)])
    save(im,'finger_50x61',(50,61))
    # AI artwork is used only as the table, resized by the game asset pipeline.
    bg=pg.image.load(str(ROOT/'art/table-source.png'))
    pg.image.save(pg.transform.smoothscale(bg,(1200,900)), str(OUT/'Nostalgy.png'))
    save(badge('16',(128,128),True),'icon',(128,128))
    print('Built', len(list(OUT.glob('*.png'))), 'PNG assets')

if __name__=='__main__': main()
