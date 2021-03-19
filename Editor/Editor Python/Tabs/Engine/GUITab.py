import sys
sys.path.append("./Tabs/Engine/GUI")

import wx
from globals import *

from Lifebars import *
from Portraits import *
from ComboGUI import *
from GUISprites import *


class GUITab(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        
        panel = wx.Panel(self, size=(WINDOW_WIDTH, WINDOW_HEIGHT))
        
        nb = wx.Notebook(panel)
        
        lb = Lifebars(nb)
        pt = Portraits(nb)
        cb = ComboGUI(nb)
        gs = GUISprites(nb)
        
        nb.AddPage(lb, "Lifebars")
        nb.AddPage(pt, "Portraits")
        nb.AddPage(cb, "Combo GUI")
        nb.AddPage(gs, "Sprites")
        
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(nb, 1, wx.EXPAND)
        
        self.SetSizer(sizer)
