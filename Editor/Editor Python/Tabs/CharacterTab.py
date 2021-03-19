import sys
sys.path.append("./Tabs/Characters")

import wx
from globals import *

from CharacterData import *
from CharacterSprites import *

class CharacterTab(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        
        panel = wx.Panel(self, size=(WINDOW_WIDTH, WINDOW_HEIGHT))
        nb = wx.Notebook(panel)
        
        cd = CharacterData(nb)
        cs = CharacterSprites(nb)
        
        nb.AddPage(cd, "Data")
        nb.AddPage(cs, "Sprites")
        
        sizer = wx.BoxSizer()
        sizer.Add(nb, 1, wx.EXPAND)
        
        self.SetSizer(sizer)

