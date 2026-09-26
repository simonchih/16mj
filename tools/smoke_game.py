"""Play real AI rounds, including scoring and redeal; optionally use native SDL."""
import argparse
import os
import sys
from pathlib import Path
parser=argparse.ArgumentParser()
parser.add_argument('--native',action='store_true')
parser.add_argument('--rounds',type=int,default=8)
parser.add_argument('--seed',type=int,default=16)
args=parser.parse_args()
if not args.native: os.environ['SDL_VIDEODRIVER']='dummy'
os.environ.setdefault('SDL_AUDIODRIVER','dummy')
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT))
import pygame
import p16mj as g

class Finished(Exception): pass
class FastClock:
    def tick(self,*args): pass
g.frame_clock=FastClock()
g.p0_is_AI=True
g.Add_Delay=False
g.random.seed(args.seed)
original=g.display_all
rounds=0
frames=0
scored=False
ended=False
shots=ROOT/'art'
shots.mkdir(exist_ok=True)

def display(win_id,did=-1,akong=None,end_game=False):
    global rounds,frames,scored,ended
    frames+=1
    pygame.event.pump()
    if frames>20000: raise RuntimeError('Smoke-test frame limit exceeded')
    if win_id==-1 and not end_game and ended:
        ended=False
        scored=False
        if rounds>=args.rounds: raise Finished()
    scoring=g.calc_tai==1
    original(win_id,did,akong,end_game)
    if frames==40:
        pygame.image.save(g.screen,str(shots/'gameplay.png'))
    if scoring and not scored:
        pygame.image.save(g.screen,str(shots/'scoring.png'))
        rounds+=1; scored=True; ended=True
        print('Scored round',rounds,'winner',win_id,flush=True)
    elif end_game and not ended:
        rounds+=1; ended=True
        print('Drawn round',rounds,flush=True)

g.display_all=display
try:
    g.main()
except Finished:
    print('PASS:',rounds,'complete rounds;',frames,'frames; seed',args.seed)
finally:
    pygame.quit()
