# -*-coding=utf-8 -*-
import wx
class MyFrame(wx.Frame):
    def OnclickBtn(self, event):
        wx.MessageBox('我是内容', '我是标题')
    def __init__(self):
        wx.Frame.__init__(self, None, -1, 'dialog demo', size = (300, 200))
        panel = wx.Panel(self)
        btn = wx.Button(panel, -1, 'click', pos = (70, 30))
        btn.Bind(wx.EVT_BUTTON, self.OnclickBtn)
if 1 == 1:
    app = wx.App()
    MyFrame().Show()
    app.MainLoop()
