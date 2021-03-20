import sys
sys.path.append("./Tabs/Fireballs/Mascot/")

import wx
from globals import *

from MascotFSM import *
from MascotData import *
from MascotCommands import *

class Mascot(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        
        panel = wx.Panel(self, size=(WINDOW_WIDTH, WINDOW_HEIGHT))
        nb = wx.Notebook(panel)
        
        md = MascotData(nb)
        mf = MascotFSM(nb)
        mc = MascotCommands(nb)
        
        nb.AddPage(md, "Data")
        nb.AddPage(mf, "FSM")
        nb.AddPage(mc, "Commands")
        
        sizer = wx.BoxSizer()
        sizer.Add(nb, 1, wx.EXPAND)
        
        self.SetSizer(sizer)

        
        
