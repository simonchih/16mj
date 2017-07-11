import random, os
import time 
import pygame
import math
import copy
from pygame.locals import *
from sys import exit

background_image_filename = 'Image/Nostalgy.gif'

t1_image_filename = 'Image/MJt1.gif'
t2_image_filename = 'Image/MJt2.gif'
t3_image_filename = 'Image/MJt3.gif'
t4_image_filename = 'Image/MJt4.gif'
t5_image_filename = 'Image/MJt5.gif'
t6_image_filename = 'Image/MJt6.gif'
t7_image_filename = 'Image/MJt7.gif'
t8_image_filename = 'Image/MJt8.gif'
t9_image_filename = 'Image/MJt9.gif'

s1_image_filename = 'Image/MJs1.gif'
s2_image_filename = 'Image/MJs2.gif'
s3_image_filename = 'Image/MJs3.gif'
s4_image_filename = 'Image/MJs4.gif'
s5_image_filename = 'Image/MJs5.gif'
s6_image_filename = 'Image/MJs6.gif'
s7_image_filename = 'Image/MJs7.gif'
s8_image_filename = 'Image/MJs8.gif'
s9_image_filename = 'Image/MJs9.gif'

w1_image_filename = 'Image/MJw1.gif'
w2_image_filename = 'Image/MJw2.gif'
w3_image_filename = 'Image/MJw3.gif'
w4_image_filename = 'Image/MJw4.gif'
w5_image_filename = 'Image/MJw5.gif'
w6_image_filename = 'Image/MJw6.gif'
w7_image_filename = 'Image/MJw7.gif'
w8_image_filename = 'Image/MJw8.gif'
w9_image_filename = 'Image/MJw9.gif'

f1_image_filename = 'Image/MJf1.gif'
f2_image_filename = 'Image/MJf2.gif'
f3_image_filename = 'Image/MJf3.gif'
f4_image_filename = 'Image/MJf4.gif'

u1_image_filename = 'Image/MJd1.gif'
u2_image_filename = 'Image/MJd2.gif'
u3_image_filename = 'Image/MJd3.gif'

h1_image_filename = 'Image/MJh1.gif'
h2_image_filename = 'Image/MJh2.gif'
h3_image_filename = 'Image/MJh3.gif'
h4_image_filename = 'Image/MJh4.gif'
h5_image_filename = 'Image/MJh5.gif'
h6_image_filename = 'Image/MJh6.gif'
h7_image_filename = 'Image/MJh7.gif'
h8_image_filename = 'Image/MJh8.gif'

mjback_image_filename = 'Image/mjback.gif'

SCREEN_SIZE = (1200, 900) 
pygame.init()

#pygame.display.set_icon(pygame.image.load("Image/as_arrow.png"))
screen = pygame.display.set_mode(SCREEN_SIZE, 0, 32)#SCREEN_SIZE, FULLSCREEN, 32)
pygame.display.set_caption("16 Mahjong")

screen_width, screen_height = SCREEN_SIZE
        
background = pygame.image.load(background_image_filename).convert()
t1 = pygame.image.load(t1_image_filename).convert()
t2 = pygame.image.load(t2_image_filename).convert()
t3 = pygame.image.load(t3_image_filename).convert()
t4 = pygame.image.load(t4_image_filename).convert()
t5 = pygame.image.load(t5_image_filename).convert()
t6 = pygame.image.load(t6_image_filename).convert()
t7 = pygame.image.load(t7_image_filename).convert()
t8 = pygame.image.load(t8_image_filename).convert()
t9 = pygame.image.load(t9_image_filename).convert()

s1 = pygame.image.load(s1_image_filename).convert()
s2 = pygame.image.load(s2_image_filename).convert()
s3 = pygame.image.load(s3_image_filename).convert()
s4 = pygame.image.load(s4_image_filename).convert()
s5 = pygame.image.load(s5_image_filename).convert()
s6 = pygame.image.load(s6_image_filename).convert()
s7 = pygame.image.load(s7_image_filename).convert()
s8 = pygame.image.load(s8_image_filename).convert()
s9 = pygame.image.load(s9_image_filename).convert()

w1 = pygame.image.load(w1_image_filename).convert()
w2 = pygame.image.load(w2_image_filename).convert()
w3 = pygame.image.load(w3_image_filename).convert()
w4 = pygame.image.load(w4_image_filename).convert()
w5 = pygame.image.load(w5_image_filename).convert()
w6 = pygame.image.load(w6_image_filename).convert()
w7 = pygame.image.load(w7_image_filename).convert()
w8 = pygame.image.load(w8_image_filename).convert()
w9 = pygame.image.load(w9_image_filename).convert()

f1 = pygame.image.load(f1_image_filename).convert()
f2 = pygame.image.load(f2_image_filename).convert()
f3 = pygame.image.load(f3_image_filename).convert()
f4 = pygame.image.load(f4_image_filename).convert()

u1 = pygame.image.load(u1_image_filename).convert()
u2 = pygame.image.load(u2_image_filename).convert()
u3 = pygame.image.load(u3_image_filename).convert()

h1 = pygame.image.load(h1_image_filename).convert()
h2 = pygame.image.load(h2_image_filename).convert()
h3 = pygame.image.load(h3_image_filename).convert()
h4 = pygame.image.load(h4_image_filename).convert()
h5 = pygame.image.load(h5_image_filename).convert()
h6 = pygame.image.load(h6_image_filename).convert()
h7 = pygame.image.load(h7_image_filename).convert()
h8 = pygame.image.load(h8_image_filename).convert()

mjback = pygame.image.load(mjback_image_filename).convert()

mjback2 = pygame.transform.rotate(mjback , -90)
mjback3 = pygame.transform.rotate(mjback , -180)
mjback4 = pygame.transform.rotate(mjback , -270)

p_num = 16
mjp = 0
# 0~3: player 0~3
mjloc = [(300, 800), (50, 120), (250, 90), (1100, 120)]
#player 0 mj location
p0_mjloc = []
p0_mj_width = t1.get_width()-10
player_mj_num = [p_num, p_num, p_num, p_num]
player_mj = [[0]*p_num, [0]*p_num, [0]*p_num, [0]*p_num]
all_mj = [0]*144

def index_to_pic(index):
    if 0 == index:
        return t1
    elif 1 == index:
        return t2
    elif 2 == index:
        return t3
    elif 3 == index:
        return t4
    elif 4 == index:
        return t5
    elif 5 == index:
        return t6
    elif 6 == index:
        return t7
    elif 7 == index:
        return t8
    elif 8 == index:
        return t9
    elif 9 == index:
        return s1
    elif 10 == index:
        return s2
    elif 11 == index:
        return s3
    elif 12 == index:
        return s4
    elif 13 == index:
        return s5
    elif 14 == index:
        return s6
    elif 15 == index:
        return s7
    elif 16 == index:
        return s8
    elif 17 == index:
        return s9
    elif 18 == index:
        return w1
    elif 19 == index:
        return w2
    elif 20 == index:
        return w3
    elif 21 == index:
        return w4
    elif 22 == index:
        return w5
    elif 23 == index:
        return w6
    elif 24 == index:
        return w7
    elif 25 == index:
        return w8
    elif 26 == index:
        return w9
    elif 27 == index:
        return f1
    elif 28 == index:
        return f2
    elif 29 == index:
        return f3
    elif 30 == index:
        return f4
    elif 31 == index:
        return u1
    elif 32 == index:
        return u2
    elif 33 == index:
        return u3
    elif 34 == index:
        return h1
    elif 35 == index:
        return h2
    elif 36 == index:
        return h3
    elif 37 == index:
        return h4
    elif 38 == index:
        return h5
    elif 39 == index:
        return h6
    elif 40 == index:
        return h7
    elif 41 == index:
        return h8

def next_two_not_block(block, mj_num, next):
    n0 = next_not_block(block, mj_num, next)
    if -1 == n0:
        return -1, -1
    n1 = next_not_block(block, mj_num, n0+1)
    if -1 == n1:
        return n0, -1
    
    return n0, n1

# return -1 if exceed mj_num    
def next_not_block(block, mj_num, next):
    i = next
    while i < mj_num:
        if 0 == block[i]:
            return i
        i += 1
        
    return -1

def next_not_same(mj, mj_num, id):
    i = id+1
    v = mj[id]
    while i < mj_num:
        if v == mj[i]:
            i += 1
            continue
        else:
            return i
    return -1

# -1: Can't gon, 0~mj_num - 1: start of mj index    
def gon(mj, mj_num, value):
    for i in range(mj_num - 2):
        if value == mj[i] == mj[i+1] == mj[i+2]:
            return i
    return -1
# -1: Can't pon, 0~mj_num - 1: start of mj index
def pon(mj, mj_num, value):
    for i in range(mj_num - 1):
        if value == mj[i] == mj[i+1]:
            return i
    return -1

# []: Can't eat, [a, b, c]: eat index
def eat(mj, mj_num, value):
    eindex = []
    if value >= 27:
        return eindex
    
    for i in range(mj_num - 1):
        if mj[i] >= 27:
            continue
        elif  mj[i]//9 == mj[i+1]//9 == value//9:
            if mj[i] + 2 == mj[i+1] + 1 == value or mj[i] + 2 == value + 1 == mj[i+1] or value + 2 == mj[i] + 1 == mj[i+1]:
                eindex.append(i)
        
    return eindex
def hear(mj, mj_num):
    block = [0] * mj_num
    
    c = 0
    while c < mj_num:
        if mj_num - 1 == c:
            mj_hear = 0
            break
        #check pair
        if mj[c] == mj[c+1]:
            block[c] = 1
            block[c+1] = 1
            i = 0
            
            # mj_hear 1:hear, 0:NOT hear
            mj_hear = 1
            two_s = 0
            while i < mj_num:
                if 1 == block[i]:
                    i += 1
                    continue
                
                n1, n2 = next_two_not_block(block, mj_num, i+1)
                
                if -1 == n1 and -1 == n2:
                    mj_hear = 0
                    break
                elif n1 != -1 and -1 == n2:
                    if 1 == two_s:
                        mj_hear = 0
                        break
                    elif mj[i] == mj[n1] or (mj[i] < 27 and mj[i]//9 == mj[n1]//9 and mj[i]+1 == mj[n1]):
                        two_s = 1
                        i += 2
                        continue
                    else:
                        mj_hear = 0
                        break
                else:
                    if mj[i] == mj[n1] == mj[n2]:
                        i += 3
                        continue
                    elif mj[i] < 27 and mj[i]//9 == mj[n1]//9 == mj[n2]//9 and mj[i]+1 == mj[n1] and mj[n1]+1 == mj[n2]:
                        i += 3
                        continue
                    else:
                        if 1 == two_s:
                            mj_hear = 0
                            break
                        elif mj[i] == mj[n1] or (mj[i] < 27 and mj[i]//9 == mj[n1]//9 and mj[i]+1 == mj[n1]):
                            two_s = 1
                            i += 2
                            continue
                        else:
                            mj_hear = 0
                            break
                i += 1
            if 1 == mj_hear:
                return 1
                
            block[c] = 0
            block[c+1] = 0
            c += 2
        else:    
            c += 1
    
    # Check NOT pair
    c = 0
    while c < mj_num:
        nt = next_not_same(mj, mj_num, c)
        if -1 == nt:
            # the end
            block[c] = 1
        elif nt - c > 1:
            c = nt
            # sequence
            continue
        else:
            # only one
            block[c] =1
            
        i = 0
        # mj_hear 1:hear, 0:NOT hear
        mj_hear = 1
        while i < mj_num:
            if 1 == block[i]:
                i += 1
                continue
            
            n1, n2 = next_two_not_block(block, mj_num, i+1)
            
            if -1 == n2:
                mj_hear = 0
                break
            else:
                if mj[i] == mj[n1] == mj[n2]:
                    i += 3
                    continue
                elif mj[i] < 27 and mj[i]//9 == mj[n1]//9 == mj[n2]//9 and mj[i]+1 == mj[n1] and mj[n1]+1 == mj[n2]:
                    i += 3
                    continue
                else:
                    mj_hear = 0
                    break
            i += 1
        if 1 == mj_hear:
            return 1
            
        block[c] = 0 
        c += 1
    
    return 0
    
# rturn 1: hu, 0: NOT hu, mj must sort   
def hu(mj, mj_num):
    block = [0] * mj_num
    
    c = 0
    while c < mj_num:
        if mj_num - 1 == c:
            break
        #check pair
        if mj[c] == mj[c+1]:
            block[c] = 1
            block[c+1] = 1
            i = 0
            
            # mj_hu 1:hu, 0:NOT hu
            mj_hu = 1
            while i < mj_num:
                if 1 == block[i]:
                    i += 1
                    continue
                
                n1, n2 = next_two_not_block(block, mj_num, i+1)
                
                if n1 != -1 and n2 != -1:
                    if mj[i] == mj[n1] == mj[n2]:
                        i += 3
                        continue
                    elif mj[i] < 27 and mj[i]//9 == mj[n1]//9 == mj[n2]//9 and mj[i]+1 == mj[n1] and mj[n1]+1 == mj[n2]:
                        i += 3
                        continue
                    else:
                        mj_hu = 0
                        break
                else:
                    mj_hu = 0
                    break
                i += 1
            if 1 == mj_hu:
                return 1
                
            block[c] = 0
            block[c+1] = 0
            c += 2
            
        c += 1
    
    return 0
    
def draw_p0_mj(pmj, pmjloc, mjnum):
    for c, xy in enumerate(pmjloc):
        if c == mjnum:
            break
        (x, y) = xy
        screen.blit(index_to_pic(pmj[c]), (x, y))

def draw_mj_column(mj_pic, xy, mj_num):
    (startx, starty) = xy
    for y in range(starty, starty + mj_num*mj_pic.get_height(), mj_pic.get_height()):
        screen.blit(mj_pic, (startx, y))

def draw_mj_row(mj_pic, xy, mj_num):
    (startx, starty) = xy
    for x in range(startx, startx + mj_num*mj_pic.get_width(), mj_pic.get_width()):
        screen.blit(mj_pic, (x, starty))

def fill_background():
    for y in range(0, screen_height, background.get_height()):
        for x in range(0, screen_width, background.get_width()):
            screen.blit(background, (x, y))

def display_all():
    fill_background()
    draw_p0_mj(player_mj[0], p0_mjloc, player_mj_num[0])
    draw_mj_column(mjback2, mjloc[1], player_mj_num[1])
    draw_mj_row(mjback3, mjloc[2], player_mj_num[2])
    draw_mj_column(mjback4, mjloc[3], player_mj_num[3])
            
def main():
    global all_mj
    global player_mj_num
    global player_mj
    global p0_mjloc
    global mjp
    
    first = 1
    p0_mjloc_ini = []
    
    # assign all mj
    for i in range(34):
        for repeat in range(4):
            all_mj[4*i+repeat] = i
    
    j = 34
    for i in range(136, 144):
        all_mj[i] = j
        j += 1
    # end assign all mj
    
    ii = 0
    (startx, starty) = mjloc[0]
    for x in range(startx, startx + p_num*p0_mj_width, p0_mj_width):
        p0_mjloc_ini.append([x, starty])
        ii += 1
    
    while True:
        
        if 1 == first:
            random.shuffle(all_mj)
            for i in range(0, p_num*4, 4):
                player_mj[0][i//4] = all_mj[i]
                player_mj[1][i//4] = all_mj[i+1]
                player_mj[2][i//4] = all_mj[i+2]
                player_mj[3][i//4] = all_mj[i+3]
            player_mj_num = [p_num, p_num, p_num, p_num]
            p0_mjloc_org = copy.deepcopy(p0_mjloc_ini)
            p0_mjloc = copy.deepcopy(p0_mjloc_ini)
            mjp = p_num*4
            display_all()
            pygame.display.update()
            time.sleep(2)
            
            player_mj[0].sort()
            player_mj[1].sort()
            player_mj[2].sort()
            player_mj[3].sort()
            
            first = 0
        
        display_all()
        pygame.display.update()
        
        for event in pygame.event.get():
            if event.type == QUIT:
                exit()
            if event.type == MOUSEBUTTONDOWN:
                (mouseX, mouseY) = pygame.mouse.get_pos()
            elif event.type == MOUSEBUTTONUP:
                (mouseX, mouseY) = pygame.mouse.get_pos()
        
        select = None
        for c, v in enumerate(p0_mjloc_org):
            if c == player_mj_num:
                break
            (mouseX, mouseY) = pygame.mouse.get_pos()
            if v[0] < mouseX < v[0] + p0_mj_width and v[1] < mouseY < v[1] + t1.get_height():
                p0_mjloc = copy.deepcopy(p0_mjloc_org)
                p0_mjloc[c][1] = p0_mjloc_org[c][1] - 10
                select = c
                break
            
        if None == select:
            p0_mjloc = copy.deepcopy(p0_mjloc_org)
                
    exit()
		
if __name__ == "__main__":
    main()
    