import wx
from globals import *

class SoundsTab(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        t = wx.StaticText(self, -1, "This is the Sounds Tab", (WINDOW_WIDTH, WINDOW_HEIGHT))
