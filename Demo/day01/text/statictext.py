'''
Created on 2017-6-6

@author: WuFan
'''
import wx
class MyFrame(wx.Frame):
    def __init__(self):
        wx.Frame.__init__(self, None, -1, 'xixi', size = (300, 200))
        panel = wx.Panel(self)
        lable = wx.StaticText(panel, -1, 'text show only', (100, 19))
        text = wx.TextCtrl(panel, -1, 'input', (100, 50))
        text.SetInsertionPoint(3)
        text.AppendText('11111')
        text.SetInsertionPoint(2)
  
app = wx.App()
mFrame = MyFrame()
mFrame.Show()
app.MainLoop()