import sys
sys.path.append("./Tabs/Background")

import wx
from globals import *

from BackgroundList import *
from CameraData import *
from Editor import *

class BackgroundTab(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        
        panel = wx.Panel(self, size=(WINDOW_WIDTH, WINDOW_HEIGHT))
        nb = wx.Notebook(panel)
        
        bl = BackgroundList(nb)
        cd = CameraData(nb)
        ed = EditorLevel(nb)
        
        nb.AddPage(bl, "List")
        nb.AddPage(cd, "Camera Data")
        nb.AddPage(ed, "Level Editor")
        
        sizer = wx.BoxSizer()
        sizer.Add(nb, 1, wx.EXPAND)
        
        self.SetSizer(sizer)

