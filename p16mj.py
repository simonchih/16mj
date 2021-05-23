import random, os
import time
import pygame
import math
import copy
import hu_result
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

l0_image_filename = 'Image/l0.gif'
l1_image_filename = 'Image/l1.gif'
l2_image_filename = 'Image/l2.gif'
l3_image_filename = 'Image/l3.gif'
lred0_image_filename = 'Image/lred0.gif'
lred1_image_filename = 'Image/lred1.gif'
lred2_image_filename = 'Image/lred2.gif'
lred3_image_filename = 'Image/lred3.gif'

liu_image_filename = 'Image/liu.gif'
g_image_filename = 'Image/g.gif'

host_image_filename = 'Image/host.gif'

mjback_image_filename = 'Image/mjback.gif'
mjb_image_filename = 'Image/mjb.gif'

hu_image_filename = 'Image/hu.gif'
button_image_filename = 'Image/50x50_mjb.gif'
com_hear_image_filename = 'Image/50x50_hear.gif'
finger_filename = 'Image/finger_50x61.gif'

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

l0 = pygame.image.load(l0_image_filename).convert()
l1 = pygame.image.load(l1_image_filename).convert()
l2 = pygame.image.load(l2_image_filename).convert()
l3 = pygame.image.load(l3_image_filename).convert()
lred0 = pygame.image.load(lred0_image_filename).convert()
lred1 = pygame.image.load(lred1_image_filename).convert()
lred2 = pygame.image.load(lred2_image_filename).convert()
lred3 = pygame.image.load(lred3_image_filename).convert()

liu = pygame.image.load(liu_image_filename).convert()
g = pygame.image.load(g_image_filename).convert()

host_img = pygame.image.load(host_image_filename).convert()

mjback = pygame.image.load(mjback_image_filename).convert()
mjbk   = pygame.image.load(mjb_image_filename).convert()

finger = pygame.image.load(finger_filename).convert()

mjback2 = pygame.transform.rotate(mjback , 90)
mjback3 = pygame.transform.rotate(mjback , 180)
mjback4 = pygame.transform.rotate(mjback , 270)

hu_button = pygame.image.load(hu_image_filename).convert()
button = pygame.image.load(button_image_filename).convert()
com_hear = pygame.image.load(com_hear_image_filename).convert()

p_num = 16
mjp = 0
mjb = 143
turn_id = 0
host_id = 0
winner = -1
host_num = 0
circle = 0
handle_drop_done = -1
# display tai. 0: ini and normal display. 1: calculate tai. 2: ready to set calc_tai 0
calc_tai = 0
# location of mj number font remains
renum_loc = (470, 10)
# open door loc
wind_loc = (250, 10)
# 0~3: player 0~3
mjloc = [(300, 815), (1100, 120), (250, 90), (50, 120)]
huloc = [(575, 630), (910, 425), (575, 270), (240, 425)]
# only for first_hear
hear_loc = [(1100, 800), (1150, 70), (180, 40), (10, 800)]
p0_is_AI = False
Add_Delay = True
end_game_loc = (450, 380)
p0_get_loc_org = (880, 815)
p0_get_loc = []
eat_index = []
#dict: calculate tai result
result = {}
getmj = None
gethu = False
east_to_north = []
player_door = [0] * 4
#player 0 mj location
p0_mjloc = []
# 2: won't show get mj, 1:get done, 0:get from mjp, -1: get from mjb
get_done = [0] * 4
# 0: NOT hear, 1: Sky hear, 2: Ground hear
first_hear = [0] * 4
hear_status = [False] * 4
# 0:ini, 1:after first drop, 2: after first hear or after 2 turn drop, 3~
first_turn = [0] * 4
#button loc
button_loc = [(1000, 800), (1050, 800), (1100, 800), (1000, 850), (1050, 850), (1100, 850)]
#0: Disable, 1: Enable, 2: Clicked (for eat and dark kong only)
# button_enable[0]: pon, button_enable[1]: kong, button_enable[2]: hear
# button_enable[3]: eat, button_enable[4]: hu, button_enable[5]: back
button_enable = [0] * 6
drop_mj_loc = [[(460, 645)]*64, [(930, 320)]*64, [(460, 260)]*64, [(220, 320)]*64]
drop_mj = [[], [], [], []]
lloc = [(410, 710), (1155, 400), (750, 205), (5, 400)]
hostloc = [(360, 710), (1155, 450), (800, 205), (5, 450)]
hmj_loc = [[(460, 700)], [(985, 320)], [(460, 205)], [(165, 320)]]
htext_loc = [(750, 700), (950, 270), (380, 205), (165, 270)]
hmj = [[], [], [], []]
# add kong mj index of dmj
add_kong_mj = None
bool_pre_kong = False
bool_last_one = False
enter_finger_code_twice = False
add_kong_loc = [[], [], [], []]
dmj_loc = [[(280, 755)], [(1040, 150)], [(280, 150)], [(110, 150)]]
# [type, [value]] in dmj. type 0: eat, 1: show kong, 2: dark kong, 3: pon
# if type == 2 (dark kong), Only one value property, e.g. [type, [v]]
dmj = [[], [], [], []]
p0_mj_width = t1.get_width()-10
player_mj_num = [p_num, p_num, p_num, p_num]
player_mj = [[0]*p_num, [0]*p_num, [0]*p_num, [0]*p_num]
all_mj = [0]*144

# time in seconds between each step
step = 1

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
    elif 44 == index:
        #location 0
        return l0
    elif 45 == index:
        return l1
    elif 46 == index:
        return l2
    elif 47 == index:
        return l3
    elif 48 == index:
        # location red 0
        return lred0
    elif 49 == index:
        return lred1
    elif 50 == index:
        return lred2
    elif 51 == index:
        return lred3
    elif 52 == index:
        return host_img
    elif 53 == index:
        return com_hear
    elif 54 == index:
        return finger

def wind_index_to_text(opi):
    # east to north
    if 0 == opi:
        return "東"
    elif 1 == opi:
        return "南"
    elif 2 == opi:
        return "西"
    elif 3 == opi:
        return "北"

def pid_to_image(pid, index):
    pic = index_to_pic(index)

    if 0 == pid:
        return pic
    elif 1 == pid:
        return pygame.transform.rotate(pic , 90)
    elif 2 == pid:
        return pygame.transform.rotate(pic , 180)
    elif 3 == pid:
        return pygame.transform.rotate(pic , 270)

def delay(second):
    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
    time.sleep(second)

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

def select_mj(p0_mjloc_org, tid = 0, smj = None):
    global p0_mjloc

    select = None
    for c in range(player_mj_num[tid]):
        (mouseX, mouseY) = pygame.mouse.get_pos()
        ii = p_num - player_mj_num[tid] + c
        (x, y) = p0_mjloc_org[ii]
        if x < mouseX < x + p0_mj_width and y < mouseY < y + t1.get_height():
            p0_mjloc = copy.deepcopy(p0_mjloc_org)
            p0_mjloc[ii][1] = p0_mjloc_org[ii][1] - 10

            if smj != None:
                jj = p_num - player_mj_num[tid] + smj
                p0_mjloc[jj][1] = p0_mjloc_org[jj][1] - 10

            select = c
            break

    if None == select:
        p0_mjloc = copy.deepcopy(p0_mjloc_org)
        if smj != None:
            jj = p_num - player_mj_num[tid] + smj
            p0_mjloc[jj][1] = p0_mjloc_org[jj][1] - 10

    return select

# reset button except hear button
def reset_p0_button():
    global button_enable

    hear_enable = button_enable[2]
    button_enable = [0] * len(button_loc)
    if 2 == hear_enable:
        button_enable[2] = hear_enable

def button_enable_chk():
    for i in range(len(button_loc)):
        if 2 == i and 1 == button_enable[i]:
            return True
        elif i != 2 and button_enable[i] > 0:
            return True
    return False

def check_p0_button(mj, mj_num, myvalue = None, dj = None, value = None, chk_eat = False, chk_huonly = False):
    global button_enable
    global add_kong_mj

    reset_p0_button()

    enable = False

    if False == hear_status[0]:
        if True == chk_huonly:
            if myvalue != None and 1 == hu_result.hu(mj, myvalue):
                button_enable[4] = 1
                enable = True
            elif value != None and 1 == hu_result.hu(mj, value):
                button_enable[4] = 1
                button_enable[5] = 1
                enable = True
        # It's NOT possible for myvalue != None and value != None
        elif None == value and None == myvalue:
            if 0 == button_enable[2] and 1 == hear(mj, mj_num):
                button_enable[2] = 1
                button_enable[5] = 1
                enable = True
        elif None == value: # myvalue != None
            temp_mj, temp_mj_num = hu_result.insert_mj(myvalue, mj)
            if dark_kong(temp_mj, temp_mj_num) != -1:
                button_enable[1] = 1
                enable = True

            if player_add_kong(dj, mj, myvalue) != None:
                button_enable[1] = 1
                enable = True

            if 1 == hu_result.hu(mj, myvalue):
                button_enable[4] = 1
                enable = True
        else: # value != None
            if False == chk_eat:
                if pon(mj, mj_num, value) != -1:
                    button_enable[0] = 1
                    button_enable[5] = 1
                    enable = True
                if kong(mj, mj_num, value) != -1:
                    button_enable[1] = 1
                    button_enable[5] = 1
                    enable = True
            elif eat(mj, mj_num, value) != []: #chk_eat == True
                button_enable[3] = 1
                button_enable[5] = 1
                enable = True

            if 1 == hu_result.hu(mj, value):
                button_enable[4] = 1
                button_enable[5] = 1
    elif myvalue != None and 1 == hu_result.hu(mj, myvalue):
        button_enable[4] = 1
        button_enable[5] = 1
        enable = True
    elif value != None and 1 == hu_result.hu(mj, value):
        button_enable[4] = 1
        button_enable[5] = 1
        enable = True

    return enable

# -1: Can't add kong, 0~4: index of dmj
def add_kong(dj, value):
    for i, orgv in enumerate(dj):
        tp = orgv[0]
        if 3 == tp:
            v = orgv[1][0]
            if v == value:
                return i
    return -1

# return index of dmj, index of tmj, tmj, tmj_num
# return None if player can't add kong
def player_add_kong(dj, mj, gmj):
    if gmj != None:
        tmj, tmj_num = hu_result.insert_mj(gmj, mj)

    for i in range(tmj_num):
        aki = add_kong(dj, tmj[i])
        if aki != -1:
            return aki, i, tmj, tmj_num

    return None

def p0_add_kong(dj, mj, gmj, dindex):
    if None == dindex:
        return None
    elif gmj != None:
        tmj, tmj_num = hu_result.insert_mj(gmj, mj)

    for i in range(tmj_num):
        if 3 == dj[dindex][0] and tmj[i] == dj[dindex][1][0]:
            return i, tmj, tmj_num

    return None

def hear_dark_kong(mj, mj_num, gmj, tloc):
    # gdone in this function is only 2 for dark_kong_value = None
    # or -1 for dark_kong_value != None
    gdone = 2
    dark_kong_value = None

    tmj, tmj_num = hu_result.insert_mj(gmj, mj)

    di = dark_kong(tmj, tmj_num)
    if di != -1:
        temp_mj = list(filter(lambda a: a != tmj[di], tmj))
        temp_mj_num = len(temp_mj)
        dark_kong_value = tmj[di]
        if 1 == hear(temp_mj, temp_mj_num):
            gdone = -1
            screen.blit(write(u"暗槓", (0, 0, 255)), tloc)
            pygame.display.update()
            if True == Add_Delay:
                delay(1*step)      
            return temp_mj, temp_mj_num, gdone, dark_kong_value

    return mj, mj_num, gdone, dark_kong_value

# -1: Can't kong, 0~mj_num - 4: start of mj index
def dark_kong(mj, mj_num):
    for i in range(mj_num - 3):
        if mj[i] == mj[i+1] == mj[i+2] == mj[i+3]:
            return i
    return -1

# -1: Can't kong, 0~mj_num - 3: start of mj index
def kong(mj, mj_num, value):
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
                    elif mj[i] < 27 and mj[i]//9 == mj[n1]//9 and mj[i]+2 == mj[n1]:
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
                    elif 0 == two_s and mj[i] == mj[n1]:
                        two_s = 1
                        block[i] = block[n1] = 1
                    else:
                        m1, m2 = next_two_not_blsame(block, mj_num, i+1, mj, mj[i])
                        if m1 != -1 and m2 != -1:
                            if mj[i] < 27 and mj[i]//9 == mj[m1]//9 == mj[m2]//9 and mj[i]+1 == mj[m1] and mj[m1]+1 == mj[m2]:
                                block[i] = block[m1] = block[m2] = 1
                                i += 1
                                continue
                            elif 1 == two_s:
                                mj_hear = 0
                                break
                            elif mj[i] < 27 and mj[i]//9 == mj[m1]//9 and mj[i]+1 == mj[m1]:
                                two_s = 1
                                block[i] = block[m1] = 1
                                i += 1
                                continue
                            elif mj[i] < 27 and mj[i]//9 == mj[m1]//9 and mj[i]+2 == mj[m1]:
                                two_s = 1
                                block[i] = block[m1] = 1
                                i += 1
                                continue
                            else:
                                mj_hear = 0
                                break
                        elif m1 != -1:
                            if 1 == two_s:
                                mj_hear = 0
                                break
                            elif mj[i] == mj[m1] or (mj[i] < 27 and mj[i]//9 == mj[m1]//9 and mj[i]+1 == mj[m1]):
                                two_s = 1
                                block[i] = block[m1] = 1
                                i += 1
                                continue
                            elif mj[i] == mj[m1] or (mj[i] < 27 and mj[i]//9 == mj[m1]//9 and mj[i]+2 == mj[m1]):
                                two_s = 1
                                block[i] = block[m1] = 1
                                i += 1
                                continue
                            else:
                                mj_hear = 0
                                break
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

                    if m1 != -1 and m2 != -1:
                        if mj[i] < 27 and mj[i]//9 == mj[m1]//9 == mj[m2]//9 and mj[i]+1 == mj[m1] and mj[m1]+1 == mj[m2]:
                            block[i] = block[m1] = block[m2] = 1
                            i += 1
                            continue
                        else:
                            mj_hear = 0
                            break
                    else:
                        mj_hear = 0
                        break

        if 1 == mj_hear:
            return 1

        block = [0] * mj_num
        c += 1

    return 0

# Output: None, 0~3
def drop1_hmj7(turn_id):
    global mjp
    global mjb
    global getmj

    if 1 == len(hmj[turn_id]):
        dhid = (turn_id + 1) % 4
        while True:
            if turn_id == dhid:
                break
            elif 7 == len(hmj[dhid]):
                if (mjb - mjp) >= 16:
                        # this getmj for turn_id, NOT winner id (dhid)
                        getmj = all_mj[mjb]
                        mjb -= 1
                return handle_hu(dhid, turn_id, False, None, True)
            else:
                dhid = (dhid + 1) % 4

    return None

# Output: None, 0~3
def hmj7_get1(turn_id):
    if 7 == len(hmj[turn_id]):
        dhid = (turn_id + 1) % 4
        while True:
            if turn_id == dhid:
                break
            elif 1 == len(hmj[dhid]):
                return handle_hu(turn_id, dhid, False, None, True)
            else:
                dhid = (dhid + 1) % 4

    return None

# hid: winner id
def handle_hu(hid, drop_id = -1, get_hu = True, akong = None, hhu = False):
    global player_mj
    global player_mj_num
    global host_num
    global first_turn
    global gethu
    global winner
    global result
    global calc_tai

    gethu = get_hu
    winner = hid

    # debug only
    if hid < 0 or hid > 3:
        print("Crash!!!, hid=%d"%hid)
    # end debug only

    display_all(hid, drop_id, akong)
    pygame.display.update()
    if True == Add_Delay:
        delay(4*step)

    if hid == host_id:
        host_num += 1
    else:
        host_num = 0

    if -1 == drop_id:
        result = hu_result.hu_result(player_mj[hid], dmj[hid], host_num, first_turn[hid], hmj[hid], circle, player_door[hid], bool_last_one, getmj, first_hear[hid], None, hhu, False, bool_pre_kong)
    else:
        if akong != None:
            dp = dmj[drop_id][akong][1][0]
            bool_akong = True
        else:
            dp = drop_mj[drop_id][-1]
            bool_akong = False

        result = hu_result.hu_result(player_mj[hid], dmj[hid], host_num, first_turn[hid], hmj[hid], circle, player_door[hid], bool_last_one, None, first_hear[hid], dp, hhu, bool_akong, False)

    calc_tai = 1
    display_all(hid, drop_id, akong)
    pygame.display.update()
    return hid

# p0 is NOT get hu
def handle_p0_hu_only(hid, drop_id):
    global handle_drop_done
    global button_enable

    br = False
    win = -1
    while 1 == button_enable[4]:
        bselect = click_p0_button()
        if 5 == bselect:
            break
        elif 4 == bselect:
            win = handle_hu(hid, drop_id, False)
            handle_drop_done = 3
            br = True
            break

    return br, win

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
        display_all(winner)
        screen.blit(write(u"補花", (0, 0, 255)), htext_loc[pid])
        pygame.display.update()
        if True == Add_Delay:
            delay(1*step)

    return tget_num

def draw_hu(win_id):
    if win_id >= 0:
        screen.blit(pid_to_image(win_id, 43), huloc[win_id])

def draw_p0_mj(pmj, pmjloc, mjnum):
    for c in range(mjnum):
        i = p_num - mjnum + c
        (x, y) = pmjloc[i]
        screen.blit(pid_to_image(0, pmj[c]), (x, y))

    if 1 == get_done[turn_id] and 0 == turn_id and getmj != None:
        # draw get mj
        screen.blit(pid_to_image(0, getmj), p0_get_loc)

def draw_mj_column(mj_pic, xy, mj_num, draw_all = -1):
    (startx, starty) = xy
    gap = 5

    if -1 == draw_all:
        for y in range(starty, starty + mj_num*mj_pic.get_height(), mj_pic.get_height()):
            screen.blit(mj_pic, (startx, y))
    elif 1 == draw_all:
        c = mj_num - 1
        for y in range(starty + (mj_num-1)*p0_mj_width, starty - 1, (-1)*p0_mj_width):
            screen.blit(pid_to_image(draw_all, player_mj[draw_all][c]), (startx, y))
            c -= 1

        if True == gethu:
            screen.blit(pid_to_image(draw_all, getmj), (startx, starty - gap - t1.get_width()))

    elif 3 == draw_all: # reverse older
        c = 0
        for y in range(starty, starty + mj_num*p0_mj_width, p0_mj_width):
            screen.blit(pid_to_image(draw_all, player_mj[draw_all][c]), (startx, y))
            c += 1

        if True == gethu:
            screen.blit(pid_to_image(draw_all, getmj), (startx, starty + gap + t1.get_width() + (mj_num-1)*p0_mj_width))

def draw_mj_row(mj_pic, xy, mj_num, draw_all = -1):
    (startx, starty) = xy
    if -1 == draw_all:
        for x in range(startx, startx + mj_num*mj_pic.get_width(), mj_pic.get_width()):
            screen.blit(mj_pic, (x, starty))
    else: # reverse older
        gap = 5
        c = mj_num - 1
        for x in range(startx + (mj_num-1)*p0_mj_width, startx - 1, (-1)*p0_mj_width):
            screen.blit(pid_to_image(draw_all, player_mj[draw_all][c]), (x, starty))
            c -= 1

        if True == gethu:
            screen.blit(pid_to_image(draw_all, getmj), (startx - gap - t1.get_width(), starty))

def fill_background():
    for y in range(0, screen_height, background.get_height()):
        for x in range(0, screen_width, background.get_width()):
            screen.blit(background, (x, y))

def draw_end_game(loc):
    (x, y) = loc
    gx = x + liu.get_width()
    screen.blit(liu, loc)
    screen.blit(g, (gx, y))

def display_dark_kong(pid, loc):
    (x, y) = loc
    if 0 == pid or 2 == pid:
        for i in range(3):
            screen.blit(pid_to_image(pid, 42), (x + i*p0_mj_width, y))

        screen.blit(pid_to_image(pid, 42), (x + p0_mj_width, y))
    elif 1 == pid:
        for i in range(2, -1, -1):
            screen.blit(pid_to_image(pid, 42), (x, y + i*p0_mj_width))
    elif 3 == pid:
        for i in range(3):
            screen.blit(pid_to_image(pid, 42), (x, y + i*p0_mj_width))

        screen.blit(pid_to_image(pid, 42), (x, y + p0_mj_width))

def display_show_kong(pid, value, loc):
    (x, y) = loc
    if 0 == pid or 2 == pid:
        for i in range(3):
            screen.blit(pid_to_image(pid, value), (x + i*p0_mj_width, y))

        screen.blit(pid_to_image(pid, value), (x + p0_mj_width, y))
    elif 1 == pid:
        for i in range(2, -1, -1):
            screen.blit(pid_to_image(pid, value), (x, y + i*p0_mj_width))
    elif 3 == pid:
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
        screen.blit(pid_to_image(1, fmj[1]), (x, y + 2*p0_mj_width))
        screen.blit(pid_to_image(1, middle), (x, y + p0_mj_width))
        screen.blit(pid_to_image(1, fmj[0]), (x, y))
    elif 2 == pid:
        screen.blit(pid_to_image(2, fmj[1]), (x + 2*p0_mj_width, y))
        screen.blit(pid_to_image(2, middle), (x + p0_mj_width, y))
        screen.blit(pid_to_image(2, fmj[0]), (x, y))
    elif 3 == pid:
        screen.blit(pid_to_image(3, fmj[0]), (x, y))
        screen.blit(pid_to_image(3, middle), (x, y + p0_mj_width))
        screen.blit(pid_to_image(3, fmj[1]), (x, y + 2*p0_mj_width))

def display_pon(pid, value, loc):
    (x, y) = loc
    if 0 == pid:
        for i in range(3):
            screen.blit(pid_to_image(pid, value), (x + i*p0_mj_width, y))
    elif 2 == pid:
         for i in range(2, -1, -1):
            screen.blit(pid_to_image(pid, value), (x + i*p0_mj_width, y))
    elif 1 == pid:
        for i in range(2, -1, -1):
            screen.blit(pid_to_image(pid, value), (x, y + i*p0_mj_width))
    elif 3 == pid:
        for i in range(3):
            screen.blit(pid_to_image(pid, value), (x, y + i*p0_mj_width))

def draw_dmj(win_id):

    for pid in range(4):
        for i in range(len(dmj[pid])):
            if 0 == dmj[pid][i][0]:
                display_front_eat(pid, dmj[pid][i][1], dmj[pid][i][1][2], dmj_loc[pid][i])
            elif 1 == dmj[pid][i][0]:
                display_show_kong(pid, dmj[pid][i][1][0], dmj_loc[pid][i])
            elif 2 == dmj[pid][i][0]:
                display_dark_kong(pid, dmj_loc[pid][i])
            elif 3 == dmj[pid][i][0]:
                display_pon(pid, dmj[pid][i][1][0], dmj_loc[pid][i])

            if 0 == pid and -1 == win_id and add_kong_mj != None:
                (mouseX, mouseY) = pygame.mouse.get_pos()
                (x, y) = dmj_loc[pid][i]
                if x < mouseX < x + 2*p0_mj_width + mjbk.get_width() and y < mouseY < y + mjbk.get_height():
                    pygame.draw.rect(screen, (0xff, 0, 0), (x, y, 2*p0_mj_width + mjbk.get_width() , mjbk.get_height()), 3)

def draw_hmj():
    for pid in range(4):
        if 0 == pid or 2 == pid:
            for i in range(len(hmj[pid])):
                screen.blit(pid_to_image(pid, hmj[pid][i]), hmj_loc[pid][i])
        elif 1 == pid or 3 == pid:
            for i in range(len(hmj[pid])-1, -1, -1):
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

def draw_host_location():
    global enter_finger_code_twice

    for i, l in enumerate(east_to_north):
        if l == host_id:
            screen.blit(pid_to_image(l, 52), hostloc[l])

        if l == turn_id:
            screen.blit(pid_to_image(l, 48+i), lloc[l])

            # add code below for display finger 20180327
            # avoid if NO drop_mj
            if 0 == len(drop_mj[l]):
                continue

            # avoid double enter
            if True == enter_finger_code_twice:
                continue
            else:
                enter_finger_code_twice = True

            PIC_finger_index = 54

            # if i is last one try to handle finger display
            i = len(drop_mj[l]) - 1
            (finger_x, finger_y) = drop_mj_loc[l][i]

            if 0 == l:
                fx = finger_x
                fy = finger_y + t1.get_height()
            elif 1 == l:
                fx = finger_x + t1.get_width()
                fy = finger_y
            elif 2 == l:
                fx = finger_x
                fy = finger_y - finger.get_height()
            elif 3 == l:
                fx = finger_x - finger.get_width()
                fy = finger_y
            else:
                print("Impossible!pid(l) is NOT 0~3!")

            screen.blit(pid_to_image(l, PIC_finger_index), (fx, fy))
            # end finger code 20180327

        else:
            screen.blit(pid_to_image(l, 44+i), lloc[l])

def draw_hear():
    for i, h in enumerate(first_hear):
        if 0 == i:
            continue
        elif h != 0:
            screen.blit(pid_to_image(i, 53), hear_loc[i])

def draw_text():
    screen.blit(write(u"%s風%s局"%(wind_index_to_text(circle), wind_index_to_text(player_door[host_id])), (255, 255, 255)), wind_loc)
    screen.blit(write(u"麻將剩餘:%d"%(mjb - mjp + 1), (255, 255, 255)), renum_loc)

def draw_ctai(r):
    (x, y)= (50, 290)
    (mx, my) = (300, 200) # for mj loc
    (dx, dy) = (300, 140) # for dj loc
    (hx, hy) = (300, 80) #for hj loc

    i = 0
    s = 0
    gap = 5

    for c in range(len(r.hj)):
        screen.blit(pid_to_image(0, r.hj[c]), (hx, hy))
        hx += p0_mj_width

    for tv in r.dj:
        t = tv[0]
        v = tv[1]
        if 0 == t:
            display_front_eat(0, v, v[2], (dx, dy))
        elif 1 == t or 2 == t:
            display_show_kong(0, v[0], (dx, dy))
        elif 3 == t:
            display_pon(0, v[0], (dx, dy))

        dx += 2*p0_mj_width + mjbk.get_width() + gap

    for c in range(len(r.mj)):
        screen.blit(pid_to_image(0, r.mj[c]), (mx, my))
        mx += p0_mj_width

    if r.gethu != None:
        # draw get mj
        screen.blit(pid_to_image(0, r.gethu), (mx+10, my))
    elif r.drophu != None:
        screen.blit(pid_to_image(0, r.drophu), (mx+10, my))

    for key, value in r.table.items():
        if value != 0:
            s += value
            screen.blit(write(u"%s: %2d台\n"%(key, value), (255, 255, 255)), (x, y))
            if 0 == i%3:
                x = 450
            elif 1 == i%3:
                x = 850
            else:
                y += 40
                x = 50
            i += 1

    screen.blit(write(u"總共: %3d台\n"%s, (255, 255, 255)), (850, y+40))

# here did is drop player id
def display_all(win_id, did = -1, akong = None, end_game = False):
    global calc_tai

    fill_background()

    if 0 == calc_tai:
        draw_p0_mj(player_mj[0], p0_mjloc, player_mj_num[0])
        draw_p123_mj(win_id)
        draw_dmj(win_id)
        draw_hmj()
        draw_drop_mj()
        draw_p0_button()
        # draw_drop_mj should first than draw host location
        draw_host_location()
        draw_hear()
        draw_hu(win_id)
        draw_text()

        if end_game:
            draw_end_game(end_game_loc)

        if did != -1:
            if akong != None:
                (x, y) = add_kong_loc[did][akong]
                p = pid_to_image(did, dmj[did][akong][1][0])
            else:
                # NOT (x, y) = drop_mj_loc[did][-1], since the number of drop_mj_loc is maximum
                (x, y) = drop_mj_loc[did][len(drop_mj[did])-1]

                p = pid_to_image(did, drop_mj[did][-1])
            pygame.draw.rect(screen, (0xff, 0, 0), (x, y, p.get_width(), p.get_height()), 3)
    elif 1 == calc_tai:
        # Test temp
        #result = hu_result.hu_result([1,1,2,3,4,4,4,4,5,6], [[0, [6,8,7]], [2, [0,0,0]]], 0, 1, [34, 35, 36], 0, 0, False, 1, 0, None, False, False, False)
        # End test temp

        (bx, by) = (575, 820)  #for button loc
        fill_background()
        pygame.draw.rect(screen, (0, 0, 0), (20, 20, 1160, 860), 3)
        draw_ctai(result)
        while 1 == calc_tai:
            # draw back button
            screen.blit(button, (bx, by))
            (mouseX, mouseY) = pygame.mouse.get_pos()
            if bx < mouseX < bx + button.get_width() and by < mouseY < by + button.get_height():
                screen.blit(write(index_to_btext(5), (0, 255, 0), 30), (bx+10, by+5))
            else:
                screen.blit(write(index_to_btext(5), (0, 0, 0), 30), (bx+10, by+5))

            pygame.display.update()

            if True == p0_is_AI:
                if True == Add_Delay:
                    delay(5*step)
                calc_tai = 2
                break

            for event in pygame.event.get():
                if event.type == QUIT:
                    exit()
                elif event.type == MOUSEBUTTONDOWN:
                    if bx < mouseX < bx + button.get_width() and by < mouseY < by + button.get_height():
                        calc_tai = 2
                        break

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

def p0_button_proc(mouseX, mouseY):
    global button_enable
    global hear_status

    l = len(button_loc)

    # hu is 0 or 1, can't be 2
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
                        reset_p0_button()
                        return i
                    else: # False == no2, return None
                        continue
                elif 0 == i or 1 == i or 2 == i or 3 == i :
                    button_enable[i] = 2
                    if 2 == i:
                        hear_status[0] = True
                        if 1 == first_turn[0]:
                        # Ground hear
                            first_turn[0] += 1
                            first_hear[0] = 2
                # 4 == i
                return i
    return None

def click_p0_button():
    bs = None
    (mouseX, mouseY) = pygame.mouse.get_pos()

    for event in pygame.event.get():
        if event.type == QUIT:
            exit()
        elif event.type == MOUSEBUTTONDOWN:
            bs = p0_button_proc(mouseX, mouseY)
            if bs != None:
                return bs

    display_all(winner)
    pygame.display.update()

    return bs

def handle_p0_sky_hear():
    global frist_turn
    global first_hear

    check_p0_button(player_mj[turn_id], player_mj_num[turn_id])

    while 1 == button_enable[2]:
        (mouseX, mouseY) = pygame.mouse.get_pos()

        for event in pygame.event.get():
            if event.type == QUIT:
                exit()
            elif event.type == MOUSEBUTTONDOWN:
                s = p0_button_proc(mouseX, mouseY)
                if 5 == s:
                    break
                elif 2 == s:
                    # Sky hear
                    first_turn[0] = 2
                    first_hear[0] = 1
                    break

        display_all(winner)
        pygame.display.update()


def write(msg="pygame is cool", color= (0,0,0), size = 36):
    #myfont = pygame.font.SysFont("None", 32) #To avoid py2exe error
    myfont = pygame.font.Font("wqy-zenhei.ttf",size)
    mytext = myfont.render(msg, True, color)
    mytext = mytext.convert_alpha()
    return mytext

# assume eati:[a, c] where a index < c index
# this function return 0 for smallest, 2 for biggest
def eat_middle_position(eati, value):
        if value + 2 == eati[0] + 1 == eati[1]:
            return 0
        elif eati[0] + 2 == value + 1 == eati[1]:
            return 1
        else: # eati[0] + 2 == eati[1] + 1 == value
            return 2

def AI_drop_for_eat(tid, eati):
    global player_mj
    global player_mj_num

    tmj = player_mj[tid][:]
    tmj_num = player_mj_num[tid]

    block = [0] * tmj_num

    block[eati[0]] = block[eati[1]] = 1

    block = add_block3(tmj, tmj_num, block)
    block0_num = block.count(0)

    if block0_num > 2:
        block = add_block2(tmj, tmj_num, block)

    di = next_not_block(block, len(block))
    if -1 == di:
        print("di == -1")
        input("wrong")

    return tmj[di]

def mjAI(tid, getv = None):
    global player_mj
    global player_mj_num
    global dmj
    global drop_mj
    global add_kong_mj
    global getmj

    if None == getv:
        tmj = player_mj[tid][:]
        tmj_num = player_mj_num[tid]
    elif 1 == proc_add_hmj(tid, True, getv):
        return -1
    else:
        #add_kong_mj = None
        if player_add_kong(dmj[tid], player_mj[tid], getv) != None:
            aki, vi, player_mj[tid], player_mj_num[tid] = player_add_kong(dmj[tid], player_mj[tid], getv)
            screen.blit(write(u"加槓", (0, 0, 255)), htext_loc[tid])
            dmj[tid][aki] = [1, [getv]]

            del player_mj[tid][vi]
            player_mj_num[tid] = len(player_mj[tid])

            pygame.display.update()
            if True == Add_Delay:
                delay(1*step)

            add_kong_mj = aki
            return -1

        tmj, tmj_num = hu_result.insert_mj(getv, player_mj[tid])

        if 0 == tid:
            getmj = None

    si = dark_kong(tmj, tmj_num)
    if si != -1 and getv != None:
        screen.blit(write(u"暗槓", (0, 0, 255)), htext_loc[tid])
        pygame.display.update()
        if True == Add_Delay:
            delay(1*step)
        player_mj[tid] = list(filter(lambda a: a != tmj[si], tmj))
        player_mj_num[tid] = len(player_mj[tid])
        dmj[tid].append([2, [tmj[si]]])
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

    display_all(winner)
    pygame.display.update()
    if True == Add_Delay:
        delay(1*step)

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
    global host_num
    global eat_index
    global add_kong_loc
    global add_kong_mj
    global handle_drop_done
    global first_turn
    global first_hear
    global winner
    global circle
    global bool_pre_kong
    global bool_last_one
    global calc_tai
    global enter_finger_code_twice
    global east_to_north

    first = 1
    p0_mjloc_ini = []
    host_id = random.randint(0, 3) #0 <= host_id <= 3
    east_to_north.append(host_id)

    # assign east_to_north
    ei = (host_id + 1) % 4
    while True:
        if ei == host_id:
            break
        else:
            east_to_north.append(ei)
            ei = (ei + 1) % 4
    # end assign east_to_north

    #temp 20180811
    #east_to_north = [0, 1, 2, 3]
    #end temp 20180811

    # assign player_door

    # w: 0~3 is east, south, west, north
    w = 0
    for p in east_to_north:
        player_door[p] = w
        w += 1
    # end assign player_door

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

    # assign dmj_loc, add_kong_loc
    for i, loc in enumerate(dmj_loc):
        (x, y) = loc[0]
        if 0 == i or 2 == i:
            add_kong_loc[i].append((x+p0_mj_width, y))
        else:
            add_kong_loc[i].append((x, y+p0_mj_width))

    gap = 5
    for pi in range(4):
        for i in range(1, 5):
            (x, y) = dmj_loc[pi][i-1]
            if 0 == pi or 2 == pi:
                dmj_loc[pi].append((x + 2*p0_mj_width + mjbk.get_width() + gap, y))
                (ax, ay) = dmj_loc[pi][-1]
                add_kong_loc[pi].append((ax + p0_mj_width, ay))
            else: #1 == pi or 3 == pi:
                dmj_loc[pi].append((x, y + 2*p0_mj_width + mjbk.get_width() + gap))
                (ax, ay) = dmj_loc[pi][-1]
                add_kong_loc[pi].append((ax, ay + p0_mj_width))
    # end assign dmj loc, add_kong_loc

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
                            drop_mj_loc[pi][i*8] = (x - i*55, y)
                        elif 2 == pi:
                            drop_mj_loc[pi][i*8] = (x, y + i*55)
                        elif 3 == pi:
                            drop_mj_loc[pi][i*8] = (x + i*55, y)
                else:
                    (x, y) = drop_mj_loc[pi][i*8+j-1]
                    if 0 == pi or 2 == pi:
                        drop_mj_loc[pi][i*8+j] = (x + p0_mj_width, y)
                    else: #1 == pi or 3 == pi:
                        drop_mj_loc[pi][i*8+j] = (x, y + p0_mj_width)

    for pi in range(4):
        if 1 == pi or 2 == pi: # reverse older
            drop_mj_loc[pi][0:8] = drop_mj_loc[pi][7::-1]
            for i in range(1, 4):
                drop_mj_loc[pi][8*i:8*(i+1)] = drop_mj_loc[pi][8*(i+1)-1:8*i-1:-1]
        drop_mj_loc[pi][32:64] = drop_mj_loc[pi][0:32]
    # end assign drop_mj_loc

    while True:
        while (mjb - mjp) >= 16:

            if 1 == first:
                # winner: -1, ini. 0~3: winner id
                winner = -1
                # 0:ini, 1:tai, 2:ready to 0(ini)
                calc_tai = 0

                turn_id = host_id
                # check_button, 0: ini
                check_button = 0 #local variable
                getmj = None
                gethu = False
                bool_pre_kong = False
                bool_last_one = False
                hear_status = [False] * 4
                first_hear = [0] * 4
                first_turn = [0] * 4
                get_done = [0] * 4
                eat_index = []
                button_enable = [0] * len(button_loc)
                dmj = [[], [], [], []]
                hmj = [[], [], [], []]
                drop_mj = [[], [], [], []]
                player_mj = [[0]*p_num, [0]*p_num, [0]*p_num, [0]*p_num]
                player_mj_num = [p_num, p_num, p_num, p_num]

                random.shuffle(all_mj)

                if 16 == p_num:
                    for i in range(0, p_num, 4):
                        j = i//4
                        for pid in range(4):
                            if 0 == pid:
                                player_mj[turn_id][i:i+4] = all_mj[p_num*j:p_num*j+4]
                            elif 1 == pid:
                                player_mj[(turn_id+1)%4][i:i+4] = all_mj[p_num*j+4:p_num*j+8]
                            elif 2 == pid:
                                player_mj[(turn_id+2)%4][i:i+4] = all_mj[p_num*j+8:p_num*j+12]
                            elif 3 == pid:
                                player_mj[(turn_id+3)%4][i:i+4] = all_mj[p_num*j+12:p_num*j+16]
                else: # 13 == p_num:
                    j = 0
                    for i in range(0, p_num, 1):
                        player_mj[turn_id][i] = all_mj[j]
                        player_mj[(turn_id+1)%4][i] = all_mj[j+1]
                        player_mj[(turn_id+2)%4][i] = all_mj[j+2]
                        player_mj[(turn_id+3)%4][i] = all_mj[j+3]
                        j += 4

                player_mj_num = [p_num, p_num, p_num, p_num]
                p0_mjloc_org = copy.deepcopy(p0_mjloc_ini)
                p0_mjloc = copy.deepcopy(p0_mjloc_ini)
                p0_get_loc = list(p0_get_loc_org)
                mjp = p_num*4
                display_all(winner)
                pygame.display.update()
                if True == Add_Delay:
                    delay(1*step)

                #temp
                #dmj[0].append([3, [1]])
                #dmj[0].append([0, [5,6,7]])
                #dmj[0].append([3, [13]])
                #player_mj[0] = [4, 6, 13, 14, 14, 18, 19, 25, 26, 26]
                #player_mj_num[0] = len(player_mj[0])
                #end temp

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
                                player_mj[pid], player_mj_num[pid] = hu_result.insert_mj(all_mj[mjb], player_mj[pid])
                                mjb -= 1

                first = 0

            display_all(winner)
            # Temp Test Code
            #for i in range(5):
            #    display_dark_kong(0, dmj_loc[0][i])
            #    display_dark_kong(1, dmj_loc[1][i])
            #    display_dark_kong(2, dmj_loc[2][i])
            #    display_dark_kong(3, dmj_loc[3][i])
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

            # handle_drop_done. -1: ini, 0: handle player drop mj, 1: done and drop mj again (for pon and kong), 2: done and get from mjb, 3: hu, 4: need to handle p0 drop mj, 5: after pon and kong drop, handle hear. 6: after eat drop, handle hear. 7: all done to continue next process. 8: all done (for return button and NOT eat), end process
            handle_drop_done = -1
            add_kong_mj = None

            if True == p0_is_AI:
                # auto debug only
                for p in range(4):
                    if player_mj_num[p] != len(player_mj[p]):
                        input("Len error!")
                    if player_mj_num[p] != 16 and player_mj_num[p] != 13 and player_mj_num[p] != 10 and player_mj_num[p] != 7 and player_mj_num[p] != 4 and player_mj_num[p] != 1:
                        input("Num error!")
                # End auto debug

                for event in pygame.event.get():
                    if event.type == QUIT:
                        exit()

            if 0 == first_turn[turn_id] and None == getmj:
                if False == p0_is_AI and 0 == turn_id:
                    handle_p0_sky_hear()

                elif 1 == hear(player_mj[turn_id], player_mj_num[turn_id]):
                    # Sky hear
                    hear_status[turn_id] = True
                    first_turn[turn_id] = 2
                    first_hear[turn_id] = 1

            if 0 == get_done[turn_id] or -1 == get_done[turn_id]:
                # check if last one
                if 16 == (mjb - mjp):
                    bool_last_one = True

                if 0 == get_done[turn_id]:
                    bool_pre_kong = False
                    getmj = all_mj[mjp]
                    mjp += 1
                elif -1 == get_done[turn_id]:
                    bool_pre_kong = True
                    getmj = all_mj[mjb]
                    mjb -= 1

                if len(hmj[turn_id]) == 8:
                    winner = handle_hu(turn_id, -1, False, None, True)
                    break
                elif hmj7_get1(turn_id) != None:
                    break

                if 0 == proc_add_hmj(turn_id, True, getmj):
                    get_done[turn_id] = 1
                    if 0 == turn_id and False == p0_is_AI:
                        if 0 == check_button:
                            check_p0_button(player_mj[turn_id], player_mj_num[turn_id], getmj, dmj[turn_id])
                            check_button = 1
                    else:
                        # Check hu
                        if 1 == hu_result.hu(player_mj[turn_id], getmj):
                            winner = handle_hu(turn_id)
                            break
                        else:
                            bool_pre_kong = False
                elif drop1_hmj7(turn_id) != None:
                    break
                else:
                    get_done[turn_id] = -1
                    continue
            else:
                bool_pre_kong = False

            if False == p0_is_AI and 0 == turn_id:
                # button_enable[4] to check hu, 0: NOT hu, 1:hu
                if True == hear_status[turn_id] and 0 == button_enable[4]:
                    player_mj[turn_id], player_mj_num[turn_id], get_done[turn_id], dk_value = hear_dark_kong(player_mj[turn_id], player_mj_num[turn_id], getmj, htext_loc[turn_id])

                    if 2 == get_done[turn_id]:
                        drop_mj[turn_id].append(getmj)
                        handle_drop_done = 0

                        display_all(winner)
                        pygame.display.update()
                        if True == Add_Delay:
                            delay(1*step)
                    elif -1 == get_done[turn_id] and dk_value != None:
                        dmj[turn_id].append([2, [dk_value]])
                        continue
                elif True  == hear_status[turn_id] and 1 == button_enable[4]:
                    br = False
                    while True:
                        bselect = click_p0_button()
                        if 4 == bselect:
                            reset_p0_button()
                            winner = handle_hu(turn_id)
                            br = True
                            break
                        elif 5 == bselect:
                            drop_mj[turn_id].append(getmj)
                            handle_drop_done = 0

                            display_all(winner)
                            pygame.display.update()
                            if True == Add_Delay:
                                delay(1*step)
                            break

                    if True == br:
                        break

            elif True == hear_status[turn_id]:
                player_mj[turn_id], player_mj_num[turn_id], get_done[turn_id], dk_value = hear_dark_kong(player_mj[turn_id], player_mj_num[turn_id], getmj, htext_loc[turn_id])

                if 2 == get_done[turn_id]:
                    drop_mj[turn_id].append(getmj)
                    handle_drop_done = 0

                    display_all(winner)
                    pygame.display.update()
                    if True == Add_Delay:
                        delay(1*step)
                elif -1 == get_done[turn_id] and dk_value != None:
                    dmj[turn_id].append([2, [dk_value]])
                    continue
            else: # For AI player 1~3, check hu before
                get_done[turn_id] = mjAI(turn_id, getmj)
                if 2 == get_done[turn_id]:
                    handle_drop_done = 0
                    first_turn[turn_id] += 1
                    if 1 == hear(player_mj[turn_id], player_mj_num[turn_id]):
                        hear_status[turn_id] = True
                        if 1 == first_turn[turn_id]:
                        #Ground hear
                            first_turn[turn_id] += 1
                            first_hear[turn_id] = 2

                elif -1 == get_done[turn_id]:
                    if None == add_kong_mj:
                        continue
                    else:
                        did = (turn_id + 1) % 4
                        br = False
                        while True:
                            if did == turn_id:
                                break
                            elif False == p0_is_AI and 0 == did:
                                if check_button < 2: # check_button == 0 or 1
                                    check_p0_button(player_mj[did], player_mj_num[did], myvalue = None, dj = None, value = dmj[turn_id][add_kong_mj][1][0], chk_eat = False, chk_huonly = True)
                                    check_button = 2

                                br, winner = handle_p0_hu_only(did, turn_id)
                                if True == br:
                                    break
                                else:
                                    did = (did + 1) % 4
                            elif 1 == hu_result.hu(player_mj[did], dmj[turn_id][add_kong_mj][1][0]):
                                winner = handle_hu(did, turn_id, False, add_kong_mj)
                                br = True
                                break
                            else:
                                did = (did + 1) % 4
                        if True == br:
                            break
                        continue

            if False == p0_is_AI and 0 == turn_id and False == hear_status[turn_id]:
                select = None
                ak_select = None

                for c in range(player_mj_num[0]):
                    (mouseX, mouseY) = pygame.mouse.get_pos() # using old position first time
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
                        #get mj index is 99
                        select = 99

                if None == select:
                    p0_mjloc = copy.deepcopy(p0_mjloc_org)
                    p0_get_loc = list(p0_get_loc_org)

                for d in range(len(dmj[0])):
                    (mouseX, mouseY) = pygame.mouse.get_pos()
                    (x, y) = dmj_loc[0][d]
                    if x < mouseX < x + 2*p0_mj_width + mjbk.get_width() and y < mouseY < y + mjbk.get_height():
                        ak_select = d

                if 2 == button_enable[1]:
                    add_kong_mj = ak_select

                display_all(winner)
                pygame.display.update()

                if get_done[turn_id] != 2:
                    br = False

                    (mouseX, mouseY) = pygame.mouse.get_pos()
                    for event in pygame.event.get():
                        if event.type == QUIT:
                            exit()
                        elif event.type == MOUSEBUTTONDOWN:
                            # if NOT dark kong proc
                            if select != None and button_enable[1] != 2:
                                ebutton = False
                                p0_mjloc = copy.deepcopy(p0_mjloc_org)
                                if 99 == select:
                                    drop_mj[turn_id].append(getmj)
                                    ebutton = check_p0_button(player_mj[turn_id], player_mj_num[turn_id])
                                    get_done[turn_id] = 2
                                    first_turn[turn_id] += 1

                                    display_all(winner)
                                    pygame.display.update()
                                    if True == Add_Delay:
                                        delay(1*step)
                                else: # select != None:
                                    drop_mj[turn_id].append(player_mj[turn_id][select])
                                    del player_mj[turn_id][select]
                                    player_mj[turn_id], player_mj_num[turn_id] = hu_result.insert_mj(getmj, player_mj[turn_id])
                                    ebutton = check_p0_button(player_mj[turn_id], player_mj_num[turn_id])
                                    get_done[turn_id] = 2
                                    first_turn[turn_id] += 1

                                    display_all(winner)
                                    pygame.display.update()
                                    if True == Add_Delay:
                                        delay(1*step)
                                if False == ebutton:
                                    # here get_done[turn_id] == 2
                                    handle_drop_done = 0
                                    break

                            if True == button_enable_chk():
                                # handle dark kong
                                bselect = None
                                bselect = p0_button_proc(mouseX, mouseY)
                                if 4 == bselect: # if hu and 0 == turn_id
                                    reset_p0_button()
                                    winner = handle_hu(turn_id)
                                    br = True
                                    break
                                elif 2 == button_enable[1]: #if add kong or dark kong
                                    if p0_add_kong(dmj[turn_id], player_mj[turn_id], getmj, add_kong_mj) != None:
                                        vi, player_mj[turn_id], player_mj_num[turn_id] = p0_add_kong(dmj[turn_id], player_mj[turn_id], getmj, add_kong_mj)

                                        screen.blit(write(u"加槓", (0, 0, 255)), htext_loc[turn_id])
                                        dmj[turn_id][add_kong_mj] = [1, [player_mj[turn_id][vi]]]
                                        del player_mj[turn_id][vi]
                                        player_mj_num[turn_id] = len(player_mj[turn_id])

                                        pygame.display.update()
                                        if True == Add_Delay:
                                            delay(1*step)

                                        did = (turn_id + 1) % 4
                                        br = False
                                        while True:
                                            if did == turn_id:
                                                break
                                            elif 1 == hu_result.hu(player_mj[did], dmj[turn_id][add_kong_mj][1][0]):
                                                winner = handle_hu(did, turn_id, get_hu = False, akong = add_kong_mj)
                                                br = True
                                                break
                                            else:
                                                did = (did + 1) % 4
                                        reset_p0_button()
                                        if True == br:
                                            break
                                        get_done[turn_id] = -1
                                        continue

                                    elif select != None and select != 99:
                                        value = player_mj[turn_id][select]
                                        gi = [select]
                                        for i in range(player_mj_num[turn_id]):
                                            if i == select:
                                                continue
                                            elif value == player_mj[turn_id][i]:
                                                gi.append(i)

                                        gi.sort(reverse=True)
                                        if value == getmj and 3 == len(gi):
                                            screen.blit(write(u"暗槓", (0, 0, 255)), htext_loc[turn_id])
                                            pygame.display.update()
                                            if True == Add_Delay:
                                                delay(1*step)

                                            for i in gi:
                                                del player_mj[turn_id][i]
                                            player_mj_num[turn_id] = len(player_mj[turn_id])
                                            dmj[turn_id].append([2, [gi[0]]])
                                            get_done[turn_id] = -1
                                            reset_p0_button()
                                            break
                                        elif 4 == len(gi):
                                            screen.blit(write(u"暗槓", (0, 0, 255)), htext_loc[turn_id])
                                            pygame.display.update()
                                            if True == Add_Delay:
                                                delay(1*step)

                                            for i in gi:
                                                del player_mj[turn_id][i]
                                            player_mj[turn_id], player_mj_num[turn_id] = hu_result.insert_mj(getmj, player_mj[turn_id])
                                            dmj[turn_id].append([2, [gi[0]]])
                                            get_done[turn_id] = -1
                                            reset_p0_button()
                                            break
                    if True == br:
                        break
                else: #if 2 == get_done[turn_id]:
                    if False == button_enable_chk():
                        handle_drop_done = 0

                    #bselect = None
                    bselect = click_p0_button()
                    #if 4 == bselect: # if hu, it seems impossible happen
                    #    reset_p0_button()
                    #    winner = handle_hu(turn_id) # 0 == turn_id
                    #    break
                    if 5 == bselect: #return
                        handle_drop_done = 0
                    elif 2 == bselect: #hear
                        reset_p0_button()
                        handle_drop_done = 0

            display_all(winner)
            pygame.display.update()
            # Handle drop mj
            while 0 == handle_drop_done or 1 == handle_drop_done or 4 == handle_drop_done:

                # 20180421, display finger
                enter_finger_code_twice = False

                draw_drop_mj()
                draw_host_location()
                pygame.display.update()

                if True == Add_Delay:
                    delay(1*step) #delay for finger display
                # End 20180421 display finger

                did = (turn_id + 1)%4
                run_once = False
                br = False

                while True:
                    if did == turn_id:
                        handle_drop_done = 0
                        break
                    elif False == run_once:
                        hid = (turn_id + 1)%4
                        br = False
                        while hid != turn_id:
                            if False == p0_is_AI and 0 == hid:
                                    if check_button < 2: # check_button == 0 or 1
                                        check_p0_button(player_mj[hid], player_mj_num[hid], myvalue = None, dj = None, value = drop_mj[turn_id][-1])
                                        check_button = 2

                                    br, winner = handle_p0_hu_only(hid, turn_id)
                                    if True == br:
                                        break
                                    else:
                                        hid = (hid + 1)%4
                            # Check hu for p1~3
                            elif 1 == hu_result.hu(player_mj[hid], drop_mj[turn_id][-1]):
                                winner = handle_hu(hid, turn_id, False)
                                br = True
                                break
                            else:
                                hid = (hid + 1)%4
                        if True == br:
                            break

                        run_once = True
                    # temp 20180811
                    #print('did', did, 'turn_id', turn_id, 'check_button', check_button)
                    # end temp 20180811
                    if False == p0_is_AI and 0 == did:
                        if check_button < 3:
                            check_p0_button(player_mj[did], player_mj_num[did], myvalue = None, dj = None, value = drop_mj[turn_id][-1])
                            check_button = 3
                        if True == button_enable_chk() and handle_drop_done != 4 and handle_drop_done != 5:

                            #bselect = None
                            bselect = click_p0_button()
                            if 2 == button_enable[0]: #pon
                                pi = pon(player_mj[did], player_mj_num[did], drop_mj[turn_id][-1])
                                if pi != -1:
                                    # 3: pon
                                    dmj[did].append([3, [drop_mj[turn_id][-1]]])
                                    drop_mj[turn_id] = drop_mj[turn_id][:-1]
                                    player_mj[did] = player_mj[did][:pi] + player_mj[did][pi+2:]
                                    player_mj_num[did] = len(player_mj[did])
                                    display_all(winner)
                                    screen.blit(write(u"碰", (0, 0, 255)), htext_loc[did])
                                    pygame.display.update()
                                    if True == Add_Delay:
                                        delay(1*step)

                                    reset_p0_button()
                                    handle_drop_done = 4

                                    display_all(winner)
                                    pygame.display.update()
                                    first_turn[did] += 1
                                    continue
                            if 2 == button_enable[1]: #kong
                                gi = kong(player_mj[did], player_mj_num[did], drop_mj[turn_id][-1])
                                if gi != -1:
                                    # 1: show kong
                                    dmj[did].append([1, [drop_mj[turn_id][-1]]])
                                    drop_mj[turn_id] = drop_mj[turn_id][:-1]
                                    player_mj[did] = player_mj[did][:gi] + player_mj[did][gi+3:]
                                    player_mj_num[did] = len(player_mj[did])
                                    display_all(winner)
                                    screen.blit(write(u"槓", (0, 0, 255)), htext_loc[did])
                                    pygame.display.update()
                                    if True == Add_Delay:
                                        delay(1*step)

                                    reset_p0_button()
                                    handle_drop_done = 2

                                    display_all(winner)
                                    pygame.display.update()

                                    check_button = 0
                                    get_done[turn_id] = 0
                                    turn_id = did
                                    first_turn[did] += 1
                                    break
                            if 5 == bselect:
                                did = (did + 1)%4
                                break
                        elif 4 == handle_drop_done: #begin if True == button_enable_chk():
                            # for drop mj
                            select = select_mj(p0_mjloc_org)
                            display_all(winner)
                            pygame.display.update()

                            for event in pygame.event.get():
                                if event.type == QUIT:
                                    exit()
                                elif event.type == MOUSEBUTTONDOWN:
                                    if select != None:
                                        drop_mj[did].append(player_mj[did][select])
                                        del player_mj[did][select]
                                        player_mj_num[did] = len(player_mj[did])
                                        p0_mjloc = copy.deepcopy(p0_mjloc_org)
                                        display_all(winner)
                                        pygame.display.update()
                                        first_turn[did] += 1

                                        ebutton = check_p0_button(player_mj[did], player_mj_num[did])

                                        if False == ebutton:
                                            handle_drop_done = 1
                                            get_done[turn_id] = 0
                                            turn_id = did
                                            #check_button = 1
                                            check_button = 0
                                            break
                                        else:
                                            handle_drop_done = 5
                                            break

                                        display_all(winner)
                                        pygame.display.update()
                                        if True == Add_Delay:
                                            delay(1*step)
                        elif 5 == handle_drop_done:
                            if False == button_enable_chk():
                                handle_drop_done = 1
                                get_done[turn_id] = 0
                                turn_id = did
                                check_button = 0
                                break

                            #bselect = None
                            bselect = click_p0_button()
                            if 5 == bselect: #return
                                handle_drop_done = 1
                                get_done[turn_id] = 0
                                turn_id = did
                                #check_button = 1
                                check_button = 0
                                break
                            elif 2 == bselect: #hear
                                reset_p0_button()
                                handle_drop_done = 1
                                get_done[turn_id] = 0
                                turn_id = did
                                #check_button = 1
                                check_button = 0
                                break
                        elif 2 == handle_drop_done:
                            break
                        else:
                            did = (did + 1)%4
                    else: #begin if False == p0_is_AI and 0 == did:
                        gi = kong(player_mj[did], player_mj_num[did], drop_mj[turn_id][-1])
                        if  gi!= -1:
                            # 1: show kong
                            dmj[did].append([1, [drop_mj[turn_id][-1]]])
                            drop_mj[turn_id] = drop_mj[turn_id][:-1]
                            player_mj[did] = player_mj[did][:gi] + player_mj[did][gi+3:]
                            player_mj_num[did] = len(player_mj[did])
                            display_all(winner)
                            screen.blit(write(u"槓", (0, 0, 255)), htext_loc[did])
                            pygame.display.update()
                            if True == Add_Delay:
                                delay(1*step)
                            handle_drop_done = 2

                            get_done[turn_id] = 0
                            turn_id = did
                            check_button = 0
                            first_turn[did] += 1
                            break

                        pi = pon(player_mj[did], player_mj_num[did], drop_mj[turn_id][-1])
                        if pi != -1:
                            # 3: pon
                            dmj[did].append([3, [drop_mj[turn_id][-1]]])
                            drop_mj[turn_id] = drop_mj[turn_id][:-1]
                            player_mj[did] = player_mj[did][:pi] + player_mj[did][pi+2:]
                            player_mj_num[did] = len(player_mj[did])
                            display_all(winner)
                            screen.blit(write(u"碰", (0, 0, 255)), htext_loc[did])
                            pygame.display.update()
                            if True == Add_Delay:
                                delay(1*step)
                            handle_drop_done = 1

                            get_done[turn_id] = 0
                            turn_id = did
                            mjAI(turn_id)
                            check_button = 0
                            first_turn[did] += 1
                            break

                        did = (did + 1)%4

                if True == br:
                    break
                elif 1 == handle_drop_done:
                    continue
                elif 0 == handle_drop_done:
                    did = (turn_id + 1)%4
                    if False == p0_is_AI and 0 == did:
                        if check_button < 4:
                            check_p0_button(player_mj[did], player_mj_num[did], myvalue = None, dj = None, value = drop_mj[turn_id][-1], chk_eat = True)
                            check_button = 4
                        if True == button_enable_chk() and button_enable[3] != 0:
                            smj = None
                            while True:
                                select = select_mj(p0_mjloc_org, did, smj)

                                display_all(winner)
                                pygame.display.update()

                                if 0 == handle_drop_done:
                                    (mouseX, mouseY) = pygame.mouse.get_pos()
                                    br = False
                                    bselect = None
                                    for event in pygame.event.get():
                                        if event.type == QUIT:
                                            exit()
                                        elif event.type == MOUSEBUTTONDOWN:
                                            bselect = p0_button_proc(mouseX, mouseY)
                                            if select != None and 2 == button_enable[3]: #eat
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
                                                        dmj[did].append([0, etempv])
                                                        drop_mj[turn_id] = drop_mj[turn_id][:-1]
                                                        del player_mj[did][sort_index[1]]
                                                        del player_mj[did][sort_index[0]]

                                                        player_mj_num[did] = len(player_mj[did])
                                                        display_all(winner)

                                                        screen.blit(write(u"吃", (0, 0, 255)), htext_loc[did])
                                                        pygame.display.update()
                                                        if True == Add_Delay:
                                                            delay(1*step)

                                                        reset_p0_button()
                                                        p0_mjloc = copy.deepcopy(p0_mjloc_org)
                                                        handle_drop_done = 4
                                                        smj = None
                                                        first_turn[did] += 1
                                                        continue
                                                    else: # Can't eat
                                                        smj = None
                                                else: #smj != None and select == smj
                                                    smj = None
                                            elif 5 == bselect:
                                                handle_drop_done = 8
                                                break
                                            else: # None == select or 0 or 1 == button_enable[3]
                                                smj = None
                                    if True == br:
                                        break
                                elif 4 == handle_drop_done:
                                    for event in pygame.event.get():
                                        if event.type == QUIT:
                                            exit()
                                        elif event.type == MOUSEBUTTONDOWN:
                                            if select != None:
                                                drop_mj[did].append(player_mj[did][select])
                                                del player_mj[did][select]
                                                player_mj_num[did] = len(player_mj[did])
                                                p0_mjloc = copy.deepcopy(p0_mjloc_org)
                                                display_all(winner)
                                                pygame.display.update()
                                                if True == Add_Delay:
                                                    delay(1*step)
                                                first_turn[did] += 1

                                                ebutton = check_p0_button(player_mj[did], player_mj_num[did])

                                                handle_drop_done = 6
                                                if False == ebutton:
                                                    get_done[turn_id] = 0
                                                    turn_id = did
                                                    #check_button = 1
                                                    check_button = 0
                                                    break

                                                break
                                elif 6 == handle_drop_done:
                                    if False == button_enable_chk():
                                        handle_drop_done = 7
                                        get_done[turn_id] = 0
                                        turn_id = did
                                        #check_button = 1
                                        check_button = 0
                                        break

                                    #bselect = None
                                    bselect = click_p0_button()
                                    if 5 == bselect: #return
                                        handle_drop_done = 7
                                        get_done[turn_id] = 0
                                        turn_id = did
                                        #check_button = 1
                                        check_button = 0
                                        break
                                    elif 2 == bselect: #hear
                                        reset_p0_button()
                                        handle_drop_done = 7
                                        get_done[turn_id] = 0
                                        turn_id = did
                                        #check_button = 1
                                        check_button = 0
                                        break
                                elif 8 == handle_drop_done:
                                    break
                            if 7 == handle_drop_done:
                                handle_drop_done = 0
                                continue
                            elif 8 == handle_drop_done:
                                handle_drop_done = 0
                    else:
                        etemp = eat(player_mj[did], player_mj_num[did], drop_mj[turn_id][-1])
                        if etemp != []: # avoid eat i and then drop i
                            if drop_mj[turn_id][-1] == AI_drop_for_eat(did, etemp):
                                #print('a', player_mj[did][etemp[0]], player_mj[did][etemp[1]], drop_mj[turn_id][-1])
                                etemp = [] #Won't eat
                            else:
                                ev = eat_middle_position([player_mj[did][etemp[0]], player_mj[did][etemp[1]]], drop_mj[turn_id][-1])
                                consider_drop = AI_drop_for_eat(did, etemp)
                                if (2 == ev and consider_drop + 3 == drop_mj[turn_id][-1] and consider_drop%9 != 8) or (0 == ev and consider_drop == drop_mj[turn_id][-1] + 3 and consider_drop%9 != 0):
                                    #print('b', player_mj[did][etemp[0]], player_mj[did][etemp[1]], drop_mj[turn_id][-1], consider_drop)
                                    etemp = [] #Won't eat
                        if etemp != []: # do eat process
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
                            display_all(winner)

                            screen.blit(write(u"吃", (0, 0, 255)), htext_loc[did])
                            pygame.display.update()
                            if True == Add_Delay:
                                delay(1*step)

                            get_done[turn_id] = 0
                            turn_id = did
                            mjAI(turn_id)
                            check_button = 0
                            first_turn[did] += 1
                            continue
                if 2 == handle_drop_done:
                    get_done[turn_id] = -1
                elif 0 == handle_drop_done:
                    get_done[turn_id] = 0
                    getmj = None
                    check_button = 0
                    p0_mjloc = copy.deepcopy(p0_mjloc_org)
                    reset_p0_button()

                    turn_id = (turn_id + 1)%4
                break
            # End handle drop mj
            if winner != -1:
                break

        if -1 == winner:
            display_all(-1, end_game = True)
            pygame.display.update()
            if True == Add_Delay:
                delay(3*step)
        elif host_id != winner: #winner != -1
            # host_num set to 0 in handle_hu
            #host_num = 0
            host_id = (host_id + 1)%4
            if host_id == east_to_north[0]:
                circle = (circle + 1)%4

        first = 1
        mjp = 0
        mjb = 143
        #print("End Game")
    exit()

if __name__ == "__main__":
    main()
    #try:
    #    main()
    #except Exception as e:
    #    print(e)
    #    input("Press Enter key to continue")
