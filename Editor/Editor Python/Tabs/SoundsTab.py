import sys
sys.path.append("./Tabs/Sounds/")

import wx
from globals import *

from Sounds import *
from Music import *

class SoundsTab(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        
        panel = wx.Panel(self, size=(WINDOW_WIDTH, WINDOW_HEIGHT))
        nb = wx.Notebook(panel)
        
        sd = Sounds(nb)
        mu = Music(nb)
        
        nb.AddPage(sd, "Sounds")
        nb.AddPage(mu, "Music")
        
        sizer = wx.BoxSizer()
        sizer.Add(nb, 1, wx.EXPAND)
        
        self.SetSizer(sizer)

