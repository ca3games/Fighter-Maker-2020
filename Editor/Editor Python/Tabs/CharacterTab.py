import sys
sys.path.append("./Tabs/Characters")

import wx
from globals import *

from CharacterData import *
from CharacterSprites import *
from Hitbox import *
from Animations import *
from SparksCharacters import *
from Commands import *
from HitStatesCharacter import *
from FSM import *
from AI import *

class CharacterTab(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        
        panel = wx.Panel(self, size=(WINDOW_WIDTH, WINDOW_HEIGHT))
        nb = wx.Notebook(panel)
        
        cd = CharacterData(nb)
        cs = CharacterSprites(nb)
        ht = HitBox(nb)
        an = Animations(nb)
        sc = SparksCharacter(nb)
        co = Commands(nb)
        hc = HitStatesCharacter(nb)
        fm = FSM(nb)
        ai = AI(nb)
        
        nb.AddPage(cd, "Data")
        nb.AddPage(cs, "Sprites")
        nb.AddPage(ht, "Hitbox")
        nb.AddPage(an, "Animations")
        nb.AddPage(sc, "Sparks")
        nb.AddPage(co, "Commands")
        nb.AddPage(hc, "HitStates")
        nb.AddPage(fm, "FSM")
        nb.AddPage(ai, "AI")
        
        sizer = wx.BoxSizer()
        sizer.Add(nb, 1, wx.EXPAND)
        
        self.SetSizer(sizer)

