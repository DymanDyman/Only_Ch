# -*- coding=utf-8 -*-
import wx
class MyFrame(wx.Frame):

    
    def ShuX(self, event):
        print '数学被点击了'
    
    
    def __init__(self):
        wx.Frame.__init__(self, None, -1, '我是Frame')
        panel = wx.Panel(self)
        menubar = wx.MenuBar()
        self.SetMenuBar(menubar)
        menu1 = wx.Menu()
        menubar.Append(menu1, '学科')
        shuxue = menu1.Append(-1, '数学')
        yuwen = menu1.Append(-1, '语文')
        self.Bind(wx.EVT_MENU, self.ShuX, shuxue)
        #二级菜单
        zonghe=wx.Menu()
        zonghe.Append(-1,'我是1')
        zonghe.Append(-1,'我是2')
        zonghe.Append(-1,'我是3')
        menu1.AppendMenu(-1,'点击选择二级菜单',zonghe)
        
        menu2 = wx.Menu()
        menubar.Append(menu2, '性别')
        nan = menu2.Append(-1, '男性')
        nv = menu2.Append(-1, '女性')
        
        menu3 = wx.Menu()       
        wuyong = menu3.Append(-1, '111') 
        menubar.Insert(0, menu3, '我是插入的')
        menubar.EnableTop(0,False)
        
        
app = wx.App()
MyFrame().Show()
app.MainLoop()


