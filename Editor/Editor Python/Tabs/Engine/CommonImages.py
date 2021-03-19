import wx
from globals import *

class CommonImages(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        t = wx.StaticText(self, -1, "This is the Lifebar Tab", (WINDOW_WIDTH, WINDOW_HEIGHT))
