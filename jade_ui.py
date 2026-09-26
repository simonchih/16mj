"""Rendering-only jade/gold theme. Never consumes the game's random stream."""
import math
import random
from functools import lru_cache
from pathlib import Path
import pygame

ROOT = Path(__file__).resolve().parent
GOLD = (238, 201, 116)
IVORY = (255, 244, 213)
MINT = (142, 223, 174)

@lru_cache(maxsize=32)
def font(size):
    return pygame.font.Font(str(ROOT/'wqy-zenhei.ttf'), size)

def label(text, size=22, color=IVORY):
    return font(size).render(text.strip(), True, color)

def panel(screen, rect, fill=(6, 41, 30), border=(125, 105, 57), radius=12):
    pygame.draw.rect(screen, fill, rect, border_radius=radius)
    pygame.draw.rect(screen, border, rect, 1, border_radius=radius)

def table_overlay(screen):
    # Quiet center medallion. The discard rivers surround this reserved area.
    c=(600,475)
    pygame.draw.circle(screen,(12,66,46),c,74)
    pygame.draw.circle(screen,(83,107,63),c,74,1)
    pygame.draw.circle(screen,(52,94,62),c,67,1)
    t=label('16',46,(128,149,95))
    screen.blit(t,t.get_rect(center=(600,464)))
    t=label('台 灣 麻 將',12,(132,158,114))
    screen.blit(t,t.get_rect(center=(600,507)))
    panel(screen,(210,18,790,47),radius=14)
    t=label('翡翠麻將',22,GOLD)
    screen.blit(t,(228,28))

def hud(screen, wind, remaining, turn, dealer_count):
    screen.blit(label(wind,20),(370,30))
    screen.blit(label('牌山  %02d'%max(0,remaining),20,GOLD),(515,30))
    screen.blit(label('連莊 %d'%dealer_count,18),(680,32))
    screen.blit(label('輪到你出牌' if turn==0 else '電腦思考中',18,MINT),(825,32))
    screen.blit(label('點選手牌即可出牌',15,(185,200,164)),(45,810))
    screen.blit(label('吃／暗槓：再選手牌',15,(185,200,164)),(45,835))

def button(screen, image, rect, text, state, hover):
    screen.blit(image,rect)
    if state==0:
        shade=pygame.Surface(rect.size,pygame.SRCALPHA)
        shade.fill((0,18,13,125))
        screen.blit(shade,rect)
    if state==2 or (state and hover):
        pygame.draw.rect(screen,GOLD,rect.inflate(-3,-3),2,border_radius=8)
    t=label(text,29,GOLD if state==2 else IVORY if state else (102,129,111))
    screen.blit(t,t.get_rect(center=(rect.centerx-1,rect.centery-3)))

def meld_layout(pid, xy, pitch, kong=False):
    """Fit four compact kong tiles in the same footprint as three pon tiles."""
    x,y=xy
    count=4 if kong else 3
    if kong: pitch=round(pitch*.75)
    if pid in (0,2):
        points=[(x+i*pitch,y) for i in range(count)]
    else:
        points=[(x,y+i*pitch) for i in range(count)]
    return points

class Effects:
    def __init__(self):
        self.events=[]
        self.rng=random.Random(1600)
        self.last_drops=None
        self.last_winner=-1
        self.last_draw=None
        self.last_hear=(False,)*4
        self.reduced=False

    def emit(self, text, pos=(600,475), kind='action'):
        now=pygame.time.get_ticks()/1000
        # Bound event storage even during fast automated simulations.
        self.events=[e for e in self.events if now-e['start']<e['life']][-12:]
        count=64 if kind=='win' else 20 if kind=='action' else 10
        particles=[(self.rng.random()*math.tau,self.rng.uniform(25,115),self.rng.uniform(1,3)) for _ in range(count)]
        self.events.append(dict(text=text,pos=pos,kind=kind,start=now,life=3.6 if kind=='win' else 1.15,particles=particles))

    def observe(self, drops, locations, winner, getmj, turn, done, drawpos, hear):
        current=tuple(tuple(v) for v in drops)
        if self.last_drops is not None:
            for pid,river in enumerate(current):
                if len(river)>len(self.last_drops[pid]):
                    x,y=locations[pid][len(river)-1]
                    self.emit('',(x+20,y+24),'drop')
        self.last_drops=current
        draw=(getmj,turn,tuple(done),len(current[turn]))
        if draw!=self.last_draw and turn==0 and done[0]==1 and getmj is not None and len(drawpos)==2:
            self.emit('',(drawpos[0]+19,drawpos[1]+24),'draw')
        self.last_draw=draw
        for pid,ready in enumerate(hear):
            if ready and not self.last_hear[pid]:
                self.emit('聽牌',((600,720),(1000,430),(600,200),(200,430))[pid])
        self.last_hear=tuple(hear)
        if winner>=0 and winner!=self.last_winner:
            self.emit('胡牌',(600,455),'win')
        self.last_winner=winner

    def draw(self,screen):
        now=pygame.time.get_ticks()/1000
        self.events=[e for e in self.events if now-e['start']<e['life']]
        if not self.events: return
        layer=pygame.Surface(screen.get_size(),pygame.SRCALPHA)
        for e in self.events:
            age=now-e['start']; progress=age/e['life']
            alpha=int(235*min(1,(1-progress)*3))
            x,y=e['pos']; win=e['kind']=='win'
            radius=int(18+progress*(155 if win else 55))
            if not self.reduced:
                pygame.draw.circle(layer,(*GOLD,int(alpha*(1-progress))), (int(x),int(y)),radius,2)
                for a,speed,size in e['particles']:
                    px=x+math.cos(a)*speed*age
                    py=y+math.sin(a)*speed*age+age*age*16
                    pygame.draw.circle(layer,(*GOLD,alpha),(int(px),int(py)),int(size))
            if e['text']:
                yy=y-10 if self.reduced else y-10-min(age*15,25)
                caption=label(e['text'],58 if win else 32,GOLD)
                rect=caption.get_rect(center=(int(x),int(yy)))
                box=rect.inflate(44,22)
                pygame.draw.rect(layer,(3,30,21,alpha),box,border_radius=16)
                pygame.draw.rect(layer,(*GOLD,alpha),box,2,border_radius=16)
                caption.set_alpha(alpha)
                layer.blit(caption,rect)
                if win:
                    sub=label('恭 喜 胡 牌',18,IVORY)
                    sub.set_alpha(alpha)
                    layer.blit(sub,sub.get_rect(center=(int(x),box.bottom+20)))
        screen.blit(layer,(0,0))
