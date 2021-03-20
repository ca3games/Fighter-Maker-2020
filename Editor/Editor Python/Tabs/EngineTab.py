import sys
sys.path.append("./Tabs/Engine")

import wx
from globals import *

from BasicData import *
from CharacterList import *
from GUITab import *
from CommonImages import *
from SparksGUI import *
from HitStates import *
from VersusScreen import *

class EngineTab(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        
        panel = wx.Panel(self, size=(WINDOW_WIDTH, WINDOW_HEIGHT))
        nb = wx.Notebook(panel)
        
        bd = BasicData(nb)
        cl = CharacterList(nb)
        vs = VersusScreen(nb)
        gui = GUITab(nb)
        ci = CommonImages(nb)
        sp = SparksGUI(nb)
        ht = HitStates(nb)
        
        nb.AddPage(bd, "Basic Data")
        nb.AddPage(cl, "Character List")
        nb.AddPage(vs, "Versus Screen")
        nb.AddPage(gui, "GUI")
        nb.AddPage(ci, "Common Images")
        nb.AddPage(sp, "Sparks")
        nb.AddPage(ht, "HitStates")
        
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(nb, 1, wx.EXPAND)
        
        self.SetSizer(sizer)
