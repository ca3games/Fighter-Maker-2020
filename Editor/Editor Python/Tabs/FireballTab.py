import sys
sys.path.append("./Tabs/Fireballs/")

import wx
from globals import *

from CharacterFireballs import *
from Mascot import *

class FireballTab(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        
        panel = wx.Panel(self, size=(WINDOW_WIDTH, WINDOW_HEIGHT))
        nb = wx.Notebook(panel)
        
        cf = CharacterFireballs(nb)
        mc = Mascot(nb)
        
        nb.AddPage(cf, "Character Fireballs")
        nb.AddPage(mc, "Mascot")
        
        sizer = wx.BoxSizer()
        sizer.Add(nb, 1, wx.EXPAND)
        
        self.SetSizer(sizer)

