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
button_image_filename = 'Image/50x50_mjb.gif'

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
button = pygame.image.load(button_image_filename).convert()

p_num = 16
mjp = 0
mjb = 143
turn_id = 0
host_id = 0
# location of mj number font remains
renum_loc = (470, 10)
# 0~3: player 0~3
mjloc = [(300, 815), (50, 120), (250, 90), (1100, 120)]
huloc = [(575, 630), (240, 425), (575, 270), (910, 425)]
p0_is_AI = False
Add_Delay = True
p0_get_loc_org = (880, 815)
p0_get_loc = []
eat_index = []
getmj = -1
#player 0 mj location
p0_mjloc = []
# 2: won't show get mj, 1:get done, 0:get from mjp, -1: get from mjb 
get_done = [0] * 4
hear_status = [False] * 4
#button loc
button_loc = [(1000, 800), (1050, 800), (1100, 800), (1000, 850), (1050, 850), (1100, 850)]
#-1: ini, 0: Disable, 1: Enable, 2: Clicked (for eat only)
button_enable = [-1] * 6
drop_mj_loc = [[(460, 645)]*64, [(220, 320)]*64, [(460, 260)]*64, [(930, 320)]*64]
drop_mj = [[], [], [], []]
hmj_loc = [[(460, 700)], [(165, 320)], [(460, 205)], [(985, 320)]]
htext_loc = [(750, 700), (165, 270), (380, 205), (950, 270)]
hmj = [[], [], [], []]
dmj_loc = [[(280, 755)], [(110, 150)], [(280, 150)], [(1040, 150)]]
# [type, [value]] in dmj. type 0: eat, 1: show gon, 2: dark gon, 3: pon
# if type == 2 (dark gon), NO value property, e.g. [type]
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
    elif 43 == index:
        return hu_button

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

def next_two_not_blsame(block, mj_num, next, mj, sv):
    n0 = next_not_blsame(block, mj_num, mj, sv, next)
    if -1 == n0:
        return -1, -1
    n1 = next_not_blsame(block, mj_num, mj, mj[n0], n0+1)
    if -1 == n1:
        return n0, -1
    
    return n0, n1    
    
# return -1 if exceed mj_num    
def next_not_block(block, mj_num, next=0):
    i = next
    while i < mj_num:
        if 0 == block[i]:
            return i
        i += 1
        
    return -1

# return -1 if exceed mj_num    
def next_not_blsame(block, mj_num, mj, sv, next=0):
    i = next
    while i < mj_num:
        if 0 == block[i] and mj[i] != sv:
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

# Precondition, mj must sort    
def seq3_block(mj, mj_num, block):
    i = 0
    while i < mj_num - 2:
        if 1 == block[i]:
            i += 1
            continue
        else:
            m1, m2 = next_two_not_blsame(block, mj_num, i+1, mj, mj[i])            
            if m1 != -1 and m2 != -1 and mj[i] < 27 and mj[i]//9 == mj[m1]//9 == mj[m2]//9 and mj[i]+1 == mj[m1] and mj[m1]+1 == mj[m2]:
                block[i] = block[m1] = block[m2] = 1
                i += 1
                continue
        i += 1
        
    return block
    
# Precondition, mj must sort
def same3_block(mj, mj_num, block):
    i = 0
    while i < mj_num - 2:
        if 1 == block[i]:
            i += 1
        elif mj[i] == mj[i+1] == mj[i+2]:
            block[i] = block[i+1] = block[i+2] = 1
            i += 3
        else:
            i += 1
    return block

def add_block3(mj, mj_num, block):
    b = same3_block(mj, mj_num, block)
    b = seq3_block(mj, mj_num, b)
    return b

def add_block2(mj, mj_num, block):
    i = 0
    while block.count(0) > 2 and i < mj_num - 1: 
        if 0 == block[i]:
            j = next_not_block(block, mj_num, i+1)
            if j != -1:
                if mj[i] == mj[j]:
                    block[i] = block[j] = 1
                elif mj[i] < 27 and mj[i]//9 == mj[j]//9 and mj[i]+1 == mj[j]:
                    block[i] = block[j] = 1
        
        i += 1
        
    return block

def select_mj(p0_mjloc_org, tid = 0):    
    global p0_mjloc
    
    select = None
    for c in range(player_mj_num[tid]):
        (mouseX, mouseY) = pygame.mouse.get_pos()
        ii = p_num - player_mj_num[tid] + c
        (x, y) = p0_mjloc_org[ii]
        if x < mouseX < x + p0_mj_width and y < mouseY < y + t1.get_height():
            p0_mjloc = copy.deepcopy(p0_mjloc_org)
            p0_mjloc[ii][1] = p0_mjloc_org[ii][1] - 10
            select = c
            break
    
    if None == select:
        p0_mjloc = copy.deepcopy(p0_mjloc_org)
        
    return select
    
# reset button except hear button    
def reset_p0_button():    
    global button_enable
    
    hear_enable = button_enable[2]
    button_enable = [0] * len(button_loc)
    button_enable[2] = hear_enable

def button_enable_chk():
    for i in range(len(button_loc)):
        if 2 == i and 1 == button_enable[i]:
            return True
        elif i != 2 and button_enable[i] > 0:
            return True
    return False
    
def check_p0_button(mj, mj_num, myvalue = None, value = None, chk_eat = False):
    global button_enable
    
    reset_p0_button()
    
    enable = False
    
    if False == hear_status[0]:
        # It's NOT possible for myvalue != None and value != None 
        if None == value and None == myvalue:
            if 0 == button_enable[2] and 1 == hear(mj, mj_num):
                button_enable[2] = 1
                button_enable[5] = 1
                enable = True
        elif None == value: # myvalue != None
            if gon(mj, mj_num, myvalue) != -1:
                button_enable[1] = 1
                enable = True
        else: # value != None
            if False == chk_eat:
                if pon(mj, mj_num, value) != -1:
                    button_enable[0] = 1
                    button_enable[5] = 1
                    enable = True
                if gon(mj, mj_num, value) != -1:
                    button_enable[1] = 1
                    button_enable[5] = 1
                    enable = True
            elif eat(mj, mj_num, value) != -1: #chk_eat == True
                button_enable[3] = 1
                button_enable[5] = 1
                enable = True
    elif myvalue != None and 1 == hu(mj, myvalue):
        button_enable[4] = 1
        enable = True
    elif value != None and 1 == hu(mj, value):
        button_enable[4] = 1
        button_enable[5] = 1
        enable = True
    
    return enable
    
# -1: Can't gon, 0~mj_num - 4: start of mj index 
def dark_gon(mj, mj_num):
    for i in range(mj_num - 3):
        if mj[i] == mj[i+1] == mj[i+2] == mj[i+3]:
            return i
    return -1
    
# -1: Can't gon, 0~mj_num - 3: start of mj index    
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

# []: Can't eat, [a, c]: eat index
def eat(mj, mj_num, value):
    eindex = []
    if value >= 27:
        return eindex
    
    i = 0
    while i < mj_num - 1:
        if mj[i] >= 27:
            i += 1
            continue
        else:
            j = next_not_same(mj, mj_num, i)
            if -1 == j:
                break
            if  mj[i]//9 == mj[j]//9 == value//9:
                if mj[i] + 2 == mj[j] + 1 == value or mj[i] + 2 == value + 1 == mj[j] or value + 2 == mj[i] + 1 == mj[j]:
                    eindex.append(i)
                    eindex.append(j)
                    break
        i += 1
        
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
                        block[i] = block[n1] = 1
                        i += 1
                        continue
                    else:
                        mj_hear = 0
                        break
                else:
                    if mj[i] == mj[n1] == mj[n2]:
                        block[i] = block[n1] = block[n2] = 1
                        i += 1
                        continue
                    else:
                        m1, m2 = next_two_not_blsame(block, mj_num, i+1, mj, mj[i])
                        
                        if m1 != -1 and m2 != -1 and mj[i] < 27 and mj[i]//9 == mj[m1]//9 == mj[m2]//9 and mj[i]+1 == mj[m1] and mj[m1]+1 == mj[m2]:
                            block[i] = block[m1] = block[m2] = 1
                            i += 1
                            continue
                        else:
                            if 1 == two_s:
                                mj_hear = 0
                                break
                            elif mj[i] == mj[m1] or (mj[i] < 27 and mj[i]//9 == mj[m1]//9 and mj[i]+1 == mj[m1]):
                                two_s = 1
                                block[i] = block[m1] = 1
                                i += 1
                                continue
                            else:
                                mj_hear = 0
                                break
            
            if 1 == mj_hear:
                return 1
                
            block = [0] * mj_num
            c += 2
        else:    
            c += 1
    
    block = [0] * mj_num
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
                    block[i] = block[n1] = block[n2] = 1
                    i += 1
                    continue
                else:
                    m1, m2 = next_two_not_blsame(block, mj_num, i+1, mj, mj[i])
                    
                    if m1 != -1 and m2 != -1 and mj[i] < 27 and mj[i]//9 == mj[m1]//9 == mj[m2]//9 and mj[i]+1 == mj[m1] and mj[m1]+1 == mj[m2]:
                        block[i] = block[m1] = block[m2] = 1
                        i += 1
                        continue
                    else:
                        mj_hear = 0
                        break

        if 1 == mj_hear:
            return 1
            
        block = [0] * mj_num
        c += 1
    
    return 0
    
# rturn 1: hu, 0: NOT hu, mj must sort   
def hu(pmj, value):

    mj, mj_num = insert_mj(value, pmj)
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
                        block[i] = block[n1] = block[n2] = 1
                        i += 1
                        continue
                    else:
                        m1, m2 = next_two_not_blsame(block, mj_num, i+1, mj, mj[i])
                        
                        if m1 != -1 and m2 != -1 and mj[i] < 27 and mj[i]//9 == mj[m1]//9 == mj[m2]//9 and mj[i]+1 == mj[m1] and mj[m1]+1 == mj[m2]:
                            block[i] = block[m1] = block[m2] = 1
                            i += 1
                            continue
                        else:
                            mj_hu = 0
                            break
                else:
                    mj_hu = 0
                    break
                    
            if 1 == mj_hu:
                return 1
                
            block = [0] * mj_num
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
        if True == Add_Delay:
            time.sleep(1)
    
    return tget_num

def insert_mj(mjv, mj):
    return_mj = mj[:]
    for i, v in enumerate(return_mj):
        if mjv <= v:
            return_mj = return_mj[:i] + [mjv] + return_mj[i:]
            return return_mj, len(return_mj)
    
    return_mj.append(mjv)
    return return_mj, len(return_mj)

def draw_hu(win_id):
    if win_id >= 0:
        screen.blit(pid_to_image(win_id, 43), huloc[win_id])
    
def draw_p0_mj(pmj, pmjloc, mjnum):
    for c in range(mjnum):
        i = p_num - mjnum + c
        (x, y) = pmjloc[i]
        screen.blit(pid_to_image(0, pmj[c]), (x, y))
        
    if 1 == get_done[turn_id] and 0 == turn_id:
        # draw get mj
        screen.blit(pid_to_image(0, getmj), p0_get_loc)

def draw_mj_column(mj_pic, xy, mj_num, draw_all = -1):
    (startx, starty) = xy
    if -1 == draw_all:
        for y in range(starty, starty + mj_num*mj_pic.get_height(), mj_pic.get_height()):
            screen.blit(mj_pic, (startx, y))
    elif 1 == draw_all:
        c = 0
        for y in range(starty, starty + mj_num*p0_mj_width, p0_mj_width):
            screen.blit(pid_to_image(draw_all, player_mj[draw_all][c]), (startx, y))
            c += 1
    elif 3 == draw_all: # reverse older
        c = mj_num - 1
        for y in range(starty + (mj_num-1)*p0_mj_width, starty - 1, (-1)*p0_mj_width):
            screen.blit(pid_to_image(draw_all, player_mj[draw_all][c]), (startx, y))
            c -= 1

def draw_mj_row(mj_pic, xy, mj_num, draw_all = -1):
    (startx, starty) = xy
    if -1 == draw_all:
        for x in range(startx, startx + mj_num*mj_pic.get_width(), mj_pic.get_width()):
            screen.blit(mj_pic, (x, starty))
    else: # reverse older
        c = mj_num - 1
        for x in range(startx + (mj_num-1)*p0_mj_width, startx - 1, (-1)*p0_mj_width):
            screen.blit(pid_to_image(draw_all, player_mj[draw_all][c]), (x, starty))
            c -= 1

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
            
# pid: 0~3, middle is fmj[2]
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
        screen.blit(pid_to_image(2, fmj[1]), (x + 2*p0_mj_width, y))
        screen.blit(pid_to_image(2, middle), (x + p0_mj_width, y))
        screen.blit(pid_to_image(2, fmj[0]), (x, y))
    elif 3 == pid:
        screen.blit(pid_to_image(3, fmj[1]), (x, y + 2*p0_mj_width))
        screen.blit(pid_to_image(3, middle), (x, y + p0_mj_width))
        screen.blit(pid_to_image(3, fmj[0]), (x, y))
        
def display_pon(pid, value, loc):            
    (x, y) = loc
    if 0 == pid:
        for i in range(3):
            screen.blit(pid_to_image(pid, value), (x + i*p0_mj_width, y))
    elif 2 == pid:
         for i in range(2, -1, -1):
            screen.blit(pid_to_image(pid, value), (x + i*p0_mj_width, y))
    elif 1 == pid:
        for i in range(3):
            screen.blit(pid_to_image(pid, value), (x, y + i*p0_mj_width))      
    elif 3 == pid:
        for i in range(2, -1, -1):
            screen.blit(pid_to_image(pid, value), (x, y + i*p0_mj_width))
    
def draw_dmj():
    for pid in range(4):
        for i in range(len(dmj[pid])):
            if 0 == dmj[pid][i][0]:
                display_front_eat(pid, dmj[pid][i][1], dmj[pid][i][1][2], dmj_loc[pid][i])
            elif 1 == dmj[pid][i][0]:
                display_show_gon(pid, dmj[pid][i][1][0], dmj_loc[pid][i])
            elif 2 == dmj[pid][i][0]:
                display_dark_gon(pid, dmj_loc[pid][i])
            elif 3 == dmj[pid][i][0]:
                display_pon(pid, dmj[pid][i][1][0], dmj_loc[pid][i])
        
def draw_hmj():
    for pid in range(4):
        for i in range(len(hmj[pid])):
            screen.blit(pid_to_image(pid, hmj[pid][i]), hmj_loc[pid][i])
            
def draw_drop_mj():
    for pid in range(4):
        for i in range(len(drop_mj[pid])):
            screen.blit(pid_to_image(pid, drop_mj[pid][i]), drop_mj_loc[pid][i])
        
def draw_p123_mj(win_id = -1):
    for pid in range(1,4):
        if pid == win_id:
            draw = pid
        else:
            draw = -1
        
        if 2 == pid:
            draw_mj_row(mjback3, mjloc[pid], player_mj_num[pid], draw)
        else: # player 1, 3
            draw_mj_column(mjback4, mjloc[pid], player_mj_num[pid], draw)
        

def display_all(win_id = -1, did = -1):
    fill_background()
    draw_p0_mj(player_mj[0], p0_mjloc, player_mj_num[0])
    draw_p123_mj(win_id)
    draw_dmj()
    draw_hmj()
    draw_drop_mj()
    draw_p0_button()
    draw_hu(win_id)
    screen.blit(write(u"麻將剩餘:%d"%(mjb - mjp + 1), (255, 255, 255)), renum_loc)
    if did != -1:
        (x, y) = drop_mj_loc[did][len(drop_mj[did])-1]
        p = pid_to_image(did, drop_mj[did][-1])
        pygame.draw.rect(screen, (0xff, 0, 0), (x, y, p.get_width(), p.get_height()), 3)

def index_to_btext(index):
    if 0 == index:
        return u"碰"
    elif 1 == index:
        return u"槓"
    elif 2 == index:
        return u"聽"
    elif 3 == index:
        return u"吃"
    elif 4 == index:
        return u"胡"
    elif 5 == index:
        return u"返"

def draw_p0_button():
    # Test only
    #button_enable = [1] * 6
    # End Test only
    for i in range(len(button_loc)):
        if button_enable[i] > 0:
            (mouseX, mouseY) = pygame.mouse.get_pos()
            (x, y) = button_loc[i]
            screen.blit(button, button_loc[i])
            if 2 == button_enable[i]:
                screen.blit(write(index_to_btext(i), (255, 0, 0), 30), (x+10, y+5))
            elif x < mouseX < x + button.get_width() and y < mouseY < y + button.get_height():
                screen.blit(write(index_to_btext(i), (0, 255, 0), 30), (x+10, y+5))
            else:
                screen.blit(write(index_to_btext(i), (0, 0, 0), 30), (x+10, y+5))
    
def click_p0_button(mouseX, mouseY):
    global button_enable
    global hear_status
    
    l = len(button_loc)
    
    for i in range(l):
        if button_enable[i] > 0:
            (x, y) = button_loc[i]            
            if x < mouseX < x + button.get_width() and y < mouseY < y + button.get_height():
                if 2 == button_enable[i]:
                    if 0 == i or 1 == i or 3 == i: # Can't off hear, hu, return
                        button_enable[i] = 1
                        return i
                # if 1 == button_enable[i]    
                elif 5 == i:
                    no2 = True
                    for j in range(l):
                        if 2 == j or 4 == j or 5 == j: # Can't off hear, hu, return
                            continue
                        elif 2 == button_enable[j]:
                            no2 = False
                            button_enable[j] = 1
                    
                    if True == no2: # True == no2, return 5
                        return i
                    else: # False == no2, return None
                        continue
                elif 0 == i or 1 == i or 2 == i or 3 == i :
                    button_enable[i] = 2
                    if 2 == i:
                        hear_status[0] = True
                # 4 == i
                return i
                
def write(msg="pygame is cool", color= (0,0,0), size = 36):    
    #myfont = pygame.font.SysFont("None", 32) #To avoid py2exe error
    myfont = pygame.font.Font("wqy-zenhei.ttf",size)
    mytext = myfont.render(msg, True, color)
    mytext = mytext.convert_alpha()
    return mytext 

def mjAI(tid, getv = None):
    global player_mj
    global player_mj_num
    global dmj
    global drop_mj
    
    if None == getv:
        tmj = player_mj[tid][:]
        tmj_num = player_mj_num[tid]
    elif 1 == proc_add_hmj(tid, True, getv):
        return -1
    else:
        tmj, tmj_num = insert_mj(getv, player_mj[tid])
    
    si = dark_gon(tmj, tmj_num)
    if si != -1 and getv != None:
        player_mj[tid] = list(filter(lambda a: a != tmj[si], tmj))
        player_mj_num[tid] = len(player_mj[tid])
        dmj[tid].append([2])
        return -1
    
    block = [0] * tmj_num
    block = add_block3(tmj, tmj_num, block)
    block0_num = block.count(0)
    
    if block0_num > 2:
        block = add_block2(tmj, tmj_num, block)
    
    di = next_not_block(block, len(block))
    if -1 == di:
        print("di == -1")
        input("wrong")
    drop_mj[tid].append(tmj[di])
    player_mj[tid] = tmj[:di] + tmj[di+1:]
    player_mj_num[tid] = len(player_mj[tid])
    
    return 2
    
def main():
    global all_mj
    global player_mj_num
    global player_mj
    global p0_mjloc
    global mjp
    global mjb
    global drop_mj_loc
    global drop_mj
    global hmj_loc
    global hmj
    global dmj_loc
    global dmj
    global turn_id
    global get_done
    global p0_get_loc
    global getmj
    global button_enable
    global hear_status
    global host_id
    global eat_index
    
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
    
    # reverse older
    hmj_loc[2] = hmj_loc[2][::-1]
    hmj_loc[3] = hmj_loc[3][::-1]
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
                        
    for pi in range(4):
        if 2 == pi or 3 == pi: # reverse older
            drop_mj_loc[pi][0:8] = drop_mj_loc[pi][7::-1]
            for i in range(1, 4):
                drop_mj_loc[pi][8*i:8*(i+1)] = drop_mj_loc[pi][8*(i+1)-1:8*i-1:-1]
        drop_mj_loc[pi][32:64] = drop_mj_loc[pi][0:32]
    # end assign drop_mj_loc
    
    while True:
        while (mjb - mjp + 1) > 0:
            
            if 1 == first:
                # winner: -1, ini. 0~3: winner id
                winner = -1
                turn_id = host_id
                # check_button, 0: ini
                check_button = 0 #local variable
                hear_status = [False] * 4
                get_done = [0] * 4
                eat_index = []
                button_enable = [-1] * len(button_loc)
                dmj = [[], [], [], []]
                hmj = [[], [], [], []]
                drop_mj = [[], [], [], []]
                player_mj = [[0]*p_num, [0]*p_num, [0]*p_num, [0]*p_num]
                player_mj_num = [p_num, p_num, p_num, p_num]
                
                random.shuffle(all_mj)
                for i in range(0, p_num*4, 4):
                    player_mj[turn_id][i//4] = all_mj[i]
                    player_mj[(turn_id+1)%4][i//4] = all_mj[i+1]
                    player_mj[(turn_id+2)%4][i//4] = all_mj[i+2]
                    player_mj[(turn_id+3)%4][i//4] = all_mj[i+3]
                player_mj_num = [p_num, p_num, p_num, p_num]
                p0_mjloc_org = copy.deepcopy(p0_mjloc_ini)
                p0_mjloc = copy.deepcopy(p0_mjloc_ini)
                p0_get_loc = list(p0_get_loc_org)
                mjp = p_num*4
                display_all()
                pygame.display.update()
                if True == Add_Delay:
                    time.sleep(1)
                
                player_mj[0].sort()
                player_mj[1].sort()
                player_mj[2].sort()
                player_mj[3].sort()
                
                p4_noh = [0] * 4
                
                while p4_noh.count(1) < 4:
                    for pid in range(4):
                        get_num = proc_add_hmj(pid)
                        if 0 == get_num:
                            p4_noh[pid] = 1
                        else:
                            for j in range(get_num):
                                player_mj[pid], player_mj_num[pid] = insert_mj(all_mj[mjb], player_mj[pid])
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
            #for i in range(4):
            #    screen.blit(pid_to_image(i, 43), huloc[i])
            #screen.blit(button, button_loc[0])
            # End Temp Test
            pygame.display.update()

            # handle_drop_done. -1: ini, 0: handle player drop mj, 1: done and drop mj again, 2: done and get from mjb, 3: hu, 4: need to handle p0 drop mj, 5: p0 eat and drop mj done
            handle_drop_done = -1

            if 0 == (mjb - mjp + 1):
                break
            elif 0 == get_done[turn_id] or -1 == get_done[turn_id]:
                if 0 == get_done[turn_id]:
                    getmj = all_mj[mjp]
                    mjp += 1
                elif -1 == get_done[turn_id]:
                    getmj = all_mj[mjb]
                    mjb -= 1
                if 0 == proc_add_hmj(turn_id, True, getmj):
                    get_done[turn_id] = 1
                    if 0 == turn_id and False == p0_is_AI:
                        if 0 == check_button:
                            check_p0_button(player_mj[turn_id], player_mj_num[turn_id], getmj)
                            check_button = 1
                    else:
                        # Check hu
                        if 1 == hu(player_mj[turn_id], getmj):
                            temp_mj, temp_mj_num = insert_mj(getmj, player_mj[turn_id])
                            if turn_id != 0:
                                player_mj[turn_id] = list(temp_mj)
                                player_mj_num[turn_id] = temp_mj_num
                            winner = turn_id
                            display_all(winner)
                            pygame.display.update()
                            if True == Add_Delay:
                                time.sleep(9)
                            break
                elif len(hmj[turn_id]) == 8:
                    winner = turn_id
                    display_all(winner)
                    pygame.display.update()
                    if True == Add_Delay:
                        time.sleep(9)
                    break
                else:
                    get_done[turn_id] = -1
                    continue

            # For AI player 1~3, check hu before
            if False == p0_is_AI and 0 == turn_id:
                # button_enable[4] to check hu, 0: NOT hu, 1:hu
                if True == hear_status[turn_id] and 0 == button_enable[4]:
                    drop_mj[turn_id].append(getmj)
                    handle_drop_done = 0
                    get_done[turn_id] = 2 
            elif True == hear_status[turn_id]:
                drop_mj[turn_id].append(getmj)
                handle_drop_done = 0
                get_done[turn_id] = 2
            else:
                get_done[turn_id] = mjAI(turn_id, getmj)
                if 2 == get_done[turn_id]:
                    handle_drop_done = 0
                    if 1 == hear(player_mj[turn_id], player_mj_num[turn_id]):
                        hear_status[turn_id] = True
                elif -1 == get_done[turn_id]:
                    continue

            if False == p0_is_AI and 0 == turn_id and False == hear_status[turn_id]:
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
                if 1 == get_done[0]:
                    (mouseX, mouseY) = pygame.mouse.get_pos()
                    (x, y) = p0_get_loc_org
                    if x < mouseX < x + t1.get_width() and y < mouseY < y + t1.get_height():
                        p0_get_loc[1] = p0_get_loc_org[1] - 10
                        #get mj index is 16(p_num)
                        select = p_num
                
                if None == select:
                    p0_mjloc = copy.deepcopy(p0_mjloc_org)
                    p0_get_loc = list(p0_get_loc_org)

            for event in pygame.event.get():
                if event.type == QUIT:
                    exit()
                elif False == p0_is_AI and 0 == turn_id:
                    if event.type == MOUSEBUTTONDOWN:
                        (mouseX, mouseY) = pygame.mouse.get_pos()
                        if select != None and get_done[turn_id] != 2:
                            ebutton = False
                            if p_num == select:
                                drop_mj[turn_id].append(getmj)
                                ebutton = check_p0_button(player_mj[turn_id], player_mj_num[turn_id])
                                get_done[turn_id] = 2
                            else: # select != None:
                                drop_mj[turn_id].append(player_mj[turn_id][select])
                                del player_mj[turn_id][select]
                                player_mj[turn_id], player_mj_num[turn_id] = insert_mj(getmj, player_mj[turn_id])
                                ebutton = check_p0_button(player_mj[turn_id], player_mj_num[turn_id])
                                get_done[turn_id] = 2
                            if False == ebutton:
                                handle_drop_done = 0
                                break
                        elif 2 == get_done[turn_id]:
                            if False == button_enable_chk():
                                handle_drop_done = 0
                                break
                            
                            bselect = None
                            bselect = click_p0_button(mouseX, mouseY)
                            if 4 == bselect: # if hu
                                reset_p0_button()
                                winner = turn_id
                                display_all(winner)
                                pygame.display.update()
                                if True == Add_Delay:
                                    time.sleep(9)
                                break
                            elif 5 == bselect: #return
                                reset_p0_button()
                                handle_drop_done = 0
                                break
                            elif 2 == bselect: #hear
                                reset_p0_button()
                                handle_drop_done = 0
                                break

            display_all()
            pygame.display.update()
            
            # Handle drop mj
            while 0 == handle_drop_done or 1 == handle_drop_done or 4 == handle_drop_done:
                did = (turn_id + 1)%4
                while True:
                    if did == turn_id:
                        handle_drop_done = 0
                        break
                    else:
                        if False == p0_is_AI and 0 == did:
                                if 1 == check_button:
                                    check_p0_button(player_mj[did], player_mj_num[did], None, drop_mj[turn_id][-1])
                                    check_button = 2
                        # Check hu
                        elif 1 == hu(player_mj[did], drop_mj[turn_id][-1]):
                            winner = did
                            display_all(winner, turn_id)
                            pygame.display.update()
                            handle_drop_done = 3
                            if True == Add_Delay:
                                time.sleep(9)
                            break
                    if False == p0_is_AI and 0 == did:
                        if True == button_enable_chk():
                            select = slect_mj(p0_mjloc_org)
                            display_all()
                            pygame.display.update()
                            
                            for event in pygame.event.get():
                                if event.type == QUIT:
                                    exit()
                                elif event.type == MOUSEBUTTONDOWN:
                                    bselect = None
                                    bselect = click_p0_button(mouseX, mouseY)
                                    if select != None:
                                        if 2 == button_enable[0]: #pon
                                            pi = pon(player_mj[did], player_mj_num[did], drop_mj[turn_id][-1])
                                            if pi != -1:
                                                # 3: pon
                                                dmj[did].append([3, [drop_mj[turn_id][-1]]])
                                                drop_mj[turn_id] = drop_mj[turn_id][:-1]
                                                player_mj[did] = player_mj[did][:pi] + player_mj[did][pi+2:]
                                                player_mj_num[did] = len(player_mj[did])
                                                display_all()            
                                                screen.blit(write(u"碰", (0, 0, 255)), htext_loc[did])
                                                pygame.display.update()
                                                if True == Add_Delay:
                                                    time.sleep(1)
                                                
                                                reset_p0_button()
                                                handle_drop_done = 4
                                        if 2 == button_enable[1]: #gon
                                            gi = pon(player_mj[did], player_mj_num[did], drop_mj[turn_id][-1])
                                            if gi != -1:
                                                # 1: show gon
                                                dmj[did].append([1, [drop_mj[turn_id][-1]]])
                                                drop_mj[turn_id] = drop_mj[turn_id][:-1]
                                                player_mj[did] = player_mj[did][:gi] + player_mj[did][gi+3:]
                                                player_mj_num[did] = len(player_mj[did])
                                                display_all()            
                                                screen.blit(write(u"槓", (0, 0, 255)), htext_loc[did])
                                                pygame.display.update()
                                                if True == Add_Delay:
                                                    time.sleep(1)
                                                
                                                reset_p0_button()
                                                handle_drop_done = 4
                                        display_all()
                                        pygame.display.update()
                        elif 4 == handle_drop_done: #begin if True == button_enable_chk():
                            select = slect_mj(p0_mjloc_org)
                            display_all()
                            pygame.display.update()
                            
                            for event in pygame.event.get():
                                if event.type == QUIT:
                                    exit()
                                elif event.type == MOUSEBUTTONDOWN:
                                    if select != None:
                                        drop_mj[turn_id].append(player_mj[turn_id][select])
                                        del player_mj[turn_id][select]
                                        display_all()
                                        pygame.display.update()
                                        
                                        handle_drop_done = 1
                                        get_done[turn_id] = 0
                                        turn_id = did
                                        break
                        else:
                            did = (did + 1)%4
                    else: #begin if False == p0_is_AI and 0 == did:
                        gi = gon(player_mj[did], player_mj_num[did], drop_mj[turn_id][-1])
                        if  gi!= -1:
                            # 1: show gon
                            dmj[did].append([1, [drop_mj[turn_id][-1]]])
                            drop_mj[turn_id] = drop_mj[turn_id][:-1]
                            player_mj[did] = player_mj[did][:gi] + player_mj[did][gi+3:]
                            player_mj_num[did] = len(player_mj[did])
                            display_all()            
                            screen.blit(write(u"槓", (0, 0, 255)), htext_loc[did])
                            pygame.display.update()
                            if True == Add_Delay:
                                time.sleep(1)
                            handle_drop_done = 2
                            
                            get_done[turn_id] = 0
                            turn_id = did
                            break
                            
                        pi = pon(player_mj[did], player_mj_num[did], drop_mj[turn_id][-1])
                        if pi != -1:
                            # 3: pon
                            dmj[did].append([3, [drop_mj[turn_id][-1]]])
                            drop_mj[turn_id] = drop_mj[turn_id][:-1]
                            player_mj[did] = player_mj[did][:pi] + player_mj[did][pi+2:]
                            player_mj_num[did] = len(player_mj[did])
                            display_all()            
                            screen.blit(write(u"碰", (0, 0, 255)), htext_loc[did])
                            pygame.display.update()
                            if True == Add_Delay:
                                time.sleep(1)
                            handle_drop_done = 1
                            
                            get_done[turn_id] = 0
                            turn_id = did
                            mjAI(turn_id)
                            break
                    
                        did = (did + 1)%4            
                                
                if 1 == handle_drop_done:
                    continue
                elif 0 == handle_drop_done:
                    did = (turn_id + 1)%4
                    if False == p0_is_AI and 0 == did:
                        if True == button_enable_chk():
                            smj = None
                            while True:
                                # proc for slect
                                select = None
                                for c in range(player_mj_num[did]):
                                    (mouseX, mouseY) = pygame.mouse.get_pos()
                                    ii = p_num - player_mj_num[did] + c
                                    (x, y) = p0_mjloc_org[ii]
                                    if x < mouseX < x + p0_mj_width and y < mouseY < y + t1.get_height():
                                        p0_mjloc = copy.deepcopy(p0_mjloc_org)
                                        p0_mjloc[ii][1] = p0_mjloc_org[ii][1] - 10
                                        
                                        if smj != None:
                                            jj = p_num - player_mj_num[did] + smj
                                            p0_mjloc[jj][1] = p0_mjloc_org[jj][1] - 10
                                        
                                        select = c
                                        break
                                
                                if None == select:
                                    p0_mjloc = copy.deepcopy(p0_mjloc_org)
                                    if smj != None:
                                        jj = p_num - player_mj_num[did] + smj
                                        p0_mjloc[jj][1] = p0_mjloc_org[jj][1] - 10
                                # end proc for select
                                
                                display_all()
                                pygame.display.update()
                                
                                if 0 == handle_drop_done:
                                    for event in pygame.event.get():
                                        if event.type == QUIT:
                                            exit()
                                        elif event.type == MOUSEBUTTONDOWN:
                                            bselect = None
                                            bselect = click_p0_button(mouseX, mouseY)
                                            if select != None:
                                                if 2 == button_enable[3]: #eat
                                                    if None == smj:
                                                        smj = select
                                                    elif select != smj:
                                                        sort_value = []
                                                        sort_index = []
                                                        if select < smj:
                                                            sort_index = [select, smj]
                                                            sort_value = [player_mj[did][select], player_mj[did][smj]]
                                                        else:
                                                            sort_index = [smj, select]
                                                            sort_value = [player_mj[did][smj], player_mj[did][select]]
                                                        if player_mj[did][select] < 27 and sort_value[0]//9 == sort_value[1]//9 == drop_mj[turn_id][-1]//9 and (sort_value[0] + 2 == sort_value[1] + 1 == drop_mj[turn_id][-1] or sort_value[0] + 2 == drop_mj[turn_id][-1] + 1 == sort_value[1] or  drop_mj[turn_id][-1] + 2 == sort_value[0] + 1 == sort_value[1]):
                                                            etempv = [sort_value[0], sort_value[1]]
                                                            etempv.append(drop_mj[turn_id][-1])
                                                            # 0: eat
                                                            dmj[did].append(0, etempv)
                                                            drop_mj[turn_id] = drop_mj[turn_id][:-1]
                                                            del player_mj[did][sort_index[1]]
                                                            del player_mj[did][sort_index[0]]
                                                            
                                                            player_mj_num[did] = len(player_mj[did])
                                                            display_all()            
                                                            screen.blit(write(u"吃", (0, 0, 255)), htext_loc[did])
                                                            pygame.display.update()
                                                            if True == Add_Delay:
                                                                time.sleep(1)
                                                            
                                                            reset_p0_button()
                                                            handle_drop_done = 4
                                                            smj = None
                                                            break
                                                    else:
                                                        smj = None
                                elif 4 == handle_drop_done:
                                    for event in pygame.event.get():
                                        if event.type == QUIT:
                                            exit()
                                        elif event.type == MOUSEBUTTONDOWN:
                                            if select != None:
                                                drop_mj[did].append(player_mj[did][select])
                                                del player_mj[did][select]
                                                display_all()
                                                pygame.display.update()
                                                
                                                handle_drop_done = 5
                                                get_done[turn_id] = 0
                                                turn_id = did
                                                break
                                    
                            if 5 == handle_drop_done:
                                handle_drop_done = 0
                                continue
                    else: 
                        etemp = eat(player_mj[did], player_mj_num[did], drop_mj[turn_id][-1])
                        if etemp != []:
                            etempv = []
                            for i in range(2):
                                etempv.append(player_mj[did][etemp[i]])
                            etempv.append(drop_mj[turn_id][-1])
                            # 0: eat
                            dmj[did].append([0, etempv])
                            drop_mj[turn_id] = drop_mj[turn_id][:-1]

                            # player_mj[did] = player_mj[did][:etemp[0]] + player_mj[did][etemp[0]+1:etemp[1]] + player_mj[did][etemp[1]+1:]
                            # delete in reverse older
                            del player_mj[did][etemp[1]]
                            del player_mj[did][etemp[0]]
                            
                            player_mj_num[did] = len(player_mj[did])
                            display_all()            
                            screen.blit(write(u"吃", (0, 0, 255)), htext_loc[did])
                            pygame.display.update()
                            if True == Add_Delay:
                                time.sleep(1)
                            
                            get_done[turn_id] = 0
                            turn_id = did
                            mjAI(turn_id)
                            continue
                if 2 == handle_drop_done:
                    get_done[turn_id] = -1
                elif 0 == handle_drop_done: 
                    get_done[turn_id] = 0
                    check_button = 0
                    reset_p0_button()
                    turn_id = (turn_id + 1)%4
                break
            # End handle drop mj
            if winner != -1:
                break
        
        if host_id != winner:
            host_id = (host_id + 1)%4
            
        first = 1
        mjp = 0
        mjb = 143
        print("End Game")
    exit()
		
if __name__ == "__main__":
    try:
        main()
    except Exception as e:
        print(e)
        input("Press Enter key to continue")
    