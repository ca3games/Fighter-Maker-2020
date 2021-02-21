import wx
from globals import *

class ScreensTab(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        t = wx.StaticText(self, -1, "This is the Screens Tab", (WINDOW_WIDTH, WINDOW_HEIGHT))
