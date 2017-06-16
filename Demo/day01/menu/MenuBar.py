# -*- coding=utf-8 -*-
import wx
class MyFramm(wx.Frame):

    
    def VN1(self, event):
        print '我是第一行信息'
    
    
    def male2(self,event):
        print '我是女'
    
    
    def __init__(self):
        wx.Frame.__init__(self, None, -1, 'menu demo')
        panel = wx.Panel(self)
        menubar = wx.MenuBar()
        self.SetMenuBar(menubar)
        menu1 = wx.Menu()
        menubar.Append(menu1, '行信息')
        menu2=wx.Menu()
        menubar.Append(menu2,'性别')
        
        X = menu1.Append(-1, '第一行')
        Y = menu1.Append(-1, '第二行')
        self.Bind(wx.EVT_MENU, self.VN1, X)
        M=menu2.Append(-1,'男')
        N=menu2.Append(-1,'女')
        self.Bind(wx.EVT_MENU, self.male2, N)
if 1 == 1:
    app = wx.App()
    MyFramm().Show()
    app.MainLoop()
