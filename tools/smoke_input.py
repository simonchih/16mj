"""Exercise scripted mouse input through the SDL event queue and human discard branch."""
import os
import sys
from pathlib import Path
os.environ.setdefault('SDL_AUDIODRIVER','dummy')
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT))
import pygame
import p16mj as g

class Finished(Exception): pass
g.random.seed(42)
g.Add_Delay=False
g.p0_is_AI=False
original=g.display_all
frames=0
armed=0

def display(*args,**kwargs):
    global frames,armed
    frames+=1
    if frames>250: raise RuntimeError('Human input smoke-test timed out')
    original(*args,**kwargs)
    if g.drop_mj[0]:
        assert len(g.drop_mj[0])==1
        assert len(g.player_mj[0])==16
        pygame.image.save(g.screen,str(ROOT/'art/human-input.png'))
        raise Finished()
    if g.turn_id==0 and g.get_done[0]==1 and g.getmj is not None:
        x,y=g.p0_get_loc_org
        # Supply deterministic pointer coordinates even on an unfocused test window.
        pygame.mouse.get_pos = lambda: (x+20,y+20)
        armed+=1
        if armed==2:
            pygame.event.post(pygame.event.Event(pygame.MOUSEBUTTONDOWN,button=1,pos=(x+20,y+20)))

g.display_all=display
try:
    g.main()
except Finished:
    print('PASS: scripted human mouse discard; 16 tiles remain; frames',frames)
finally:
    pygame.quit()
