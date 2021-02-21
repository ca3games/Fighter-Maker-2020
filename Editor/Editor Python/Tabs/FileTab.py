import wx
from globals import *

class FileTab(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        t = wx.StaticText(self, -1, "This is the first tab", (WINDOW_WIDTH, WINDOW_HEIGHT))
