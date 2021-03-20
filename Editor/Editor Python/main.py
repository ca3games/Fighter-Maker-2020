import sys
sys.path.append("./Tabs/")

from BackgroundTab import *
from CharacterTab import *
from EngineTab import *
from FileTab import *
from FireballTab import *
from ScreensTab import *
from SoundsTab import *
import wx
from globals import *


class MainEditor(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, title="Fighter Maker 2020", style = wx.DEFAULT_FRAME_STYLE & ~(wx.RESIZE_BORDER | wx.MAXIMIZE_BOX))
        self.SetSize(WINDOW_WIDTH, WINDOW_HEIGHT)

        panel = wx.Panel(self)
        nb = wx.Notebook(panel)

        bt = BackgroundTab(nb)
        ct = CharacterTab(nb)
        et = EngineTab(nb)
        ft = FileTab(nb)
        fbt = FireballTab(nb)
        st = ScreensTab(nb)
        snt = SoundsTab(nb)

        nb.AddPage(ft, "File")
        nb.AddPage(et, "Engine")
        nb.AddPage(ct, "Characters")
        nb.AddPage(bt, "Backgrounds")
        nb.AddPage(st, "Screens")
        nb.AddPage(snt, "Sounds")
        nb.AddPage(fbt, "Fireballs")

        sizer = wx.BoxSizer()
        sizer.Add(nb, 1, wx.EXPAND)
        panel.SetSizer(sizer)


if __name__ == "__main__":
    app = wx.App()
    MainEditor().Show()
    app.MainLoop()
        
