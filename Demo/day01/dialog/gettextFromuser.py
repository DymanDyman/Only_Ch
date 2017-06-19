# -*-coding=utf-8 -*-
import wx
class MyFrame(wx.Frame):
    def OnclickBtn(self, event):
        name=wx.GetTextFromUser('请输入：','name needed')
        print 'name is :',name

    
    def OncheckBtn(self,event):
        lan=['aaa','bbb','ccc','ddd','fff','ggg']
        choice=wx.GetSingleChoice('请选择','标题',lan)
        print '我的选择是：',choice
    
    
    def __init__(self):
        wx.Frame.__init__(self, None, -1, 'dialog demo', size = (300, 200))
        panel = wx.Panel(self)
        btn = wx.Button(panel, -1, '输入名字', pos = (30, 30))
        btn.Bind(wx.EVT_BUTTON, self.OnclickBtn)
        btn2 = wx.Button(panel, -1, '选择名字', pos = (70, 90))
        btn2.Bind(wx.EVT_BUTTON, self.OncheckBtn)
if 1 == 1:
    app = wx.App()
    MyFrame().Show()
    app.MainLoop()
