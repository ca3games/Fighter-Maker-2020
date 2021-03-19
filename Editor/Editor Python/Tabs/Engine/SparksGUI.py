import sys
sys.path.append("./Tabs/Engine/GUI/Sparks")

import wx
from globals import *

from ListSparks import *
from EditorSpark import *

class SparksGUI(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        
        panel = wx.Panel(self, size=(WINDOW_WIDTH, WINDOW_HEIGHT))
        
        nb = wx.Notebook(panel)
        
        ls = ListSparks(nb)
        es = EditorSpark(nb)
        
        nb.AddPage(ls, "List")
        nb.AddPage(es, "Editor")
        
        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(nb, 1, wx.EXPAND)
        
        self.SetSizer(sizer)
        
        
