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
mjb_image_filename = 'Image/mjb.gif'

hu_image_filename = 'Image/hu.gif'

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
mjbk   = pygame.image.load(mjb_image_filename).convert()

mjback2 = pygame.transform.rotate(mjback , -90)
mjback3 = pygame.transform.rotate(mjback , -180)
mjback4 = pygame.transform.rotate(mjback , -270)

hu_button = pygame.image.load(hu_image_filename).convert()

p_num = 16
mjp = 0
mjb = 143
turn_id = 0
# location of mj number font remains
renum_loc = (470, 10)
# 0~3: player 0~3
mjloc = [(300, 815), (50, 120), (250, 90), (1100, 120)]
p0_is_AI = False
p0_get_loc_org = (880, 815)
p0_get_loc = []
getmj = -1
#player 0 mj location
p0_mjloc = []
get_done = [False] * 4
#button loc
button_loc = [(1000, 800), (1050, 800), (1000, 850), (1050, 850)]
drop_mj_loc = [[(460, 645)]*64, [(220, 320)]*64, [(460, 260)]*64, [(930, 320)]*64]
drop_mj = [[], [], [], []]
hmj_loc = [[(460, 700)], [(165, 320)], [(460, 205)], [(985, 320)]]
htext_loc = [(750, 700), (165, 270), (380, 205), (950, 270)]
hmj = [[], [], [], []]
dmj_loc = [[(280, 755)], [(110, 150)], [(280, 150)], [(1040, 150)]]
# [type, [value]] in dmj. type 0: eat, 1: show gon, 2: dark gon
dmj = [[], [], [], []]
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
    elif 42 == index:
        return mjbk

def pid_to_image(pid, index):
    pic = index_to_pic(index)

    if 0 == pid:
        return pic
    elif 1 == pid:
        return pygame.transform.rotate(pic , -90)
    elif 2 == pid:
        return pygame.transform.rotate(pic , -180)
    elif 3 == pid:
        return pygame.transform.rotate(pic , -270)
    
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

def check_get_hmj(mj, mj_num):
    rhmj = []
    get_num = 0
    start = -1
    for i in range(mj_num):
        if 42 > mj[i] > 33:
            if -1 == start:
                start = i
            rhmj.append(mj[i])
            get_num += 1
            
    if 0 == get_num:        
        return mj, rhmj, get_num
    else:
        return mj[:start], rhmj, get_num

def proc_add_hmj(pid, get = False, value = -1):
    global hmj
    global player_mj
    global player_mj_num
    
    tmj = []
    thmj = []
    tget_num = 0
    
    if True == get:
        if 42 > value > 33:
            hmj[pid].append(value)
            tget_num = 1
    
    else:
        tmj, thmj, tget_num = check_get_hmj(player_mj[pid], player_mj_num[pid])
    
        if tget_num > 0:
            player_mj[pid] = tmj
            player_mj_num[pid] = len(tmj)
            hmj[pid].extend(thmj)
    
    if tget_num > 0:
        display_all()            
        screen.blit(write(u"補花", (0, 0, 255)), htext_loc[pid])
        pygame.display.update()
        time.sleep(1)
    
    return tget_num

def insert_mj(mjv, pid):
    global player_mj
    global player_mj_num
    
    for i, v in enumerate(player_mj[pid]):
        if mjv <= v:
            player_mj[pid] = player_mj[pid][:i] + [mjv] + player_mj[pid][i:]
            player_mj_num[pid] = len(player_mj[pid])
            return
    
    player_mj[pid].append(mjv)
    player_mj_num[pid] = len(player_mj[pid])
    
def draw_p0_mj(pmj, pmjloc, mjnum):
    for c in range(mjnum):
        i = p_num - mjnum + c
        (x, y) = pmjloc[i]
        screen.blit(pid_to_image(0, pmj[c]), (x, y))
        
    if True == get_done[turn_id]:
        # draw get mj
        screen.blit(pid_to_image(0, getmj), p0_get_loc)

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

def display_dark_gon(pid, loc):
    (x, y) = loc
    if 0 == pid or 2 == pid:
        for i in range(3):
            screen.blit(pid_to_image(pid, 42), (x + i*p0_mj_width, y))
        
        screen.blit(pid_to_image(pid, 42), (x + p0_mj_width, y))
    elif 1 == pid or 3 == pid:
        for i in range(3):
            screen.blit(pid_to_image(pid, 42), (x, y + i*p0_mj_width))
        
        screen.blit(pid_to_image(pid, 42), (x, y + p0_mj_width))
    
def display_show_gon(pid, value, loc):            
    (x, y) = loc
    if 0 == pid or 2 == pid:
        for i in range(3):
            screen.blit(pid_to_image(pid, value), (x + i*p0_mj_width, y))
        
        screen.blit(pid_to_image(pid, value), (x + p0_mj_width, y))
    elif 1 == pid or 3 == pid:
        for i in range(3):
            screen.blit(pid_to_image(pid, value), (x, y + i*p0_mj_width))
        
        screen.blit(pid_to_image(pid, value), (x, y + p0_mj_width))
            
# pid: 0~3
def display_front_eat(pid, fmj, middle, loc):
    (x, y) = loc
    if 0 == pid:
        screen.blit(pid_to_image(0, fmj[0]), (x, y))
        screen.blit(pid_to_image(0, middle), (x + p0_mj_width, y))
        screen.blit(pid_to_image(0, fmj[1]), (x + 2*p0_mj_width, y))
    elif 1 == pid:
        screen.blit(pid_to_image(1, fmj[0]), (x, y))
        screen.blit(pid_to_image(1, middle), (x, y + p0_mj_width))
        screen.blit(pid_to_image(1, fmj[1]), (x, y + 2*p0_mj_width))
    elif 2 == pid:
        screen.blit(pid_to_image(2, fmj[0]), (x, y))
        screen.blit(pid_to_image(2, middle), (x + p0_mj_width, y))
        screen.blit(pid_to_image(2, fmj[1]), (x + 2*p0_mj_width, y))
    elif 3 == pid:
        screen.blit(pid_to_image(3, fmj[0]), (x, y))
        screen.blit(pid_to_image(3, middle), (x, y + p0_mj_width))
        screen.blit(pid_to_image(3, fmj[1]), (x, y + 2*p0_mj_width))

def draw_dmj():
    for pid in range(4):
        for i in range(len(dmj[pid])):
            screen.blit(pid_to_image(pid, dmj[pid][i]), dmj_loc[pid][i])        
        
def draw_hmj():
    for pid in range(4):
        for i in range(len(hmj[pid])):
            screen.blit(pid_to_image(pid, hmj[pid][i]), hmj_loc[pid][i])
            
def draw_drop_mj():
    for pid in range(4):
        for i in range(len(drop_mj[pid])):        
            screen.blit(pid_to_image(pid, drop_mj[pid][i]), drop_mj_loc[pid][i])
        
def display_all():
    fill_background()
    draw_p0_mj(player_mj[0], p0_mjloc, player_mj_num[0])
    draw_mj_column(mjback2, mjloc[1], player_mj_num[1])
    draw_mj_row(mjback3, mjloc[2], player_mj_num[2])
    draw_mj_column(mjback4, mjloc[3], player_mj_num[3])
    draw_dmj()
    draw_hmj()
    draw_drop_mj()
    screen.blit(write(u"麻將剩餘:%d"%(mjb - mjp + 1), (255, 255, 255)), renum_loc)

def write(msg="pygame is cool", color= (0,0,0)):    
    #myfont = pygame.font.SysFont("None", 32) #To avoid py2exe error
    myfont = pygame.font.Font("wqy-zenhei.ttf",36)
    mytext = myfont.render(msg, True, color)
    mytext = mytext.convert_alpha()
    return mytext 
    
def main():
    global all_mj
    global player_mj_num
    global player_mj
    global p0_mjloc
    global mjp
    global mjb
    global drop_mj_loc
    global hmj_loc
    global dmj_loc
    global dmj
    global turn_id
    global get_done
    global p0_get_loc
    global getmj
    
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
    
    # assign p0_mjloc
    ii = 0
    (startx, starty) = mjloc[0]
    for x in range(startx, startx + p_num*p0_mj_width, p0_mj_width):
        p0_mjloc_ini.append([x, starty])
        ii += 1
    # end p0_mjloc
    
    # assign dmj_loc
    gap = 5
    for pi in range(4):
        for i in range(1, 5):
            (x, y) = dmj_loc[pi][i-1]
            if 0 == pi or 2 == pi:
                dmj_loc[pi].append((x + 2*p0_mj_width + mjbk.get_width() + gap, y))
            else: #1 == pi or 3 == pi:
                dmj_loc[pi].append((x, y + 2*p0_mj_width + mjbk.get_height() + gap))
    # end assign dmj loc
    
    # assign hmj_loc
    for pi in range(4):
        for i in range(1, 8):
            (x, y) = hmj_loc[pi][i-1]
            if 0 == pi or 2 == pi:
                hmj_loc[pi].append((x + p0_mj_width, y))
            else: #1 == pi or 3 == pi:
                hmj_loc[pi].append((x, y + p0_mj_width))
    
    # end assign hmj_loc
    
    # assign drop_mj_loc
    for pi in range(4):
        for i in range(4):
            for j in range(8):
                if 0 == j:
                    if 0 == i:
                        continue
                    else:
                        (x, y) = drop_mj_loc[pi][0]
                        if 0 == pi:
                            drop_mj_loc[pi][i*8] = (x, y - i*55)
                        elif 1 == pi:
                            drop_mj_loc[pi][i*8] = (x + i*55, y)
                        elif 2 == pi:
                            drop_mj_loc[pi][i*8] = (x, y + i*55)
                        elif 3 == pi:
                            drop_mj_loc[pi][i*8] = (x - i*55, y)
                else:
                    (x, y) = drop_mj_loc[pi][i*8+j-1]
                    if 0 == pi or 2 == pi:
                        drop_mj_loc[pi][i*8+j] = (x + p0_mj_width, y)
                    else: #1 == pi or 3 == pi:
                        drop_mj_loc[pi][i*8+j] = (x, y + p0_mj_width)
                        
    
    drop_mj_loc[32:64] = drop_mj_loc[0:32]
    # end assign drop_mj_loc
    
    while (mjb - mjp + 1) > 0:
        
        if 1 == first:
            get_done = [False] * 4
            random.shuffle(all_mj)
            for i in range(0, p_num*4, 4):
                player_mj[0][i//4] = all_mj[i]
                player_mj[1][i//4] = all_mj[i+1]
                player_mj[2][i//4] = all_mj[i+2]
                player_mj[3][i//4] = all_mj[i+3]
            player_mj_num = [p_num, p_num, p_num, p_num]
            p0_mjloc_org = copy.deepcopy(p0_mjloc_ini)
            p0_mjloc = copy.deepcopy(p0_mjloc_ini)
            p0_get_loc = list(p0_get_loc_org)
            mjp = p_num*4
            display_all()
            pygame.display.update()
            time.sleep(1)
            
            player_mj[0].sort()
            player_mj[1].sort()
            player_mj[2].sort()
            player_mj[3].sort()
            
            for pid in range(4):
                while True:
                    get_num = proc_add_hmj(pid)
                    if 0 == get_num:
                        break
                    else:
                        for j in range(get_num):
                            insert_mj(all_mj[mjb], pid)
                            mjb -= 1
            
            first = 0
        
        display_all()
        # Temp Test Code
        #for i in range(5):
        #    display_dark_gon(0, dmj_loc[0][i])
        #    display_dark_gon(1, dmj_loc[1][i])
        #    display_dark_gon(2, dmj_loc[2][i])
        #    display_dark_gon(3, dmj_loc[3][i])
        #
        #for i in range(8):
        #    screen.blit(pid_to_image(0, 40), hmj_loc[0][i])
        #    screen.blit(pid_to_image(1, 39), hmj_loc[1][i])
        #    screen.blit(pid_to_image(2, 38), hmj_loc[2][i])
        #    screen.blit(pid_to_image(3, 37), hmj_loc[3][i])
        #
        #for i in range(32):
        #    screen.blit(pid_to_image(0, 4), drop_mj_loc[0][i])
        #    screen.blit(pid_to_image(1, 5), drop_mj_loc[1][i])
        #    screen.blit(pid_to_image(2, 6), drop_mj_loc[2][i])
        #    screen.blit(pid_to_image(3, 7), drop_mj_loc[3][i])
        #screen.blit(write(u"麻將剩餘:%d"%(mjb - mjp + 1), (0, 0, 255)), (470, 10))
        # End Temp Test
        pygame.display.update()
        
        if False == get_done[turn_id]:
            getmj = all_mj[mjp]
            mjp += 1
            get_done[turn_id] = True
        
        for event in pygame.event.get():
            if event.type == QUIT:
                exit()
            elif False == p0_is_AI:
                if event.type == MOUSEBUTTONDOWN:
                    (mouseX, mouseY) = pygame.mouse.get_pos()
                elif event.type == MOUSEBUTTONUP:
                    (mouseX, mouseY) = pygame.mouse.get_pos()

        if False == p0_is_AI:
            select = None
            for c in range(player_mj_num[0]):
                (mouseX, mouseY) = pygame.mouse.get_pos()
                ii = p_num - player_mj_num[0] + c
                (x, y) = p0_mjloc_org[ii]
                if x < mouseX < x + p0_mj_width and y < mouseY < y + t1.get_height():
                    p0_mjloc = copy.deepcopy(p0_mjloc_org)
                    p0_mjloc[ii][1] = p0_mjloc_org[ii][1] - 10
                    select = c
                    break
            if True == get_done[0]:
                (mouseX, mouseY) = pygame.mouse.get_pos()
                (x, y) = p0_get_loc_org
                if x < mouseX < x + t1.get_width() and y < mouseY < y + t1.get_height():
                    p0_get_loc[1] = p0_get_loc_org[1] - 10
                    #get mj index is 16(p_num)
                    select = p_num
            
            if None == select:
                p0_mjloc = copy.deepcopy(p0_mjloc_org)
                p0_get_loc = list(p0_get_loc_org)
                
    exit()
		
if __name__ == "__main__":
    main()
    