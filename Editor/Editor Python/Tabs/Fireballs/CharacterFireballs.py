import sys
sys.path.append("./Tabs/Fireballs/Fireballs/")

import wx
from globals import *

from FireballChar import *
from FireballFSM import *
from FireballSprites import *
from FireballAnimation import *

class CharacterFireballs(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        
        panel = wx.Panel(self, size=(WINDOW_WIDTH, WINDOW_HEIGHT))
        nb = wx.Notebook(panel)
        
        fb = FireballChar(nb)
        ff = FireballFSM(nb)
        fs = FireballSprites(nb)
        fa = FireballAnimation(nb)
        
        nb.AddPage(fb, "Fireball")
        nb.AddPage(ff, "FSM")
        nb.AddPage(fs, "Sprites")
        nb.AddPage(fa, "Animation")
        
        sizer = wx.BoxSizer()
        sizer.Add(nb, 1, wx.EXPAND)
        
        self.SetSizer(sizer)

