# -*- coding=utf-8 -*-
import wx
class My(wx.Frame):

    
    def OnC(self, event):
        print 'c语音'
    
    
    def OnPhp(self, event):
        print 'php语言'
    
    
    def OnJava(self, event):
        print 'java'
    
    
    def __init__(self):
        wx.Frame.__init__(self, None, -1, 'demo', size = (400, 300))
        panel = wx.Panel(self)
        bar = wx.MenuBar()
        menu1 = wx.Menu()
        bar.Append(menu1, 'Language')
        self.SetMenuBar(bar)
        
        c = menu1.AppendCheckItem(-1, 'C')
        php = menu1.AppendRadioItem(-1, 'php')
        java = menu1.AppendRadioItem(-1, 'java')
        self.Bind(wx.EVT_MENU, self.OnC, c)
        self.Bind(wx.EVT_MENU, self.OnPhp, php)
        self.Bind(wx.EVT_MENU, self.OnJava, java)
        
app = wx.App()
My().Show()
app.MainLoop()
