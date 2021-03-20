import sys
sys.path.append("./Tabs/Screens/")

import wx
from globals import *

from ScreenList import *
from EditorScreens import *
from Intro import *
from Ending import *
from StoryMode import *
from Victory import *
from IntroBattle import *
from Transitions import *

class ScreensTab(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        
        panel = wx.Panel(self, size=(WINDOW_WIDTH, WINDOW_HEIGHT))
        nb = wx.Notebook(panel)
        
        sl = ScreensList(nb)
        ed = EditorScreens(nb)
        nt = Intro(nb)
        en = Ending(nb)
        st = StoryMode(nb)
        vt = Victory(nb)
        ib = IntroBattle(nb)
        tr = Transitions(nb)
        
        nb.AddPage(sl, "Screen Lists")
        nb.AddPage(ed, "Editor")
        nb.AddPage(st, "Story Mode")
        nb.AddPage(nt, "Intro")
        nb.AddPage(en, "Ending")
        nb.AddPage(vt, "Victory")
        nb.AddPage(ib, "Intro Battle")
        nb.AddPage(tr, "Transitions")
        
        sizer = wx.BoxSizer()
        sizer.Add(nb, 1, wx.EXPAND)
        
        self.SetSizer(sizer)


