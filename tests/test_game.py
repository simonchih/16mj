"""Rule boundaries and visual/integration regressions; uses SDL's headless driver."""
import os
os.environ['SDL_VIDEODRIVER']='dummy'
os.environ['SDL_AUDIODRIVER']='dummy'
import sys
from pathlib import Path
import unittest
ROOT=Path(__file__).resolve().parents[1]
sys.path.insert(0,str(ROOT))
import pygame
import p16mj as g
import jade_ui

class Rules(unittest.TestCase):
    def test_pon_requires_two_in_hand_plus_discard(self):
        self.assertEqual(g.pon([4],1,4),-1)
        self.assertEqual(g.pon([4,4],2,4),0)
        self.assertEqual(g.pon([4,5],2,4),-1)

    def test_open_kong_requires_three_plus_discard(self):
        self.assertEqual(g.kong([4,4],2,4),-1)
        self.assertEqual(g.kong([4,4,4],3,4),0)
        self.assertEqual(g.kong([4,4,5],3,4),-1)

    def test_concealed_kong_requires_four(self):
        self.assertEqual(g.dark_kong([4,4,4],3),-1)
        self.assertEqual(g.dark_kong([4,4,4,4],4),0)
        self.assertEqual(g.dark_kong([4,4,4,5],4),-1)

    def test_added_kong_requires_matching_pon(self):
        self.assertEqual(g.add_kong([[3,[4]]],4),0)
        self.assertEqual(g.add_kong([[3,[4]]],5),-1)
        self.assertEqual(g.add_kong([[1,[4]]],4),-1)

    def test_eat_does_not_cross_suits_or_use_honors(self):
        self.assertEqual(g.eat([7,8],2,9),[])
        self.assertEqual(g.eat([27,28],2,29),[])
        self.assertEqual(g.eat([0,1],2,2),[0,1])

    def test_winning_sixteen_tile_hand(self):
        self.assertEqual(g.hu_result.hu([0,0,0,1,2,3,9,10,11,18,19,20,27,27,27,31],31),1)

class Rendering(unittest.TestCase):
    def test_action_button_selection_and_cancel(self):
        old=g.button_enable[:]
        try:
            g.button_enable=[1,1,0,1,1,1]
            x,y=g.button_loc[1]
            self.assertEqual(g.p0_button_proc(x+25,y+25),1)
            self.assertEqual(g.button_enable[1],2)
            self.assertEqual(g.p0_button_proc(x+25,y+25),1)
            self.assertEqual(g.button_enable[1],1)
            x,y=g.button_loc[5]
            self.assertEqual(g.p0_button_proc(x+25,y+25),5)
            self.assertEqual(g.button_enable,[0]*6)
        finally: g.button_enable=old

    def test_kong_four_distinct_positions_every_seat(self):
        for pid in range(4):
            pon=jade_ui.meld_layout(pid,(300,300),34)
            kong=jade_ui.meld_layout(pid,(300,300),34,True)
            self.assertEqual(len(set(pon)),3)
            self.assertEqual(len(set(kong)),4)
            self.assertLessEqual(3*26+g.kong_image(0,4).get_width(),112)
            class Recorder:
                def __init__(self): self.calls=[]
                def blit(self,im,pos): self.calls.append((im,pos))
            old=g.screen
            try:
                r=Recorder(); g.screen=r
                g.display_show_kong(pid,4,(300,300))
                self.assertEqual(len(r.calls),4)
                self.assertTrue(all(im is g.kong_image(pid,4) for im,_ in r.calls))
                r.calls=[]
                g.display_dark_kong(pid,(300,300))
                self.assertEqual(len(r.calls),4)
                r.calls=[]
                g.display_pon(pid,4,(300,300))
                self.assertEqual(len(r.calls),3)
            finally: g.screen=old

    def test_all_assets_load_and_have_transparency(self):
        files=list((ROOT/'Image').glob('*.png'))
        self.assertEqual(len(files),61)
        for p in files:
            im=pygame.image.load(str(p))
            self.assertGreater(im.get_width(),0)
            if p.name!='Nostalgy.png': self.assertTrue(im.get_flags() & pygame.SRCALPHA,p.name)
        for index in range(55):
            for pid in range(4): self.assertIsNotNone(g.pid_to_image(pid,index))

    def test_effects_do_not_change_game_rng(self):
        g.random.seed(33)
        before=g.random.getstate()
        for text in ('碰','槓','暗槓','加槓','吃','聽牌','補花','胡牌'):
            g.effects.emit(text,kind='win' if text=='胡牌' else 'action')
        g.effects.draw(g.screen)
        self.assertEqual(before,g.random.getstate())

    def test_present_restores_underlying_frame(self):
        g.screen.fill((12,80,42))
        before=pygame.image.tobytes(g.screen,'RGB')
        g.effects.emit('槓')
        g.present()
        self.assertEqual(before,pygame.image.tobytes(g.screen,'RGB'))

    def test_delay_processes_quit(self):
        pygame.event.post(pygame.event.Event(pygame.QUIT))
        try:
            with self.assertRaises(SystemExit): g.delay(1)
        finally:
            pygame.init()
            g.screen=pygame.display.set_mode(g.SCREEN_SIZE)

if __name__=='__main__': unittest.main()
