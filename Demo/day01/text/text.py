'''
Created on 2017-6-6

@author: WuFan
'''
import wx
class XinFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, -1,'biaoti', size = (300, 200))
        lable = wx.StaticText(self, -1, 'hellopython', (100, 10))
        lable.SetForegroundColour('white')
        lable.SetBackgroundColour('BLUE')

        text = wx.StaticText(self, -1, 'wufan\nwusi', (100, 50), (200, -1), wx.ALIGN_CENTER)
        text.SetForegroundColour('green')
        text.SetBackgroundColour('yellow')
       
app = wx.App()
xframe = XinFrame()
xframe.Show()
app.MainLoop()
        
